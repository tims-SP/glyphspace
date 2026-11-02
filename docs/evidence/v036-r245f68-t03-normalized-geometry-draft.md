# V0.36 R245F68 · Root T03 normalized geometry draft (not Accepted)

Date: 2026-11-03. Branch: audit/r245f68-t03-normalized-geometry-20261103.

## Real implementation
- Inherited the actual R245F67 cumulative ZIP SHA256 `25b8ee3a2d9c36ab1b113a7bc7ec4da680e8d90cf1a7387757196ca9b4ba8307`, preserving **3788/3788** member SHA256 hashes.
- Added an isolated Chromium candidate with read-only `snapshot(id)` and `exportAll()` for **151** legacy visual SVG instances. Each draft exposes `{x,y,width,height,anchor,ox,oy}` in a **100×100** coordinate system using actual rendered alpha pixels; 5 related-only associations are excluded. Candidate IDs are separate from old array indices.
- Two independent Chromium `about:blank` contexts exported identical 151-record draft JSON: SHA256 `b1abc3d88653b402c2fbe1f4569d41c50e85b83968482be577af44be2145de30`. Concurrent preview geometry changes fail the whole export; non-target geometry and three-view transforms are preserved.
- New Chromium QA **22/22**; inherited F67 **63/63**, F56 **35/35**, F65 **98/98**, T00 frozen baseline **52/52**: **270/270** selected checks in working extraction. The two independent restored copies ran **266/266 each** (T00 no-screenshot mode has 48 rather than 52 checks), with no member drift.
- Cumulative ZIP **3802** files, SHA256 `9cc7725e38ee6265270941ed4a47f0acf41564c77cadfbde70bf13ef1e1f64d3`. Python zipfile and system unzip each verified 3802/3802 member SHA256 before and after QA; independently re-exported catalog matched byte-for-byte.
- Full source, test scripts, draft catalog, archive member SHA list and independent restoration reports are preserved in the R245F68 conversation cumulative ZIP, not in production entry.

## Acceptance boundary
The measured bbox is an **uncertified rendering of legacy SVG**, not original-reference certified inkBBox or approved asset. All 151 records are `planning_only`, `referenceShapeId=null`, `assetId=null`, `sourceCertified=false`, `permanentIdApproved=false`. No official glyph, permanent ID, missing-root count, user localStorage, production HTML or 176 legacy codes changed.

**Root T00–T11 = 0/12 Accepted**; T01 source keys 0/25; T02 approved permanent IDs 0; T03 not production integrated; T04 real-user migration not accepted; T05 confirmed missing count unknown; T06–T11 not accepted. R10 original ZIP (184 members) is present; R11/R12/R35 originals and R12 20 SVGs remain missing. No full historical QA, true source license/stroke certification, real screen-reader, Android/iOS device, or user-storage migration was run. GitHub main R246 is a separate lineage; do not merge ZIP histories.

Frozen V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`; frozen 2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`, both unchanged.
