# R155 · Root T01/T02 native JPEG pixel ownership graph (isolated; not Accepted)

Date: 2026-10-27 (Asia/Shanghai). GitHub main before execution: `c16398782fc977e4ddaddc3bbd24b370266af35d`. The six mandatory source documents were read. Parent R154 cumulative ZIP SHA256 `ea6340b4207aa8e9b223140bbdc47436bfa9092814579fea102ca2bc0457b051`, **1931/1931 inherited file SHA256 identical**. R155 independent cumulative ZIP: **1942 files**, SHA256 `99f0c1315800dccceec75331cf01eba86989be01abf788e602e660a0a8c69125`. Two independent restorations (Python zipfile and system unzip): **1942/1942 SHA** before and after QA, each **1859/1859 selected QA** (1730 inherited + 129 new). Complete historical QA **not-run**.

## Actual new source work

Read the original frozen 2008 JPEG bytes, SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`, and the R146 crosswalk. Independently recomputed **170/170 native RGB crop hashes across 25 keys**. Exhaustively compared same-image rectangles to construct a source-pixel overlap graph, without deriving glyphs from fonts, thresholds or SVGs.

**18 overlap edges, zero cross-key edges:** 2 exact duplicate **legacy-slot** crops (E:1/E:8 and K:2/K:3); 8 exact legacy-to-observation crop aliases (K four, M four); 6 partial legacy/observation overlaps; 2 mutual overlaps between unbound physical observations (V shares **57 native pixels**; X shares **32 native pixels**). Per-key edges: B1, E1, J1, K5, M4, V4, X2. V shared region contains 52 distinct RGB triples; X shared region 31. RGB variation can reflect JPEG compression/background and **does not prove shared ink, a stroke, or a separate root**.

The R155 cumulative ZIP contains `v036_round155/source_pixel_ownership.py`, `qa_source_pixel_ownership.py`, the complete `R155_native_source_pixel_ownership.json` (18 edge records with shared native rectangle/RGB SHA/review gates), and `R155_overlap_review_sheet.png` (blue legacy ROI, red physical observation ROI; diagnostic only). New QA **129/129**, including independent native crop and overlap SHA checks and fail-closed adversarial mutation cases. Inherited selected R142–R154 QA **1730/1730**. No real browser, user storage, or device QA was run in R155.

## Acceptance and blockers

The overlaps are **review ROIs**, not certified ink masks. Formal source review remains **0/25 keys**; approved permanent IDs **0**; confirmed missing root count **unknown/null**; original Root T00–T11 **0/12 Accepted**. In particular, K/E duplicate crops and V/X physical overlaps require legal same-source high-resolution original bytes and stroke-by-stroke ownership adjudication. Historical R10–12/R35 ZIPs and R12's 20 SVGs remain missing; GitHub Releases empty, main tree and locally mounted R145–R154 archives and Library search did not recover them. Full historical QA, Android/iOS real devices, and actual screen-reader QA remain not-run. Frozen V0.35 HTML, original 2008 JPEG, 176 codes, historical SVGs and user localStorage unchanged. No third-party original was redistributed.

Root task semantics are unchanged; R36–40 UI work remains UI-01 through UI-05, not T03/T05 acceptance. This is **source review prioritization**, not a formal shape, ID, completeness or publication certification.
