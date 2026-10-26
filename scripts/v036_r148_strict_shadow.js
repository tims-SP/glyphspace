/* R148: isolated, read-only V0.35 v16 snapshot preflight; NOT a migration.
 * This code is not loaded by the frozen production index.html.
 * The caller must supply frozen defaults; the digest below prevents substitution.
 * All storage reads are against a disposable profile or an injected FakeStore.
 */
(function (root, factory) {
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  else Object.defineProperty(root, 'GlyphSpaceR148', {value: Object.freeze(api), configurable: false});
})(typeof globalThis === 'object' ? globalThis : this, function () {
  'use strict';
  const SOURCE_KEY = 'wubi06-root-coordinate-overrides-v16-svg';
  const FROZEN_DEFAULTS_SHA = 'd6ab1468b77f46e0322c1b6ee061ff011c1fb399752b462ebb546afc74002a88';
  const VALID_KEYS = 'GFDSAHJKLMTREWQYUIOPNBVCX';
  const own = (o, k) => Object.prototype.hasOwnProperty.call(o, k);
  const isPoint = p => Array.isArray(p) && p.length === 3 && p.every(v => typeof v === 'number' && Number.isFinite(v)) &&
    p[0] >= 0 && p[0] <= 90 && p[1] >= 12 && p[1] <= 88 && p[2] >= 9 && p[2] <= 29;
  const hex = b => Array.from(new Uint8Array(b), v => v.toString(16).padStart(2, '0')).join('');
  async function sha256(cryptoAPI, s) {
    if (!cryptoAPI || !cryptoAPI.subtle || typeof cryptoAPI.subtle.digest !== 'function') throw Error('crypto_unavailable');
    return hex(await cryptoAPI.subtle.digest('SHA-256', new TextEncoder().encode(s)));
  }
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
  async function readLegacy({store, cryptoAPI, defaults, expectedSourceSHA = null, origin, expectedOrigin, lockManager}) {
    if (!store || typeof store.getItem !== 'function') throw Error('missing_store');
    if (!origin || !expectedOrigin || origin !== expectedOrigin || !/^http:\/\/127\.0\.0\.1:\d+$/.test(origin)) throw Error('unsafe_origin');
    if (!lockManager || typeof lockManager.request !== 'function') throw Error('locks_unavailable');
    const run = async () => {
      if (!defaults || Object.keys(defaults).length !== 25 ||
          Object.keys(defaults).some(k => k.length !== 1 || !VALID_KEYS.includes(k)) ||
          Object.values(defaults).reduce((n, v) => n + (Array.isArray(v) ? v.length : 0), 0) !== 156 ||
          await sha256(cryptoAPI, JSON.stringify(defaults)) !== FROZEN_DEFAULTS_SHA) throw Error('untrusted_defaults');
      const raw = store.getItem(SOURCE_KEY);
      if (typeof raw !== 'string' || raw.length < 2 || raw.length > 200000) throw Error('missing_or_oversized_source');
      let data;
      try { data = JSON.parse(raw); } catch (_) { throw Error('invalid_json'); }
      rejectDuplicateObjectKeys(raw);
      if (!data || typeof data !== 'object' || Array.isArray(data) || Object.keys(data).length === 0) throw Error('invalid_source_object');
      const keys = Object.keys(data), edits = [], sourceSlotAliases = [];
      for (const k of keys) {
        if (!own(defaults, k) || !Array.isArray(data[k]) || data[k].length !== defaults[k].length) throw Error('invalid_source_key_or_length:' + k);
        for (let j = 0; j < data[k].length; j++) {
          const p = data[k][j];
          if (!isPoint(p)) throw Error('invalid_coordinate:' + k + ':' + j);
          const alias = k + ':' + j;
          sourceSlotAliases.push(alias);
          if (JSON.stringify(p) !== JSON.stringify(defaults[k][j])) edits.push({alias, coordinate: p.slice()});
        }
      }
      const sourceSHA = await sha256(cryptoAPI, raw);
      if (expectedSourceSHA !== null && sourceSHA !== expectedSourceSHA) throw Error('source_changed');
      if (store.getItem(SOURCE_KEY) !== raw) throw Error('source_changed_during_read');
      return Object.freeze({sourceSHA, sourceKeys: keys.slice().sort(),
        absentKeys: Object.keys(defaults).filter(k => !own(data, k)),
        sourceSlots: sourceSlotAliases.length, sourceSlotAliases, explicitEdits: edits,
        approvedPermanentIds: 0, writes: 0, productionMigration: 'not-run'});
    };
    return lockManager.request('__glyphspace_r148_strict_shadow_read_only__', {mode: 'shared'}, run);
  }
  return Object.freeze({SOURCE_KEY, FROZEN_DEFAULTS_SHA, rejectDuplicateObjectKeys, readLegacy});
});
