# V0.36 R173 · Root T01/T02 — real 3508×2480 pixel topology of 41 overlapping review ROIs (NOT certification)

2026-10-28. Source: [GitHub Actions run 40557130807](https://github.com/tims-SP/glyphspace/actions/runs/40557130807), job 122376068762, **completed/success**. This workflow actually downloaded the pinned 996823-byte external ZIP in its temporary runner memory, verified ZIP SHA256 `fb7a9984a84be12a71d71dc86088b8859762ca97cb9a3db173b4a8adaf0b9707`, extracted 1348865-byte JPEG in memory and verified JPEG SHA256 `47c5d53f6cf57ac67c957c6510a3e2696072c3ce63e73024ed025367f31c600e`, 3508×2480. It then read original highres pixels for 41 R172 p95-envelope intersection pairs. The local ZIP/container **does not** include or read the external JPEG; no image pixels were published.

Source coordinate metadata SHA256: `1300d30b60f4d308dd7a8c17fcacf528a42f950f6122589e8c42fd2eb5f83310`. R172 parent source SHA and affine-derived review-only envelopes are preserved. **Third-party license not established; formal T01 key certification 0/25; permanent IDs approved 0; true missing-root count unknown; T00–T11 0/12 Accepted.**

## Actual highres observations

| Threshold (grayscale <) | Pairs with any dark pixels in shared review ROI | Pairs with an 8-connected component touching shared + both exclusive regions |
|---:|---:|---:|
| 100 | 31/41 | 10/41 |
| 160 | **34/41** | **12/41** |
| 210 | 35/41 | 16/41 |

Ten pairs have **identical geometric review envelopes** (aliases/overlays, not ten independently identified glyphs). Twenty pairs appeared only after R172's 3px p95 review padding; at grayscale threshold 160, **13/20** contain dark shared pixels and **10/20** have a dark connected component touching both exclusive regions. These are **review-priority signals**, not proof that the two observations are one stroke, one root, or a collision. At threshold 160, all 21 pre-existing pairs contain dark pixels; only 2/21 have a bridging component. JPEG artifacts, labels, borders and antialiasing can affect the counts.

## All 41 remote CI pair measurements at grayscale threshold 160

| # | Key | A | B | Added by p95 margin | Exact same envelope | Shared dark pixels | Bridging components |
|---:|:--:|---|---|:--:|:--:|---:|---:|
| 0 | A | `legacy:A:6` | `legacy:A:7` | yes | no | 19 | 1 |
| 1 | A | `legacy:A:7` | `legacy:A:8` | yes | no | 4 | 1 |
| 2 | B | `legacy:B:0` | `obs96-6263b6c983ac028cca06` | no | no | 7 | 0 |
| 3 | B | `legacy:B:3` | `legacy:B:5` | yes | no | 0 | 0 |
| 4 | B | `legacy:B:7` | `obs96-6263b6c983ac028cca06` | no | no | 171 | 0 |
| 5 | E | `legacy:E:1` | `legacy:E:7` | no | no | 34 | 1 |
| 6 | E | `legacy:E:1` | `legacy:E:8` | no | yes | 78 | 0 |
| 7 | E | `legacy:E:3` | `legacy:E:4` | yes | no | 0 | 0 |
| 8 | E | `legacy:E:7` | `legacy:E:8` | no | no | 34 | 1 |
| 9 | F | `legacy:F:0` | `legacy:F:1` | yes | no | 34 | 1 |
| 10 | F | `legacy:F:3` | `legacy:F:4` | yes | no | 8 | 1 |
| 11 | F | `legacy:F:5` | `legacy:F:6` | yes | no | 49 | 1 |
| 12 | H | `legacy:H:1` | `legacy:H:7` | yes | no | 0 | 0 |
| 13 | I | `legacy:I:1` | `legacy:I:2` | yes | no | 9 | 1 |
| 14 | J | `legacy:J:1` | `obs96-f1241fd6a2fb4c62103d` | no | no | 115 | 0 |
| 15 | K | `K-physical-lower-left` | `legacy:K:2` | no | yes | 430 | 0 |
| 16 | K | `K-physical-lower-left` | `legacy:K:3` | no | yes | 430 | 0 |
| 17 | K | `K-physical-lower-right` | `legacy:K:4` | no | yes | 490 | 0 |
| 18 | K | `K-physical-upper-left` | `legacy:K:0` | no | yes | 915 | 0 |
| 19 | K | `legacy:K:2` | `legacy:K:3` | no | yes | 430 | 0 |
| 20 | L | `legacy:L:5` | `legacy:L:6` | yes | no | 7 | 1 |
| 21 | M | `M-candidate:2008-M-vis-01` | `legacy:M:0` | no | yes | 1120 | 0 |
| 22 | M | `M-candidate:2008-M-vis-02` | `legacy:M:1` | no | yes | 524 | 0 |
| 23 | M | `M-candidate:2008-M-vis-03` | `legacy:M:2` | no | yes | 591 | 0 |
| 24 | M | `M-candidate:2008-M-vis-05` | `M-candidate:2008-M-vis-06` | yes | no | 60 | 0 |
| 25 | M | `M-candidate:2008-M-vis-05` | `legacy:M:3` | no | yes | 446 | 0 |
| 26 | M | `M-candidate:2008-M-vis-06` | `legacy:M:3` | yes | no | 60 | 0 |
| 27 | M | `M-candidate:2008-M-vis-07` | `M-candidate:2008-M-vis-08` | yes | no | 24 | 1 |
| 28 | N | `legacy:N:1` | `legacy:N:2` | yes | no | 51 | 1 |
| 29 | N | `legacy:N:3` | `legacy:N:6` | yes | no | 3 | 0 |
| 30 | P | `legacy:P:4` | `legacy:P:5` | yes | no | 38 | 2 |
| 31 | Q | `legacy:Q:0` | `legacy:Q:6` | yes | no | 0 | 0 |
| 32 | Q | `legacy:Q:2` | `legacy:Q:5` | yes | no | 0 | 0 |
| 33 | R | `legacy:R:4` | `legacy:R:6` | yes | no | 0 | 0 |
| 34 | V | `legacy:V:1` | `obs96-bb547ff8768f0de0842a` | yes | no | 0 | 0 |
| 35 | V | `legacy:V:3` | `obs96-bb547ff8768f0de0842a` | no | no | 113 | 0 |
| 36 | V | `legacy:V:4` | `obs96-85a2d4e019bd8bd881f7` | no | no | 201 | 0 |
| 37 | V | `legacy:V:4` | `obs96-bb547ff8768f0de0842a` | no | no | 97 | 0 |
| 38 | V | `obs96-85a2d4e019bd8bd881f7` | `obs96-bb547ff8768f0de0842a` | no | no | 30 | 0 |
| 39 | X | `legacy:X:0` | `obs96-9d7d33d4acb81dabb21e` | no | no | 42 | 0 |
| 40 | X | `obs96-2fb9aa095236cc551ee4` | `obs96-9d7d33d4acb81dabb21e` | no | no | 21 | 0 |

## Limits / follow-up

An 8-connected dark component is only a pixel-topology observation. No semantic stroke segmentation, same-source proof, authorization for redistribution, permanent identity adjudication or formal SVG promotion was performed. The p95 review envelope is not a maximum-error guarantee. M/K/E/B/J/R/X/V remain under independent identity and contour review. R11/R12/R35 original ZIPs and R12's 20 SVGs remain missing. Real same-origin Web Locks/localStorage migration, Android/iOS devices, real screen reader QA and full historical QA remain blocked/not-run. Frozen V0.35 HTML, 2008 reference JPEG, 176 legacy encodings, historical formal SVG and user storage were not changed.
