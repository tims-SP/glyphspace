#!/usr/bin/env python3
"""R149 T04: actual Chromium same-origin/Web Locks/localStorage strict R148 reader QA.
Only synthetic data on disposable 127.0.0.1, never a production migration.
"""
import copy, hashlib, http.server, json, pathlib, re, socketserver, tempfile, threading
from playwright.sync_api import sync_playwright

FROZEN_SHA='fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc'
KEY='wubi06-root-coordinate-overrides-v16-svg'
ROOT=pathlib.Path(__file__).resolve().parents[1]
checks=[]
def check(name,ok):
    checks.append({'testId':name,'result':'pass' if ok else 'fail'})
    if not ok: raise AssertionError(name)
class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*args): pass
def main():
    raw_html=(ROOT/'index.html').read_bytes()
    check('frozen-html-sha',hashlib.sha256(raw_html).hexdigest()==FROZEN_SHA)
    match=re.search(rb'const ROOT_COORDS=(\{[^\n]+\});',raw_html)
    if not match: raise AssertionError('missing ROOT_COORDS')
    defaults=json.loads(match.group(1))
    check('frozen-25-keys-156-slots',len(defaults)==25 and sum(map(len,defaults.values()))==156)
    partial={k:copy.deepcopy(defaults[k]) for k in ('G','K','X')}
    partial['G'][0][0]+=1;partial['K'][2][1]+=1;partial['X'][0][2]+=1
    raw=json.dumps(partial,separators=(',',':'))
    expected=hashlib.sha256(raw.encode()).hexdigest()
    js=str(ROOT/'scripts/v036_r148_strict_shadow.js')
    with tempfile.TemporaryDirectory(prefix='glyphspace-r149-origin-') as tmp:
        pathlib.Path(tmp,'index.html').write_text('<!doctype html><title>R149 synthetic only</title>')
        class H(Handler):
            def __init__(self,*a,**kw): super().__init__(*a,directory=tmp,**kw)
        with socketserver.TCPServer(('127.0.0.1',0),H) as server:
            threading.Thread(target=server.serve_forever,daemon=True).start()
            origin='http://127.0.0.1:'+str(server.server_address[1])
            try:
                with sync_playwright() as p:
                    browser=p.chromium.launch(headless=True)
                    ctx=browser.new_context()
                    a,b=ctx.new_page(),ctx.new_page()
                    try:
                        for page in (a,b):
                            page.goto(origin+'/index.html',wait_until='domcontentloaded',timeout=15000)
                            page.add_script_tag(path=js)
                        check('two-tabs-same-real-origin',a.evaluate('location.origin')==b.evaluate('location.origin')==origin)
                        check('real-crypto-locks-localstorage',a.evaluate('!!crypto.subtle&&!!navigator.locks&&!!localStorage'))
                        b.evaluate("()=>{window.events=[];addEventListener('storage',e=>{if(e.key==='wubi06-root-coordinate-overrides-v16-svg')events.push(e.newValue)})}")
                        a.evaluate("arg=>{localStorage.setItem('r149-sentinel','keep');localStorage.setItem(arg.key,arg.raw)}",{'key':KEY,'raw':raw})
                        b.wait_for_function('events.length===1',timeout=5000)
                        check('cross-tab-storage-event',b.evaluate('events.length')==1)
                        before=a.evaluate('Object.keys(localStorage).sort()')
                        args={'defaults':defaults,'expected':expected,'origin':origin}
                        read="""async arg=>GlyphSpaceR148.readLegacy({store:localStorage,cryptoAPI:crypto,defaults:arg.defaults,expectedSourceSHA:arg.expected,origin:location.origin,expectedOrigin:arg.origin,lockManager:navigator.locks})"""
                        ra=a.evaluate(read,args);rb=b.evaluate(read,args)
                        check('both-tabs-identical',ra==rb)
                        check('three-keys-22-absent',ra['sourceKeys']==['G','K','X'] and len(ra['absentKeys'])==22)
                        check('three-edits',sorted(e['alias'] for e in ra['explicitEdits'])==['G:0','K:2','X:0'])
                        check('pinned-raw-sha',ra['sourceSHA']==expected)
                        check('read-only-no-approved-id',ra['writes']==0 and ra['approvedPermanentIds']==0 and ra['productionMigration']=='not-run')
                        check('source-raw-unchanged',a.evaluate('k=>localStorage.getItem(k)',KEY)==raw)
                        check('unrelated-storage-unchanged',a.evaluate("localStorage.getItem('r149-sentinel')")=='keep')
                        check('no-added-keys',a.evaluate('Object.keys(localStorage).sort()')==before)
                        def reject(name,source,fragment):
                            a.evaluate('arg=>localStorage.setItem(arg.key,arg.raw)',{'key':KEY,'raw':source})
                            error=a.evaluate("""async arg=>{try{await GlyphSpaceR148.readLegacy({store:localStorage,cryptoAPI:crypto,defaults:arg.defaults,expectedSourceSHA:null,origin:location.origin,expectedOrigin:arg.origin,lockManager:navigator.locks});return 'ACCEPTED'}catch(e){return String(e)}}""",args)
                            check('reject-'+name,error!='ACCEPTED' and fragment in error)
                        g=json.dumps(partial['G'],separators=(',',':'))
                        reject('literal-duplicate','{"G":'+g+',"G":'+g+'}','duplicate_json_key')
                        reject('escaped-duplicate','{"G":'+g+',"\\u0047":'+g+'}','duplicate_json_key')
                        reject('nested-duplicate','{"G":'+g+',"x":{"a":1,"a":2}}','duplicate_json_key')
                        reject('wrong-length',json.dumps({'G':partial['G'][:-1]}),'invalid_source_key_or_length')
                        reject('out-of-range',json.dumps({'G':[[91,28,20]]+partial['G'][1:]}),'invalid_coordinate')
                        reject('unknown-key',json.dumps({'ZZ':[[12,28,20]]}),'invalid_source_key_or_length')
                        reject('invalid-json','{"G":','invalid_json')
                        a.evaluate('arg=>localStorage.setItem(arg.key,arg.raw)',{'key':KEY,'raw':raw})
                        bad=a.evaluate("""async arg=>{try{await GlyphSpaceR148.readLegacy({store:localStorage,cryptoAPI:crypto,defaults:arg.defaults,expectedSourceSHA:'0'.repeat(64),origin:location.origin,expectedOrigin:arg.origin,lockManager:navigator.locks});return false}catch(e){return String(e).includes('source_changed')}}""",args)
                        check('wrong-source-sha-rejected',bad)
                        changed=copy.deepcopy(defaults);changed['G'][0][0]+=1
                        bad=a.evaluate("""async arg=>{try{await GlyphSpaceR148.readLegacy({store:localStorage,cryptoAPI:crypto,defaults:arg.defaults,expectedSourceSHA:arg.expected,origin:location.origin,expectedOrigin:arg.origin,lockManager:navigator.locks});return false}catch(e){return String(e).includes('untrusted_defaults')}}""",{**args,'defaults':changed})
                        check('mutated-frozen-defaults-rejected',bad)
                        bad=a.evaluate("""async arg=>{try{await GlyphSpaceR148.readLegacy({store:localStorage,cryptoAPI:crypto,defaults:arg.defaults,expectedSourceSHA:arg.expected,origin:location.origin,expectedOrigin:'http://127.0.0.1:1',lockManager:navigator.locks});return false}catch(e){return String(e).includes('unsafe_origin')}}""",args)
                        check('origin-mismatch-rejected',bad)
                        a.evaluate("""()=>{window.release=null;window.held=false;navigator.locks.request('__glyphspace_r148_strict_shadow_read_only__',{mode:'exclusive'},()=>new Promise(resolve=>{window.release=resolve;window.held=true}))}""")
                        a.wait_for_function('window.held',timeout=5000)
                        b.evaluate("""arg=>{window.done=false;window.answer=null;GlyphSpaceR148.readLegacy({store:localStorage,cryptoAPI:crypto,defaults:arg.defaults,expectedSourceSHA:arg.expected,origin:location.origin,expectedOrigin:arg.origin,lockManager:navigator.locks}).then(r=>{window.done=true;window.answer=r},e=>{window.done=true;window.answer=String(e)})}""",args)
                        b.wait_for_timeout(250)
                        check('real-exclusive-lock-blocks-shared-read',b.evaluate('!window.done'))
                        a.evaluate('window.release()')
                        b.wait_for_function('window.done',timeout=5000)
                        check('queued-read-resumes-after-release',b.evaluate('window.answer.sourceSHA')==expected)
                        check('final-raw-unchanged',a.evaluate('k=>localStorage.getItem(k)',KEY)==raw)
                        check('final-sentinel-unchanged',a.evaluate("localStorage.getItem('r149-sentinel')")=='keep')
                    finally:
                        ctx.close();browser.close()
            finally: server.shutdown()
if __name__=='__main__':
    status='pass'
    try: main()
    except Exception as exc:
        status='blocked' if 'ERR_BLOCKED_BY_ADMINISTRATOR' in str(exc) else 'fail'
        checks.append({'testId':'execution-error','result':status,'detail':repr(exc)})
    report={'round':149,'taskId':'T04','result':status,'passed':sum(x['result']=='pass' for x in checks),'checks':checks,'environment':'disposable real Chromium 127.0.0.1 two tabs','formalAcceptance':False,'userStorageTouched':False,'productionMigration':'not-run','screenReaderQA':'not-run','mobileDeviceQA':'not-run'}
    pathlib.Path('t04_r149_strict_origin_results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print('R149 real-origin',status,report['passed'],'/',len(checks))
    raise SystemExit(0 if status=='pass' else (2 if status=='blocked' else 1))
