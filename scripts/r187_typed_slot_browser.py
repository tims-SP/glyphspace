#!/usr/bin/env python3
"""R187 real Chromium: typed null/empty shadow recovery, disposable fixture only."""
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
 def ck(n,v):
  if not v:raise AssertionError(n)
  checks.append(n)
 async def reject(n,fn,needle):
  try:await fn()
  except Exception as e:ck(n,needle in str(e));return
  raise AssertionError(n+':unexpected success')
 server=http.server.ThreadingHTTPServer(('127.0.0.1',0),Handler)
 threading.Thread(target=server.serve_forever,daemon=True).start()
 try:
  async with async_playwright() as p:
   browser=await p.chromium.launch(headless=True,args=['--no-sandbox'])
   try:
    ctx=await browser.new_context();a=await ctx.new_page();b=await ctx.new_page()
    url=f'http://127.0.0.1:{server.server_port}/index.html'
    ck('real-two-tab-loopback',(await a.goto(url)).status==200 and (await b.goto(url)).status==200)
    ck('empty-temporary-context',await a.evaluate('localStorage.length===0'))
    await a.evaluate('localStorage.setItem("r187-fixture-source","fixture")')
    setup="""async()=>{
      const {createDisposableTransactionCore}=await import('/r187_typed_slot_transaction_core.mjs');
      const S='r187-fixture-source',H='__glyphspace_disposable_r187_shadow',J='__glyphspace_disposable_r187_journal';
      const sha=async x=>Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256',new TextEncoder().encode(x)))).map(v=>v.toString(16).padStart(2,'0')).join('');
      const plan={sourceSHA:await sha(localStorage.getItem(S)),issued:true};
      const core=createDisposableTransactionCore({sourceKey:S,shadowKey:H,journalKey:J,
       read:k=>localStorage.getItem(k),write:(k,v)=>v===null?localStorage.removeItem(k):localStorage.setItem(k,v),
       sha256:sha,withLock:fn=>navigator.locks.request('r187-fixture-lock',{mode:'exclusive'},fn),
       verifySourcePlan:async p=>p?.issued===true&&p.sourceSHA===plan.sourceSHA,
       buildPayload:async()=>({isDisposable:true,approvedPermanentIds:0,identityMappings:[],productionMigration:'not-run'}),allowFaults:true});
      window.R187={S,H,J,plan,core};return isSecureContext&&!!navigator.locks;
    }"""
    ck('real-secure-web-locks',await a.evaluate(setup))
    ck('second-tab-real-web-locks',await b.evaluate(setup))
    await reject('real-crash-after-shadow',lambda:a.evaluate('()=>R187.core.stage(R187.plan,{fault:"crash-after-shadow"})'),'injected_crash-after-shadow')
    ck('real-v3-journal',await b.evaluate('()=>JSON.parse(localStorage.getItem(R187.J)).schema==="glyphspace-r187-disposable-journal-v3"'))
    await b.evaluate('()=>localStorage.setItem(R187.H,"")')
    await reject('real-foreign-empty-refused',lambda:a.evaluate('()=>R187.core.recover()'),'recovery_conflict_shadow_changed')
    ck('real-empty-preserved',await b.evaluate('()=>localStorage.getItem(R187.H)===""&&localStorage.getItem(R187.J)!==null'))
    await b.evaluate('()=>localStorage.removeItem(R187.H)')
    ck('real-null-recovered',(await a.evaluate('()=>R187.core.recover()'))['recovered'] is True)
    ck('real-journal-cleared',await b.evaluate('()=>localStorage.getItem(R187.J)===null'))
    await b.evaluate('()=>localStorage.setItem(R187.H,"")')
    await reject('real-crash-from-empty',lambda:a.evaluate('()=>R187.core.stage(R187.plan,{fault:"crash-after-shadow"})'),'injected_crash-after-shadow')
    await b.evaluate('()=>localStorage.removeItem(R187.H)')
    await reject('real-foreign-null-refused',lambda:a.evaluate('()=>R187.core.recover()'),'recovery_conflict_shadow_changed')
    ck('real-null-preserved',await b.evaluate('()=>localStorage.getItem(R187.H)===null&&localStorage.getItem(R187.J)!==null'))
    await b.evaluate('()=>localStorage.setItem(R187.H,"")')
    ck('real-empty-recovered',(await a.evaluate('()=>R187.core.recover()'))['recovered'] is True)
    ck('real-empty-byte-preserved',await b.evaluate('()=>localStorage.getItem(R187.H)===""'))
    ck('real-source-untouched',await a.evaluate('()=>localStorage.getItem(R187.S)==="fixture"'))
    other=await browser.new_context();c=await other.new_page();await c.goto(url)
    ck('other-context-isolated',await c.evaluate('localStorage.length===0'))
    await other.close();await a.evaluate('localStorage.clear()');await ctx.close()
   finally:await browser.close()
 finally:server.shutdown();server.server_close()
 result={'round':187,'task':'T04','passed':len(checks),'checks':checks,'allPassed':True,
  'environment':'real Chromium two tabs fresh loopback origin; synthetic issuer fixture',
  'productionMigration':'not-run','formalAccepted':False,'userStorageTouched':False}
 (ROOT/'R187_typed_slot_browser_QA.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'passed':len(checks),'allPassed':True}))
if __name__=='__main__':asyncio.run(main())
