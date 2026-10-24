# R95 · K键物理来源位置与旧槽身份隔离（2026-10-24）
> 原始任务：**T01参考图清点 / T02语义与独立身份前置**；关联T05。**隔离证据，不是字根认证或正式验收**。

## 实际来源与发现
- 父ZIP：第94轮隔离累计恢复包，SHA256 `2dcbc8880ab8adde82a8693c5c05f163d81c1476763a10d57d925d4a296df4fc`；真实读取并核对 **1319/1319** 父成员SHA。
- 2008 JPEG 原始字节SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`；R46阻断账本、R88原生ROI、R89 K:4差异交叉校验。Pillow与OpenCV独立解码的4个物理ROI原生RGB SHA一致。
- **4个来源物理位置（非4个正式字根）**：左上 `[1066,403,23,26]`，右上圈内 `[1121,399,29,25]`，左下 `[1066,461,21,24]`，右下 `[1127,462,24,22]`。圈内的语义类别仍不明。
- 冻结旧槽共5项：K:0只可作为左上历史框审阅；K:1是关联项；K:2「川」与K:3「丨」历史共享左下同一裁框，**两者阻断不解除**。**K:3目前没有独立来源ROI**，不得从K:2复制来源来制造第二个身份。K:4冻结「〢」Path与右下可见形态存在待逐笔复核的语义/轮廓差异，不能自动替换或改名。
- 新增隔离Python来源身份仲裁模块：仅允许K:0/K:2/K:4原位置的`review_only`审阅笔记，拒绝K:3借框、圈注重绑、伪造sourceCertified、licenseVerified、永久ID、错位或修改历史账本。没有分配referenceShapeId、assetId、永久instanceId或正式SVG。

## 可复验QA与恢复
- 新增**36/36**原生来源及负例QA；继承R81/R86/R87/R88/R89/R90/R91/R92/R93/R94十组定向旧QA，共**11/11组**通过。浏览器旧QA是Chromium `about:blank`真实SVG DOM，不是完整同源/真机QA。
- 新累计ZIP **1331文件**，SHA256 **`7deea5a9de203a1cefee6f52ca988f7d26c5588b6b0316a68fab42c2b1dd6db0`**；Python zipfile与系统unzip分别独立解压，两个环境均复跑11组新旧QA、QA后**1331/1331 SHA一致**。ZIP原始字节仅在外部交付，不在GitHub。
- 初次打包遗漏父包中的10个历史`.pyc`文件，被继承文件数门禁拒绝；最终重打包已保留父包全部1319成员。双恢复合并脚本曾超时，第二环境随后独立运行QA及逐文件SHA复验成功。不得将超时算通过。
- 独立临时Chromium profile + 127.0.0.1原点探针返回 `ERR_BLOCKED_BY_ADMINISTRATOR`；真实Web Locks/localStorage事务**blocked/not-run**。Android/iOS实体设备及真实读屏**not-run**。
- 检索已挂载文件、第94轮父ZIP、GitHub main递归树（72项）及公开releases（空）：第10–12/35轮ZIP及第12轮20 SVG仍未找到；GitHub Actions历史artifact未穷尽。合法同源高清原始字节/许可未取得。

## 冻结与正式状态
V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`、176旧编码、正式SVG和用户真实存储**未改动**。T01 **0/25**、真实缺根数未知、T02正式永久ID **0**、原始T00–T11 **0/12 Accepted**。本轮的4个物理位置、审阅代码、36项QA均不能升级任何正式状态。

回滚：删除外部R95隔离累计包/审阅输出即可，GitHub仅新增本证据与状态文档，不触碰正式发布入口。
