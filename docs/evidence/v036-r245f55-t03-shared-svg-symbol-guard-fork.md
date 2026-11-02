# R245F55 · Root T03 shared SVG symbol source async integrity (isolated candidate)

Date: 2026-11-02. **Formal T00–T11 Accepted: 0/12**.

## Reproduced defect and actual fix
Real Chromium about:blank reproduced R245F53 accepting an asynchronous placement after the referenced shared SVG `defs` path `d` changed while `Image` decoding was pending. R245F53 validated the instance markup, but not the shared symbol source. R245F55 freezes the shared symbol `defs.innerHTML`, checks it during instance validation and again after asynchronous image decode. Mutation of path geometry, addition/removal of symbol nodes, style changes, and pre-call mutation fail closed; standalone paint measurement also rejects stale source. Normal placement, optical correction, 151 legacy visible instances, and 156 unapproved identity drafts remain functional. The source is an isolated HTML candidate, not the production entry.

## Archive and independent reproducibility
- Parent R245F54 cumulative ZIP SHA256: `97013f27a78bab79492bcf30474663460ff994bc8d7d2da67eebab3dc530dd9f`, **3597/3597 inherited member SHA**.
- R245F55 cumulative ZIP SHA256: `28fd54a3b8ff132b4c11a6c14838c69e9f5550378aabf0e78d3db07f1c423dec`, **3616 members**.
- Python ZipFile and system unzip independent recovery: **3616/3616 member SHA** each; zero post-QA drift.
- New Chromium QA: **31/31**, including old defect reproduction. R245F50/F51/F52/F53 old QA directly on new HTML: **348+175+217+20=760/760**. Each final independent recovery ran **791/791** selected QA. Full historical suite: **not-run**.
- Test surface: Chromium 144, isolated `about:blank`, no user storage. Not a real screen reader, Android/iOS device, high-resolution original stroke certification, or production migration.

## Immutable baselines and blockers
- V0.35 HTML SHA256: `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`.
- 2008 reference JPEG SHA256: `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`.
- Frozen 176 codes, formal SVGs, production entry and user localStorage unchanged.
- T01 source-certified keys **0/25**, T02 approved permanent IDs **0**, T05 missing-root count **unknown**, T03 formal inkBBox and production integration incomplete. Root **0/12 Accepted**.
- Original round 11/12/35 ZIPs, round-12 20 SVGs, and R246 main cumulative ZIP bytes remain missing; no claim of complete history.
- Next: prioritize legal same-source high-res per-stroke M/K/E/B/J/R/X/V arbitration and independent IDs, then integrate certified assets.

The cumulative ZIP and final QA reports are delivered as conversation artifacts, not publicly redistributed through this repository.
