# R212 · Root T03 — HTML矩形overflow裁剪保守墨迹包络（隔离、非验收）

2026-10-29。正确原始任务：**T03 SVG坐标内核**；非UI-03/UI-05。

## 可复现问题与实质修复

R211的`outer_html_paint_gate.mjs`对任何HTML祖先`overflow:hidden/clip/scroll`均失败关闭，合法滚动键帽也无法得到局部几何。R212新增`v036_round212/rectangular_overflow_ink_envelope.mjs`（独立累计ZIP内，源码SHA256 `8e7144e93043bb74f78e54c5397fd700afef6400e3e3a78cd4c308bdac22c0e7`），从R210的含stroke原始`inkBBox`出发，使用真实Chromium `getScreenCTM`、HTML祖先padding-box及滚动后屏幕矩阵，逐层相交得到`visibleInkUpperBoundBBox`。原始`inkBBox`保持不变。完全裁剪返回null；不支持的旋转、透明、mask、filter、clip-path等拒绝。

**语义边界：** 结果是可能可见墨迹的保守矩形**上界**，不是实际逐像素inkBBox，更不是原图逐笔认证。模块保持`sourceCertified=false`、`productionIntegrated=false`、`formalAccepted=false`。不修改生产HTML、正式SVG、176旧编码或用户存储。

## 实际验证

- 父R211累计ZIP SHA256 `ddc0127fe6317f1c9f336b00069766f5b1ea2ff5178be2e328024d4036a99739`；实际解压并逐文件核验**2663/2663 SHA一致**。
- 真实Chromium `about:blank`：906组旧SVG在无裁剪状态保持几何一致；100×100黑矩形截图10000像素、40×50隐藏溢出2000、滚动25×10后2000、完全裁剪0、`overflow:clip` 2000；嵌套裁剪、拒绝旋转/opacity/clip-path覆盖在新增21/21浏览器检查内。
- 旧选定QA：R197 Node35、R198 Node41、R210 Chromium12及静态12、R211 Chromium14及静态12，共**126/126**；新Chromium21及静态12，共**33/33**；本轮**159/159**。R211递归670套件尝试超时，未计入通过；完整历史全量not-run。
- R212累计ZIP **2675文件**，SHA256 `4f4fd0283aa87dba0f95224c5e6afc5a11ca67b048ab8c263be5e79ce9e296ae`。Python zipfile与系统unzip两次独立解压各**2675/2675 SHA**、各真实重跑**159/159 QA**，QA后文件变化0。
- 冻结V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`；2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`，均复核未变。

## 阻断与正式验收

**T00–T11 0/12 Accepted**；T03未生产集成；T01正式认证0/25键、T02正式永久ID0、T05缺根数未知。R11/R12/R35原始ZIP及R12 20 SVG未恢复；未获得同源高清原始字节与许可，逐笔认证not-run。真实同源Web Locks/localStorage blocked/not-run；真实读屏、Android/iOS真机及完整历史全量QA not-run。无历史连续全量声明。回滚：删除R212隔离模块/累计包，不触碰冻结生产入口。
