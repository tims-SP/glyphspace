# R245F67 · Root T03 三视图 SVG 外层属性及视口完整性修复（隔离候选，非验收）

日期：2026-11-03。工作轨道：**Root T03 SVG坐标内核**，不是 UI-01～UI-05。

## 缺陷、修复及复现

实际读取 R245F66 隔离累计 ZIP（3777 成员，SHA256 `c5a2ce9d2a11f9c361077a28321c835e8a403b39bbf081a8d3b8ec4935c5d6a5`），逐成员 CRC/SHA 继承一致。R245F56 的隔离三视图候选只校验字形内层 markup 和少量来源属性，真实 Chromium 复现 **12/12 外层属性/视口篡改仍被错误提交**，包括 mini/focus/full 的 `viewBox`、`preserveAspectRatio`、`style`、`class`、`opacity`、`font-weight`、`data-source`。

R245F67 在隔离 HTML 中对每个字形的非事务属性和 25 键 SVG viewport 属性进行基线对照，只放行由预览器控制的 `transform` 和经规划身份绑定器复核的两个草案注释字段。同步光学校正及异步 Image 解码后提交均失败关闭。正常 100×100、painted inkBBox 候选、三视图同步与 151 旧可视/156 规划身份不变。

**真实新旧选定 QA：984/984**（新 Chromium 63、继承 F56 35、F50 348、F51 175、F52 217、T00 48、F65 98）。累计 ZIP **3788 文件**，SHA256 `25b8ee3a2d9c36ab1b113a7bc7ec4da680e8d90cf1a7387757196ca9b4ba8307`。Python zipfile 与系统 unzip 两套独立解压各 **3788/3788 SHA、984/984 选定 QA、QA 后 0 漂移**。完整历史全量 QA **not-run**。

## 验收边界

- 测试在本地真实 Chromium `about:blank` 和隔离目录进行，不接触用户 localStorage。真实同源 Web Locks/localStorage、真实屏幕阅读器、Android/iOS 真机：**not-run**。
- T01 来源正式认证 0/25；T02 批准永久 ID 0；T03 仍是隔离候选，正式 100×100/inkBBox/锚点内核尚未接入生产；T05 真正缺根数未知。原始 T00–T11 **0/12 Accepted**。
- R10 原始 ZIP 已恢复；R11/R12/R35 原始 ZIP 与 R12 的 20 SVG 仍缺；R246 主线累计包没有与 R245F 分支混合。
- 冻结 V0.35 HTML SHA `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`，2008 JPEG SHA `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`，176 旧编码、正式 SVG、生产入口和用户 Storage 均未修改。
- **实际候选 HTML、构建脚本、浏览器 QA 和累计 ZIP 在 R245F67 独立恢复包中**；此 GitHub 提交仅同步状态、技术证据与原始任务账本，不冒称代码已合并生产。

下一步先合法高清来源逐笔裁定 K:2/K:3 和 M 微形，再签发永久身份、将几何内核与正式资产集成。重复安全防护测试不能替代来源认证。
