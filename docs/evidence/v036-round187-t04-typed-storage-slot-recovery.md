# R187 · Root T04: typed storage-slot journal (isolated, not accepted)

Date: 2026-10-28. This is **Root T04**, not UI-01–UI-05 and not formal acceptance.

## Reproduced defect

R186 `beforeSHA = SHA256(before ?? "")` aliases a missing localStorage key (`null`) and a present empty string (`""`). In a crash-after-shadow journal with `before=null`, a noncooperating writer can replace the shadow with `""`; R186 recovery mistakenly considers it the original state and removes the foreign empty-string value. The R187 Node test reproduces that destructive behavior on the unchanged R186 core.

## Implementation

New `scripts/r187_typed_slot_transaction_core.mjs` hashes a **typed** slot: `SHA256(JSON.stringify([raw === null ? 0 : 1, raw]))`. Both before/next journal digests and recovery comparisons use this representation. Journal schema is `glyphspace-r187-disposable-journal-v3`; legacy R186 v2 journals are rejected without mutation. This is a disposable core with no approved permanent IDs, no production migration and no user Storage access.

## Executed evidence

- R186 parent cumulative ZIP SHA256: `0897ac244652dd7fa93038c5717967e8d8a47b61599abf11015ef85ba289b456`; 2310/2310 inherited member SHA256 exact.
- R187 cumulative isolated ZIP: 2325 files; SHA256 `6f35d9e783986ab16245fcdca7e567808bcab3411cc299aa4252c99361b22ae3`. This ZIP is a conversation artifact, **not** stored in GitHub.
- Actually rerun selected inherited QA 270/270, new Node defect regression 18/18, new static 17/17 = **305/305**.
- Two independent restores: Python zipfile 2325/2325 SHA and 305/305 QA; system unzip 2325/2325 SHA and 305/305 QA; no file SHA changed after either QA run.
- Remote real Chromium fresh 127.0.0.1 same-origin, two tabs, actual Web Locks/localStorage, **17/17**. GitHub Actions run [40654063434](https://github.com/tims-SP/glyphspace/actions/runs/40654063434) succeeded on commit `f2e842c8a124aa535b8abe4eda89e7b6c0629111`. Artifact ID `12801160213` independently downloaded, ZIP SHA256 `cebf673d75c26e179860574bf6bf80e99f0c39efe31558ff962e6d6efa091ff3`, internal JSON 17/17. This remote test uses the **same R187 ESM** but a synthetic source-plan fixture, not the actual R148/R152/R178/R179 issuer chain.
- Local Chromium navigation: `ERR_BLOCKED_BY_ADMINISTRATOR` = **blocked/not-run**. Full historical QA, formal v16 migration, Android/iOS device and real screen-reader QA = **not-run**.

## Source integrity and boundaries

Frozen V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`; 2008 reference JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`, both rechecked in the cumulative archive. No change to frozen production entry, 176 old encodings, formal SVG or user storage. No third-party high-resolution source license. R10 original ZIP recovered earlier; R11/R12/R35 original ZIP and R12 20 SVG remain unavailable.

**Acceptance:** T00–T11 **0/12 Accepted**; T01 **0/25** formally source-certified; permanent IDs approved **0**; missing-root count **unknown**. This is an isolated T04 safety improvement, not a completed migration.

**Remaining risk:** localStorage has no atomic compare-and-swap; a noncooperating script can still race after the final check. R187 only closes the specific null/empty alias, and a malicious same-origin script able to forge the journal cannot be excluded by this mechanism.
