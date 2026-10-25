# V0.36 第128轮 · 原始T03：冻结SVG真实涂色像素遮罩交集（隔离，非验收）

- 时间：2026-10-26；来源：冻结V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`；父第127轮累计ZIP SHA256 `f2692f705f93b26b3e722c86b61725dcc22b506d2c1eda95b29f32347eb6eb6e`。
- 真实实现：Chromium `about:blank` 临时上下文加载冻结HTML，克隆原始DOM中的单独字根与单独`.diagram-marker`，保持原始`<use>`、SVG Path、stroke和CSS；分别渲染400×400与800×800白底遮罩，以220/245两档阈值计算独立涂色像素交集。只读、未触碰用户原点或存储。
- 第127轮9组保守BBox候选中，**5组确有绘制像素重叠**：Q:4/marker0（800px阈值245交集694像素）、Y:3/marker1（303）、J:4/marker1（648）、L:1/marker2（1032）、L:1/marker3（327）；**4组无涂色像素交集**：Y:3/marker0、H:4/marker1、J:4/marker2、N:7/marker0。2组额外阴性对照也为0；400/800和两阈值下重叠/不重叠分类一致。
- **边界**：这证明当前Chromium独立绘制层的像素重叠，不证明其为未批准的视觉缺陷；部分区位笔画徽记可能有意与字根重叠。不能凭此自动移动、删除或认证任何字根。像素计数依赖抗锯齿、字体和DPR；未完成正式矢量/跨设备判定。
- 新QA 73/73，继承第127轮定向QA 819/819。第127轮父1663/1663逐文件SHA继承；第128轮累计ZIP **1679文件**、SHA256 `0606855e57ec7e83c8240cc25148802d1aef654833e36933eab6a98605e940b0`；Python zipfile与系统unzip两套独立恢复各892/892，恢复后1679/1679文件SHA一致。完整历史全量QA为not-run。
- ZIP中包含可复跑脚本`v036_round128/measure_true_paint_masks.py`、`qa_render_replay.py`、`qa_true_paint_masks.py`、`run_targeted_qa.py`、11组遮罩审计JSON与只读复核PNG；**ZIP本体不在GitHub**。
- 正式状态：T00–T11 **0/12 Accepted**；T01正式0/25、正式永久ID0、T03未集成、T05未完成。第10–12/35轮历史ZIP及第12轮20SVG缺失；许可、原图逐笔、真实同源迁移、Android/iOS真机、真实读屏、完整历史QA均未完成。冻结入口、176编码、正式SVG、用户存储均未修改。
