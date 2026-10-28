/** R187 / Root T04: disposable conflict-aware transaction core.
 * Candidate-only; no production migration, stable IDs, or user Storage access.
 * Unlike R183, a recovery journal records typed before/next SHA and refuses
 * to overwrite a shadow changed by a non-cooperating writer. Web Locks alone
 * cannot exclude scripts which ignore the lock; this is fail-closed detection,
 * not a general atomic compare-and-swap primitive for localStorage.
 * R187 closes R186 null/empty shadow aliasing; R186 v2 journals fail closed.
 */
export function createDisposableTransactionCore({read,write,sha256,withLock,
  sourceKey,shadowKey,journalKey,verifySourcePlan,buildPayload,allowFaults=false}) {
  for(const fn of [read,write,sha256,withLock,verifySourcePlan,buildPayload])
    if(typeof fn!=='function')throw Error('missing_required_adapter');
  if(![sourceKey,shadowKey,journalKey].every(k=>typeof k==='string'&&k.length>0)||
    new Set([sourceKey,shadowKey,journalKey]).size!==3||
    !shadowKey.startsWith('__glyphspace_disposable_')||
    !journalKey.startsWith('__glyphspace_disposable_'))throw Error('unsafe_key_namespace');
  const schema='glyphspace-r187-disposable-journal-v3';
  const hex=/^[0-9a-f]{64}$/;
  const allowedFaults=new Set([null,'after-journal','after-shadow','crash-after-journal','crash-after-shadow']);
  let busy=false;
  const get=k=>read(k);
  const put=(k,v)=>{
    if(k!==shadowKey&&k!==journalKey)throw Error('write_outside_disposable_namespace');
    if(v!==null&&typeof v!=='string')throw Error('invalid_write_value');
    return write(k,v);
  };
  const digest=async raw=>{
    const value=await sha256(raw);
    if(typeof value!=='string'||!hex.test(value))throw Error('invalid_digest');
    return value;
  };
  const sourceDigest=async()=>{
    const raw=get(sourceKey);
    if(typeof raw!=='string')throw Error('missing_legacy_source');
    return digest(raw);
  };
  const lock=fn=>withLock(async()=>{
    if(busy)throw Error('reentrant_transaction');
    busy=true;try{return await fn()}finally{busy=false}
  });
  // A missing shadow and an explicitly stored empty string are DIFFERENT states.
  // Hash the typed storage slot, never (raw ?? ''), to prevent null/empty aliasing.
  const slotDigest=raw=>digest(JSON.stringify([raw===null?0:1,raw]));
  const journalFor=async(before,next,sourceSHA)=>JSON.stringify({schema,sourceSHA,
    before,beforeSHA:await slotDigest(before),nextSHA:await slotDigest(next)});
  const parseJournal=async raw=>{
    let j;
    try{j=JSON.parse(raw)}catch{throw Error('corrupt_rollback_journal')}
    if(!j||typeof j!=='object'||Array.isArray(j)||
      Object.keys(j).sort().join(',')!=='before,beforeSHA,nextSHA,schema,sourceSHA'||
      j.schema!==schema||!hex.test(j.sourceSHA)||
      !(j.before===null||typeof j.before==='string')||
      !hex.test(j.beforeSHA)||!hex.test(j.nextSHA)||
      j.beforeSHA!==await slotDigest(j.before))throw Error('corrupt_rollback_journal');
    return j;
  };
  async function stage(plan,{fault=null}={}) {
    if(!allowedFaults.has(fault))throw Error('unknown_fault_injection');
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
      const next=JSON.stringify(payload),before=get(shadowKey);
      if(before===next)return Object.freeze({status:'idempotent',writes:0});
      const j=await journalFor(before,next,plan.sourceSHA);
      let journalWritten=false;
      try{
        put(journalKey,j);journalWritten=true;
        if(get(journalKey)!==j)throw Error('journal_changed_after_write');
        if(fault==='after-journal'||fault==='crash-after-journal')
          throw Object.assign(Error('injected_'+fault),{crash:fault.startsWith('crash-')});
        if(get(shadowKey)!==before)throw Error('shadow_changed_before_write');
        if(await sourceDigest()!==plan.sourceSHA)throw Error('source_changed_before_shadow');
        if(get(journalKey)!==j||get(shadowKey)!==before)
          throw Error('concurrent_change_before_shadow');
        put(shadowKey,next);
        if(fault==='after-shadow'||fault==='crash-after-shadow')
          throw Object.assign(Error('injected_'+fault),{crash:fault.startsWith('crash-')});
        if(get(shadowKey)!==next)throw Error('shadow_changed_after_write');
        if(await sourceDigest()!==plan.sourceSHA)throw Error('source_changed_before_commit');
        if(get(journalKey)!==j||get(shadowKey)!==next)
          throw Error('concurrent_change_before_commit');
        put(journalKey,null);
        return Object.freeze({status:'disposable_staged',sourceSHA:plan.sourceSHA});
      }catch(e){
        if(journalWritten&&!e.crash){
          const jNow=get(journalKey),hNow=get(shadowKey);
          if(jNow!==j||(hNow!==before&&hNow!==next))
            throw new AggregateError([e],'rollback_conflict_preserved');
          try{
            put(shadowKey,before);
            if(get(shadowKey)!==before||get(journalKey)!==j)
              throw Error('rollback_readback_conflict');
            put(journalKey,null);
          }catch(rollbackError){
            throw new AggregateError([e,rollbackError],'rollback_failed_journal_retained');
          }
        }
        throw e;
      }
    });
  }
  async function recover(){return lock(async()=>{
    const raw=get(journalKey);
    if(raw===null)return Object.freeze({recovered:false});
    const j=await parseJournal(raw);
    const shadow=get(shadowKey);
    const actualSHA=await slotDigest(shadow);
    if(get(journalKey)!==raw)throw Error('recovery_journal_changed');
    if(actualSHA!==j.beforeSHA&&actualSHA!==j.nextSHA)
      throw Error('recovery_conflict_shadow_changed');
    if(get(shadowKey)!==shadow)throw Error('recovery_shadow_changed_during_digest');
    let sourceChanged;
    try{sourceChanged=await sourceDigest()!==j.sourceSHA}catch{sourceChanged=true}
    if(get(journalKey)!==raw||get(shadowKey)!==shadow)
      throw Error('recovery_concurrent_change');
    put(shadowKey,j.before);
    if(get(shadowKey)!==j.before||get(journalKey)!==raw)
      throw Error('recovery_write_conflict_journal_retained');
    put(journalKey,null);
    return Object.freeze({recovered:true,sourceChangedSinceJournal:sourceChanged});
  })}
  return Object.freeze({stage,recover,keys:Object.freeze({sourceKey,shadowKey,journalKey})});
}