const fs=require('fs'),path=require('path'),os=require('os'),http=require('http'),crypto=require('crypto');
const {chromium}=require('playwright');
const root='/tmp/glyphspace-r245f53-docs/scripts';
const files=['v036_r148_strict_shadow.js','v036_r152_source_bound_plan.js','r194_r178_freshness.js','r194_r179_realm.js','r192_idempotent_freshness_core.mjs','r194_real_issuer_r192_bridge.mjs','r194_frozen_root_coords.json'];
const source='wubi06-root-coordinate-overrides-v16-svg',shadow='__glyphspace_disposable_r194_shadow',journal='__glyphspace_disposable_r194_journal',lock='__glyphspace_disposable_r194_exclusive__';
const checks=[], sha=s=>crypto.createHash('sha256').update(s).digest('hex');
function ck(name,condition,detail){checks.push({name,result:condition?'pass':'fail',detail:condition?undefined:detail});if(!condition)throw Error('QA_FAIL '+name+' '+JSON.stringify(detail));}
(async()=>{
 const tmp=fs.mkdtempSync('/tmp/glyphspace-r245f54-real-'); const web=path.join(tmp,'web');fs.mkdirSync(web);
 let browser,server;const log={round:'R245F54',taskId:'T04',sourceType:'synthetic V0.35 25 keys / 156 slots',productionMigration:'not-run',userStorageTouched:false,formalAccepted:false,approvedPermanentIds:0,checks};
 try{
  for(const f of files){fs.copyFileSync(path.join(root,f),path.join(web,f));ck('module-present-'+f,true)}
  fs.writeFileSync(path.join(web,'index.html'),'<!doctype html><meta charset="utf-8"><title>R245F54 disposable</title>');
  server=http.createServer((req,res)=>{const name=decodeURIComponent(req.url.split('?')[0]).slice(1)||'index.html';if(!files.includes(name)&&name!=='index.html'){res.writeHead(404);res.end();return;}res.setHeader('Content-Type',name.endsWith('.mjs')||name.endsWith('.js')?'text/javascript':name.endsWith('.json')?'application/json':'text/html');res.end(fs.readFileSync(path.join(web,name)));});
  await new Promise(r=>server.listen(0,'127.0.0.1',r));const origin='http://127.0.0.1:'+server.address().port;
  ck('loopback-only-server',server.address().address==='127.0.0.1');
  browser=await chromium.launchPersistentContext(path.join(tmp,'profile'),{headless:true,executablePath:'/root/.cache/ms-playwright/chromium_headless_shell-1194/chrome-linux/headless_shell',args:['--no-sandbox']});
  const a=browser.pages()[0],b=await browser.newPage();let errors=[];a.on('pageerror',e=>errors.push('A:'+e));b.on('pageerror',e=>errors.push('B:'+e));
  for(const p of [a,b]){
   await p.goto(origin+'/index.html');for(const f of files.slice(0,4))await p.addScriptTag({url:origin+'/'+f});
   await p.evaluate(async()=>{const m=await import('/r194_real_issuer_r192_bridge.mjs');window.bridgeFactory=m.createRealmIssuedDisposableBridge;window.bridge=m.createRealmIssuedDisposableBridge();window.events=[];addEventListener('storage',e=>window.events.push({key:e.key,url:e.url}));});
  }
  ck('real-shared-origin-two-tabs',await a.evaluate('location.origin')===origin&&await b.evaluate('location.origin')===origin);
  ck('real-Web-Locks-Crypto-Storage',await a.evaluate('isSecureContext&&!!navigator.locks&&!!crypto.subtle&&localStorage instanceof Storage'));
  const defaults=JSON.parse(fs.readFileSync(path.join(web,'r194_frozen_root_coords.json')));ck('25-keys',Object.keys(defaults).length===25);ck('156-slots',Object.values(defaults).reduce((s,a)=>s+a.length,0)===156);
  await a.evaluate(({defaults,source})=>{let d=structuredClone(defaults);for(const a of Object.values(d))for(const p of a)p[0]++;localStorage.setItem(source,JSON.stringify(d));localStorage.setItem('r245f54-unrelated','sentinel')},{defaults,source});
  const raw=await a.evaluate(s=>localStorage.getItem(s),source);log.syntheticSourceSHA256=sha(raw);
  for(const p of [a,b])await p.evaluate(async d=>{window.plan=await bridge.issue(d)},defaults);
  const info=await a.evaluate('({sha:plan.sourceSHA,aliases:plan.sourceSlotAliases.length,edits:plan.explicitEdits.length,approved:plan.approvedPermanentIds})');
  ck('real-issued-156-edits',info.sha===sha(raw)&&info.aliases===156&&info.edits===156&&info.approved===0,info);
  await a.evaluate(n=>{navigator.locks.request(n,{mode:'exclusive'},async()=>{window.holding=true;await new Promise(r=>window.release=r)})},lock);
  await a.waitForFunction('window.holding===true');
  await b.evaluate(()=>{window.stageState='pending';bridge.stage(plan).then(r=>window.stageState=r.status,e=>window.stageState='error:'+e.message)});
  await b.waitForTimeout(300);ck('cross-tab-Web-Lock-waits',await b.evaluate('stageState')==='pending');
  await a.evaluate('window.release()');await b.waitForFunction('stageState!=="pending"');
  ck('cross-tab-stage-after-release',await b.evaluate('stageState')==='disposable_staged',await b.evaluate('stageState'));
  await a.waitForFunction('events.some(e=>e.key==="__glyphspace_disposable_r194_shadow")');
  ck('real-storage-event-observed',await a.evaluate('events.some(e=>e.key==="__glyphspace_disposable_r194_shadow")'));
  const payload=JSON.parse(await a.evaluate(s=>localStorage.getItem(s),shadow));
  ck('disposable-shadow-156-no-approved-ids',payload.explicitEdits.length===156&&payload.sourceSlotAliases.length===156&&payload.approvedPermanentIds===0&&payload.identityMappings.length===0&&payload.productionMigration==='not-run');
  ck('source-exact-after-stage',await a.evaluate(s=>localStorage.getItem(s),source)===raw);
  ck('unrelated-sentinel-preserved',await a.evaluate('localStorage.getItem("r245f54-unrelated")')==='sentinel');
  ck('journal-clean-after-stage',await a.evaluate(s=>localStorage.getItem(s),journal)===null);
  const idem=await a.evaluate(eval('async()=> {const r=await bridge.stage(plan);return {status:r?.status,keys:Object.keys(r||{}),r}}'));console.log('IDEMPOTENT_DEBUG',JSON.stringify(idem));ck('other-tab-idempotent',idem.status==='idempotent',idem);
  const crash=await a.evaluate(eval('async()=>{try{await bridgeFactory({qaFaults:true,revision:1}).stage(plan,{fault:"crash-after-journal"});return "unexpected"}catch(e){return e.message}}'));
  ck('crash-after-journal-real',crash==='injected_crash-after-journal',crash);
  const j=await a.evaluate(s=>localStorage.getItem(s),journal),before=await a.evaluate(s=>localStorage.getItem(s),shadow);
  ck('crash-journal-retained',typeof j==='string'&&j.length>100);
  const pending=await b.evaluate(eval('async()=>{try{await bridge.stage(plan);return "unexpected"}catch(e){return e.message}}'));
  ck('other-tab-rejects-pending',pending==='pending_recovery_required',pending);
  await a.evaluate(s=>localStorage.setItem(s,'foreign-writer'),shadow);
  const conflict=await b.evaluate(eval('async()=>{try{await bridge.recover();return "unexpected"}catch(e){return e.message}}'));
  ck('foreign-writer-conflict-fails-closed',conflict==='recovery_conflict_shadow_changed',conflict);
  ck('foreign-bytes-and-journal-preserved',await a.evaluate(s=>localStorage.getItem(s),shadow)==='foreign-writer'&&await a.evaluate(s=>localStorage.getItem(s),journal)===j);
  await a.evaluate(({s,v})=>localStorage.setItem(s,v),{s:shadow,v:before});
  const recovered=await b.evaluate(eval('async()=>bridge.recover()'));
  ck('other-tab-recovers',recovered.recovered===true&&await a.evaluate(s=>localStorage.getItem(s),shadow)===before&&await a.evaluate(s=>localStorage.getItem(s),journal)===null,recovered);
  await a.evaluate(s=>{let d=JSON.parse(localStorage.getItem(s));d.M[0][0]++;localStorage.setItem(s,JSON.stringify(d))},source);
  const stale=await b.evaluate(eval('async()=>{try{await bridge.stage(plan);return "unexpected"}catch(e){return e.message}}'));
  ck('stale-source-rejected',stale!=='unexpected'&&/source|stale|invalid/.test(stale),stale);
  ck('stale-does-not-write-shadow',await a.evaluate(s=>localStorage.getItem(s),shadow)===before&&await a.evaluate(s=>localStorage.getItem(s),journal)===null);
  await a.evaluate(({s,v})=>localStorage.setItem(s,v),{s:source,v:raw});
  ck('restored-source-idempotent',await b.evaluate(eval('async()=> (await bridge.stage(plan)).status'))==='idempotent');
  ck('no-page-errors',errors.length===0,errors);
  ck('no-approved-IDs',JSON.parse(await a.evaluate(s=>localStorage.getItem(s),shadow)).approvedPermanentIds===0);
 }catch(e){log.error=String(e);log.stack=e.stack;}
 finally{if(browser)await browser.close();if(server)await new Promise(r=>server.close(r));log.privateProfileRemoved=false;fs.rmSync(tmp,{recursive:true,force:true});log.privateProfileRemoved=!fs.existsSync(tmp);}
 ck('private-profile-deleted',log.privateProfileRemoved);
 log.passed=checks.filter(x=>x.result==='pass').length;log.failed=checks.filter(x=>x.result==='fail').length;log.allPassed=!log.error&&log.failed===0;
 fs.writeFileSync('/tmp/glyphspace-r245f54-browser/R245F54_remote_real_origin_QA.json',JSON.stringify(log,null,2)+'\n');
 console.log(JSON.stringify({passed:log.passed,failed:log.failed,allPassed:log.allPassed,error:log.error,sourceSHA:log.syntheticSourceSHA256,privateProfileRemoved:log.privateProfileRemoved}));
 if(!log.allPassed)process.exitCode=1;
})().catch(e=>{console.error(e.stack);process.exitCode=1});
