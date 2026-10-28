#!/usr/bin/env python3
"""R194: R148/R152/R178/R179 real issuer + R192 core on a fresh real Chromium origin.
Uses only a temporary 127.0.0.1 profile. No production user storage or migration.
"""
import asyncio, http.server, json, threading
from pathlib import Path
from playwright.async_api import async_playwright

ROOT=Path(__file__).resolve().parent
S='wubi06-root-coordinate-overrides-v16-svg'
H='__glyphspace_disposable_r194_shadow'
J='__glyphspace_disposable_r194_journal'
class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self,*args,**kwargs):super().__init__(*args,directory=str(ROOT),**kwargs)
    def log_message(self,*args):pass
    def guess_type(self,path):return 'text/javascript' if path.endswith('.mjs') else super().guess_type(path)

async def setup(page):
    for f in ('v036_r148_strict_shadow.js','v036_r152_source_bound_plan.js','r194_r178_freshness.js','r194_r179_realm.js'):
        await page.add_script_tag(url='/'+f)
    await page.evaluate("""async()=>{
      const {createRealmIssuedDisposableBridge}=await import('/r194_real_issuer_r192_bridge.mjs');
      window.r194Factory=createRealmIssuedDisposableBridge;
      window.r194Defaults=await (await fetch('/r194_frozen_root_coords.json')).json();
    }""")

async def main():
    checks=[]
    def ck(n,v):
        if not v:raise AssertionError(n)
        checks.append(n)
    srv=http.server.ThreadingHTTPServer(('127.0.0.1',0),Handler)
    threading.Thread(target=srv.serve_forever,daemon=True).start()
    try:
      async with async_playwright() as p:
        browser=await p.chromium.launch(headless=True,executable_path='/usr/bin/chromium' if Path('/usr/bin/chromium').exists() else None,args=['--no-sandbox'])
        try:
          ctx=await browser.new_context()
          a,b=await ctx.new_page(),await ctx.new_page()
          url=f'http://127.0.0.1:{srv.server_port}/index.html'
          ck('two-real-loopback-tabs',(await a.goto(url)).status==200 and (await b.goto(url)).status==200)
          ck('secure-context-with-locks',await a.evaluate('isSecureContext && !!navigator.locks && !!crypto.subtle'))
          ck('fresh-isolated-storage',await a.evaluate('localStorage.length===0'))
          await setup(a);await setup(b)
          ck('all-four-real-issuers',await a.evaluate('!!GlyphSpaceR148 && !!GlyphSpaceR152 && !!GlyphSpaceR178 && !!GlyphSpaceR179'))
          ck('156-frozen-coordinates',await a.evaluate('Object.values(r194Defaults).reduce((n,v)=>n+v.length,0)===156'))
          await a.evaluate("""async()=>{
            const fixture={G:structuredClone(r194Defaults.G),K:structuredClone(r194Defaults.K),X:structuredClone(r194Defaults.X)};
            fixture.G[0][0]++;fixture.K[2][1]++;fixture.X[0][2]++;
            window.R194Raw=JSON.stringify(fixture);
            localStorage.setItem('wubi06-root-coordinate-overrides-v16-svg',R194Raw);
            localStorage.setItem('r194-unrelated','preserve');
            window.R194Bridge=r194Factory();
            window.R194Plan=await R194Bridge.issue(r194Defaults);
          }""")
          ck('real-issued-plan-with-three-edits',await a.evaluate('R194Plan.explicitEdits.length===3'))
          ck('real-issued-plan-frozen',await a.evaluate('Object.isFrozen(R194Plan)'))
          ck('source-raw-preserved-after-issuance',await a.evaluate(f'localStorage.getItem({json.dumps(S)})===R194Raw'))
          ck('stage-with-real-issuer',(await a.evaluate('()=>R194Bridge.stage(R194Plan)'))['status']=='disposable_staged')
          ck('idempotent-with-real-issuer',(await a.evaluate('()=>R194Bridge.stage(R194Plan)'))['status']=='idempotent')
          ck('shadow-zero-approved-ids',await b.evaluate(f'JSON.parse(localStorage.getItem({json.dumps(H)})).approvedPermanentIds===0'))
          ck('journal-clean-after-stage',await b.evaluate(f'localStorage.getItem({json.dumps(J)})===null'))
          ck('source-byte-exact-after-stage',await a.evaluate(f'localStorage.getItem({json.dumps(S)})===R194Raw'))
          ck('unrelated-key-preserved',await b.evaluate('localStorage.getItem("r194-unrelated")==="preserve"'))
          rejected=await a.evaluate("""async()=>{
            try{await R194Bridge.stage(structuredClone(R194Plan));return ''}
            catch(e){return String(e)}
          }""")
          ck('clone-not-issued-rejected','plan_not_issued' in rejected)
          await a.evaluate("""async()=>{
            window.R194Crash=r194Factory({qaFaults:true,revision:1});
            try{await R194Crash.stage(R194Plan,{fault:'crash-after-shadow'})}
            catch(e){window.R194CrashError=String(e)}
          }""")
          ck('real-issuer-crash-injected',await a.evaluate('R194CrashError.includes("injected_crash-after-shadow")'))
          ck('crash-journal-retained',await b.evaluate(f'localStorage.getItem({json.dumps(J)})!==null'))
          await b.evaluate('window.R194Recovery=r194Factory()')
          ck('other-tab-recovery',(await b.evaluate('()=>R194Recovery.recover()'))['recovered'] is True)
          ck('recovery-cleared-journal',await a.evaluate(f'localStorage.getItem({json.dumps(J)})===null'))
          ck('recovery-restored-old-shadow',await a.evaluate(f'JSON.parse(localStorage.getItem({json.dumps(H)})).revision===0'))
          await b.evaluate(f'localStorage.removeItem({json.dumps(H)})')
          await a.evaluate("""async()=>{
            window.R194Plan2=await R194Bridge.issue(r194Defaults);
            try{await R194Crash.stage(R194Plan2,{fault:'crash-after-shadow'})}
            catch(e){window.R194Crash2=String(e)}
          }""")
          ck('typed-journal-from-absent',await b.evaluate(f'JSON.parse(localStorage.getItem({json.dumps(J)})).before===null'))
          await b.evaluate(f'localStorage.setItem({json.dumps(H)},"")')
          conflict=await b.evaluate("""async()=>{try{await R194Recovery.recover();return ''}catch(e){return String(e)}}""")
          ck('foreign-empty-shadow-conflict','recovery_conflict_shadow_changed' in conflict)
          ck('foreign-empty-and-journal-preserved',await b.evaluate(f'localStorage.getItem({json.dumps(H)})==="" && localStorage.getItem({json.dumps(J)})!==null'))
          await b.evaluate(f'localStorage.removeItem({json.dumps(H)})')
          ck('typed-null-recovery',(await b.evaluate('()=>R194Recovery.recover()'))['recovered'] is True)
          ck('typed-recovery-cleans-journal',await b.evaluate(f'localStorage.getItem({json.dumps(J)})===null'))
          await b.evaluate(f'localStorage.setItem({json.dumps(S)},localStorage.getItem({json.dumps(S)})+" ")')
          stale=await a.evaluate("""async()=>{try{await R194Bridge.stage(R194Plan);return ''}catch(e){return String(e)}}""")
          ck('source-change-after-issuance-rejected','source_stale_since_issuance' in stale)
          ck('source-mutation-preserved',await b.evaluate(f'localStorage.getItem({json.dumps(S)}).endsWith(" ")'))
          ck('no-shadow-after-typed-recovery',await b.evaluate(f'localStorage.getItem({json.dumps(H)})===null'))
          isolated=await browser.new_context();c=await isolated.new_page();await c.goto(url)
          ck('separate-browser-context-isolated',await c.evaluate('localStorage.length===0'))
          await isolated.close()
          await a.evaluate('localStorage.clear()')
          ck('temporary-storage-cleaned',await b.evaluate('localStorage.length===0'))
          await ctx.close()
        finally:await browser.close()
    finally:srv.shutdown();srv.server_close()
    result={'round':194,'rootTask':'T04','passed':len(checks),'checks':checks,'allPassed':True,
      'environment':'real Chromium, fresh 127.0.0.1 origin, two tabs, actual R148/R152/R178/R179 issuer + R192 ESM',
      'sourceFixture':'frozen V0.35 156 default coordinates + synthetic three-key v16 overrides',
      'formalAccepted':False,'productionMigration':'not-run','userStorageTouched':False}
    (ROOT/'R194_real_browser_QA.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'passed':len(checks),'allPassed':True}))

if __name__=='__main__':asyncio.run(main())
