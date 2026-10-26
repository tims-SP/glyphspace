#!/usr/bin/env python3
"""R150: disposable real-origin Chromium test of immutable v16 alias shadow plan.
No user profile, production origin, or migration writes are used.
"""
import copy, hashlib, http.server, json, pathlib, re, socketserver, tempfile, threading, sys, shutil
from playwright.sync_api import sync_playwright

ROOT=pathlib.Path(__file__).resolve().parents[1]
KEY='wubi06-root-coordinate-overrides-v16-svg'
checks=[]
def check(id,ok):
    checks.append({'testId':id,'result':'pass' if ok else 'fail'})
    if not ok:raise AssertionError(id)
class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*args):pass

def main():
    html=(ROOT/'index.html').read_bytes()
    check('frozen-html',hashlib.sha256(html).hexdigest()=='fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc')
    defaults=json.loads(re.search(rb'const ROOT_COORDS=(\{[^\n]+\});',html).group(1))
    check('25-keys-156-slots',len(defaults)==25 and sum(map(len,defaults.values()))==156)
    fixture={k:copy.deepcopy(defaults[k]) for k in ('G','K','X')}
    fixture['G'][0][0]+=1;fixture['K'][2][1]+=1;fixture['X'][0][2]+=1
    raw=json.dumps(fixture,separators=(',',':'))
    sha=hashlib.sha256(raw.encode()).hexdigest()
    with tempfile.TemporaryDirectory(prefix='glyphspace-r150-real-') as tmp:
        pathlib.Path(tmp,'index.html').write_text('<!doctype html><title>R150 disposable</title>')
        class H(Handler):
            def __init__(self,*a,**kw):super().__init__(*a,directory=tmp,**kw)
        with socketserver.TCPServer(('127.0.0.1',0),H) as server:
            threading.Thread(target=server.serve_forever,daemon=True).start()
            origin='http://127.0.0.1:'+str(server.server_address[1])
            try:
                with sync_playwright() as p:
                    browser=p.chromium.launch(headless=True, **({"executable_path":shutil.which("chromium")} if shutil.which("chromium") else {}))
                    context=browser.new_context()
                    a,b=context.new_page(),context.new_page()
                    try:
                        for page in (a,b):
                            page.goto(origin+'/index.html',wait_until='domcontentloaded',timeout=15000)
                            page.add_script_tag(path=str(ROOT/'scripts/v036_r148_strict_shadow.js'))
                            page.add_script_tag(path=str(ROOT/'scripts/v036_r150_alias_plan.js'))
                        check('real-same-origin',a.evaluate('location.origin')==b.evaluate('location.origin')==origin)
                        check('real-locks-crypto-store',a.evaluate('!!navigator.locks&&!!crypto.subtle&&!!localStorage'))
                        b.evaluate("()=>{window.r150events=[];addEventListener('storage',e=>{if(e.key==='wubi06-root-coordinate-overrides-v16-svg')r150events.push(e.newValue)})}")
                        a.evaluate("v=>{localStorage.setItem('r150-sentinel','keep');localStorage.setItem('wubi06-root-coordinate-overrides-v16-svg',v)}",raw)
                        b.wait_for_function('r150events.length===1',timeout=5000)
                        check('cross-tab-storage-event',b.evaluate('r150events.length')==1)
                        args={'defaults':defaults,'sourceSHA':sha,'origin':origin}
                        expr="""async arg=>GlyphSpaceR150.planReadOnly({strictReader:GlyphSpaceR148,store:localStorage,cryptoAPI:crypto,defaults:arg.defaults,expectedSourceSHA:arg.sourceSHA,origin:location.origin,expectedOrigin:arg.origin,lockManager:navigator.locks})"""
                        pa=a.evaluate(expr,args);pb=b.evaluate(expr,args)
                        check('cross-tab-plan-equality',pa==pb)
                        check('source-sha-pinned',pa['sourceSHA']==sha)
                        check('three-keys-22-absent',pa['sourceKeys']==['G','K','X'] and len(pa['absentKeys'])==22)
                        check('three-edits',sorted(x['alias'] for x in pa['explicitEdits'])==['G:0','K:2','X:0'])
                        check('alias-count-unique',len(pa['sourceSlotAliases'])==pa['sourceSlots'] and len(set(pa['sourceSlotAliases']))==pa['sourceSlots'])
                        check('no-approved-ids-no-migration',pa['approvedPermanentIds']==0 and pa['writes']==0 and pa['productionMigration']=='not-run')
                        check('verify-plan',a.evaluate("async arg=>GlyphSpaceR150.verifyPlan(await GlyphSpaceR150.planReadOnly({strictReader:GlyphSpaceR148,store:localStorage,cryptoAPI:crypto,defaults:arg.defaults,expectedSourceSHA:arg.sourceSHA,origin:location.origin,expectedOrigin:arg.origin,lockManager:navigator.locks}),crypto)",args))
                        check('raw-source-preserved',a.evaluate("localStorage.getItem('wubi06-root-coordinate-overrides-v16-svg')")==raw)
                        check('unrelated-sentinel-preserved',a.evaluate("localStorage.getItem('r150-sentinel')")=='keep')
                        bad=a.evaluate("""async arg=>{try{await GlyphSpaceR150.planReadOnly({strictReader:GlyphSpaceR148,store:localStorage,cryptoAPI:crypto,defaults:arg.defaults,expectedSourceSHA:arg.sourceSHA,origin:location.origin,expectedOrigin:arg.origin,lockManager:navigator.locks,permanentIds:{'G:0':'draft'}});return false}catch(e){return String(e).includes('formal_ids_not_approved')}}""",args)
                        check('reject-premature-id-binding',bad)
                        check('no-apply-or-commit',a.evaluate("typeof GlyphSpaceR150.apply==='undefined'&&typeof GlyphSpaceR150.commit==='undefined'"))
                    finally:context.close();browser.close()
            finally:server.shutdown()
if __name__=='__main__':
    status='pass'
    try:main()
    except Exception as e:
        status='blocked' if 'ERR_BLOCKED_BY_ADMINISTRATOR' in str(e) or "Executable doesn't exist" in str(e) else 'fail'
        checks.append({'testId':'execution-error','result':status,'detail':repr(e)})
    report={'round':150,'taskId':'T04','result':status,'passed':sum(x['result']=='pass' for x in checks),'checks':checks,'environment':'two real Chromium tabs, disposable loopback origin' if status=='pass' else 'blocked/not-run','formalAcceptance':False,'userStorageTouched':False,'productionMigration':'not-run'}
    out=pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else pathlib.Path('t04_r150_alias_origin_results.json')
    out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print('R150 real-origin',status,report['passed'],'/',len(checks),flush=True)
    raise SystemExit(0 if status=='pass' else 2 if status=='blocked' else 1)
