# R214 · Root T03 SVG根视口裁剪保守上界（隔离，非验收）

**2026-10-29；原始任务T03，不属于UI-01至UI-05。** 从R213已验证累计ZIP真实继承2688/2688文件SHA，父ZIP SHA256 `5907af02850e0084528b3082f6524e9fd8750d20a88ecbcf9eeae7fb5aee7089`。起始GitHub main为`90792492877eb8217fb43b1414ba3682b0b5b842`。

## 实际实现与问题

R213只计算HTML祖先overflow裁剪，没有处理根`<svg>`本身的`overflow:hidden/clip`。当Path绘制超出SVG viewport时，R213仍将外溢部分报告为“可能可见墨迹”。本轮在**隔离恢复包**`v036_round214/svg_viewport_ink_envelope.mjs`新增根SVG视口裁剪上界：以SVG实际屏幕viewport矩形与R213屏幕保守墨迹上界求交，使用`getScreenCTM()`反投影；保留原始`inkBBox`。支持正向轴对齐缩放、嵌套HTML裁剪；完全裁剪返回null；非零SVG边框/内边距及不可靠几何失败关闭。

这只是**保守矩形上界**，不是逐像素精确墨迹，更不是参考图形态认证。未修改正式SVG、生产入口、旧编码或用户Storage。R214源代码、Chromium截图像素QA、静态QA、父SHA清单和审计随累计ZIP交付，不将ZIP误称为GitHub仓库内文件。

## 实测结果

真实Chromium `about:blank`：SVG隐藏溢出10000黑像素、`overflow:clip`10000、`overflow:visible`19600、`scale(.5)`隐藏2500、完全裁剪0、局部裁剪200、HTML+SVG双裁剪4200；非零边框和padding被拒绝。冻结151个旧SVG实例的三视图×编辑前后**906组原始inkBBox不变**。新增Chromium 40/40、静态18/18，实际重跑选定旧QA 203/203，总**261/261**；完整历史全量QA not-run。

R213父ZIP逐文件继承**2688/2688 SHA一致**；R214独立累计ZIP**2701文件**，SHA256 `d06b8400bece34bf9e6fb36ac1c88f7ff33df5e2ada15d2a04902d8de4a6c1da`。Python zipfile和系统unzip各自独立解压**2701/2701 SHA一致**，各自重跑**261/261 QA**，恢复后SHA变化0。打包与QA合并进程首次超时，随后在两份独立解压目录分别成功完成QA与SHA复核；超时本身不计通过。

本轮独立临时Chromium尝试127.0.0.1真实原点，返回`ERR_BLOCKED_BY_ADMINISTRATOR`；Web Locks/localStorage真实同源QA为blocked/not-run，未触碰用户原有存储。Android/iOS真机、真实读屏、同源高清原图原始字节/许可/逐笔审阅均not-run/未取得。R11/R12/R35原始ZIP及R12的20 SVG仍缺；R10仅有R164历史恢复证据。

## 正式验收边界

T00–T11仍**0/12 Accepted**；T01正式0/25键、T02正式永久ID0、T05真实缺根数未知。T03未生产集成；当前上界不能用于签发T06/T07的轮廓或位置认证。冻结V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`，2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`，未修改。下一轮优先M/K/E/B/J/R/X/V来源逐笔与合法同源高清原始字节，T03再处理精确墨迹及生产依赖。
