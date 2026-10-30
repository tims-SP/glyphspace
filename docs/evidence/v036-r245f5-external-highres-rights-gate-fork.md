# R245F5 · 第三方高清候选原始字节与版权隔离（Root T01/T02，关联T05）

**状态：非认证、非生产、R245F4独立分叉。原始T00–T11全部 accepted=false。**

## 真实来源检索

读取 GitHub `main` 的 STATUS、原始规划、T00–T11 账本、追踪表、验收规范和 AGENTS.md。主线记录 R246，ZIP SHA `3f2c863af624bee7f9e2c96c3c0262fbb9af777924264612b49da2cc948da6fe`，但该 ZIP 的实际字节仍不可用，不冒充 R247 主线继承。

冻结 V0.35 HTML 中已存在一个外部高清图地址：`CNMan/UnicodeCJK-WuBi06/imgs/zgjwt_jt_2583x1363.jpg`。本轮通过 GitHub 连接器**实际读取该文件完整 base64 原始字节**，独立解码并计算 SHA256、解析 JPEG SOF0：

- 357376 字节；**2583×1363**；JPEG。
- SHA256：`ca0afcb4d3d2ee47d34bc78751b230917d0113ec58497135677265ecc449359b`。
- Git blob SHA1：`8c502456a824e67a318a4e33274959e848d8ce94`。
- 原文件：[CNMan 高清候选](https://github.com/CNMan/UnicodeCJK-WuBi06/blob/master/imgs/zgjwt_jt_2583x1363.jpg)。

与冻结2008用户参考JPEG（1536×1086，SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`）直接视觉比较，**两图不是同一图版的高低清版本**：候选是黑白重排键盘、独立补码区；冻结图是彩色键帽并含口诀/原版权声明。只能作为独立参考，**不得标记为“同源高清原件”**。

[来源仓库 ReadMe.md](https://github.com/CNMan/UnicodeCJK-WuBi06/blob/master/ReadMe.md) 的版权部分明确称所有权利归王码公司，并提示请勿商用。尚无图像再分发授权，因此**不将外部JPEG放入公开GitHub、累计ZIP或正式SVG资产**。

## 实际交付与QA

基于真实读取的 R245F4 ZIP：SHA256 `35e42f74ec7db39a96a96d5c7b0bb9fe3c8fba8a1227aeada19d21491c317b6b`，继承 **3083/3083** 逐文件SHA一致。

新增只读候选来源清单、原始字节SHA/尺寸/格式验证器、权利隔离门禁、负例QA、恢复说明和历史缺口审计。验证器绝不授予同源证明/许可/形态认证。候选原始字节由GitHub连接器读到，但当前容器网络受DNS策略限制，**没有将候选JPEG字节放入本地ZIP**，可选 `--fetch` 网络重验未运行。

- 继承选定QA真实重跑：**2105/2105**。
- 本轮新增只读来源验证QA：**20/20**。
- 累计选定QA：**2125/2125**，不是正式验收。
- 累计ZIP：**3090文件**，SHA256 `e9a08e0ac401db814bd8fafd0ae5127edf902c8dcc4e0cd7db9cde95680faca0`。
- Python / 系统 unzip 两套独立恢复：各 **3090/3090 SHA**，各 **2125/2125 QA**，QA后0文件漂移。
- 完整历史全量、真实读屏、真机、正式同源高清逐笔认证：**not-run**。

R11/R12/R35历史ZIP及R12 20 SVG仍缺失；R10已于R164恢复。冻结V0.35 HTML、2008 JPEG、176编码、正式SVG、生产入口及用户原有Storage均未改动。

**正式状态：T01 0/25键认证；T02 0批准ID；T05真实缺根数未知；Root T00–T11 0/12 Accepted。**

下一步应向权利方取得同源高清原件与使用许可，或寻找确有可追溯许可的等价素材；不能用本轮候选替代正式字根来源。
