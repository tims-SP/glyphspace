#!/usr/bin/env python3
"""R190 real Chromium async-source-digest readback QA. Synthetic source;
actual R189 ESM + Web Locks + localStorage + WebCrypto, disposable profile only.
"""
import asyncio, http.server, json, threading
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parent
class Handler(http.server.SimpleHTTPRequestHandler):
 def __init__(self,*a,**kw):super().__init__(*a,directory=str(ROOT),**kw)
 def log_message(self,*a):pass
 def guess_type(self,p):return 'text/javascript' if p.endswith('.mjs') else super().guess_type(p)
async def main():
 checks=[]
 def ck(name,ok):
  if not ok:raise AssertionError(name)
  checks.append(name)
 server=http.server.ThreadingHTTPServer(('127.0.0.1',0),Handler)
 threading.Thread(target=server.serve_forever,daemon=True).start()
 try:
  async with async_playwright() as p:
   browser=await p.chromium.launch(headless=True,args=['--no-sandbox'])
   try:
    ctx=await browser.new_context();a=await ctx.new_page();b=await ctx.new_page()
    url=f'http://127.0.0.1:{server.server_port}/index.html'
    ck('two-real-loopback-tabs',(await a.goto(url)).status==200 and (await b.goto(url)).status==200)
    ck('secure-context',await a.evaluate('isSecureContext && !!navigator.locks && !!crypto.subtle'))
    ck('fresh-profile',await a.evaluate('localStorage.length===0'))
    await a.evaluate('''async()=>{
      const {createDisposableTransactionCore}=await import('/r189_source_readback_transaction_core.mjs');
      const S='r190-fixture-source',H='__glyphspace_disposable_r190_shadow',J='__glyphspace_disposable_r190_journal';
      localStorage.setItem(S,'source-before');localStorage.setItem(H,'shadow-before');
      localStorage.setItem('r190-unrelated','sentinel');
      const hex=b=>Array.from(new Uint8Array(b),v=>v.toString(16).padStart(2,'0')).join('');
      const nativeSHA=async s=>hex(await crypto.subtle.digest('SHA-256',new TextEncoder().encode(s)));
      const plan=Object.freeze({sourceSHA:await nativeSHA('source-before')});
      let calls=0,release;
      window.R190Ready=false;
      window.R190Release=()=>{if(!release)throw Error('not-ready');release()};
      const sha=async s=>{
        if(s==='source-before'&&++calls===3)
          await new Promise(r=>{release=r;window.R190Ready=true});
        return nativeSHA(s);
      };
      const core=createDisposableTransactionCore({sourceKey:S,shadowKey:H,journalKey:J,
        read:k=>localStorage.getItem(k),
        write:(k,v)=>v===null?localStorage.removeItem(k):localStorage.setItem(k,v),
        sha256:sha,withLock:fn=>navigator.locks.request('r190-exclusive',{mode:'exclusive'},fn),
        verifySourcePlan:async p=>p===plan,
        buildPayload:async()=>({isDisposable:true,approvedPermanentIds:0,identityMappings:[],productionMigration:'not-run',revision:190})});
      window.R190={core,plan,S,H,J,get calls(){return calls}};
    }''')
    pending=asyncio.create_task(a.evaluate('()=>R190.core.stage(R190.plan)'))
    for _ in range(100):
     if await a.evaluate('window.R190Ready===true'):break
     await asyncio.sleep(.05)
    ck('third-source-digest-pending',await a.evaluate('window.R190Ready===true'))
    ck('shadow-written-before-race',await b.evaluate('localStorage.getItem("__glyphspace_disposable_r190_shadow")!=="shadow-before"'))
    ck('journal-present-before-race',await b.evaluate('localStorage.getItem("__glyphspace_disposable_r190_journal")!==null'))
    ck('pending-stage-not-resolved',not pending.done())
    await b.evaluate('localStorage.setItem("r190-fixture-source","source-after")')
    await a.evaluate('window.R190Release()')
    error=''
    try:await asyncio.wait_for(pending,10)
    except Exception as e:error=str(e)
    ck('source-readback-rejects', 'source_changed_during_digest' in error)
    ck('external-source-preserved',await b.evaluate('localStorage.getItem("r190-fixture-source")==="source-after"'))
    ck('shadow-restored',await b.evaluate('localStorage.getItem("__glyphspace_disposable_r190_shadow")==="shadow-before"'))
    ck('journal-cleared',await b.evaluate('localStorage.getItem("__glyphspace_disposable_r190_journal")===null'))
    ck('unrelated-key-preserved',await b.evaluate('localStorage.getItem("r190-unrelated")==="sentinel"'))
    ck('third-source-digest-count',await a.evaluate('R190.calls===3'))
    other=await browser.new_context();c=await other.new_page();await c.goto(url)
    ck('independent-context-storage-isolated',await c.evaluate('localStorage.length===0'))
    await other.close();await a.evaluate('localStorage.clear()')
    ck('disposable-profile-cleaned',await a.evaluate('localStorage.length===0'))
    await ctx.close()
   finally:await browser.close()
 finally:server.shutdown();server.server_close()
 result={'round':190,'rootTask':'T04','passed':len(checks),'checks':checks,'allPassed':True,
  'environment':'real Chromium fresh context, two 127.0.0.1 tabs, R189 ESM, real Web Locks/localStorage/WebCrypto, controlled digest gate',
  'issuer':'synthetic-plan-only','formalAccepted':False,'productionMigration':'not-run','userStorageTouched':False}
 (ROOT/'R190_core_browser_QA.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'passed':len(checks),'allPassed':True}))
if __name__=='__main__':asyncio.run(main())
