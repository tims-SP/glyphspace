/* R152 Root T04: independent raw-source binding for issuer-bound READ-ONLY preflight.
 * Reproduces and closes an R151 trust-boundary defect: caller-injected readLegacy
 * could mint an issuer-verified plan for data that did not match store bytes.
 * Only disposable test origin/FakeStore; no production migration or user writes.
 *
 * Inherited R151 code:
 * R150 verifyPlan accepted caller-created, rehashed frozen JSON as if issued.
 * This revision binds verification to the actual plan object issued in this realm.
 * The WeakMap is ephemeral, not a portable cryptographic signature.
 *
 * R150 Root T04: disposable, READ-ONLY legacy alias migration preflight.
 * This is NOT a production migration, does not approve any permanent IDs,
 * and never writes localStorage. Requires R148's strict source reader.
 * A v16 key:index is a source alias, NOT a stable V0.36 identity.
 */
(function (root, factory) {
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  else Object.defineProperty(root, 'GlyphSpaceR152', {value: api, configurable: false});
})(typeof globalThis === 'object' ? globalThis : this, function () {
  'use strict';
  const SOURCE_KEY = 'wubi06-root-coordinate-overrides-v16-svg';
  const FROZEN_DEFAULTS_SHA = 'd6ab1468b77f46e0322c1b6ee061ff011c1fb399752b462ebb546afc74002a88';
  // Private, per-realm issuance registry. No exported minting method.
  const issuedPlans = new WeakMap();
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
  // Independent of the injected reader's output: inspect the exact raw bytes.
  // The v16 source has a simple JSON object-of-coordinate-arrays grammar.
  function rejectDuplicateObjectKeys(raw) {
    let i = 0;
    const ws = () => { while (i < raw.length && /[\x20\t\n\r]/.test(raw[i])) i++; };
    const string = () => {
      if (raw[i] !== '"') throw Error('invalid_json_string');
      const begin = i++;
      while (i < raw.length) {
        if (raw[i] === '\\') { i += 2; continue; }
        if (raw[i++] === '"') return JSON.parse(raw.slice(begin, i));
      }
      throw Error('unterminated_string');
    };
    const expect = c => { ws(); if (raw[i] !== c) throw Error('invalid_json_structure'); i++; };
    const value = depth => {
      if (depth > 8) throw Error('source_depth_limit');
      ws();
      if (raw[i] === '{') {
        i++; ws(); const seen = new Set();
        if (raw[i] === '}') { i++; return; }
        while (true) {
          ws(); const k = string();
          if (seen.has(k)) throw Error('duplicate_json_key:' + k);
          seen.add(k); expect(':'); value(depth + 1); ws();
          if (raw[i] === '}') { i++; return; }
          expect(',');
        }
      }
      if (raw[i] === '[') {
        i++; ws(); if (raw[i] === ']') { i++; return; }
        while (true) { value(depth + 1); ws(); if (raw[i] === ']') { i++; return; } expect(','); }
      }
      if (raw[i] === '"') { string(); return; }
      const begin = i;
      while (i < raw.length && !/[\x20\t\n\r,}\]]/.test(raw[i])) i++;
      if (begin === i) throw Error('invalid_json_token');
    };
    value(0); ws(); if (i !== raw.length) throw Error('invalid_json_trailing');
    return true;
  }
  async function verifyRawBinding(raw, source, view, defaults, cryptoAPI, expectedSourceSHA) {
    if (typeof raw !== 'string' || raw.length < 2 || raw.length > 200000)
      throw Error('raw_source_missing_or_oversized');
    let parsed;
    try { parsed = JSON.parse(raw); } catch (_) { throw Error('raw_source_invalid_json'); }
    rejectDuplicateObjectKeys(raw);
    if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed) || Object.keys(parsed).length === 0)
      throw Error('raw_source_invalid_object');
    const keys = Object.keys(parsed).sort();
    if (JSON.stringify(keys) !== JSON.stringify(view.keys)) throw Error('raw_source_keys_mismatch');
    const edits = [];
    for (const k of keys) {
      if (!Object.prototype.hasOwnProperty.call(defaults,k) || !Array.isArray(parsed[k]) ||
          parsed[k].length !== defaults[k].length) throw Error('raw_source_slot_count_mismatch');
      for (let i=0;i<parsed[k].length;i++) {
        const p=parsed[k][i];
        if (!Array.isArray(p) || p.length!==3 || p.some(v=>typeof v!=='number'||!Number.isFinite(v)) ||
            p[0]<0 || p[0]>90 || p[1]<12 || p[1]>88 || p[2]<9 || p[2]>29)
          throw Error('raw_source_invalid_coordinate');
        if (JSON.stringify(p)!==JSON.stringify(defaults[k][i]))
          edits.push({alias:k+':'+i,coordinate:p.slice()});
      }
    }
    edits.sort((a,b)=>a.alias.localeCompare(b.alias,'en'));
    if (JSON.stringify(edits)!==JSON.stringify(view.edits)) throw Error('raw_source_edits_mismatch');
    const actualSHA=await digest(cryptoAPI,raw);
    if (actualSHA!==source.sourceSHA ||
        (expectedSourceSHA!=null && actualSHA!==expectedSourceSHA)) throw Error('raw_source_sha_mismatch');
    return actualSHA;
  }
  // This plan has no `apply`, `commit`, or `write` operation by design.
  async function planReadOnly({strictReader, store, cryptoAPI, defaults, expectedSourceSHA, origin, expectedOrigin, lockManager, permanentIds}) {
    if (permanentIds !== undefined && permanentIds !== null) throw Error('formal_ids_not_approved');
    verifyDefaultsShape(defaults);
    if (await digest(cryptoAPI,JSON.stringify(defaults))!==FROZEN_DEFAULTS_SHA) throw Error('untrusted_defaults');
    if (!strictReader || typeof strictReader.readLegacy!=='function' ||
        strictReader.FROZEN_DEFAULTS_SHA!==FROZEN_DEFAULTS_SHA) throw Error('untrusted_strict_reader');
    if (!store || typeof store.getItem!=='function') throw Error('missing_store');
    if (!origin || origin!==expectedOrigin || !/^http:\/\/127\.0\.0\.1:\d+$/.test(origin)) throw Error('unsafe_origin');
    if (!lockManager || typeof lockManager.request!=='function') throw Error('locks_unavailable');
    const rawBefore=store.getItem(SOURCE_KEY);
    // The reader only receives a read-only facade, never the caller's writable store.
    const readOnlyStore=Object.freeze({getItem:k=>store.getItem(k)});
    const source = await strictReader.readLegacy({store:readOnlyStore,cryptoAPI,defaults,expectedSourceSHA,origin,expectedOrigin,lockManager});
    const view = validateSourceView(source,defaults);
    await verifyRawBinding(rawBefore,source,view,defaults,cryptoAPI,expectedSourceSHA);
    if (store.getItem(SOURCE_KEY)!==rawBefore) throw Error('raw_source_changed_during_plan');
    const payload = {
      schema:'glyphspace-v036-legacy-alias-shadow-v2', sourceSchema:'v16',
      sourceIntegrity:'independent_raw_v16_binding',
      sourceSHA:source.sourceSHA, frozenDefaultsSHA:FROZEN_DEFAULTS_SHA,
      sourceKeys:view.keys, absentKeys:source.absentKeys.slice().sort(),
      sourceSlots:view.aliases.length, sourceSlotAliases:view.aliases,
      explicitEdits:view.edits, approvedPermanentIds:0,
      bindingState:'blocked_pending_T01_T02_formal_identity', writes:0,
      productionMigration:'not-run'
    };
    const planSHA = await digest(cryptoAPI,JSON.stringify(payload));
    const issued = deepFreeze({...payload,planSHA});
    issuedPlans.set(issued, {planSHA, sourceSHA:source.sourceSHA});
    return issued;
  }
  async function verifyPlan(plan, cryptoAPI) {
    const issuance = plan && typeof plan === 'object' ? issuedPlans.get(plan) : null;
    if (!issuance) throw Error('plan_not_issued_by_this_realm');
    if (!Object.isFrozen(plan) || plan.schema!=='glyphspace-v036-legacy-alias-shadow-v2' ||
        plan.frozenDefaultsSHA!==FROZEN_DEFAULTS_SHA ||
        plan.sourceIntegrity!=='independent_raw_v16_binding' || plan.approvedPermanentIds!==0 ||
        plan.writes!==0 || plan.productionMigration!=='not-run' ||
        plan.bindingState!=='blocked_pending_T01_T02_formal_identity') throw Error('untrusted_plan');
    const {planSHA,...payload}=plan;
    if (!/^[0-9a-f]{64}$/.test(planSHA||'') ||
        planSHA !== issuance.planSHA || plan.sourceSHA !== issuance.sourceSHA ||
        await digest(cryptoAPI,JSON.stringify(payload))!==planSHA) throw Error('plan_digest_mismatch');
    return true;
  }
  return Object.freeze({SOURCE_KEY,FROZEN_DEFAULTS_SHA,planReadOnly,verifyPlan});
});
