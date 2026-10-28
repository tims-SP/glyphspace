/** R194 / Root T04 — source-issued browser realm -> R187 typed-slot conflict-aware disposable core.
 * Isolated loopback test profile ONLY. Does not write V0.35 source key,
 * assign permanent IDs, or migrate user data. The original R148/R152/R178/R179
 * issuer modules and R187 core are used unmodified, byte-for-byte.
 */
import {createDisposableTransactionCore} from './r192_idempotent_freshness_core.mjs';
const SOURCE_KEY='wubi06-root-coordinate-overrides-v16-svg';
const SHADOW_KEY='__glyphspace_disposable_r194_shadow';
const JOURNAL_KEY='__glyphspace_disposable_r194_journal';
const LOCK_NAME='__glyphspace_disposable_r194_exclusive__';
const hex=bytes=>Array.from(new Uint8Array(bytes),v=>v.toString(16).padStart(2,'0')).join('');

export function createRealmIssuedDisposableBridge({qaFaults=false,revision=0}={}) {
  // Refuse non-loopback execution BEFORE touching any Storage property.
  const loc=globalThis.location;
  if(!loc || loc.protocol!=='http:' || loc.hostname!=='127.0.0.1' ||
     !/^http:\/\/127\.0\.0\.1:[1-9][0-9]{0,4}$/.test(loc.origin) ||
     Number(loc.port)>65535 || globalThis.isSecureContext!==true)
    throw Error('unsafe_browser_realm');
  if(!Number.isSafeInteger(revision)||revision<0||revision>1000000 ||
     typeof qaFaults!=='boolean') throw Error('invalid_disposable_qa_configuration');
  const reader=globalThis.GlyphSpaceR148;
  const issuer=globalThis.GlyphSpaceR152;
  const freshness=globalThis.GlyphSpaceR178;
  const realm=globalThis.GlyphSpaceR179;
  if(!reader||!issuer||!freshness||!realm||
     [reader.SOURCE_KEY,issuer.SOURCE_KEY,freshness.SOURCE_KEY,realm.SOURCE_KEY].some(x=>x!==SOURCE_KEY)||
     typeof issuer.verifyPlan!=='function'||
     typeof realm.issueReadOnlyPlan!=='function'||
     typeof realm.attestIssuedPlan!=='function') throw Error('actual_issuer_modules_required');
  const locks=globalThis.navigator?.locks;
  const subtle=globalThis.crypto?.subtle;
  if(typeof locks?.request!=='function'||typeof subtle?.digest!=='function')
    throw Error('real_web_locks_and_crypto_required');
  const storage=globalThis.localStorage;
  if(!storage||typeof storage.getItem!=='function'||typeof storage.setItem!=='function'||
     typeof storage.removeItem!=='function') throw Error('realm_storage_required');
  const allowedReads=new Set([SOURCE_KEY,SHADOW_KEY,JOURNAL_KEY]);
  const read=key=>{
    if(!allowedReads.has(key))throw Error('read_outside_isolated_namespace');
    return storage.getItem(key);
  };
  const write=(key,value)=>{
    if(key!==SHADOW_KEY&&key!==JOURNAL_KEY)
      throw Error('write_outside_isolated_namespace');
    if(value===null)storage.removeItem(key);
    else storage.setItem(key,value);
  };
  const sha256=async raw=>hex(await subtle.digest('SHA-256',new TextEncoder().encode(raw)));
  const verifySourcePlan=async plan=>{
    if(await issuer.verifyPlan(plan,globalThis.crypto)!==true)return false;
    const att=await realm.attestIssuedPlan(plan);
    return att?.sourceSHA===plan.sourceSHA && att?.sourceUnchangedAtObservation===true &&
      att?.writes===0 && att?.approvedPermanentIds===0;
  };
  const buildPayload=async plan=>({schema:'glyphspace-r194-disposable-shadow-v1',
    sourceSHA:plan.sourceSHA,sourceSlotAliases:plan.sourceSlotAliases,
    explicitEdits:plan.explicitEdits,revision,
    isDisposable:true,identityMappings:[],approvedPermanentIds:0,
    productionMigration:'not-run'});
  const core=createDisposableTransactionCore({sourceKey:SOURCE_KEY,
    shadowKey:SHADOW_KEY,journalKey:JOURNAL_KEY,read,write,sha256,
    withLock:fn=>locks.request(LOCK_NAME,{mode:'exclusive'},fn),
    verifySourcePlan,buildPayload,allowFaults:qaFaults});
  return Object.freeze({
    keys:Object.freeze({sourceKey:SOURCE_KEY,shadowKey:SHADOW_KEY,journalKey:JOURNAL_KEY}),
    issue:defaults=>realm.issueReadOnlyPlan({defaults}),
    stage:(plan,options)=>core.stage(plan,options),
    recover:()=>core.recover(),
  });
}
