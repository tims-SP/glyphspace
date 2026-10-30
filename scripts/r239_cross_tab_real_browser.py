#!/usr/bin/env python3
"""R239 Root T04: R238 concurrency recovery on real fresh Chromium same-origin.
Synthetic 25-key 156-slot data only; never open user profiles or existing origins.
"""
import asyncio, http.server, json, threading, traceback
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parent
S="wubi06-root-coordinate-overrides-v16-svg"
H="__glyphspace_disposable_r194_shadow"
J="__glyphspace_disposable_r194_journal"
class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self,*a,**kw):super().__init__(*a,directory=str(ROOT),**kw)
    def log_message(self,*a):pass
    def guess_type(self,path):return "text/javascript" if path.endswith(".mjs") else super().guess_type(path)
async def main():
    checks=[];error=None
    def ck(name,ok):
        if not ok:raise AssertionError(name)
        checks.append(name)
    srv=http.server.ThreadingHTTPServer(("127.0.0.1",0),Handler)
    threading.Thread(target=srv.serve_forever,daemon=True).start()
    try:
        async with async_playwright() as p:
            browser=await p.chromium.launch(headless=True,args=["--no-sandbox"])
            try:
                ctx=await browser.new_context()
                a,b=await ctx.new_page(),await ctx.new_page()
                url=f"http://127.0.0.1:{srv.server_port}/index.html"
                ck("two-real-tabs",(await a.goto(url)).status==200 and (await b.goto(url)).status==200)
                ck("secure-web-locks",await a.evaluate("isSecureContext && !!navigator.locks?.request && !!crypto.subtle"))
                ck("fresh-origin",await a.evaluate("localStorage.length===0"))
                for page in (a,b):
                    for f in ("v036_r148_strict_shadow.js","v036_r152_source_bound_plan.js","r194_r178_freshness.js","r194_r179_realm.js"):
                        await page.add_script_tag(url="/"+f)
                    await page.evaluate("""async()=>{
                      const {createRealmIssuedDisposableBridge}=await import('/r194_real_issuer_r192_bridge.mjs');
                      window.makeBridge=createRealmIssuedDisposableBridge;
                      window.defaults=await(await fetch('/r194_frozen_root_coords.json')).json();
                    }""")
                ck("25-keys",await a.evaluate("Object.keys(defaults).length===25"))
                ck("156-slots",await a.evaluate("Object.values(defaults).reduce((n,x)=>n+x.length,0)===156"))
                await a.evaluate("""()=>{let all=structuredClone(defaults);for(const x of Object.values(all))for(const s of x)s[0]++;
                  window.sourceRaw=JSON.stringify(all);localStorage.setItem('wubi06-root-coordinate-overrides-v16-svg',sourceRaw);
                  localStorage.setItem('r239-unrelated','keep')}""")
                for page in (a,b):await page.evaluate("async()=>{window.bridge=makeBridge();window.plan=await bridge.issue(defaults)}")
                ck("both-issued",await a.evaluate("plan.explicitEdits.length===156") and await b.evaluate("plan.explicitEdits.length===156"))
                x,y=await asyncio.gather(a.evaluate("()=>bridge.stage(plan)"),b.evaluate("()=>bridge.stage(plan)"))
                ck("exclusive-lock-and-idempotence",sorted([x["status"],y["status"]])==["disposable_staged","idempotent"])
                ck("shadow-156",await b.evaluate(f"""()=>{{let x=JSON.parse(localStorage.getItem({json.dumps(H)}));return x.explicitEdits.length===156&&x.approvedPermanentIds===0&&x.identityMappings.length===0}}"""))
                ck("journal-clean",await a.evaluate(f"localStorage.getItem({json.dumps(J)})===null"))
                await a.evaluate("""async()=>{window.crash=makeBridge({qaFaults:true,revision:1});try{await crash.stage(plan,{fault:'crash-after-journal'})}catch(e){window.crashError=String(e)} }""")
                ck("crash-injected",await a.evaluate('crashError.includes("injected_crash-after-journal")'))
                ck("journal-shared",await b.evaluate(f"localStorage.getItem({json.dumps(J)})!==null"))
                rejected=await b.evaluate("async()=>{try{await bridge.stage(plan);return ''}catch(e){return String(e)}}")
                ck("pending-recovery-blocks-stage","pending_recovery_required" in rejected)
                await b.evaluate(f"""()=>{{window.journal=localStorage.getItem({json.dumps(J)});window.before=localStorage.getItem({json.dumps(H)});localStorage.setItem({json.dumps(H)},'external-conflict')}}""")
                conflict=await a.evaluate("async()=>{try{await bridge.recover();return ''}catch(e){return String(e)}}")
                ck("noncooperative-writer-blocked","recovery_conflict_shadow_changed" in conflict)
                ck("conflict-and-journal-retained",await b.evaluate(f'localStorage.getItem({json.dumps(H)})==="external-conflict" && localStorage.getItem({json.dumps(J)})===journal'))
                await b.evaluate(f"()=>localStorage.setItem({json.dumps(H)},before)")
                ck("cross-tab-recover",(await b.evaluate("()=>bridge.recover()"))["recovered"] is True)
                ck("recovery-cleans-journal",await a.evaluate(f"localStorage.getItem({json.dumps(J)})===null"))
                await b.evaluate(f"""()=>localStorage.setItem({json.dumps(J)},'{{"schema":"forged"}}')""")
                corrupt=await a.evaluate("async()=>{try{await bridge.recover();return ''}catch(e){return String(e)}}")
                ck("forged-journal-rejected","corrupt_rollback_journal" in corrupt)
                ck("forged-journal-preserved",await b.evaluate(f"localStorage.getItem({json.dumps(J)})!==null"))
                await b.evaluate(f"()=>localStorage.removeItem({json.dumps(J)})")
                await b.evaluate("""()=>{let x=JSON.parse(localStorage.getItem('wubi06-root-coordinate-overrides-v16-svg'));x.X.at(-1)[1]++;localStorage.setItem('wubi06-root-coordinate-overrides-v16-svg',JSON.stringify(x))}""")
                stale=await a.evaluate("async()=>{try{await bridge.stage(plan);return ''}catch(e){return String(e)}}")
                ck("stale-source-rejected","source_stale_since_issuance" in stale)
                ck("unrelated-preserved",await a.evaluate('localStorage.getItem("r239-unrelated")==="keep"'))
                isolated=await browser.new_context();c=await isolated.new_page();await c.goto(url)
                ck("separate-profile-isolated",await c.evaluate("localStorage.length===0"))
                await isolated.close()
                await a.evaluate("localStorage.clear()")
                ck("cleanup",await b.evaluate("localStorage.length===0"))
                await ctx.close()
            finally:await browser.close()
    except Exception as e:error=repr(e)+"\n"+traceback.format_exc()[-2000:]
    finally:srv.shutdown();srv.server_close()
    result={"round":239,"rootTask":"T04","passed":len(checks),"expected":22,"checks":checks,"allPassed":error is None and len(checks)==22,"error":error,"environment":"real Chromium fresh 127.0.0.1 two tabs Web Locks/localStorage/WebCrypto","fixture":"synthetic 25 keys / 156 slots","productionMigration":"not-run","formalAccepted":False,"userStorageTouched":False}
    (ROOT/"R239_real_browser_QA.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"passed":len(checks),"expected":22,"allPassed":result["allPassed"],"error":error},ensure_ascii=False))
    if not result["allPassed"]:raise SystemExit(1)
if __name__=="__main__":asyncio.run(main())
