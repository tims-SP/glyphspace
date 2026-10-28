/* R179 Root T04 — isolated browser-realm-bound READ-ONLY v16 preflight.
 * The R178 core accepted caller-provided `origin`, `store`, `cryptoAPI`, and
 * `lockManager`. Those inputs can describe a fictitious loopback origin while
 * the code actually executes on a different origin. Bind to the executing
 * browser realm instead; refuse non-loopback realms BEFORE reading storage.
 * Only for a new disposable loopback profile. NOT production migration.
 */
(function (root, factory) {
  const api = factory(root);
  if (typeof module === 'object' && module.exports) module.exports = api;
  else Object.defineProperty(root, 'GlyphSpaceR179', {value: api, configurable: false});
})(typeof globalThis === 'object' ? globalThis : this, function (host) {
  'use strict';
  // Capture issuers from this realm, not from caller-controlled arguments.
  const reader = host.GlyphSpaceR148;
  const issuer = host.GlyphSpaceR152;
  const freshness = host.GlyphSpaceR178;
  const SOURCE_KEY = 'wubi06-root-coordinate-overrides-v16-svg';
  function realmBindings() {
    // Check origin first: no localStorage getter is evaluated on other origins.
    const origin = host.location && host.location.origin;
    if (typeof origin !== 'string' || !/^http:\/\/127\.0\.0\.1:[1-9][0-9]{0,4}$/.test(origin) ||
        Number(origin.slice(origin.lastIndexOf(':') + 1)) > 65535)
      throw Error('unsafe_realm_origin');
    if (host.isSecureContext !== true) throw Error('insecure_realm');
    if (!reader || !issuer || !freshness ||
        reader.SOURCE_KEY !== SOURCE_KEY || issuer.SOURCE_KEY !== SOURCE_KEY ||
        freshness.SOURCE_KEY !== SOURCE_KEY ||
        typeof reader.readLegacy !== 'function' ||
        typeof issuer.planReadOnly !== 'function' ||
        typeof freshness.attestCurrentSource !== 'function')
      throw Error('source_modules_unavailable');
    const locks = host.navigator && host.navigator.locks;
    const cryptoAPI = host.crypto;
    if (!locks || typeof locks.request !== 'function') throw Error('realm_locks_unavailable');
    if (!cryptoAPI || !cryptoAPI.subtle || typeof cryptoAPI.subtle.digest !== 'function')
      throw Error('realm_crypto_unavailable');
    const storage = host.localStorage;
    if (!storage || typeof storage.getItem !== 'function') throw Error('realm_storage_unavailable');
    // Never pass the writable Storage object to downstream modules.
    const store = Object.freeze({getItem(key) {
      if (key !== SOURCE_KEY) throw Error('non_source_key_access');
      return storage.getItem(SOURCE_KEY);
    }});
    return {origin, expectedOrigin:origin, store, cryptoAPI, lockManager:locks};
  }
  async function issueReadOnlyPlan({defaults} = {}) {
    const bindings = realmBindings();
    return issuer.planReadOnly({strictReader:reader, defaults, ...bindings});
  }
  async function attestIssuedPlan(plan) {
    const bindings = realmBindings();
    return freshness.attestCurrentSource({plan, ...bindings});
  }
  return Object.freeze({SOURCE_KEY, issueReadOnlyPlan, attestIssuedPlan});
});
