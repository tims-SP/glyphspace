# R245F16 · Root T01/T02 source-trace import epoch isolation (fork; not certification)

## Reproduced bug

The independently verified R245F15 cumulative ZIP (SHA256 `abd45644160fc933bb7a1b83e9a16bb94e5932e6ba8ed012e6302785ab7b1a60`) was read and all 3194 members matched their SHA256 manifest. The inherited R245F4 source workbench had an asynchronous `#traceImport` listener without the `evidenceEpoch` guard already used for review-note imports.

In actual Chromium `about:blank`, verified the frozen 2008 JPEG, created a valid two-point native-pixel trace for A:5, suspended `File.text()`, reverified the **same byte-identical JPEG**, then resumed `File.text()`. R245F4 incorrectly accepted the stale 1-stroke trace. This is an actual stale-evidence import, not an empty JSON or a static-only demonstration.

## Isolated fix and verification

The R245F16 candidate snapshots `evidenceEpoch` before `File.text()` and checks epoch plus source/registry verification after the await and before mutating `traceRecords`. Uninterrupted valid imports still succeed. Stale same-SHA re-verification, invalid JPEG revocation, and malformed schema are rejected without destroying the prior trace.

- Inherited R245F4 Chromium QA: **21/21**.
- Inherited R245F15 Chromium QA: **37/37**.
- New Chromium QA, including old-bug reproduction and 1280×800 DPR1 / 390×844 DPR2 isolated regression: **33/33**.
- Selected actually rerun: **91/91**; not the full 808 assertions or all historical QA.
- New cumulative ZIP: **3204 members**, SHA256 `bc343a657e317838bcf289ccc058bdd1a49a37e70e09f79664638acf1d8db939`.
- Python zipfile and system unzip restored **3204/3204 SHA256** independently; both ran **91/91** QA, with zero file drift.

The full ZIP, new HTML candidate, test scripts, SHA256 manifest, source audit, and two-restoration evidence are separate conversation artifacts; no binary asset was committed to this public repository.

## Acceptance and provenance boundaries

The frozen V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`, 2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`, 176 old codes, historical SVGs, production entry and real user storage were not modified.

**This fork does not inherit the R246 mainline M cross-crop ownership fix.** Main at `03c29e0fcc4b968224b9fdf37bc6d45b54da6b97` reports R246 / 3054 members, but its ZIP bytes are still unavailable. Do not treat this as R247 or merge without a real R246 reconciliation.

R11/R12/R35 original ZIPs and R12 20 SVGs remain missing; licensed same-source high-resolution image and per-stroke source authentication remain unverified. T01 0/25 certified, T02 0 permanent IDs approved, T05 actual missing count unknown; **original T00–T11 remain 0/12 Accepted**. Real same-origin Web Locks/localStorage, physical devices, screen reader and complete historical QA were **not run**.

Task identity remains Root T01/T02; UI-01..UI-05 are unrelated. Next priority is actual R246 ZIP and licensed same-source high-res provenance, not more isolated UI tests.
