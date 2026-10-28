# R193 · Root T04 real Chromium stale-idempotent source race (isolated, non-acceptance)

**Date:** 2026-10-28. **Original task:** T04 storage and legacy migration, not UI track.

R192 ESM is executed unmodified in two real Chromium tabs on a fresh ephemeral 127.0.0.1 origin. After a successful first stage and a normal idempotent second stage, the third stage pauses during asynchronous buildPayload. A second tab changes the synthetic source. The candidate rejects the stale idempotent result and preserves external source, previous shadow, unrelated key, and absence of journal.

- R193 real Chromium GitHub Actions run **40703055405**: **success, 15/15**. Original artifact ID **12822268035**, ZIP SHA256 `0c8dc9e0a5cba157a4365aa34c153d9d624704b07ceb462a2343620792fe6592`; artifact ZIP was downloaded, CRC-checked, and its JSON independently parsed.
- Previously unverified R190 real Chromium run **40677542370**: success **15/15**; artifact ID **12810883545**, SHA256 `732e07e39fff772c274ab74f069da2beeaab2fa3e52e0c6f30e8b946fe356e68`. R192 Node run **40693763253**: success **13/13**, artifact ID **12819140066**, SHA256 `f2162d4d04b07ec02d7a121ae47b07a339048d3ae78d113f00b76e2e6d0f7b4e`.
- Parent R192 cumulative ZIP SHA256 `7e844d4126ed6b830088e9346f288509d317646d3d5eaa729cf91e0dfdb014c9`, 2402/2402 exact SHA inheritance; R193 cumulative ZIP 2417 members, SHA256 `88d7258d80cc83aed15b17fa8c97482202dd6d113b49454c610b15896003e6d7`. Python and system unzip independent restores each 2417/2417 SHA, selected inherited 588/588 plus new static 12/12 = **600/600**, no file changes after QA. Remote browser 15/15 is separate and not included in 600.
- Local Chromium was actually launched but loopback navigation returned `ERR_BLOCKED_BY_ADMINISTRATOR`: **blocked/not-run**. The real browser test uses a **synthetic issued plan**, NOT the full R148/R152/R178/R179 issuer chain, and does NOT migrate user data.
- Missing original R11/R12/R35 ZIP and R12 20 SVG persist; R10 restored previously. High-resolution legal source bytes and per-stroke source approval remain blocked; T01 0/25 certified, T02 zero approved permanent IDs, missing-root count unknown. Full historical QA, Android/iOS, real screen-reader QA, production integration and migration **not-run**.
- Frozen V0.35 HTML, 2008 JPEG, 176 encodings, production SVG, production entry and user Storage remain untouched. Original T00–T11: **0/12 Accepted**.

Code: `scripts/r193_idempotent_real_browser.py`; CI: `.github/workflows/r193-t04-idempotent-real-browser.yml`. This is a **candidate T04 browser regression**, not a T04 acceptance certificate.
