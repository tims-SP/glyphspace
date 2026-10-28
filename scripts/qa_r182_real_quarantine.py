#!/usr/bin/env python3
"""R182: real browser disposable quarantine transaction/rollback QA, never user storage."""
import http.server,json,tempfile,threading,hashlib
from pathlib import Path
from playwright.sync_api import sync_playwright
JS=r"""
(()=>{const S='r182-v16',Q='r182-shadow',J='r182-journal',L='r182-lock';
const h=async s=>Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256',new TextEncoder().encode(s)))).map(x=>x.toString(16).padStart(2,'0')).join('');
const put=(k,v)=>v===null?localStorage.removeItem(k):localStorage.setItem(k,v);
const stage=(expected,fault='')=>navigator.locks.request(L,async()=>{
 if(localStorage.getItem(J)!==null)throw Error('pending-recovery');
 const src=localStorage.getItem(S);
 if(src===null||await h(src)!==expected)throw Error('stale-source');
 const before=localStorage.getItem(Q);
 put(J,JSON.stringify({before,beforeHash:await h(before??''),sourceHash:expected}));
 try{
  if(fault==='crash-journal')throw Error('crash-journal');
  if(await h(localStorage.getItem(S)??'')!==expected)throw Error('source-changed');
  put(Q,JSON.stringify({sourceHash:expected,sourceSnapshot:src,approvedPermanentIds:0,identityMappings:[],productionMigration:'not-run'}));
  if(fault==='crash-shadow'||fault==='fail-shadow')throw Error(fault);
  if(await h(localStorage.getItem(S)??'')!==expected)throw Error('source-changed');
  put(J,null);return 'staged';
 }catch(e){if(!e.message.startsWith('crash-')){put(Q,before);put(J,null)}throw e}
});
const recover=()=>navigator.locks.request(L,async()=>{
 const raw=localStorage.getItem(J);if(raw===null)return {recovered:false};
 let j;try{j=JSON.parse(raw)}catch{throw Error('corrupt-journal')}
 if(!j||!(j.before===null||typeof j.before==='string')||!(/^[0-9a-f]{64}$/).test(j.sourceHash)||j.beforeHash!==await h(j.before??''))throw Error('corrupt-journal');
 const changed=await h(localStorage.getItem(S)??'')!==j.sourceHash;
 put(Q,j.before);put(J,null);return {recovered:true,sourceChanged:changed};
});
window.R182={S,Q,J,L,h,stage,recover};
})();
"""
class H(http.server.SimpleHTTPRequestHandler):
 def __init__(self,*a,directory=None,**kw):super().__init__(*a,directory=directory,**kw)
 def log_message(self,*a):pass
checks=[]
def ck(name,ok):
 assert ok,name
 checks.append(name)
def reject(name,fn,needle):
 try:fn()
 except Exception as e:ck(name,needle in str(e));return
 raise AssertionError(name+' unexpectedly succeeded')
with tempfile.TemporaryDirectory(prefix='r182-disposable-') as d:
 Path(d,'index.html').write_text('<!doctype html><title>Disposable</title>')
 server=http.server.ThreadingHTTPServer(('127.0.0.1',0),lambda *a,**kw:H(*a,directory=d,**kw))
 threading.Thread(target=server.serve_forever,daemon=True).start()
 try:
  with sync_playwright() as p:
   browser=p.chromium.launch(channel='chrome',headless=True,args=['--no-sandbox'])
   try:
    context=browser.new_context();a=context.new_page();b=context.new_page()
    url=f'http://127.0.0.1:{server.server_port}/index.html'
    ck('real-two-tab-http',a.goto(url).status==200 and b.goto(url).status==200)
    for tab in (a,b):tab.add_script_tag(content=JS)
    ck('secure-loopback',a.evaluate('isSecureContext && location.hostname==="127.0.0.1"'))
    ck('fresh-storage',a.evaluate('localStorage.length===0'))
    raw='{"schema":"v16","K:2":[21,22,23]}';digest=hashlib.sha256(raw.encode()).hexdigest()
    a.evaluate('v=>localStorage.setItem(R182.S,v)',raw)
    ck('real-webcrypto-digest',a.evaluate('()=>R182.h(localStorage.getItem(R182.S))')==digest)
    ck('cross-tab-source-visible',b.evaluate('v=>localStorage.getItem(R182.S)===v',raw))
    ck('real-locked-quarantine',a.evaluate('v=>R182.stage(v)',digest)=='staged')
    ck('no-permanent-ids',b.evaluate('()=>JSON.parse(localStorage.getItem(R182.Q)).approvedPermanentIds===0'))
    ck('success-clears-journal',a.evaluate('localStorage.getItem(R182.J)===null'))
    ck('v16-unchanged',a.evaluate('v=>localStorage.getItem(R182.S)===v',raw))
    before=a.evaluate('localStorage.getItem(R182.Q)')
    reject('normal-failure-rolls-back',lambda:a.evaluate('v=>R182.stage(v,"fail-shadow")',digest),'fail-shadow')
    ck('old-shadow-restored',a.evaluate('v=>localStorage.getItem(R182.Q)===v&&localStorage.getItem(R182.J)===null',before))
    reject('crash-leaves-journal',lambda:a.evaluate('v=>R182.stage(v,"crash-shadow")',digest),'crash-shadow')
    ck('journal-survives-reload',b.reload().status==200 and b.evaluate('localStorage.getItem("r182-journal")!==null'))
    b.add_script_tag(content=JS)
    reject('stage-blocked-until-recover',lambda:b.evaluate('v=>R182.stage(v)',digest),'pending-recovery')
    ck('real-recovery',b.evaluate('()=>R182.recover()')['recovered'])
    ck('recovered-old-shadow',b.evaluate('v=>localStorage.getItem(R182.Q)===v&&localStorage.getItem(R182.J)===null',before))
    newer=raw.replace('21,22,23','22,22,23');a.evaluate('v=>localStorage.setItem(R182.S,v)',newer)
    reject('stale-source-rejected',lambda:b.evaluate('v=>R182.stage(v)',digest),'stale-source')
    ck('stale-source-no-shadow-write',a.evaluate('v=>localStorage.getItem(R182.Q)===v',before))
    nd=hashlib.sha256(newer.encode()).hexdigest()
    reject('crash-after-journal',lambda:b.evaluate('v=>R182.stage(v,"crash-journal")',nd),'crash-journal')
    a.evaluate('v=>localStorage.setItem(R182.S,v)',raw)
    result=b.evaluate('()=>R182.recover()')
    ck('recovery-detects-source-change',result['recovered'] and result['sourceChanged'])
    ck('recovery-preserves-new-source',a.evaluate('v=>localStorage.getItem(R182.S)===v',raw))
    a.evaluate('localStorage.setItem(R182.J,"{tampered")')
    reject('corrupt-journal-fails-closed',lambda:b.evaluate('()=>R182.recover()'),'corrupt-journal')
    other=browser.new_context();c=other.new_page();c.goto(url)
    ck('other-context-isolated',c.evaluate('localStorage.length===0'));other.close()
    a.evaluate('localStorage.clear()')
    ck('disposable-fixture-cleaned',a.evaluate('localStorage.length===0'))
    context.close()
   finally:browser.close()
 finally:server.shutdown();server.server_close()
assert len(checks)==24,(len(checks),checks)
result={'round':182,'rootTask':'T04','passed':24,'expected':24,'checks':checks,'allPassed':True,'realSameOrigin':True,'disposableContext':True,'productionMigration':'not-run','formalAccepted':False,'userStorageTouched':False}
Path('R182_real_quarantine_CI_QA.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':24,'expected':24,'allPassed':True}))
