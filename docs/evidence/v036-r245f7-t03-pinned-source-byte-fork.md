# R245F7 · Root T03 frozen-input byte-pinned geometry gate (isolated fork)

This evidence describes a real implementation in the independent cumulative ZIP. It is **not** a source-shape certification or an integrated production release.

## Defect and implementation

R245F6 compares all 151 draft catalog items and 25 key memberships against a catalog rebuilt from parsed source/vector JSON. The caller can, however, substitute both JSON objects and the candidate coherently; R245F6 accepts the internally consistent forged source. It also did not reject arbitrary extra catalog-level authority fields.

R245F7 adds `v036_r245f7/pinned_byte_geometry_attestation.mjs` in the cumulative ZIP. It accepts only raw `ArrayBuffer`/typed-array bytes, checks both SHA256 digests using WebCrypto before JSON decoding, then delegates to R245F6 strict catalog comparison. An exact top-level keyset is enforced. The separate explicit-pending optical geometry patch entry point remains available; no certification flags are promoted.

| Frozen input | SHA256 |
| --- | --- |
| R50 source paths JSON | `1d03c98a3dbd7074305e50cbb604447865ef2f9cde7786261aa9252b49860089` |
| R54 analytical vector bounds JSON | `65f3835499e64211e0f787cce7c2e33d18bea11c3d75204ee9e0f1eedf097f48` |
| V0.35 HTML (unchanged) | `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc` |
| 2008 reference JPEG (unchanged) | `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49` |

## Actual execution and restoration

- R245F6 parent ZIP SHA256 `be4e95ee257a6f9d61bfd11974bc69458f80b0f4fedf99556f94185d80674a5f`; 3099/3099 members independently inherited by SHA256.
- Inherited selected QA actually rerun: **2150/2150**. New Node WebCrypto positive/negative tests: **17/17**. Selected total: **2167/2167**. This is not full historical QA.
- R245F7 cumulative ZIP: **3110 members**, SHA256 `a8d0c3aed1ae7c315c4a1bab742ad591bd508cb8dbb977ecce4112bcedbaa405`.
- Two fresh extraction paths, Python `zipfile` and system `unzip`: each **3110/3110 member SHA256**, **2167/2167 selected QA**, and zero file changes after QA.
- Attempted Chromium on isolated `127.0.0.1` with temporary profile: `net::ERR_BLOCKED_BY_ADMINISTRATOR`; **blocked, 0 pass**, not counted as QA.
- Complete historical full QA, same-origin production migration, real screenreader, physical Android/iOS, licensed same-source high-resolution stroke review, formal production single HTML integration: **not-run**.

## Baseline, acceptance, safety

GitHub `main` remained at R246 commit `03c29e0fcc4b968224b9fdf37bc6d45b54da6b97` during this run. R246 cumulative ZIP original bytes were not found; this work forks the independently verified R245F6 archive, **not R246**. No main-branch or production-entry modification. R11/R12/R35 original ZIPs and R12's 20 SVGs remain missing; R10 was recovered in another historical source but not claimed as part of a complete sequence here.

**Root T00–T11: 0/12 Accepted.** T01 0/25 source-certified keys; T02 approved permanent IDs 0; T03 not integrated; T05 true missing-root count unknown. Frozen HTML, 176 encodings, historical formal SVG and user localStorage were not modified.

The runnable implementation, 17-case Node QA, inherited 2150-case QA runner, original parent-member SHA manifest, audit, report, and two recovery checks are contained in the R245F7 cumulative ZIP. The GitHub branch records the evidence and task state without claiming that the archive's full source tree has been uploaded.
