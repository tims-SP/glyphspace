# R154 · Root T03 prototype-safe instance registry (isolated; not Accepted)

Date: 2026-10-27 (Asia/Shanghai). Parent: R153 ZIP SHA256 `106319af615d7a5afb4c122306d649435137d7c502e1a084c7de45137c5b378d`, 1918/1918 inherited file SHA. New cumulative ZIP: 1931 files, SHA256 `ea6340b4207aa8e9b223140bbdc47436bfa9092814579fea102ca2bc0457b051`. Python zipfile and system unzip restored separately; each 1931/1931 SHA, 1730/1730 selected QA, SHA unchanged after QA. Full historical QA **not-run**.

## Reproduced defect and repair

R48 isolated `planImmutableInstances` writes instance IDs into a normal `{}` object. Passing a valid string ID `__proto__` silently replaces the registry prototype; `Object.hasOwn(result, '__proto__')` is false and `Object.keys(result)` omits that instance. This is a real isolated-registry correctness defect, not evidence of exploitation of the frozen production entry.

The R154 isolated adapter `v036_round154/safe_svg_instance_registry.mjs` uses `Object.create(null)` and `Object.defineProperty` for immutable own keys, rejects inherited or accessor asset keys, preserves R48 100×100 inkBBox/anchor/optical transform semantics, and keeps instance IDs independent of insertion order. Source and regression scripts are inside the cumulative ZIP; frozen R48 source is unchanged.

## Actual test evidence

- R154 Node 22 VM: **24/24** new assertions, including reproduced R48 negative control, reserved IDs `__proto__`/`constructor`/`toString`, immutable geometry, inherited/accessor asset rejection, 151/151 uncertified draft transform parity, insertion/removal/reordering stability, and frozen V0.35/reference SHA.
- Selected inherited R142–R152 Python/Node tests: **1706/1706**. This excludes historical full-suite tests and real browser/phone/screen-reader QA.
- Two independent extractions: Python zipfile **1931/1931 SHA, 1730/1730 QA**; system unzip **1931/1931 SHA, 1730/1730 QA**. Both post-QA file SHA unchanged. Python bytecode writes suppressed in these read-only restores.
- Previous R153 authorized disposable-origin Chromium CI run [40418102420](https://github.com/tims-SP/glyphspace/actions/runs/40418102420) completed success on 2026-10-26 23:23 UTC; job logs show R153 **22/22**, inherited browser checks 33/33, 27/27, 16/16, 22/22. This is **prior-round evidence**, not R154 browser QA.

## Formal gates still blocked

T00–T11 **0/12 Accepted**; T01 **0/25 source-certified keys**, formal permanent IDs **0**, T03 **not production-integrated**, T04 production migration **not accepted**, T05 complete reference coverage **not established**. R10–R12/R35 ZIPs and R12 20 SVGs missing; original high-resolution JPEG license and glyph-by-glyph approval missing; true Android/iOS and actual screen-reader QA 0. Frozen V0.35 HTML, 2008 JPEG, 176 legacy encodings, historical formal SVG and user localStorage untouched. UI-01–UI-05 remain separate from original Root T03/T05.
