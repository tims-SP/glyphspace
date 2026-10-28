/** R192 remote CI smoke: actual old and new ESM, no browser or user storage. */
import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {createDisposableTransactionCore as oldCore} from './r189_source_readback_transaction_core.mjs';
import {createDisposableTransactionCore as newCore} from './r192_idempotent_freshness_core.mjs';
const source='fixture-source',S='source',H='__glyphspace_disposable_r192_shadow',J='__glyphspace_disposable_r192_journal';
const sha=x=>createHash('sha256').update(x).digest('hex');
const plan=Object.freeze({sourceSHA:sha(source)});
const payload=()=>({isDisposable:true,approvedPermanentIds:0,identityMappings:[],productionMigration:'not-run',revision:192});
let count=0;
function make(core){
 const data=new Map([[S,source]]);let ready,release,pause=false;
 const gate=new Promise(r=>release=r),entered=new Promise(r=>ready=r);
 const obj=core({sourceKey:S,shadowKey:H,journalKey:J,
  read:k=>data.get(k)??null,write:(k,v)=>v===null?data.delete(k):data.set(k,v),
  sha256:async x=>sha(x),withLock:fn=>fn(),verifySourcePlan:async p=>p===plan,
  buildPayload:async()=>{if(pause){ready();await gate}return payload()}});
 return {data,obj,entered,release,pause:()=>{pause=true}};
}
for(const [name,ctor,expected] of [['old',oldCore,'idempotent'],['new',newCore,'source_changed_before_idempotent']]){
 const f=make(ctor);assert.equal((await f.obj.stage(plan)).status,'disposable_staged');count++;
 const oldShadow=f.data.get(H);f.pause();
 const pending=f.obj.stage(plan);await f.entered;f.data.set(S,'external-change');f.release();
 if(name==='old'){assert.equal((await pending).status,expected);count++}
 else{await assert.rejects(pending,new RegExp(expected));count++}
 assert.equal(f.data.get(H),oldShadow);count++;
 assert.equal(f.data.get(S),'external-change');count++;
 assert.equal(f.data.has(J),false);count++;
}
const f=make(newCore);assert.equal((await f.obj.stage(plan)).status,'disposable_staged');count++;
assert.equal((await f.obj.stage(plan)).status,'idempotent');count++;
assert.equal(f.data.has(J),false);count++;
console.log(JSON.stringify({passed:count,allPassed:count===13,formalAccepted:false}));
assert.equal(count,13);
