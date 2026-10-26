/* R150 Root T04: disposable, READ-ONLY legacy alias migration preflight.
 * This is NOT a production migration, does not approve any permanent IDs,
 * and never writes localStorage. Requires R148's strict source reader.
 * A v16 key:index is a source alias, NOT a stable V0.36 identity.
 */
(function (root, factory) {
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  else Object.defineProperty(root, 'GlyphSpaceR150', {value: api, configurable: false});
})(typeof globalThis === 'object' ? globalThis : this, function () {
  'use strict';
  const FROZEN_DEFAULTS_SHA = 'd6ab1468b77f46e0322c1b6ee061ff011c1fb399752b462ebb546afc74002a88';
  const VALID_KEYS = 'GFDSAHJKLMTREWQYUIOPNBVCX';
  const own = (o,k) => Object.prototype.hasOwnProperty.call(o,k);
  const hex = b => Array.from(new Uint8Array(b), v=>v.toString(16).padStart(2,'0')).join('');
  async function digest(cryptoAPI, data) {
    if (!cryptoAPI || !cryptoAPI.subtle || typeof cryptoAPI.subtle.digest !== 'function') throw Error('crypto_unavailable');
    return hex(await cryptoAPI.subtle.digest('SHA-256',new TextEncoder().encode(data)));
  }
  function deepFreeze(v) {
    if (v && typeof v === 'object') {
      for (const k of Object.keys(v)) deepFreeze(v[k]);
      Object.freeze(v);
    }
    return v;
  }
  function verifyDefaultsShape(defaults) {
    if (!defaults || typeof defaults !== 'object' || Array.isArray(defaults) ||
        Object.keys(defaults).length !== 25 ||
        Object.keys(defaults).some(k=>k.length!==1 || !VALID_KEYS.includes(k)) ||
        Object.values(defaults).some(v=>!Array.isArray(v)) ||
        Object.values(defaults).reduce((n,v)=>n+v.length,0)!==156) throw Error('untrusted_defaults_shape');
  }
  function validateSourceView(source, defaults) {
    if (!source || typeof source !== 'object' || !/^[0-9a-f]{64}$/.test(source.sourceSHA || '') ||
        source.writes!==0 || source.approvedPermanentIds!==0 || source.productionMigration!=='not-run')
      throw Error('untrusted_source_view');
    if (!Array.isArray(source.sourceKeys) || !Array.isArray(source.absentKeys) ||
        !Array.isArray(source.sourceSlotAliases) || !Array.isArray(source.explicitEdits)) throw Error('invalid_source_view_arrays');
    const keys = source.sourceKeys.slice().sort();
    if (new Set(keys).size!==keys.length || keys.some(k=>!own(defaults,k)) ||
        JSON.stringify(keys)!==JSON.stringify(source.sourceKeys) ||
        JSON.stringify(source.absentKeys.slice().sort())!==JSON.stringify(Object.keys(defaults).filter(k=>!keys.includes(k)).sort()))
      throw Error('source_key_coverage_mismatch');
    const aliases = keys.flatMap(k=>defaults[k].map((_,i)=>k+':'+i)).sort();
    const actual = source.sourceSlotAliases.slice().sort();
    if (aliases.length!==source.sourceSlots || new Set(actual).size!==actual.length ||
        JSON.stringify(aliases)!==JSON.stringify(actual)) throw Error('source_alias_coverage_mismatch');
    const edits = source.explicitEdits.map(e=>({alias:e.alias,coordinate:e.coordinate.slice()})).sort((a,b)=>a.alias.localeCompare(b.alias,'en'));
    if (new Set(edits.map(e=>e.alias)).size!==edits.length || edits.some(e=>
        !aliases.includes(e.alias) || !Array.isArray(e.coordinate) || e.coordinate.length!==3 ||
        e.coordinate.some(x=>typeof x!=='number'||!Number.isFinite(x)) ||
        JSON.stringify(e.coordinate)===JSON.stringify(defaults[e.alias.split(':')[0]][Number(e.alias.split(':')[1])])
    )) throw Error('invalid_edit_set');
    return {keys,aliases,edits};
  }
  // This plan has no `apply`, `commit`, or `write` operation by design.
  async function planReadOnly({strictReader, store, cryptoAPI, defaults, expectedSourceSHA, origin, expectedOrigin, lockManager, permanentIds}) {
    if (permanentIds !== undefined && permanentIds !== null) throw Error('formal_ids_not_approved');
    verifyDefaultsShape(defaults);
    if (await digest(cryptoAPI,JSON.stringify(defaults))!==FROZEN_DEFAULTS_SHA) throw Error('untrusted_defaults');
    if (!strictReader || typeof strictReader.readLegacy!=='function' ||
        strictReader.FROZEN_DEFAULTS_SHA!==FROZEN_DEFAULTS_SHA) throw Error('untrusted_strict_reader');
    const source = await strictReader.readLegacy({store,cryptoAPI,defaults,expectedSourceSHA,origin,expectedOrigin,lockManager});
    const view = validateSourceView(source,defaults);
    const payload = {
      schema:'glyphspace-v036-legacy-alias-shadow-v1', sourceSchema:'v16',
      sourceSHA:source.sourceSHA, frozenDefaultsSHA:FROZEN_DEFAULTS_SHA,
      sourceKeys:view.keys, absentKeys:source.absentKeys.slice().sort(),
      sourceSlots:view.aliases.length, sourceSlotAliases:view.aliases,
      explicitEdits:view.edits, approvedPermanentIds:0,
      bindingState:'blocked_pending_T01_T02_formal_identity', writes:0,
      productionMigration:'not-run'
    };
    const planSHA = await digest(cryptoAPI,JSON.stringify(payload));
    return deepFreeze({...payload,planSHA});
  }
  async function verifyPlan(plan, cryptoAPI) {
    if (!plan || !Object.isFrozen(plan) || plan.schema!=='glyphspace-v036-legacy-alias-shadow-v1' ||
        plan.frozenDefaultsSHA!==FROZEN_DEFAULTS_SHA || plan.approvedPermanentIds!==0 ||
        plan.writes!==0 || plan.productionMigration!=='not-run' ||
        plan.bindingState!=='blocked_pending_T01_T02_formal_identity') throw Error('untrusted_plan');
    const {planSHA,...payload}=plan;
    if (!/^[0-9a-f]{64}$/.test(planSHA||'') || await digest(cryptoAPI,JSON.stringify(payload))!==planSHA) throw Error('plan_digest_mismatch');
    return true;
  }
  return Object.freeze({FROZEN_DEFAULTS_SHA,planReadOnly,verifyPlan});
});
