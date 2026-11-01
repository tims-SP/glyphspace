# R245F50 · Root T03 standalone preview glyph rendering fix (isolated, NOT Accepted)

2026-11-02. Parent: R245F49 isolated cumulative ZIP SHA256 `53693fcdd1941a8fb0c6f03508ddf506ba52a73d9aa8de571fc3e3af53ce235b`, 3544 files.

## Reproduced regression

R245F49's standalone three-view HTML contains `<use href="#wb17-...">` and `#wb20-...` references, but no corresponding SVG symbol definitions. In real local Chromium, loaded into an isolated `about:blank` page, **151/151 full-keyboard glyphs had empty 0×0 getBBox**. The prior 672 QA assertions missed actual glyph visibility; those assertions must not be interpreted as successful visual validation.

## Fix, implementation and tests

R245F50 rebuilds a standalone candidate by embedding the **147 wb17 + 2 wb20** symbol definitions from the frozen V0.35 HTML (SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`). It adds fail-closed missing-reference validation and Chromium canvas alpha-raster painted bounds in 100×100 coordinates (400px raster, alpha >16/255), with an ink-center candidate. This measures **rendered legacy SVG paint**, not certified source ink.

Fresh Chromium `about:blank` QA: **348/348**, including 151 geometry comparisons, 151 nonempty painted instances, 25 focus-key cases, 5 two-resolution comparisons, missing-symbol and invalid-input rejection, and three-view optical update/reset. Visual screenshot was manually inspected.

Parent inherited SHA: **3544/3544**. New cumulative ZIP: **3552 members**, SHA256 `9b605c44a3b434c582846e1435ee1c60388181eac6c5a71a7ff552d8d9036f1a`. Python zipfile and system unzip restored independently: **3552/3552** SHA each; each independently reran **348/348** QA; zero post-QA drift. Full historical QA **not-run**.

## Formal boundary

Root **0/12 Accepted**; T01 source certified 0/25; T02 approved permanent IDs 0; T03 production integration not done; T05 missing roots unknown. Source provenance/license and true stroke-by-stroke comparison are not certified. Real same-origin storage/Web Locks, screen reader, physical Android/iOS and full historical QA **not-run**. R246 root ZIP bytes and R11/R12/R35 original ZIPs plus R12 20 SVG remain missing. Frozen production HTML, 176 legacy codes, official SVG, and user Storage were not changed.

**Scope:** This is a functional correction of an isolated T03 candidate. It is not a new production release or acceptance certification.
