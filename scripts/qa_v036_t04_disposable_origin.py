#!/usr/bin/env python3
"""Disposable-origin T04 browser regression. Never touches user data or production URL."""
import http.server
import json
import pathlib
import socketserver
import tempfile
import threading
from playwright.sync_api import sync_playwright

INSTALL = r"""async ns => {
  if(location.hostname !== '127.0.0.1' || !ns.startsWith('__glyphspace_t04_ci__')) throw Error('unsafe_origin');
  if(!navigator.locks || !crypto.subtle || !localStorage) throw Error('unsupported');
  const headKey=ns+'head', recordKey=ns+'record:', pendingKey=ns+'pending';
  const hash=async x=>[...new Uint8Array(await crypto.subtle.digest('SHA-256',new TextEncoder().encode(x)))].map(v=>v.toString(16).padStart(2,'0')).join('');
  const read=async()=>{
    const head=localStorage.getItem(headKey);
    if(head===null)return {head:null,value:null};
    const raw=localStorage.getItem(recordKey+head);
    if(raw===null || await hash(raw)!==head)throw Error('record_corrupt');
    const r=JSON.parse(raw);
    if(r.schemaVersion!==1 || r.kind!=='isolated_preview_only' || r.productionReady!==false || !Number.isInteger(r.value))throw Error('schema_drift');
    return {head,value:r.value};
  };
  const commit=async(expected,value)=>navigator.locks.request(ns+'exclusive',async()=>{
    if(localStorage.getItem(pendingKey)!==null)throw Error('recovery_required');
    const current=await read();if(current.head!==expected)throw Error('stale_head');
    const raw=JSON.stringify({schemaVersion:1,kind:'isolated_preview_only',productionReady:false,previous:expected,value});
    const next=await hash(raw);
    localStorage.setItem(recordKey+next,raw);localStorage.setItem(headKey,next);
    return {head:next,value};
  });
  const rollback=async expected=>navigator.locks.request(ns+'exclusive',async()=>{
    if(localStorage.getItem(pendingKey)!==null)throw Error('recovery_required');
    const current=await read();if(current.head!==expected)throw Error('stale_head');
    if(expected===null)throw Error('no_revision');
    const raw=localStorage.getItem(recordKey+expected);
    if(raw===null || await hash(raw)!==expected)throw Error('record_corrupt');
    const r=JSON.parse(raw);
    if(r.schemaVersion!==1 || r.kind!=='isolated_preview_only' || r.productionReady!==false || !Number.isInteger(r.value))throw Error('schema_drift');
    if(r.previous!==null){
      if(typeof r.previous!=='string' || !/^[a-f0-9]{64}$/.test(r.previous))throw Error('invalid_previous');
      const previous=localStorage.getItem(recordKey+r.previous);
      if(previous===null || await hash(previous)!==r.previous)throw Error('predecessor_corrupt');
      const p=JSON.parse(previous);
      if(p.schemaVersion!==1 || p.kind!=='isolated_preview_only' || p.productionReady!==false || !Number.isInteger(p.value))throw Error('predecessor_schema_drift');
    }
    if(r.previous===null)localStorage.removeItem(headKey);else localStorage.setItem(headKey,r.previous);
    return read();
  });
  // R109: real-origin crash-journal recovery, never production migration.
  const journalCommit=async(expected,value,phase)=>navigator.locks.request(ns+'exclusive',async()=>{
    if(localStorage.getItem(pendingKey)!==null)throw Error('recovery_required');
    const current=await read();if(current.head!==expected)throw Error('stale_head');
    if(!Number.isInteger(value)||value<0||value>1000)throw Error('invalid_value');
    const raw=JSON.stringify({schemaVersion:1,kind:'isolated_preview_only',productionReady:false,previous:expected,value});
    const next=await hash(raw);
    localStorage.setItem(pendingKey,JSON.stringify({previous:expected,next}));
    if(phase==='after_pending')return {simulatedCrash:true,phase};
    localStorage.setItem(recordKey+next,raw);
    if(phase==='after_record')return {simulatedCrash:true,phase};
    localStorage.setItem(headKey,next);
    if(phase==='after_head')return {simulatedCrash:true,phase};
    localStorage.removeItem(pendingKey);
    return {head:next,value};
  });
  const recover=async()=>navigator.locks.request(ns+'exclusive',async()=>{
    const pendingRaw=localStorage.getItem(pendingKey);
    if(pendingRaw===null)return {status:'clean',...(await read())};
    const pending=JSON.parse(pendingRaw);
    const validHash=x=>typeof x==='string' && /^[a-f0-9]{64}$/.test(x);
    if(!pending || !(pending.previous===null || validHash(pending.previous)) || !validHash(pending.next))throw Error('invalid_pending');
    const current=await read();
    if(current.head!==pending.previous && current.head!==pending.next)throw Error('ambiguous_pending');
    localStorage.removeItem(pendingKey);
    return {status:current.head===pending.next?'committed_after_head':'aborted_before_head',...current};
  });
  window.t04={headKey,recordKey,pendingKey,commit,rollback,read,journalCommit,recover,ns};
  return true;
}"""

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args): pass

def run():
    results=[]
    def check(name,ok):
        results.append({'name':name,'result':'pass' if ok else 'fail'})
        if not ok: raise AssertionError(name)
    with tempfile.TemporaryDirectory(prefix='glyphspace-t04-ci-') as temp:
        pathlib.Path(temp,'index.html').write_text('<!doctype html><title>T04 disposable</title>')
        class H(Handler):
            def __init__(self,*a,**k):super().__init__(*a,directory=temp,**k)
        with socketserver.TCPServer(('127.0.0.1',0),H) as server:
            threading.Thread(target=server.serve_forever,daemon=True).start()
            origin='http://127.0.0.1:'+str(server.server_address[1])
            ns='__glyphspace_t04_ci__'+str(server.server_address[1])+':'
            with sync_playwright() as p:
                browser=p.chromium.launch(headless=True)
                context=browser.new_context()
                a,b=context.new_page(),context.new_page()
                try:
                    for page in (a,b):
                        page.goto(origin+'/index.html',wait_until='domcontentloaded',timeout=15000)
                        page.evaluate(INSTALL,ns)
                    check('same-disposable-origin',a.evaluate('location.origin')==b.evaluate('location.origin')==origin)
                    b.evaluate("window.events=[];window.addEventListener('storage',e=>{if(e.key&&e.key.startsWith(t04.ns))events.push(e.key)})")
                    first=a.evaluate('async()=>t04.commit(null,11)')
                    b.wait_for_function('window.events.includes(t04.headKey)')
                    check('cross-tab-event',b.evaluate('window.events.includes(t04.headKey)'))
                    check('cross-tab-read',b.evaluate('async()=>t04.read()')['value']==11)
                    second=b.evaluate('async h=>t04.commit(h,22)',first['head'])
                    saved=a.evaluate('h=>localStorage.getItem(t04.recordKey+h)',first['head'])
                    a.evaluate('h=>localStorage.removeItem(t04.recordKey+h)',first['head'])
                    missing=b.evaluate('async h=>{try{await t04.rollback(h);return false}catch(e){return String(e).includes("predecessor_corrupt")}}',second['head'])
                    check('missing-predecessor-rejected',missing)
                    check('missing-predecessor-head-preserved',a.evaluate('localStorage.getItem(t04.headKey)')==second['head'])
                    a.evaluate('(v)=>localStorage.setItem(t04.recordKey+v.head,"{}")',{'head':first['head']})
                    corrupt=b.evaluate('async h=>{try{await t04.rollback(h);return false}catch(e){return String(e).includes("predecessor_corrupt")}}',second['head'])
                    check('corrupt-predecessor-rejected',corrupt)
                    check('corrupt-predecessor-head-preserved',a.evaluate('localStorage.getItem(t04.headKey)')==second['head'])
                    a.evaluate('v=>localStorage.setItem(t04.recordKey+v.head,v.raw)',{'head':first['head'],'raw':saved})
                    check('repaired-rollback',b.evaluate('async h=>t04.rollback(h)',second['head'])['head']==first['head'])
                    check('stale-head-rejected',a.evaluate('async()=>{try{await t04.commit(null,33);return false}catch(e){return String(e).includes("stale_head")}}'))
                    # R109: actual two-tab Chromium origin, three crash phases and fail-closed pending.
                    check('clean-recovery-noop',a.evaluate('async()=>t04.recover()')['status']=='clean')
                    a.evaluate('async h=>t04.journalCommit(h,44,"after_pending")',first['head'])
                    check('pending-before-record-blocks-commit',b.evaluate('async h=>{try{await t04.commit(h,55);return false}catch(e){return String(e).includes("recovery_required")}}',first['head']))
                    check('pending-before-record-aborts',b.evaluate('async()=>t04.recover()')['status']=='aborted_before_head')
                    check('head-after-pending-unchanged',a.evaluate('async()=>t04.read()')['head']==first['head'])
                    a.evaluate('async h=>t04.journalCommit(h,44,"after_record")',first['head'])
                    check('pending-after-record-blocks-rollback',b.evaluate('async h=>{try{await t04.rollback(h);return false}catch(e){return String(e).includes("recovery_required")}}',first['head']))
                    check('pending-after-record-aborts',b.evaluate('async()=>t04.recover()')['status']=='aborted_before_head')
                    check('head-after-record-unchanged',a.evaluate('async()=>t04.read()')['head']==first['head'])
                    a.evaluate('async h=>t04.journalCommit(h,44,"after_head")',first['head'])
                    check('head-after-publish-visible',b.evaluate('async()=>t04.read()')['value']==44)
                    check('pending-after-head-recovers',b.evaluate('async()=>t04.recover()')['status']=='committed_after_head')
                    check('published-record-stable',a.evaluate('async()=>t04.read()')['value']==44)
                    check('rollback-after-recovery',a.evaluate('async h=>t04.rollback(h)',a.evaluate('async()=>t04.read()')['head'])['head']==first['head'])
                    check('pending-key-cleared',b.evaluate('localStorage.getItem(t04.pendingKey)') is None)
                    a.evaluate("() => {window.release=null;navigator.locks.request(t04.ns+'queue',()=>new Promise(r=>{window.release=r}))}")
                    a.wait_for_function('typeof window.release === "function"')
                    b.evaluate("() => {window.acquired=false;navigator.locks.request(t04.ns+'queue',()=>{window.acquired=true})}")
                    check('real-web-lock-exclusion',b.evaluate('window.acquired') is False)
                    a.evaluate('window.release()')
                    b.wait_for_function('window.acquired === true')
                    check('real-web-lock-release',b.evaluate('window.acquired') is True)
                finally:
                    context.close();browser.close();server.shutdown()
    return {'taskId':'T04','environment':'GitHub Actions Ubuntu Chromium, disposable 127.0.0.1 origin, two tabs','passed':len(results),'checks':results,'result':'pass','formalAcceptance':False,'userStorageTouched':False,'sourceCertification':'not-run'}

if __name__=='__main__':
    out=pathlib.Path('t04_disposable_origin_results.json')
    try:
        report=run()
    except Exception as exc:
        report={'taskId':'T04','result':'fail','error':repr(exc),'formalAcceptance':False,'userStorageTouched':False}
        out.write_text(json.dumps(report,indent=2)+'\n')
        raise
    out.write_text(json.dumps(report,indent=2)+'\n')
    print('T04 disposable origin',report['passed'],'PASS; not production migration')
