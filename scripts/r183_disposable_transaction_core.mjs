/** R183 Root T04 — shared disposable transaction core for Node and browser.
 * No globals, no Storage access, no production migration or ID assignment.
 * The caller MUST supply a disposable adapter, independent source attestation,
 * a real cooperative lock, and SHA-256. Only quarantine keys may be written.
 */
export function createDisposableTransactionCore({read,write,sha256,withLock,
  sourceKey,shadowKey,journalKey,verifySourcePlan,buildPayload,allowFaults=false}) {
  for (const f of [read,write,sha256,withLock,verifySourcePlan,buildPayload])
    if(typeof f!=='function') throw Error('missing_required_adapter');
  if(![sourceKey,shadowKey,journalKey].every(x=>typeof x==='string'&&x.length>0)||
     new Set([sourceKey,shadowKey,journalKey]).size!==3||
     !shadowKey.startsWith('__glyphspace_disposable_')||
     !journalKey.startsWith('__glyphspace_disposable_')) throw Error('unsafe_key_namespace');
  const schema='glyphspace-r183-disposable-journal-v1';
  const hex=/^[0-9a-f]{64}$/;
  let busy=false;
  const get=k=>read(k);
  const put=(k,v)=>{
    if(k!==shadowKey&&k!==journalKey)throw Error('write_outside_disposable_namespace');
    if(v!==null&&typeof v!=='string')throw Error('invalid_write_value');
    return write(k,v);
  };
  const digest=async v=>{
    const h=await sha256(v);
    if(typeof h!=='string'||!hex.test(h))throw Error('invalid_digest');
    return h;
  };
  const sourceDigest=async()=>{
    const raw=get(sourceKey);
    if(typeof raw!=='string')throw Error('missing_legacy_source');
    return digest(raw);
  };
  const journalFor=async(before,sourceSHA)=>JSON.stringify({schema,sourceSHA,before,
    beforeSHA:await digest(before??'')});
  const checkJournal=async raw=>{
    let j;
    try{j=JSON.parse(raw)}catch{throw Error('corrupt_rollback_journal')}
    if(!j||j.schema!==schema||!hex.test(j.sourceSHA)||
       !(j.before===null||typeof j.before==='string')||
       !hex.test(j.beforeSHA)||j.beforeSHA!==await digest(j.before??''))
      throw Error('corrupt_rollback_journal');
    return j;
  };
  const lock=fn=>withLock(async()=>{
    if(busy)throw Error('reentrant_transaction');
    busy=true;try{return await fn()}finally{busy=false}
  });
  async function stage(plan,{fault=null}={}) {
    if(fault!==null&&!allowFaults)throw Error('fault_injection_disabled');
    return lock(async()=>{
      if(get(journalKey)!==null)throw Error('pending_recovery_required');
      if(!plan||!hex.test(plan.sourceSHA)||await verifySourcePlan(plan)!==true)
        throw Error('invalid_issued_plan');
      if(await sourceDigest()!==plan.sourceSHA)throw Error('source_stale_since_issuance');
      const payload=await buildPayload(plan);
      if(!payload||payload.isDisposable!==true||payload.approvedPermanentIds!==0||
         payload.productionMigration!=='not-run'||
         !Array.isArray(payload.identityMappings)||payload.identityMappings.length!==0)
        throw Error('unsafe_payload');
      const next=JSON.stringify(payload);
      const before=get(shadowKey);
      if(before===next)return Object.freeze({status:'idempotent',writes:0});
      let journalWritten=false;
      try {
        const j=await journalFor(before,plan.sourceSHA);
        put(journalKey,j);journalWritten=true;
        if(fault==='after-journal'||fault==='crash-after-journal')
          throw Object.assign(Error('injected_'+fault),{crash:fault.startsWith('crash-')});
        if(await sourceDigest()!==plan.sourceSHA)throw Error('source_changed_before_shadow');
        put(shadowKey,next);
        if(fault==='after-shadow'||fault==='crash-after-shadow')
          throw Object.assign(Error('injected_'+fault),{crash:fault.startsWith('crash-')});
        if(await sourceDigest()!==plan.sourceSHA)throw Error('source_changed_before_commit');
        put(journalKey,null);
        return Object.freeze({status:'disposable_staged',sourceSHA:plan.sourceSHA});
      } catch(e) {
        if(journalWritten&&!e.crash){
          try{put(shadowKey,before);put(journalKey,null)}
          catch(rollbackError){throw new AggregateError([e,rollbackError],'rollback_failed_journal_retained')}
        }
        throw e;
      }
    });
  }
  async function recover(){return lock(async()=>{
    const raw=get(journalKey);
    if(raw===null)return Object.freeze({recovered:false});
    const j=await checkJournal(raw);
    let changed;
    try{changed=await sourceDigest()!==j.sourceSHA}catch{changed=true}
    put(shadowKey,j.before);put(journalKey,null);
    return Object.freeze({recovered:true,sourceChangedSinceJournal:changed});
  })}
  return Object.freeze({stage,recover,keys:Object.freeze({sourceKey,shadowKey,journalKey})});
}
