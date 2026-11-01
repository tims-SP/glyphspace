# V0.36 R245F31 · Root T03 pure JSON source attestation (isolated, not accepted)

This is a **pre-integration T03** source/geometry safety correction on the **R245F30 fork**, not a continuation of the R246 main ZIP and not certification of a reference-image glyph.

## Reproduced defect

R245F30 hashes `JSON.stringify(source)` and `JSON.stringify(vector)` before auditing 151 legacy SVG instances. A caller can provide a non-enumerable `toJSON` hook on the root or an individual row, which serializes the untouched source while the verifier reads modified `rows[].paths[].d`. The old audit **accepted both** source+catalog co-tampering cases (2/2 reproduced; not counted as passing new QA).

## Isolated correction

The new `v036_r245f31/t03_pure_json_source_gate.mjs` enforces a deep JSON.parse-equivalent data tree before calling R245F30's canonical-content verifier. It rejects `toJSON`, accessors, hidden fields, custom prototypes, array holes/extra fields, symbols, cycles/shared aliases, functions and non-finite numbers. A separate explicit loader verifies **raw SHA256 bytes** of the R50 source JSON (`1d03c98a3dbd7074305e50cbb604447865ef2f9cde7786261aa9252b49860089`) and R54 vector JSON (`65f3835499e64211e0f787cce7c2e33d18bea11c3d75204ee9e0f1eedf097f48`) before building the draft catalog.

Source, geometry, patch and QA code are in the independent cumulative ZIP under `v036_r245f31/`; this repository evidence note does **not** turn the isolated candidate into production.

## Actual reproducible evidence

- Parent R245F30 ZIP SHA256 `6a727d8e14df67aebe6ed3f7e6b94c4a33448918ffbe1d3dde7d3dfb1113debf`; **3357/3357 inherited SHA identical**.
- R245F31 new Node QA **23/23**, old defect reproductions **2/2** separately excluded.
- Inherited selected QA R245F24–R245F30 **284/284**; selected total **307/307**.
- New cumulative ZIP: `R245F31_isolated_R245F30_fork_T03_pure_JSON_source_attestation.zip`, **3365 members**, SHA256 `736c90caa7455b7e47468eb6390afbd9e6111e347e03e1581afb52214b73dd28`.
- Independent Python zipfile and system unzip restorations: each **3365/3365 member SHA**, each **307/307 QA**, **zero post-QA drift**.
- Original frozen V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`; original 2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`; both independently verified unchanged.
- Full historical QA **not-run**; Chromium old selected cases use **about:blank**, not real same-origin production migration. Real screenreader/physical devices **not-run**.

## Formal acceptance boundary

T01 formally certified keys **0/25**; T02 approved permanent IDs **0**; T03 **not production-integrated**; T05 actual missing-root count **unknown**; original T00–T11 **0/12 Accepted**. R246 3054-member ZIP, historical R11/R12/R35 ZIP and R12 20 SVG remain unavailable; R10 was previously restored. Same-source high-resolution license and per-stroke approval remain blocked. Production entry, 176 legacy codes, historical official SVG and user localStorage were not changed.
