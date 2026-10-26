#!/usr/bin/env python3
"""Disposable-origin T04 browser regression. Never touches user data or production URL."""
import http.server
import copy
import hashlib
import re
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


# R147: only a synthetic v16 source on this disposable origin; no production migration.
LEGACY_SHADOW = r'''async ({origin,defaults,expectedSHA}) => {
  if(location.origin!==origin || location.hostname!=='127.0.0.1' || !navigator.locks || !crypto.subtle)throw Error('unsafe_origin');
  return navigator.locks.request('__glyphspace_r147_shadow_read__',{mode:'shared'},async()=>{
    const key='wubi06-root-coordinate-overrides-v16-svg',raw=localStorage.getItem(key);
    if(raw===null||raw.length>200000)throw Error('missing_source');
    let data;try{data=JSON.parse(raw)}catch{throw Error('invalid_json')}
    if(!data||typeof data!=='object'||Array.isArray(data)||!Object.keys(data).length)throw Error('invalid_source');
    const edits=[];
    for(const [k,points] of Object.entries(data)){
      if(!Object.prototype.hasOwnProperty.call(defaults,k)||!Array.isArray(points)||points.length!==defaults[k].length)throw Error('bad_key_or_length');
      for(let i=0;i<points.length;i++){
        const p=points[i];
        if(!Array.isArray(p)||p.length!==3||p.some(x=>typeof x!=='number'||!Number.isFinite(x))||p[0]<0||p[0]>90||p[1]<12||p[1]>88||p[2]<9||p[2]>29)throw Error('bad_point');
        if(JSON.stringify(p)!==JSON.stringify(defaults[k][i]))edits.push(k+':'+i);
      }
    }
    const bytes=await crypto.subtle.digest('SHA-256',new TextEncoder().encode(raw));
    const hash=[...new Uint8Array(bytes)].map(x=>x.toString(16).padStart(2,'0')).join('');
    if(hash!==expectedSHA||localStorage.getItem(key)!==raw)throw Error('source_changed');
    return {hash,keys:Object.keys(data).sort(),absent:Object.keys(defaults).filter(k=>!(k in data)),edits:edits.sort(),writes:0,permanentIds:0};
  });
}'''

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

                    # R147 actual frozen V0.35 coordinate schema, synthetic partial legacy data.
                    frozen=pathlib.Path(__file__).resolve().parents[1].joinpath('index.html').read_bytes()
                    check('r147-frozen-v035-source-sha',hashlib.sha256(frozen).hexdigest()=='fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc')
                    defaults=json.loads(re.search(rb'const ROOT_COORDS=(\\{[^\\n]+\\});',frozen).group(1))
                    check('r147-frozen-25keys-156slots',len(defaults)==25 and sum(map(len,defaults.values()))==156)
                    fixture={k:copy.deepcopy(defaults[k]) for k in ('G','K','X')}
                    fixture['G'][0][0]+=1;fixture['K'][2][1]+=1;fixture['X'][0][2]+=1
                    raw=json.dumps(fixture,separators=(',',':'))
                    source_key='wubi06-root-coordinate-overrides-v16-svg'
                    a.evaluate('({key,raw})=>{localStorage.setItem("outside-r147-sentinel","preserve");localStorage.setItem(key,raw)}',{'key':source_key,'raw':raw})
                    args={'origin':origin,'defaults':defaults,'expectedSHA':hashlib.sha256(raw.encode()).hexdigest()}
                    keys_before=a.evaluate('Object.keys(localStorage).sort()')
                    first_shadow=a.evaluate(LEGACY_SHADOW,args)
                    second_shadow=b.evaluate(LEGACY_SHADOW,args)
                    check('r147-real-two-tab-shadow-equal',first_shadow==second_shadow)
                    check('r147-partial-keys-absent22',first_shadow['keys']==['G','K','X'] and len(first_shadow['absent'])==22)
                    check('r147-three-user-edits-only',first_shadow['edits']==['G:0','K:2','X:0'])
                    check('r147-source-sha-bound',first_shadow['hash']==args['expectedSHA'])
                    check('r147-no-user-or-production-writes',first_shadow['writes']==0 and first_shadow['permanentIds']==0 and a.evaluate('Object.keys(localStorage).sort()')==keys_before and a.evaluate('k=>localStorage.getItem(k)',source_key)==raw)
                    check('r147-unrelated-sentinel-preserved',a.evaluate('localStorage.getItem("outside-r147-sentinel")')=='preserve')
                    tampered=copy.deepcopy(fixture);tampered['G'][0][0]+=1
                    a.evaluate('({key,raw})=>localStorage.setItem(key,raw)',{'key':source_key,'raw':json.dumps(tampered,separators=(',',':'))})
                    rejected=a.evaluate('async arg=>{try{await ('+LEGACY_SHADOW+')(arg);return false}catch(e){return String(e).includes("source_changed")}}',args)
                    check('r147-changed-legacy-source-rejected',rejected)
                    a.evaluate('({key,raw})=>localStorage.setItem(key,raw)',{'key':source_key,'raw':raw})
                    check('r147-synthetic-legacy-source-restored',a.evaluate('k=>localStorage.getItem(k)',source_key)==raw)
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
