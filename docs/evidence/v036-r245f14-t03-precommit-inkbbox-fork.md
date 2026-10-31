# V0.36 R245F14 — Root T03 precommit inkBBox guard (isolated fork; NOT Accepted)

**Parent**: independently re-read R245F13 cumulative ZIP `e8e02c2478215219aa1ffe96f01fe1f0b484e8cb61298c5be1307a62a3a98039`, 3170/3170 inherited member SHA256 equal. Main remains R246 `03c29e0`; its 3054-member cumulative ZIP raw bytes are unavailable, so this is **not** a continuous R247 mainline.

**Reproduced defect**: on the R245F13 candidate, moving M visible instance 0 X slider from 13 to 90 first wrote legacy ROOT_COORDS and the isolated in-memory localStorage, then failed the analytic inkBBox gate. Real Chromium about:blank returned `candidate geometry drift`, with storage count 0→1 and no usable geometry inspection. This is a UI/storage transaction defect, not an original-reference shape judgment.

**Fix**: the isolated R245F14 HTML preflights a projected 151-visible-instance 100×100 analytic inkBBox snapshot **before** legacy slider writes, redraw or save; invalid values are rejected with user feedback while old coordinates, three-view DOM and storage stay intact. Partial legacy JSON import merges against current coordinates, validates the complete projected snapshot before any write, and preserves valid imports. Recovery script, candidate HTML and Chromium QA are contained in the cumulative ZIP.

**QA**: 40/40 new real Chromium about:blank checks (parent negative reproduction; 1280×800 DPR1, 390×844 DPR2, 844×390 DPR2; invalid slider, invalid/valid partial import, retained previous valid edit, reset and no page errors). Ten selected inherited suites 772/772; **812/812 selected**, split into 592 core and 220 browser to avoid a timed-out recursive runner. Python and system unzip independent recovery: each **3181/3181** member SHA256 and **812/812** QA, zero post-QA drift. Full historical suite: **not-run**.

**Archive**: `R245F14_isolated_R245F13_fork_precommit_ink_bbox_gate.zip`, SHA256 `4354ed408d6b4b10ea245504cabef8e58b84cddc93a89e372511440bed1b8be8`. The ZIP is an isolated working artifact, not a GitHub release.

**Boundaries**: no modification to frozen V0.35 HTML (SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`), 2008 JPEG, 176 old encodings, historical formal SVG, production entry or real user storage. T01 certified 0/25, T02 approved permanent IDs 0, T05 missing roots unknown; Root T00–T11 **0/12 Accepted**. Real same-origin production migration, licensed same-source high-resolution per-stroke verification, screen reader and physical device QA: not-run. R11/R12/R35 original ZIP and R12 20 SVG remain missing.

**Next**: obtain and independently verify the R246 original ZIP; resolve legal same-source high-resolution original, per-stroke M/K/E/B/J/R/X/V identity; then integrate and certify T03 in the real production pipeline. Do not merge this isolated branch into production.
