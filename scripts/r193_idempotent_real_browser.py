#!/usr/bin/env python3
"""R193 T04: actual R192 ESM in two isolated same-origin Chromium tabs.
Synthetic issuer plan only. Never open the user's browser profile or site.
"""
import asyncio
import http.server
import json
import threading
from pathlib import Path
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parent

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)
    def log_message(self, *args):
        pass
    def guess_type(self, path):
        return 'text/javascript' if path.endswith('.mjs') else super().guess_type(path)

async def main():
    checks = []
    def ck(name, value):
        if not value:
            raise AssertionError(name)
        checks.append(name)

    server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True, executable_path='/usr/bin/chromium' if Path('/usr/bin/chromium').exists() else None, args=['--no-sandbox'])
            try:
                context = await browser.new_context()
                a, b = await context.new_page(), await context.new_page()
                url = f'http://127.0.0.1:{server.server_port}/index.html'
                ck('real-two-tab-origin', (await a.goto(url)).status == 200 and (await b.goto(url)).status == 200)
                ck('real-secure-origin', await a.evaluate('isSecureContext && !!navigator.locks && !!crypto.subtle'))
                ck('fresh-storage', await a.evaluate('localStorage.length===0'))
                await a.evaluate("""async()=>{
                  const {createDisposableTransactionCore}=await import('/r192_idempotent_freshness_core.mjs');
                  const S='r193-synthetic-source', H='__glyphspace_disposable_r193_shadow',
                        J='__glyphspace_disposable_r193_journal';
                  localStorage.setItem(S,'source-A');localStorage.setItem('r193-unrelated','keep');
                  const hex=b=>Array.from(new Uint8Array(b),v=>v.toString(16).padStart(2,'0')).join('');
                  const sha=async s=>hex(await crypto.subtle.digest('SHA-256',new TextEncoder().encode(s)));
                  const plan=Object.freeze({sourceSHA:await sha('source-A')});
                  let gate=null;
                  const payload=()=>({isDisposable:true,approvedPermanentIds:0,identityMappings:[],productionMigration:'not-run',revision:193});
                  const core=createDisposableTransactionCore({sourceKey:S,shadowKey:H,journalKey:J,
                    read:k=>localStorage.getItem(k),
                    write:(k,v)=>v===null?localStorage.removeItem(k):localStorage.setItem(k,v),
                    sha256:sha,withLock:fn=>navigator.locks.request('r193-exclusive',{mode:'exclusive'},fn),
                    verifySourcePlan:async p=>p===plan,
                    buildPayload:async()=>{if(gate){window.R193Ready=true;await gate.promise}return payload()}});
                  window.R193={core,plan,S,H,J,
                    hold:()=>{let release;const promise=new Promise(r=>release=r);gate={promise};window.R193Ready=false;window.R193Release=()=>{gate=null;release()}}};
                }""")
                ck('initial-stage', (await a.evaluate('()=>R193.core.stage(R193.plan)'))['status'] == 'disposable_staged')
                ck('normal-idempotent', (await a.evaluate('()=>R193.core.stage(R193.plan)'))['status'] == 'idempotent')
                before = await b.evaluate('localStorage.getItem("__glyphspace_disposable_r193_shadow")')
                ck('shadow-exists', isinstance(before, str) and '"revision":193' in before)
                await a.evaluate('R193.hold()')
                pending = asyncio.create_task(a.evaluate('()=>R193.core.stage(R193.plan)'))
                for _ in range(100):
                    if await a.evaluate('window.R193Ready===true'):
                        break
                    await asyncio.sleep(.05)
                ck('payload-async-gate-reached', await a.evaluate('window.R193Ready===true'))
                ck('stage-still-pending', not pending.done())
                await b.evaluate('localStorage.setItem("r193-synthetic-source","source-B")')
                await a.evaluate('R193Release()')
                err = ''
                try:
                    await asyncio.wait_for(pending, 10)
                except Exception as exc:
                    err = str(exc)
                ck('stale-idempotent-rejected', 'source_changed_before_idempotent' in err)
                ck('external-source-preserved', await b.evaluate('localStorage.getItem("r193-synthetic-source")==="source-B"'))
                ck('shadow-not-overwritten', await b.evaluate('localStorage.getItem("__glyphspace_disposable_r193_shadow")') == before)
                ck('no-recovery-journal-created', await b.evaluate('localStorage.getItem("__glyphspace_disposable_r193_journal")===null'))
                ck('unrelated-key-preserved', await b.evaluate('localStorage.getItem("r193-unrelated")==="keep"'))
                independent = await browser.new_context()
                c = await independent.new_page()
                await c.goto(url)
                ck('other-context-isolated', await c.evaluate('localStorage.length===0'))
                await independent.close()
                await a.evaluate('localStorage.clear()')
                ck('temporary-storage-cleaned', await b.evaluate('localStorage.length===0'))
                await context.close()
            finally:
                await browser.close()
    finally:
        server.shutdown()
        server.server_close()
    result = {'round':193,'rootTask':'T04','passed':len(checks),'checks':checks,
              'allPassed':True,'issuer':'synthetic-plan-only','formalAccepted':False,
              'productionMigration':'not-run','userStorageTouched':False,
              'environment':'fresh Chromium two-tab 127.0.0.1 real Web Locks/localStorage/WebCrypto'}
    (ROOT/'R193_real_browser_QA.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'passed':len(checks),'allPassed':True}))

if __name__ == '__main__':
    asyncio.run(main())
