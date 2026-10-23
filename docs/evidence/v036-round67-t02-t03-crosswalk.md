# V0.36 Round 67 — T02/T03 audit-only identity/geometry crosswalk

Date: 2026-10-23. Track: original T02 semantics and permanent IDs, with isolated T03 geometry. **No original T00–T11 task accepted.** This is not a V0.36 release.

## Verified cumulative artifact (not hosted on GitHub)
- Round 67 ZIP: `字间_V0.36_第六十七轮隔离累计恢复包_继承第66轮_历史缺口未补齐.zip`.
- ZIP SHA256: `693eea7737e0ae55d819de842214433682e959d6068b6cba5c95deab87b0bafd`.
- 1006 files; inherited all 996/996 parent files with byte SHA256 identity. Python zipfile and system unzip independent extractions each matched 1006/1006.
- New crosswalk QA 27/27, inherited 25/25 plus round66 1/1 groups passed in both extracted copies.
- Frozen V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`; original 2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`.

## Actual new finding
Joined the round44 156-row draft, round45 extended source evidence, round46 156-row quarantine, and round63 151-row T03 geometry export without promoting draft IDs. All 151 visual entries have isolated geometry; five related associations have no visual geometry. **H:6 and H:7 have null historical `fontGlyphPathHashV035` in round44, although round63 supplies draft SVG asset IDs.** They are explicitly marked `legacyPathHashBinding=false` and cannot be silently treated as historical source-bound assets. Round46 `originalRowSHA256` hashes the extended **round45** row, not the earlier round44 schema; the new gate verifies this correctly.

Quarantine preserved exactly: 139 manual-review-only, 2 K:2/K:3 shared-source blocked, 8 invalidated, 2 B/V namespace blocked, 5 related non-independent. No permanent `instanceId`, `assetId`, or `referenceShapeId` assigned; 0/25 source-certified keys and missing-root count unknown.

## Not run / blocked
Real shared-origin Web Locks/localStorage, physical Android/iOS, and real screen readers not run in this round. Earlier browser navigation was blocked by administrator policy; do not count as pass. Round10–12 and round35 full ZIPs, round12 20 SVGs, and legal high-resolution original source remain missing. No production HTML, formal SVG, 176 old encodings, or user storage modified.

Next: recover original provenance for H:6/H:7 and K/E/B/V; finish 25-key source enumeration before permanent ID assignment. The complete executable crosswalk, test script, audit JSON and recovery QA are in the external cumulative ZIP.
