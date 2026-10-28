# V0.36 R181 — Root T04 real same-origin browser QA infrastructure (not accepted)

Date: 2026-10-28. Scope: **original T04 storage and legacy migration**, not UI-track, not production migration.

## Verified local archive
- R180 parent ZIP SHA256: `5155e490d3ec295d6f1cf6868ca0dc92397525123262f9058237c41fb44bce5f`.
- Actually read R180 archive and verified **2224/2224 inherited member SHA256**.
- R181 isolated cumulative ZIP: **2234 members**, SHA256 `060e219c8874f4164e7e5683159d85db446fc23dbfc7acccf07a5871e4ce319f`.
- Independently extracted via Python zipfile and system unzip: **2234/2234 SHA256** in each restoration, including **2224/2224 parent inheritance**.
- Actually reran new **12/12 static QA** and selected old **1181/1181 QA** in *each* independent restoration, total **1193/1193** per extraction. SHA256 still matched after QA.
- Full historical all-round QA: **not-run**.

## Real-browser QA and limitations
- Added a fresh-profile, ephemeral 127.0.0.1 HTTP test harness to check real Chromium Web Locks exclusivity/handoff, cross-tab localStorage visibility/storage events, WebCrypto source digest/staleness, and browser-context isolation.
- Local Chromium real loopback navigation returned `net::ERR_BLOCKED_BY_ADMINISTRATOR`; **0 browser checks passed locally**. This is **blocked/not-run**, not a positive real-origin result.
- Added `scripts/qa_r181_real_same_origin.py` and `.github/workflows/r181-t04-real-same-origin.yml` for independent GitHub Actions browser execution. **CI result is not yet confirmed**; do not count as passed.
- The browser harness tests browser primitives, **not** R180's private-Map migration logic, a durable migration, or production writes. No user profile, production localStorage, or permanent IDs are accessed.

## Frozen and missing evidence
- Frozen V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc` unchanged.
- Frozen 2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49` unchanged.
- 176 historical encodings, production entry, formal SVG, and user storage unchanged.
- R10 original ZIP remains embedded in R164. R11/R12/R35 original ZIPs and R12 20 SVGs remain missing; no complete historical continuity claim.
- T01 0/25 source-certified keys; formal permanent IDs 0; true missing-root count unknown; high-res image license and per-stroke certification unresolved.
- Android/iOS real devices and real screen-reader QA **not-run**.
- Original T00–T11 **0/12 Accepted**; original IDs unchanged. T04 remains **not accepted**.

## Next gate
Confirm independent CI evidence and its exact run/artifact. Even if browser primitives pass remotely, the next gate is testing actual legacy migration in a disposable, authorized, same-origin profile, including rollback and storage events. No promotion to formal T04 until dependencies and acceptance criteria are met.
