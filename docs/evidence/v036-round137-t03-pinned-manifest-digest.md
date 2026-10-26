# 字间 V0.36 · 第137轮 Root T03隔离执行报告（非正式验收）

- 父ZIP：R136，SHA256 `a60486ed2af060f774450669d6c81e3ad99edab089a46f62b33d9144470d3806`，1768文件逐项SHA继承一致。
- 新发现的真实完整性缺陷：R136把SHA作为调用者传入参数；调用者篡改字形Path或fill后重新计算SHA，R136仍接受并挂载，故“SHA验证”只能证明传入字节与调用者声明一致，不能证明字节是冻结审阅版。
- 新隔离实现 `pinned_verified_svg_renderer.js`：把R134的151条冻结派生草案SHA `89c6bbaac319f4f59d81c18ea5d0cbbb42899558c7ba7cf65fc81107de020f8a` 固定在私有模块内，公开 `GlyphSpaceR137.mountPinned(raw,view,ids)`，不接受调用者自报SHA；R136和更旧API不泄漏到页面，发现旧公开API时拒绝初始化。
- Chromium 144 about:blank真实复现R136对重新哈希的Path、fill改动均错误接受；R137对这两种改动均以`manifest-sha-mismatch`拒绝；合法151旧可视实例×三视图=453 SVG，453/453符号ID唯一；151/151冻结Path及其原始来源hash经独立Python复核一致（149 frozen_font_path、1 extracted_serif_contour、1 extracted_kanjivg_strokes）。
- 新QA 21/21，继承R132–R136 QA 77/77，共98/98定向测试；这不是完整历史全量QA。
- 限制：SHA钉住的是冻结V0.35派生的**未认证草案**，不是2008原图认证或正式永久ID；JS模块本身如被恶意替换，pin也不构成签名/信任根。仍未生产集成。
- T01正式0/25，T02正式永久ID0，T05未完成，原始T00–T11 0/12 Accepted；R10–12/R35原始ZIP与R12的20SVG未找到，高清同源原图与许可、真实同源迁移、真机、真实读屏均未验收。
- 冻结V0.35 HTML、2008原JPEG、176编码、历史正式SVG及用户原有存储均未修改。
