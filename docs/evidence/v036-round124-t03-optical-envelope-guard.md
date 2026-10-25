# V0.36 第124轮：Root T03 光学校正越界守卫（隔离实现，非验收）

日期：2026-10-26。**原始T03=100×100 SVG坐标内核、inkBBox、锚点、光学校正**；不是UI-01～05渐进键盘。

## 可复现缺陷与修复

R48隔离模块 `resolveInkTransform` 只检查目标 `geometry` 在100×100内，没有检查 `ox/oy` 光学偏移之后的实际墨迹包络。用冻结V0.35的151条Path草案（R50采样墨迹BBox、R53三视图几何）逐条注入 `ox=200`，旧解析器仍输出越界矩阵；新隔离模块 `v036_round124/optical_envelope_guard.mjs` 对变换后包络执行100×100边界与锚点重构一致性检查，越界立即拒绝，不静默裁剪或移动。

真实来源：冻结HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`；2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`。R50的inkBBox仍为Canvas采样近似值，不是矢量解析精确墨迹边界，也不是2008原图逐笔认证。

新增22/22独立检查；其中151/151原始几何不回归、151/151旧新矩阵一致、151/151恶意光学校正越界被拒绝、151/151安全小偏移可往返。继承第123轮478/478定向QA。**每套500/500**，完整历史全量QA **not-run**。

## 累计包和独立复验

- R123父ZIP SHA256 `20d5aa05ff4b26e0b5d7e46b4d2818df73b66983f184bebeb646db3f8be86812`，**1620/1620**父成员SHA继承一致。
- R124独立累计ZIP SHA256 `1b2ece4a2a2486aaf078b0fc27136c7a02f3c24b30a959832a03c9deb509aec9`，**1629文件**；ZIP存放于本轮对话交付文件，不在GitHub仓库。
- Python zipfile与系统unzip两套独立解压；两套恢复各**1629/1629**文件SHA在QA后仍一致，分别500/500定向QA。
- R124包内有代码、测试、父文件SHA清单、执行报告与缺历史审计；两套独立恢复结果另有外部JSON交付。

## 严格验收边界

- 新代码是隔离模块，**没有集成到冻结生产HTML或正式SVG**。未批准任何字根、永久ID、源图裁框、Path或光学校正。
- T01正式0/25、T02正式永久ID0、T03未正式集成、T05未完成；原始T00–T11 **0/12 Accepted**。
- R10–R12/R35 ZIP及R12的20SVG未恢复；高清来源许可、逐笔归属、真实用户迁移、Android/iOS真机、真实读屏仍未完成。
- 在全新临时Chromium profile的127.0.0.1同源探测仍遭 `ERR_BLOCKED_BY_ADMINISTRATOR`；Web Locks/localStorage真实事务 **blocked/not-run**，用户原有存储未触碰。
- 回滚：只删除隔离累计包中的 `v036_round124/`；生产入口、176编码、正式SVG不变。下一步先实现精确矢量inkBBox和正式身份门禁，再评估T03集成。
