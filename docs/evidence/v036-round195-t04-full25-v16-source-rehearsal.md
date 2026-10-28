# V0.36 R195 — Root T04 frozen 25-key v16 source rehearsal (isolated; not Accepted)

Date: 2026-10-29 (Asia/Shanghai). Task numbering follows `docs/history/V0.36-P0-original.md`; UI-01–UI-05 are separate.

## Actual work and source

- Re-read R194 cumulative ZIP (SHA256 `35eeaf4d0f9bf6b350dc915269ad46f1428d829594cfe8c3bf1894cd51734839`), verified and inherited **2447/2447** member SHA256 values.
- Used unmodified R148 strict v16 reader, R152 issuer, R178 freshness, R179 browser realm and R192 transaction core through the R194 bridge. Rehearsed all **25 keys / 156 frozen V0.35 coordinate slots**, editing each slot by 1 within the original strict bounds; tested a separate M-only sparse override.
- Tested 156/156 source aliases, 156/156 explicit edits, source SHA, source preservation, idempotence, plan cloning rejection, stale source rejection, crash/recovery, duplicate JSON key, wrong key length and out-of-range coordinate rejection. **No permanent ID was issued.**
- Node.js 22 private Map + cooperative mock Web Locks: **46/46** new runtime checks. Source/freeze static guards: **22/22**. Re-executed selected R194 inherited QA: **671/671**. Total selected **739/739**.
- This extends the R194 three-key (G/K/X) browser fixture's source coverage, but **R195 is Node-only**. R194 authorized remote real Chromium 30/30 does not certify this full25 fixture.

## Independent cumulative restore

- R195 cumulative ZIP: **2457 files**, SHA256 `6ba77588da4a7e19b2622d9da722474e3b4be910cbd2b727ee6ac663fbe2895c`.
- Python ZipFile extraction: 2457/2457 member SHA, 739/739 QA, post-QA SHA unchanged.
- System unzip extraction: 2457/2457 member SHA, 739/739 QA, post-QA SHA unchanged.
- Complete historical all-round QA **not-run**. Local Chromium actual loopback navigation **blocked/not-run** (`net::ERR_BLOCKED_BY_ADMINISTRATOR`). No actual user localStorage was read or modified.
- Frozen V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`; frozen 2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49` both independently rechecked.
- R195 scripts, QA JSON, parent per-member SHA manifest, report, and missing-history audit are inside the isolated cumulative ZIP, not the production `index.html`.

## Acceptance and blockers

- **Original T00–T11: 0/12 Accepted**; T01 source certification 0/25 keys; T02 permanent IDs approved 0; T05 actual missing-root count unknown. No production migration or T03/T05 integration.
- Original R10 ZIP retained from R164; original R11/R12/R35 ZIPs and R12 20 SVGs not recovered. No continuous historical-chain claim.
- Same-source high-resolution image rights, stroke-by-stroke shape ownership, mobile physical devices, actual screen readers and complete formal acceptance remain pending.
- No changes to frozen production HTML, formal SVGs, 176 old codes or user storage.

Next: obtain lawful original high-resolution source bytes and resolve M/K/E/B/J/R/X/V identity blockers; then bind approved IDs and test full25 real same-origin migration in an authorized disposable profile.