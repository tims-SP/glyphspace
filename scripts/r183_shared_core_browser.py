#!/usr/bin/env python3
"""R183: same ESM transaction core in real Chromium same-origin disposable context.
Never navigates to or reads any user profile/site; temp HTTP root and fresh context.
"""
import hashlib, http.server, json, tempfile, threading, shutil
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parent
SETUP=r'''async () => {
 const {createDisposableTransactionCore}=await import('/quarantine_transaction_core.mjs');
 const S='glyphspace-r183-v16-fixture',H='__glyphspace_disposable_r183_shadow',J='__glyphspace_disposable_r183_journal';
 const sha=async s=>Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256',new TextEncoder().encode(s)))).map(v=>v.toString(16).padStart(2,'0')).join('');
 const plan={sourceSHA:await sha(localStorage.getItem(S)||''),nonce:'issued-r183-fixture'};
 const args={sourceKey:S,shadowKey:H,journalKey:J,
   read:k=>localStorage.getItem(k),write:(k,v)=>v===null?localStorage.removeItem(k):localStorage.setItem(k,v),
   sha256:sha,withLock:fn=>navigator.locks.request('glyphspace-r183-disposable-lock',{mode:'exclusive'},fn),
   verifySourcePlan:async p=>p?.nonce==='issued-r183-fixture'&&p.sourceSHA===plan.sourceSHA,
   buildPayload:async p=>({schema:'r183',sourceSHA:p.sourceSHA,isDisposable:true,approvedPermanentIds:0,
      identityMappings:[],productionMigration:'not-run',revision:window.R183Revision||0}),allowFaults:true};
 window.R183={S,H,J,sha,plan,core:createDisposableTransactionCore(args)};
 return {secure:isSecureContext,locks:!!navigator.locks,sourceSHA:plan.sourceSHA};
}'''
class Handler(http.server.SimpleHTTPRequestHandler):
 def __init__(self,*a,**kw):super().__init__(*a,directory=str(ROOT),**kw)
 def log_message(self,*a):pass
 def guess_type(self,path):
  return 'text/javascript' if path.endswith('.mjs') else super().guess_type(path)
def main():
 checks=[]
 def ck(n,v):
  if not v:raise AssertionError(n)
  checks.append(n)
 def rejects(n,fn,needle):
  try:fn()
  except Exception as e:ck(n,needle in str(e));return
  raise AssertionError(n+': unexpectedly passed')
 server=http.server.ThreadingHTTPServer(('127.0.0.1',0),Handler)
 threading.Thread(target=server.serve_forever,daemon=True).start()
 url=f'http://127.0.0.1:{server.server_port}/index.html'
 try:
  with sync_playwright() as p:
   browser=p.chromium.launch(executable_path='/usr/bin/chromium' if Path('/usr/bin/chromium').exists() else None,headless=True,args=['--no-sandbox'])
   try:
    context=browser.new_context();a=context.new_page();b=context.new_page()
    ck('real-two-tab-http',a.goto(url).status==200 and b.goto(url).status==200)
    ck('initial-empty',a.evaluate('localStorage.length===0'))
    raw=json.dumps({'G':[[1,2,3]],'K':[[4,5,6]]},separators=(',',':'))
    a.evaluate('raw=>localStorage.setItem("glyphspace-r183-v16-fixture",raw)',raw)
    x=a.evaluate(SETUP);y=b.evaluate(SETUP)
    ck('real-secure-context',x['secure'] and y['secure'])
    ck('real-web-locks',x['locks'] and y['locks'])
    ck('same-esm-digest',x['sourceSHA']==y['sourceSHA']==hashlib.sha256(raw.encode()).hexdigest())
    ck('same-core-stage',a.evaluate('()=>R183.core.stage(R183.plan)')['status']=='disposable_staged')
    ck('same-core-other-tab-idempotent',b.evaluate('()=>R183.core.stage(R183.plan)')['status']=='idempotent')
    ck('no-id-mappings',a.evaluate('()=>{const x=JSON.parse(localStorage.getItem(R183.H));return x.approvedPermanentIds===0&&x.identityMappings.length===0}'))
    ck('source-preserved',b.evaluate('raw=>localStorage.getItem(R183.S)===raw',raw))
    # R184: the original fault checks ran against an identical staged payload.
    # The core correctly returned idempotent before entering the fault branch;
    # require a distinct *disposable* revision and verify exact rollback bytes.
    original_shadow=a.evaluate('localStorage.getItem(R183.H)')
    ck('baseline-revision-zero',json.loads(original_shadow)['revision']==0)
    a.evaluate('window.R183Revision=1')
    rejects('fault-after-journal',lambda:a.evaluate('()=>R183.core.stage(R183.plan,{fault:"after-journal"})'),'injected_after-journal')
    ck('journal-fault-restores-original',a.evaluate('before=>localStorage.getItem(R183.H)===before',original_shadow))
    rejects('fault-rollback',lambda:a.evaluate('()=>R183.core.stage(R183.plan,{fault:"after-shadow"})'),'injected_after-shadow')
    ck('rollback-restores-original',a.evaluate('before=>localStorage.getItem(R183.H)===before',original_shadow))
    ck('journal-clean',a.evaluate('localStorage.getItem(R183.J)===null'))
    rejects('crash-after-shadow',lambda:a.evaluate('()=>R183.core.stage(R183.plan,{fault:"crash-after-shadow"})'),'injected_crash-after-shadow')
    ck('crash-leaves-new-disposable-revision',b.evaluate('()=>JSON.parse(localStorage.getItem("__glyphspace_disposable_r183_shadow")).revision===1'))
    ck('journal-persisted',b.reload().status==200 and b.evaluate('localStorage.getItem("__glyphspace_disposable_r183_journal")!==null'))
    b.evaluate(SETUP)
    ck('recovery-new-document',b.evaluate('()=>R183.core.recover()')['recovered'])
    ck('recovery-restores-original',b.evaluate('before=>localStorage.getItem(R183.H)===before',original_shadow))
    ck('journal-cleared',b.evaluate('localStorage.getItem(R183.J)===null'))
    a.evaluate('raw=>localStorage.setItem(R183.S,raw)',raw+' changed')
    rejects('stale-source-rejected',lambda:b.evaluate('()=>R183.core.stage(R183.plan)'),'source_stale_since_issuance')
    ck('no-legacy-write',a.evaluate('raw=>localStorage.getItem(R183.S)===raw',raw+' changed'))
    other=browser.new_context();c=other.new_page();c.goto(url)
    ck('fresh-context-isolated',c.evaluate('localStorage.length===0'));other.close()
    a.evaluate('localStorage.clear()');ck('cleanup',a.evaluate('localStorage.length===0'))
    context.close()
   finally:browser.close()
 finally:server.shutdown();server.server_close()
 result={'round':184,'rootTask':'T04','passed':len(checks),'allPassed':True,'checks':checks,
 'environment':'real Chromium fresh profile 127.0.0.1 two tabs; shared ESM module',
 'formalAccepted':False,'productionMigration':'not-run','userStorageTouched':False,
 'r183FailedCI':40630751605,'faultBranch':'non-idempotent revision 1'}
 (ROOT/'R183_shared_core_browser_QA.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'passed':len(checks),'allPassed':True}))
if __name__=='__main__':main()
