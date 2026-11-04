# T03 isolated geometry kernel — 2026-11-04

Track: Root T03 (100×100 / inkBBox / anchor / optical correction), **NOT Accepted**.

Branch `work/v036-t03-geometry-20261104` adds `prototypes/t03/geometry.mjs` and `geometry.test.mjs`. Pure ESM transforms source coordinates to logical 100×100 using the longest inkBBox dimension, anchor and optical offsets; inverse transform and affine inverse reject invalid/noninvertible geometry. No DOM, storage or production integration.

Executed: `node prototypes/t03/geometry.test.mjs` — 54/54 assertions. `python3 scripts/verify_repo.py` — repository checks pass after checksum manifest refresh on VPS. This is only synthetic geometry; no browser visual QA, production three-view integration, certified shapes, authorized real-origin, screen reader or real device.

R246 parent ZIP raw bytes not present on authorized VPS. Parent member SHA inheritance, old/new cumulative QA, new cumulative ZIP and two independent ZIP extraction replays: **BLOCKED/NOT-RUN**. Do not promote R246 to independently verified baseline; latest independently verified baseline remains R46. T00–T11: 0/12 Accepted.

Frozen `index.html`, 176 legacy encodings, historical SVG and user localStorage remain untouched.

GitHub sync: the isolated module, tests and this evidence were uploaded to this feature branch via GitHub connector; the VPS local commit `8110159` is not identical to the remote commit chain. The checksum manifest on GitHub is not yet updated for these new files; GitHub branch integrity check is pending.
