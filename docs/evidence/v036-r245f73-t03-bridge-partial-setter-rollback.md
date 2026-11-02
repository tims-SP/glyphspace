# R245F73 · Root T03 — partial-setter rollback and irreversible commit quarantine

## Source / scope
- Parent fork GitHub commit: e8bb0dd1cd3c811fd9a1b939b09e9ed04f0a87b4 (R245F72); root main was 03c29e0fcc4b968224b9fdf37bc6d45b54da6b97 when checked.
- New isolated module: scripts/r245f73_t03_live_three_view_bridge_v2.js. Original F72 bridge is untouched.
- New QA: scripts/qa_r245f73_t03_bridge_faults.cjs.
- No user localStorage, production HTML, 176 codes or approved SVG modified.

## Reproduced defect
F72 calls P.setOptical before appending its rollback obligation. A setter that mutates a second target and then throws leaves the second target modified, while the first target is rolled back. Running the new fault suite against the old F72 bridge exited 1 at "partial setter rollback"; actual second optical {ox:2,oy:1} versus expected {ox:0,oy:0}.

## Fix
- Register the current target's rollback obligation before invoking P.setOptical.
- If rollback of any target fails, poison the bridge and refuse further transactions.
- If registry commit returns an unexpected revision after having committed, poison without rolling back SVG independently, avoiding a false claim of restored consistency.
- Retain existing CAS, preflight, readback and no-storage isolation.

## Real tests (authorized VPS, 2026-11-03)
- Node v24.22.2, node --check: PASS.
- Node VM isolated fault injection: 5 scenarios, 37 assertions PASS.
- Repository integrity initially failed until SHA manifest update, then rerun required.
- Original F72 failure reproduction: observed expected assertion failure, NOT a passing legacy QA.
- Actual Chromium, browser same-origin, Web Locks/localStorage, read-screen, Android/iOS: NOT RUN.
- Source image legal provenance / high-res stroke identity: NOT VERIFIED.

## Cumulative archive blocker
Files connector confirms a conversation R245F72 ZIP and materialized 87,522,718 bytes at /mnt/data/glyphspace_run_73, but Python/container execution returned ConnectionError/ResponseError; authorized VPS has no /mnt/data and no parent ZIP. The actual parent ZIP bytes could not be independently read and checked in this run. Thus parent 3869/3869 SHA inheritance, new cumulative ZIP, and two independent archive restores are BLOCKED, not claimed. No new cumulative baseline is issued. The prior F72 ZIP and SHA remain the last previously reported fork baseline, not newly verified in this run.

## Acceptance
Root T00–T11: 0/12 Accepted; T01 0/25 certified keys; T02 0 approved permanent IDs; T03 not integrated; T05 missing-root count unknown. This is isolated engineering progress only.
