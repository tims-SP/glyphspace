# 字间 V0.36 · R245F58 Root T01/T02 (T05 related; isolated, NOT Accepted)

## Reproducible change

- Parent: R245F57 ZIP SHA256 dcb6a5035f61c9bd85f80cdb20cb936f300091102711cf09578cdd2d243d48ca, 3653/3653 inherited SHA.
- Baseline R245F57 actual Chromium DOM bug: another pointer's move/up appended and prematurely committed the active trace; imported identical points were accepted as a zero-length stroke. R245F58 isolates a stroke by pointerId, aborts when a second pointer touches, and rejects zero-length imports. Old failures reproduced; new and normal mouse paths 14/14.
- The new candidate HTML is an isolated review artifact, not production source or a certified SVG asset.
- Real authorized VPS Chromium, isolated 127.0.0.1 origin and fresh temporary profile, loaded the actual private 1348865-byte 3508x2480 JPEG via native file chooser. The workbench itself verified SHA256 47c5d53f6cf57ac67c957c6510a3e2696072c3ce63e73024ed025367f31c600e using browser WebCrypto (no mock); actual mouse stroke, unapproved export/import, zero-length rejection, storage nonmutation: 14/14. QA JSON SHA256 d178f4ce49926d6f092ebcd6c9ec1eb0109ee0c5934f513969abcfff6c3dd58b. Private JPEG bytes not distributed.
- Cumulative R245F58 ZIP: 3662 members; SHA256 a9ea3ac3b6c64a85e04640b22796f8a51288d972aa02b4f089e9b9f28c542ed8. Python and system unzip independent extraction: each 3662/3662 members SHA and parent 3653/3653 inheritance, selected old 998/998 + new 14/14 = 1012/1012; additional old-browser suite on new HTML 28/28 each; post-QA file drift 0.
- Full historical QA not-run. R10 original ZIP embedded; R11/R12/R35 original ZIP, R12 20 SVG, R246 main cumulative ZIP missing. No continuous full history claim.

## Formal gates unchanged

Official same-source, licensing, per-stroke semantic certification unverified. T01 certified 0/25 keys, T02 approved permanent IDs 0, T05 confirmed missing roots null. T00–T11 remain 0/12 Accepted. Real user production migration, screen reader and Android/iOS physical device QA not-run. Frozen V0.35 HTML SHA fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc, 2008 JPEG SHA df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49, 176 old codes, production entry and user Storage untouched.

Next: legitimate original-source license/provenance, M/K/E stroke ownership, formal ID approval and T05 true missing-root inventory; never count reviewer UI tests as source certification.
