# V0.36 R222 — Root T01/T02 native disjoint crop membership (isolated, not accepted)

Date: 2026-10-30 (Asia/Shanghai). Parent R221 cumulative ZIP: 2785 members, SHA256 `6ee6599610f3ade340bed5eb4345defc894eeaac097ba2a1f08706338b50e3ef`. All 2785 parent members were actually read and verified against the external R221 manifest and extracted files.

## Substantive source work

R222 directly reads the frozen 1536×1086 2008 JPEG (SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`) and the byte-pinned R219 source index (SHA256 `5f90d9b36816f8586a883dd1a293e4a45c33cbbb135aed510981665228527f81`). It independently rechecks native RGB hashes for the 29 B/J/V/X crop rectangles. For each native source pixel, it computes the **exact set of sourceCropIds whose rectangles cover that pixel**. These sets partition each key's crop union without overlap, and are tied to source pixels by coordinate/RGB SHA256 and 4-neighbor connected-component summaries.

Results: 29 crops across B/J/V/X, 38 disjoint membership groups, 741 native pixels covered by at least two source rectangles: B 198, J 66, V 377, X 100. V has five shared membership groups, including **33 pixels covered by three independent source crops simultaneously**. The 4 review-only enlarged source cards show source rectangles and geometric overlap tint; they are not keyboard images or inferred glyph strokes. Unlike the R221 darkness heuristic, the new membership classification is exact geometry and does not use a color threshold.

**Interpretation:** Crop overlap does not prove shared strokes or semantic identity. No referenceShapeId/assetId/permanent instanceId is approved, and no new SVG is integrated. This work reduces ambiguity in the manual review queue but is not source certification.

## QA and restoration

Selected inherited QA 685/685, new independent pixel-by-pixel membership/4-neighbor/source tamper QA 317/317, static/frozen checks 14/14: **1016/1016 per restore**. New cumulative ZIP contains **2800 files**, SHA256 `7be01c7962097b5972f8ba6555de578432d42fd94874963d5aeb2f128419eef4`. Python zipfile and system unzip independently restored 2800/2800 member SHA256; each ran 1016/1016 selected QA and had zero post-QA mutations. The first combined verification timed out after the first restore QA; second restore QA and both final SHA audits were rerun separately and passed. Complete historical QA was not run.

## Formal acceptance boundaries

Original Root T00–T11 **0/12 Accepted**; T01 formally certified keys **0/25**; T02 approved permanent IDs **0**; actual missing-root count **unknown**. The 3508×2480 high-resolution original bytes are not locally available, license is unverified, and high-resolution per-stroke review is **not-run**. Real same-origin Web Locks/localStorage, actual screen reader, Android/iOS device QA, and complete historical QA are **not-run**. R10 original archive was previously recovered; R11/R12/R35 original archives and R12's 20 SVG files remain missing. Frozen V0.35 HTML, 2008 JPEG, 176 codes, production SVG/entry point, and existing user storage were not changed.

Next: obtain authorized same-source high-resolution original bytes and use the exact V triple-overlap coordinates to adjudicate stroke boundaries; independently review M's four unbound micro-crops and E/K shared-crop conflicts. Never promote overlap membership to identity or certification without separate per-stroke evidence.
