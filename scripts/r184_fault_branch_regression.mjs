/** R184 Root T04: prove the R183 browser failure was an idempotence-fixture bug,
 * and exercise the exact unchanged shared ESM core's non-idempotent rollback.
 * Private Map only; never accesses browser or user storage.
 */
import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {createDisposableTransactionCore} from './r183_disposable_transaction_core.mjs';
const S='fixture-v16', H='__glyphspace_disposable_r184_shadow', J='__glyphspace_disposable_r184_journal';
const raw='{"G":[[1,2,3]]}', sha=s=>createHash('sha256').update(s).digest('hex');
const plan=Object.freeze({sourceSHA:sha(raw),nonce:'r184-issued'});
const checks=[]; const ck=(name,condition)=>{assert.ok(condition,name);checks.push(name)};
const rejects=async(name,fn,needle)=>{let e;try{await fn()}catch(err){e=String(err)}ck(name,e?.includes(needle))};
let revision=0,writes=0,lockCount=0;
const store=new Map([[S,raw],['unrelated','untouched']]);
const args={sourceKey:S,shadowKey:H,journalKey:J,
  read:k=>store.get(k)??null,
  write:(k,v)=>{writes++;if(v===null)store.delete(k);else store.set(k,v)},
  sha256:async s=>sha(s),
  withLock:async fn=>{lockCount++;return await fn()},
  verifySourcePlan:async p=>p===plan,
  buildPayload:async p=>({schema:'r184-disposable',sourceSHA:p.sourceSHA,revision,
    isDisposable:true,approvedPermanentIds:0,identityMappings:[],productionMigration:'not-run'}),
  allowFaults:true};
const core=createDisposableTransactionCore(args);
ck('first-stage', (await core.stage(plan)).status==='disposable_staged');
const before=store.get(H);
ck('baseline-revision-zero',JSON.parse(before).revision===0);
const writesBefore=writes;
ck('original-fault-test-would-return-idempotent', (await core.stage(plan,{fault:'after-shadow'})).status==='idempotent');
ck('idempotence-has-no-writes',writes===writesBefore);
revision=1;
await rejects('after-journal-fault-exercised',()=>core.stage(plan,{fault:'after-journal'}),'injected_after-journal');
ck('after-journal-restores-exact-shadow',store.get(H)===before);
ck('after-journal-clears-journal',!store.has(J));
await rejects('after-shadow-fault-exercised',()=>core.stage(plan,{fault:'after-shadow'}),'injected_after-shadow');
ck('after-shadow-restores-exact-shadow',store.get(H)===before);
ck('after-shadow-clears-journal',!store.has(J));
await rejects('crash-after-shadow-exercised',()=>core.stage(plan,{fault:'crash-after-shadow'}),'injected_crash-after-shadow');
ck('crash-has-revision-one',JSON.parse(store.get(H)).revision===1);
ck('crash-keeps-journal',store.has(J));
const restart=createDisposableTransactionCore(args);
ck('restart-recovered',(await restart.recover()).recovered===true);
ck('restart-restores-exact-shadow',store.get(H)===before);
ck('restart-clears-journal',!store.has(J));
ck('legacy-preserved',store.get(S)===raw);
ck('unrelated-preserved',store.get('unrelated')==='untouched');
ck('all-operations-locked',lockCount>=6);
revision=2;
ck('post-recovery-stage',(await restart.stage(plan)).status==='disposable_staged');
ck('post-recovery-revision-two',JSON.parse(store.get(H)).revision===2);
const result={round:184,rootTask:'T04',passed:checks.length,checks,
  regression:'R183 GitHub Actions 40630751605 failed because fault test used identical payload',
  environment:'Node private Map, unchanged R183 shared ESM core',
  realSameOrigin:'blocked locally',formalAccepted:false,userStorageTouched:false};
if(!process.argv.includes('--no-write')){
  const fs=await import('node:fs');fs.writeFileSync(new URL('./R184_fault_branch_node_QA.json',import.meta.url),JSON.stringify(result,null,2)+'\n');
}
console.log(JSON.stringify({passed:checks.length,allPassed:true}));
