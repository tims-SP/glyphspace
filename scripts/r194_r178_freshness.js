/* R178 Root T04: disposable READ-ONLY freshness gate for R152 issued plans.
 * A valid issued plan is a snapshot, not a guarantee that legacy storage is still
 * unchanged. This gate checks the live raw source under a cooperative Web Lock.
 * It cannot authorize a write, approve IDs, or promise freshness after return.
 * Never load against user production origin. No storage write methods are used.
 */
(function (root, factory) {
  const api = factory(root);
  if (typeof module === 'object' && module.exports) module.exports = api;
  else Object.defineProperty(root, 'GlyphSpaceR178', {value: api, configurable: false});
})(typeof globalThis === 'object' ? globalThis : this, function (host) {
  'use strict';
  // Capture the exact R152 issuer at module initialization, not a caller-supplied verifier.
  const issuer = typeof module === 'object' && module.exports
    ? require('../v036_round152/legacy_v16_source_bound_plan.js') : host.GlyphSpaceR152;
  const SOURCE_KEY = 'wubi06-root-coordinate-overrides-v16-svg';
  const LOCK_NAME = '__glyphspace_r178_read_only_freshness__';
  const hex = bytes => Array.from(new Uint8Array(bytes), v=>v.toString(16).padStart(2,'0')).join('');
  const isHex = s => typeof s === 'string' && /^[0-9a-f]{64}$/.test(s);
  async function attestCurrentSource({plan, store, cryptoAPI, origin, expectedOrigin, lockManager}) {
    if (!issuer || typeof issuer.verifyPlan !== 'function' || issuer.SOURCE_KEY !== SOURCE_KEY)
      throw Error('issuer_unavailable');
    if (!origin || origin !== expectedOrigin || !/^http:\/\/127\.0\.0\.1:\d+$/.test(origin))
      throw Error('unsafe_origin');
    if (!store || typeof store.getItem !== 'function') throw Error('store_unavailable');
    if (!cryptoAPI || !cryptoAPI.subtle || typeof cryptoAPI.subtle.digest !== 'function')
      throw Error('crypto_unavailable');
    if (!lockManager || typeof lockManager.request !== 'function') throw Error('locks_unavailable');
    // Verification before acquiring the lock is only an early rejection; repeat
    // inside the lock so the issued plan is checked at the observation point.
    if (await issuer.verifyPlan(plan, cryptoAPI) !== true) throw Error('issuer_rejected_plan');
    let entered = false;
    const result = await lockManager.request(LOCK_NAME, {mode:'shared'}, async () => {
      entered = true;
      if (await issuer.verifyPlan(plan, cryptoAPI) !== true) throw Error('issuer_rejected_plan');
      if (!isHex(plan.sourceSHA) || plan.approvedPermanentIds !== 0 || plan.writes !== 0 ||
          plan.productionMigration !== 'not-run') throw Error('untrusted_plan_scope');
      const raw = store.getItem(SOURCE_KEY);
      if (typeof raw !== 'string' || raw.length < 2 || raw.length > 200000)
        throw Error('raw_source_missing_or_oversized');
      const digest = hex(await cryptoAPI.subtle.digest('SHA-256', new TextEncoder().encode(raw)));
      if (store.getItem(SOURCE_KEY) !== raw) throw Error('source_changed_during_attestation');
      if (digest !== plan.sourceSHA) throw Error('source_stale_since_issuance');
      return Object.freeze({schema:'glyphspace-v036-ephemeral-source-freshness-v1',
        sourceSHA:digest, sourceBytes:new TextEncoder().encode(raw).length,
        checkedOrigin:origin, sourceUnchangedAtObservation:true,
        writes:0, approvedPermanentIds:0, productionMigration:'not-run',
        validOnlyAtObservation:true});
    });
    if (!entered || !result || result.sourceSHA !== plan.sourceSHA || result.writes !== 0)
      throw Error('lock_callback_not_confirmed');
    return result;
  }
  return Object.freeze({SOURCE_KEY, LOCK_NAME, attestCurrentSource});
});
