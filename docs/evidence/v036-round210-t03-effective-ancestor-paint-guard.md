# V0.36 R210 · 原始 T03 有效绘制墨迹边界守卫（隔离非验收）

2026-10-29。本轮真实读取 R209 累计ZIP（2640成员，SHA256 `89c8eed7d8dfbf85b29d68565e33c1d577d79d82be73584534944c5c9c0d81df`），逐文件2640/2640 SHA继承一致，原始T00–T11编号及 `accepted=false` 未漂移。

## 真实缺陷和修复

R200 `inspectStrokeAwareInk` 计算描边保守 `inkBBox` 时未检查祖先 `<g>/<svg>` 的有效绘制属性。真实 Chromium 复现：祖先 `opacity=0`、`visibility=hidden`、全裁剪时旧模块仍返回非空 `inkBBox`。独立截图黑像素：正常3200、祖先完全透明0、全裁剪0。

R210在隔离ZIP `v036_round210/effective_paint_ink_guard.mjs` 新增真实 `getComputedStyle` 有效绘制守卫：从group到svg的祖先及直接path逐层拒绝不可见、透明度变化、clip-path、mask、filter、fill/stroke-opacity、混合模式等不能可靠量测的效果，然后调用未修改的R200墨迹边界模块。**失败关闭，不自动推断形态，不是原图认证或生产集成。**

## 实际QA和独立恢复

- 三视图（full/mini/focus）×编辑前后：906个真实旧SVG实例组，正常状态的新旧 `inkBBox` 完全一致。
- 14/14有效绘制对抗案例被新守卫拒绝，另有CSS样式表覆盖拒绝及实际截图像素验证。
- 选定旧QA 620/620 + 新Chromium 12/12 + 冻结静态12/12 = **644/644**；完整历史全量QA **not-run**。
- R210累计ZIP：**2651文件**（父2640 + 新11），SHA256 `12e329603696bd85991666c222e14f68124c920a8fb9effa2331661923433449`。
- Python zipfile与系统unzip两套独立解压均 **2651/2651 SHA**，恢复后各 **644/644 QA**，QA后SHA无变化。
- R210 ZIP及恢复证据在本轮会话交付；仓库仅保存技术证据/状态，不把64MB隔离ZIP误当生产发布。

## 正式边界

原始T00–T11仍 **0/12 Accepted**；T03没有生产集成，T01正式来源0/25、T02批准永久ID0、T05缺根数未知。合法同源高清原始字节与许可未获得；R11/R12/R35 ZIP和R12 20SVG仍缺。真实同源Web Locks/localStorage **blocked/not-run**，真机/真实读屏/完整历史全量QA **not-run**。冻结V0.35 HTML、2008 JPEG、176编码、正式SVG、生产入口及用户存储均未修改。
