# V0.36 Round 68 — H:6/H:7 extracted component provenance (T02→T03)

2026-10-23. This is an isolated provenance audit, **not** a 2008 reference-image stroke certification, a permanent-ID assignment, or production integration.

The frozen V0.35 HTML contains two explicit `EXTRACTED_COMPONENT_D` entries: H:6 具头 (one extracted contour, source metadata: Noto Serif CJK SC Regular / SIL OFL 1.1), and H:7 皮头 (three extracted strokes, source metadata: KanjiVG / CC BY-SA 3.0). Their compact JSON path SHA256 values match the round33 path source hash, round50 source hash, round63 draft asset hash and round67 vector draft hash:

- H:6: `76754995a62c72aabe891f3c250b93e85621e4cb55a68a1dc4a945450d85ad65`
- H:7: `f21086aaf4f53a2aec0ca6fca6d4f8329330f67e2866d26505983f73253d4ab5`

Round67's `fontGlyphPathHashV035=null` remains historically correct for both: these paths come from the separate extracted-component registry rather than the ordinary font glyph map. The round68 distinction is `historicalFontGlyphPathHashBinding=false` and `frozenExtractedComponentPathBinding=true`. License strings are **unverified metadata**, not independent redistribution authorization. Neither item is source-stroke certified or bound to a permanent ID.

Parent round67 ZIP: 1006 files, SHA256 `693eea7737e0ae55d819de842214433682e959d6068b6cba5c95deab87b0bafd`. Round68 isolated cumulative ZIP: **1016 files**, SHA256 `d077e82ea340675759862d156f9bb937c8bbd1833cb49717b9ce71749e877d05`. Parent 1006/1006 byte hashes preserved; independent Python zipfile and system unzip extractions each 1016/1016 SHA-matched, each reran round68 16/16 tests, round67 27/27 tests and inherited round66 25/25+1/1 QA groups. ZIP bytes remain outside GitHub.

Frozen HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc` and low-resolution 2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49` verified. Missing round10–12/35 complete archives and round12 20 SVG remain unresolved; same-source high-resolution original not obtained. T01 0/25 certified, missing-root count unknown; T00–T11 **0/12 Accepted**. Real same-origin storage, physical devices and screen readers **not-run**. No production HTML, SVG, 176 codes or user storage modified.
