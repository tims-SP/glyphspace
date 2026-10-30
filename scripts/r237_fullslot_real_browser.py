#!/usr/bin/env python3
"""R237 Root T04: 25-key/156-slot actual issuer + R192 real same-origin Chromium QA.
Disposable loopback HTTP origin and fresh browser context only. No user profile.
"""
import asyncio, http.server, json, threading, traceback
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parent
S='wubi06-root-coordinate-overrides-v16-svg'
H='__glyphspace_disposable_r194_shadow'
J='__glyphspace_disposable_r194_journal'
class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self,*a,**kw):super().__init__(*a,directory=str(ROOT),**kw)
    def log_message(self,*a):pass
    def guess_type(self,path):return 'text/javascript' if path.endswith('.mjs') else super().guess_type(path)
async def main():
    checks=[];err=None
    def ck(name,value):
        if not value:raise AssertionError(name)
        checks.append(name)
    server=http.server.ThreadingHTTPServer(('127.0.0.1',0),Handler)
    threading.Thread(target=server.serve_forever,daemon=True).start()
    try:
      async with async_playwright() as p:
        browser=await p.chromium.launch(headless=True,args=['--no-sandbox'])
        try:
          ctx=await browser.new_context()
          a,b=await ctx.new_page(),await ctx.new_page()
          url=f'http://127.0.0.1:{server.server_port}/index.html'
          ck('two-tabs',(await a.goto(url)).status==200 and (await b.goto(url)).status==200)
          ck('secure-origin-and-real-locks',await a.evaluate('isSecureContext && !!navigator.locks?.request && !!crypto.subtle'))
          ck('fresh-storage',await a.evaluate('localStorage.length===0'))
          for page in (a,b):
            for f in ('v036_r148_strict_shadow.js','v036_r152_source_bound_plan.js','r194_r178_freshness.js','r194_r179_realm.js'):
              await page.add_script_tag(url='/'+f)
            await page.evaluate("""async()=>{
              const m=await import('/r194_real_issuer_r192_bridge.mjs');
              window.factory=m.createRealmIssuedDisposableBridge;
              window.defaults=await(await fetch('/r194_frozen_root_coords.json')).json();
            }""")
          ck('25-keys',await a.evaluate('Object.keys(defaults).length===25'))
          ck('156-slots',await a.evaluate('Object.values(defaults).reduce((n,x)=>n+x.length,0)===156'))
          await a.evaluate("""async()=>{
            const all=structuredClone(defaults);
            for(const slots of Object.values(all))for(const slot of slots)slot[0]++;
            window.raw=JSON.stringify(all);
            localStorage.setItem('wubi06-root-coordinate-overrides-v16-svg',raw);
            localStorage.setItem('r237-unrelated','preserve');
            window.bridge=factory();window.plan=await bridge.issue(defaults);
          }""")
          ck('156-issued-aliases',await a.evaluate('plan.sourceSlotAliases.length===156'))
          ck('156-issued-edits',await a.evaluate('plan.explicitEdits.length===156'))
          ck('issuer-plan-frozen',await a.evaluate('Object.isFrozen(plan)'))
          ck('real-stage',(await a.evaluate('()=>bridge.stage(plan)'))['status']=='disposable_staged')
          ck('real-shadow-156',await b.evaluate("""()=>{const p=JSON.parse(localStorage.getItem('__glyphspace_disposable_r194_shadow'));return p.explicitEdits.length===156&&p.sourceSlotAliases.length===156&&p.approvedPermanentIds===0&&p.identityMappings.length===0}"""))
          ck('idempotent',(await a.evaluate('()=>bridge.stage(plan)'))['status']=='idempotent')
          ck('journal-cleared',await b.evaluate(f'localStorage.getItem({json.dumps(J)})===null'))
          ck('source-unchanged',await a.evaluate(f'localStorage.getItem({json.dumps(S)})===raw'))
          ck('unrelated-unchanged',await b.evaluate('localStorage.getItem("r237-unrelated")==="preserve"'))
          await a.evaluate("""async()=>{
            window.crash=factory({qaFaults:true,revision:1});
            try{await crash.stage(plan,{fault:'crash-after-shadow'})}
            catch(e){window.crashError=String(e)}
          }""")
          ck('crash-injected',await a.evaluate('crashError.includes("injected_crash-after-shadow")'))
          ck('crash-journal-present',await b.evaluate(f'localStorage.getItem({json.dumps(J)})!==null'))
          await b.evaluate('window.recovery=factory()')
          ck('cross-tab-recovery',(await b.evaluate('()=>recovery.recover()'))['recovered'] is True)
          ck('recovery-revision-zero',await b.evaluate(f'JSON.parse(localStorage.getItem({json.dumps(H)})).revision===0'))
          ck('recovery-cleared-journal',await a.evaluate(f'localStorage.getItem({json.dumps(J)})===null'))
          ck('recovery-preserved-source',await a.evaluate(f'localStorage.getItem({json.dumps(S)})===raw'))
          await b.evaluate("""()=>{const v=JSON.parse(localStorage.getItem('wubi06-root-coordinate-overrides-v16-svg'));v.X[v.X.length-1][1]++;localStorage.setItem('wubi06-root-coordinate-overrides-v16-svg',JSON.stringify(v))}""")
          stale=await a.evaluate("""async()=>{try{await bridge.stage(plan);return ''}catch(e){return String(e)}}""")
          ck('stale-plan-rejected','source_stale_since_issuance' in stale)
          ck('stale-shadow-preserved',await b.evaluate(f'JSON.parse(localStorage.getItem({json.dumps(H)})).revision===0'))
          other=await browser.new_context();c=await other.new_page();await c.goto(url)
          ck('independent-context-clean',await c.evaluate('localStorage.length===0'))
          await other.close()
          await a.evaluate('localStorage.clear()')
          ck('disposable-context-clean',await b.evaluate('localStorage.length===0'))
          await ctx.close()
        finally:await browser.close()
    except Exception as e:err=repr(e)+'\n'+traceback.format_exc()[-1500:]
    finally:server.shutdown();server.server_close()
    result={'round':237,'rootTask':'T04','passed':len(checks),'expected':25,'checks':checks,'allPassed':err is None and len(checks)==25,'error':err,'environment':'real Chromium fresh 127.0.0.1; actual R148/R152/R178/R179 issuer + R192 core','fixture':'25 keys / 156 synthetic legacy edits','formalAccepted':False,'productionMigration':'not-run','userStorageTouched':False}
    (ROOT/'R237_real_browser_QA.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'passed':len(checks),'expected':25,'allPassed':result['allPassed'],'error':err},ensure_ascii=False))
    if not result['allPassed']:raise SystemExit(1)
if __name__=='__main__':asyncio.run(main())
