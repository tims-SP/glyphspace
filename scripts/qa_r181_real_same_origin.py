#!/usr/bin/env python3
"""R181 T04 browser primitives QA: disposable loopback origin and fresh context only."""
import hashlib, http.server, json, os, tempfile, threading
from pathlib import Path
from playwright.sync_api import sync_playwright

EXPECTED_HTML='fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc'
EXPECTED_JPEG='df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49'
ROOT=Path(__file__).resolve().parents[1]
assert hashlib.sha256((ROOT/'index.html').read_bytes()).hexdigest()==EXPECTED_HTML
# Repo reference location may differ; check frozen entry only before browser work.
checks=[]
def ck(name, condition):
    assert condition,name
    checks.append(name)
class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self,*args,directory=None,**kwargs):super().__init__(*args,directory=directory,**kwargs)
    def log_message(self,*args):pass
with tempfile.TemporaryDirectory(prefix='glyphspace-r181-ci-') as d:
    Path(d,'index.html').write_text('<!doctype html><meta charset="utf-8"><title>R181</title>',encoding='utf8')
    server=http.server.ThreadingHTTPServer(('127.0.0.1',0),lambda *a,**kw:Handler(*a,directory=d,**kw))
    threading.Thread(target=server.serve_forever,daemon=True).start()
    url=f'http://127.0.0.1:{server.server_port}/index.html'
    try:
        with sync_playwright() as p:
            browser=p.chromium.launch(channel='chrome',headless=True,args=['--no-sandbox'])
            try:
                context=browser.new_context()
                a=context.new_page(); b=context.new_page()
                ck('first-real-http-200',a.goto(url,timeout=15000).status==200)
                ck('second-real-http-200',b.goto(url,timeout=15000).status==200)
                ck('actual-same-origin',a.evaluate('location.origin')==b.evaluate('location.origin')==url.rsplit('/',1)[0])
                ck('secure-context',a.evaluate('isSecureContext'))
                ck('web-locks-available',a.evaluate('typeof navigator.locks?.request==="function"'))
                ck('webcrypto-available',a.evaluate('typeof crypto.subtle?.digest==="function"'))
                ck('localstorage-available',a.evaluate('typeof localStorage?.setItem==="function"'))
                ck('fresh-storage-empty',a.evaluate('localStorage.length===0') and b.evaluate('localStorage.length===0'))
                key='glyphspace-r181-ephemeral-fixture'
                b.evaluate('window.events=[];addEventListener("storage",e=>window.events.push({key:e.key,old:e.oldValue,newValue:e.newValue}))')
                a.evaluate('k=>localStorage.setItem(k,"v16-1")',key)
                b.wait_for_function('window.events.length===1',timeout=8000)
                ck('storage-event-cross-tab',b.evaluate('k=>window.events[0].key===k&&window.events[0].newValue==="v16-1"',key))
                ck('storage-visible-cross-tab',b.evaluate('k=>localStorage.getItem(k)==="v16-1"',key))
                a.evaluate('''() => {window.state="waiting";window.hold=navigator.locks.request("r181-test-lock",async()=>{window.state="held";await new Promise(resolve=>window.release=resolve);window.state="released"});}''')
                a.wait_for_function('window.state==="held"')
                b.evaluate('''() => {window.state="waiting";window.wait=navigator.locks.request("r181-test-lock",async()=>{window.state="acquired"});}''')
                b.wait_for_timeout(200)
                ck('web-lock-exclusive',b.evaluate('window.state==="waiting"'))
                a.evaluate('window.release()')
                b.wait_for_function('window.state==="acquired"')
                ck('web-lock-handoff',a.evaluate('window.state==="released"'))
                digest='''async k=>navigator.locks.request("r181-digest-lock",{mode:"exclusive"},async()=>{const data=new TextEncoder().encode(localStorage.getItem(k));const b=await crypto.subtle.digest("SHA-256",data);return Array.from(new Uint8Array(b)).map(x=>x.toString(16).padStart(2,"0")).join("")})'''
                first=b.evaluate(digest,key)
                ck('real-crypto-fingerprint',first==hashlib.sha256(b'v16-1').hexdigest())
                a.evaluate('k=>localStorage.setItem(k,"v16-2")',key)
                second=b.evaluate(digest,key)
                ck('stale-source-detected',second!=first and second==hashlib.sha256(b'v16-2').hexdigest())
                separate=browser.new_context(); c=separate.new_page();c.goto(url)
                ck('context-isolation',c.evaluate('k=>localStorage.getItem(k)===null',key))
                separate.close()
                a.evaluate('k=>localStorage.removeItem(k)',key)
                ck('test-fixture-cleaned',a.evaluate('k=>localStorage.getItem(k)===null',key))
                context.close()
            finally:browser.close()
    finally:server.shutdown();server.server_close()
assert len(checks)==16
result={'round':181,'rootTask':'T04','passed':16,'expected':16,'allPassed':True,'checks':checks,'realSameOrigin':True,'disposableContext':True,'userStorageTouched':False,'productionMigration':'not-run','formalAccepted':False,'realScreenReader':'not-run','realDevices':'not-run'}
Path('R181_real_same_origin_CI_QA.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'passed':16,'allPassed':True}))
