# R161 · Root T03 151-instance geometry change witness (isolated; not Accepted)

Date: 2026-10-27. Root task **T03 = 100×100 SVG coordinate kernel / real analytic inkBBox / anchors / optical offsets**. This is also a **T08 calibration stale-review preflight**, not the UI-03 prototype and not a completed calibration workflow.

## Concrete implementation and scope

Added `v036_round161/draft_geometry_impact.mjs` and `qa_draft_geometry_impact.mjs` inside the independently restorable R161 cumulative ZIP. They consume R160's full 151-instance descriptor-safe plan, itself bound to R125's checked R50 frozen SVG Path bytes, R54 analytic vector ink envelopes and R53 draft geometry. Every draft geometry SHA256 is over an explicit canonical record of instance ID, real frozen Path SHA256, geometry, resolved optical transform and transformed inkBBox. A sorted 151-ID plan SHA256 does not depend on caller ordering.

A one-instance optical offset or width edit changes only that instance's geometry witness (150 unchanged), enabling a precise stale-review invalidation preflight. The implementation rejects incomplete/unknown IDs, substituted Path SHA, getter fields, invalid geometry and certification flags. Manifests can only be compared when issued by the current JS realm. **SHA256 is not a trusted signature**; none of these draft IDs is a formal permanent ID.

## Actual tests and archive

- Parent R160 ZIP SHA256 `50892db856dbc26c52d9b18d330f818ee4fd391ed526ca2e861d780cabccaa6b`; inherited **2007/2007 file SHA256**.
- New Node test **18/18**; inherited selected QA **2083/2083**; combined **2101/2101**.
- R161 cumulative ZIP **2016 files**, SHA256 `97327e64f2ac290edfe557fc3736b0c4c5855add2fec71735d0fdc685db65c4c`.
- Python zipfile and system unzip independent extraction: each **2016/2016 file SHA256**, each **2101/2101 targeted QA**, post-QA **2016/2016 SHA256** unchanged.
- Full historical all-round QA, real same-origin Web Locks/localStorage, Android/iOS devices and real screen reader **not-run**. No actual user storage accessed.
- Frozen V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`; 2008 reference JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49` both checked unchanged.

## Formal status and blockers

**Original T00–T11: 0/12 Accepted.** T01 0/25 officially source-certified keys, T02 0 formal permanent IDs, T03 not integrated, T04 no real-user migration acceptance, T05 incomplete and true missing-root count unknown. Historical R10–R12 and R35 ZIPs plus R12 20 SVGs not recovered. Same-source high-resolution original bytes, redistribution permission and stroke-by-stroke certification remain unresolved. The 151 draft SVGs, 176 old encodings, production HTML and user storage are unchanged. **Do not promote draft hashes to reference-shape certification or publish V0.36.**

The private cumulative ZIP contains the runnable source, QA outputs, parent member SHA manifest, missing-history audit and execution report. This public repository intentionally stores only textual evidence, not the private reference JPEG or ZIP.
