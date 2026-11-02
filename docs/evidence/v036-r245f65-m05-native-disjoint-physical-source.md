# V0.36 R245F65 · Root T01/T02 M05 crop truncation and disjoint K/M physical components (review-only)

- Parent: R245F64 isolated cumulative ZIP SHA256 `11ba7e812a8a9bcec7e778513bef279b038f3116abf7f97f0b500c379364192f`; **3750/3750 member SHA inherited**.
- New isolated cumulative ZIP: **3761 files**, SHA256 `d4f866225fd1f1baa0f6a8db4d9c6ad00ea18ff17cfd6575f308681a13ee5eb7`. Python zipfile and system unzip independently restored 3761/3761 exact member SHA, with **443/443 selected old+new QA each**, zero QA-induced member drift. Full historical QA **not-run**.
- Authorized VPS fetched third-party candidate 996823-byte high-resolution ZIP (SHA256 `fb7a9984a84be12a71d71dc86088b8859762ca97cb9a3db173b4a8adaf0b9707`) and read 3508×2480 JPEG (SHA256 `47c5d53f6cf57ac67c957c6510a3e2696072c3ce63e73024ed025367f31c600e`). Image pixels were not committed or redistributed. Official-original equivalence and license remain **unverified**.
- **New finding:** M-vis-05 (old alias M:3), registered crop `[2267,1472,2309,1524]`, also truncates its physical ink component: 7/9/9 pixels outside the bottom edge at luminance thresholds 70/100/130. Earlier R245F64 documented four other M crops (M04/06/07/08) as incomplete; **M05 is an additional issue**.
- Enlarged full M lower strip `[2260,1475,2415,1540]` contains four disjoint 8-connected physical ink components at all three thresholds, spatially corresponding to M05/M06/M07/M08. At threshold 100 the components contain 299/111/115/90 pixels. K-left and K-right each contain three physical components at all thresholds.
- Independent 8-connected BFS and row-run union-find matched in **12/12 native region×threshold comparisons**. Eleven review-only disjoint component envelopes were generated (3 K-left, 3 K-right, 1 M04, 4 M lower). These are **not** official source crops, semantic strokes, roots, SVG assets, or permanent IDs.
- Root acceptance remains **0/12 Accepted**; T01 **0/25** source-certified keys, T02 **0** approved permanent IDs, T05 missing-root count **unknown**. No formal SVG or production HTML changes. Frozen V0.35 HTML, 2008 JPEG, 176 legacy codes and user Storage unchanged.
- R10 original archive remains embedded from R164. Original R11/R12/R35 ZIPs and R12 20 SVGs remain unrecovered; R246 main cumulative ZIP was not mixed into this branch. Real screen reader, Android/iOS physical devices, user-storage migration and full historical QA are **not-run**.

**Next:** obtain source license/official provenance, human stroke-by-stroke adjudication for M05–M08 and K:2/K:3, then T02 identity approval and T05 formal SVG work. Repeated threshold/QA results cannot substitute for human source certification.

This is a Draft-only isolated evidence branch; production entry remains frozen.
