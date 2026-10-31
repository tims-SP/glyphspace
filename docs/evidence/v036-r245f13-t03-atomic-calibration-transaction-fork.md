# R245F13 · Root T03 isolated calibration transaction precommit validation

Date: 2026-10-31. Parent: verified R245F12 ZIP `46092b27bcc671aa72b0276d633a83354c382a2aeb2845215ee44e1934b8973c` (3160/3160 inherited SHA256). This is an **isolated fork**, not main R247.

## Reproduced failure and code change

R245F12 `commitCalibration` staged a valid 151-instance event and wrote it to `CURRENT` before verifying whether the full/focus/mini DOM had actually changed. Chromium reproduced a stale event with E:0 X+1 and no DOM edit; the old candidate subsequently threw `candidate geometry drift` on `inspect()`. This was state poisoning by a rejected event, not a legitimate source certification.

R245F13 candidate checks all 151 staged coordinates against actual three-view node datasets and validates instance identity, source SVG path/paint and old-or-editor transform **before** changing `CURRENT`. A commit-stage exception restores the previous `CURRENT` map. The frozen V0.35 HTML, 2008 JPEG, historical SVG, 176 coding examples, production entry and user localStorage remain unchanged.

## Actual evidence

- Parent R245F12 selected QA rerun: 731/731.
- New Chromium about:blank QA: 41/41. Desktop 1280×800 DPR1, portrait 390×844 DPR2, landscape 844×390 DPR2. Stale and out-of-ink events rejected without poisoning state; valid edit/reset and mini view still work. Separate exhaustive pass edits and restores **151/151 visible instances across 25 keys**.
- Cumulative isolated ZIP: 3170 files, SHA256 `e8e02c2478215219aa1ffe96f01fe1f0b484e8cb61298c5be1307a62a3a98039`. Parent 3160/3160 member SHA inheritance, Python and system unzip independent restore each 3170/3170 SHA, each 772/772 selected QA, zero post-QA drift.
- Combined recursive runner had an attempted timeout, so the two suites were executed separately and verified. Full historical QA **not-run**; no claim of complete historical coverage.
- Main `03c29e0` remains R246. Its cumulative ZIP original bytes are still unavailable (expected 3054 members, SHA `3f2c863af624bee7f9e2c96c3c0262fbb9af777924264612b49da2cc948da6fe`). GitHub releases empty, local exact ZIP not found; GitHub Actions artifact collection not exhaustively checked.
- R11/R12/R35 original ZIPs and R12 20 historical SVGs missing. Same-origin production migration, legal same-source high-resolution stroke review, real screenreader, physical Android/iOS and full historical QA: **not-run**.
- T01 source-certified 0/25, T02 approved permanent IDs 0, T05 actual missing-root count unknown, original T00–T11 **0/12 Accepted**. T03 remains a pre-integration candidate.

## Recovery

Extract `R245F13_isolated_R245F12_fork_atomic_calibration_transaction.zip` into a clean directory; verify every member against `R245F13_archive_member_SHA256.json`, then run `v036_r245f13/qa_r245f13_atomic_calibration.py` and inherited selected QA. Do not overwrite `index.html` or use real user storage.
