# V0.36 R183 · Root T04 · shared disposable transaction core (NOT accepted)

Date: 2026-10-28. This is **Root T04 (storage/legacy migration)**, not UI-track work.

## Verified inputs

- GitHub main: read `docs/STATUS.md`, `docs/history/V0.36-P0-original.md`, `docs/tasks/t00-t11.json`, `docs/11-traceability.md`, `docs/07-acceptance.md`, `AGENTS.md`.
- Local parent R182 ZIP SHA256: `0d44faa8e833f67eea49cc314c92559e4224055780dc9b9f25b6e729ae1e5b23`; **2247/2247 inherited member SHA256 identical**.
- Frozen V0.35 HTML SHA256: `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`.
- Frozen 2008 JPEG SHA256: `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`.

## Substantive implementation

New pure ESM `scripts/r183_disposable_transaction_core.mjs` is usable in Node and Chromium without accessing global Storage. It accepts injected read/write/SHA256/cooperative-lock/issued-plan-verification/payload-building adapters; only two `__glyphspace_disposable_` keys can be written, never the legacy source key. It implements source-freshness gates, idempotent staging, write-ahead rollback journal, simulated crash and recovery, corrupted-journal rejection, and fails closed on unapproved permanent IDs or production-migration payloads.

The cumulative ZIP includes a Node test of **the same core with the actual R148/R152/R178 issuer and frozen ROOT_COORDS**, plus a private Map test and an actual two-tab Chromium same-origin test script. This is a **new isolated core** and not a claim that R180 production/legacy code runs directly in Chromium.

## Actual QA and boundaries

- New Node private-Map QA: **44/44**.
- Actual R148/R152/R178 issuer bridge QA: **17/17**.
- Re-executed selected inherited QA: R180 48/48, R179 35/35, R181 12/12, R182 14/14 = **109/109**.
- Total executed: **170/170**. Complete historical QA: **not-run**.
- Local real 127.0.0.1 Chromium: **blocked** (`net::ERR_BLOCKED_BY_ADMINISTRATOR`); browser QA **not-run**, not counted.
- Remote GitHub Actions workflow `r183-t04-shared-core-browser.yml` added. Its real-browser result is **unverified/pending**, not counted as passed until independently inspected.
- New cumulative R183 ZIP: **2257 files**, SHA256 `65526b6e12e03f8fd6a83f9a458e5a492180fe6fd23e4134575c561395ccd185`. Python zipfile and system unzip separately recovered **2257/2257 SHA**, re-executed **170/170 QA** in each directory, and post-QA SHA remained identical. ZIP itself is not stored in GitHub.

## Formal gates

**T00–T11: 0/12 Accepted.** T01 certified 0/25; T02 formally approved IDs 0; missing root count unknown. T03 production integration and T04 production migration remain undone. R11/R12/R35 original ZIPs and R12 20 SVG still missing. High-resolution third-party source licensing, per-stroke authentication, Android/iOS, real screen readers and full historical QA remain unverified. Frozen HTML, JPEG, 176 old codes, production entry and all user storage remain untouched.

Next: independently verify remote Chromium CI against the **exact ESM core**; integrate issuer-bound browser adapter in a new disposable profile, then test cross-tab locking, crash recovery and malicious/non-cooperating writes without touching user storage. No formal task acceptance or production release is authorized.
