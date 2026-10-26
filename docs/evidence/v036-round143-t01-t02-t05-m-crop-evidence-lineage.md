# 第143轮 · Root T01/T02/T05 · M键裁框版本谱系（隔离、非验收）

## 证据与独立验证

- 原始2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`；冻结V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`。
- 实际读取R142父ZIP SHA256 `7c7cf8f7d1036f32fe7e6a89f4d65455a38db4c30ac3d2bbd08b8f0d3876be37`，1821/1821逐项SHA一致；R143累计1830文件，ZIP SHA256 `5b50c4141fdcebbbf42dda3c3e140426788f9cbcdd16f4449522d26ea55e833b`。
- 原生JPEG中M键8个观察ROI逐项重算SHA：4条仅为旧槽M:0–3的完全同框别名，另4条为无正式身份、无SVG、不可渲染的影子观察；不是确认4个新字根。
- M-vis-02旧框 `[1045,585,21,23]` 与R86证据候选框 `[1045,585,26,23]` 不同，新增5×23=115原生像素；旧框RGB SHA `844c267274b9ba14f5be5cc3e417171fd53a9181b653321e7d57be4fef949abf`，候选SHA `117d1e81fa8d57ef297491a17d1d19db3805a6db7c82a341060c374d5a4311d0`。**R86未批准变更**，旧M:1的别名仅对旧框有效。
- M-vis-04左侧两个像素 `(1016,632)`、`(1016,633)` 归属仍未定；不自动扩大或归属字根。
- 新Python QA 87/87；继承定向R142 233、R141 237、R140 25、R81 400、R86 20、R87 Node 38，共953/953。Python zipfile和系统unzip两次独立解压各1830/1830 SHA、1040/1040 QA，QA后1830/1830 SHA一致。完整历史全量QA `not-run`。
- 本轮隔离代码、原生审计JSON、原始父文件SHA清单、双恢复日志及可复现脚本仅位于累计ZIP；GitHub仅存储文字证据，不将低清来源图像作为公开正式字形。

## 阻断与回滚

- T01 0/25正式认证、T02正式永久ID0、T05正式补图未完成，原始T00–T11仍0/12 Accepted；缺根数为未知而非0。
- 缺R10–12/R35历史原始ZIP及R12的20SVG；未获得合法同源高清原图字节与分发许可。真实同源Web Locks/localStorage `blocked/not-run`，Android/iOS真机、真实屏幕阅读器 `not-run`。
- 冻结生产入口、176条旧编码、正式SVG、用户原有存储未触碰；回滚只需丢弃R143隔离新增目录与本证据，R142 ZIP仍独立可恢复。
