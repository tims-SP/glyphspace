# R232 · Root T03 — Chromium real touch input isolation (isolated, not Accepted)

Date: 2026-10-30. Parent main: `415a934f9fbd9446e89e49c6ebec32ec34c31512`; parent R231 cumulative ZIP SHA256 `f283ee92bf297a1e99e402cfba34502c25a9ceb9aa7a50e61a36cc15b1abac82`, 2912/2912 inherited member SHA match.

## Reproduced defect and isolated repair

Real Chromium CDP `Input.dispatchTouchEvent` on the R231 derived V0.35 keyboard advanced the exercise input index from 0 to 1 during optical-calibration mode in both 390×844 DPR2 and 1280×800 DPR1 emulated touch contexts (2/2 reproducible). Touch pointer targeting was retargeted to the enclosing SVG, and a synthesized click reached the key button. This was an actual unintended input regression, not a simulated `new PointerEvent` test.

R232 adds a separate opt-in `v036_round232/pointer_gesture_controller.mjs` in the cumulative ZIP. During explicit arm mode, touch hit-testing uses `elementFromPoint(clientX,clientY)`, synthesized clicks are suppressed across all three keyboard hosts, and a second touch cancels the optical transaction until all fingers lift. Disarm restores normal training taps. Real CDP touchStart/move/end covered full/focus/mini, no training leakage, multi-touch rejection, no storage writes and normal disarmed input: 48/48 browser checks.

## Byte inheritance and reproducible selected QA

- Parent R231 ZIP 2912/2912 SHA256 inherited exactly; no inherited member modified.
- Selected old QA: R230 Chromium inkBBox 46, R230 static 25, R231 mouse 50, R231 static 28 = 149/149.
- New: R231 real-touch failure reproduction 2, R232 CDP touch 48, R232 static 21 = 71/71; selected total **220/220**.
- R232 cumulative isolated ZIP: **2926 files**, SHA256 `b22ec8f6f711dcc651db624bbb8e1ab153babb2923ef39a2ac845cab05c0a1ca`.
- Independent Python zipfile and system unzip restores each verified **2926/2926** file SHA; selected QA **220/220** on each; no file SHA changes after QA. System-unzip first combined QA attempt had an intermittent R231 mouse-suite failure after 71 checks; isolated R231 mouse retry 50/50 and complete selected rerun 220/220 passed. A redundant overwrite-unzip attempt timed out; it was not counted.
- Complete recursive historical QA **not-run**.

## Formal acceptance and safety boundary

Root T00–T11 **0/12 Accepted**. T01 formally certified 0/25; T02 approved permanent IDs 0; T03 is still isolated and not production-integrated; T05 missing-root count unknown. Browser ran `about:blank` with Chromium CDP emulated touch, **not physical Android/iOS**. True same-origin Web Locks/localStorage remains **blocked/not-run** under local browser policy; real screen reader **not-run**. High-resolution same-source image original bytes/license/per-stroke certification **not acquired**. Original R10 ZIP previously recovered; R11/R12/R35 original ZIPs and R12 20 SVGs remain missing.

Frozen V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`, 2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`, 176 codes, official SVG, production entry and user's existing localStorage remain unchanged. UI-01..UI-05 not conflated with Root T03/T05.

This is an isolated cumulative recovery and audit artifact, not a V0.36 release or formal certification.
