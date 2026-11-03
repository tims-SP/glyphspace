# R245F72 · Root T03 隔离三视图事务桥接（非正式验收）

本轮从 R245F71 隔离累计 ZIP 的实际字节继承；**不是 main R246 根线的合并**，不改变生产入口。

## 实质实现

- 新增 `scripts/r245f72_t03_live_three_view_bridge.js`：将候选 `GlyphSpaceT03RegistryV2` 的 CAS 批量光学校正，先进行完整事务预演，再同步到真实 SVG 三视图，回读 raster paintedBBox 后提交不可变日志。
- 支持过期 revision、重复/未知身份、越界光学校正、外部预览修订漂移拒绝；第二个目标的 SVG setter 故障注入后逆序回滚第一个目标。
- 仅对 151 个旧可视候选实例生效，不能新增已认证资产，也不改正式 Path、ID 或用户 Storage。

## 实际验收

- R245F71 父 ZIP：3854/3854 成员 SHA256 逐一匹配；SHA256 `b05988d0a4f7102843957968815b257170c347895f0aae63a10607dce7ae8561`。
- R245F72 累计 ZIP：3869 成员（新增15）；SHA256 `a97e44a854c658166ab49e2d2295bcd67b9ae9ea6f00a3f4446fbd84aec0fcb9`。
- 本轮新增 Chromium about:blank 53/53；继承选定 F71 72、F70 56、F69 39、F68 22、F67 63、F65 98、F56 35、T00 无截图 48，合计新旧 **486/486**。
- Python 与系统 unzip 两套独立恢复，各 3869/3869 SHA、486/486 选定 QA，QA 后漂移 0。
- 冻结 V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc` 与 2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49` 均独立复核未变。
- 累计 ZIP 内含 `v036_r245f72/qa_f72.py`、实际 QA JSON、逐项审计、独立 HTML 与完整旧资产；完整历史全量 QA **not-run**。

## 正式验收边界

原始 T00–T11 **0/12 Accepted**；T01 0/25 键正式认证；T02 批准永久 ID 0；T03 正式内核未生产集成；T04 真实用户迁移未验收；T05 真实缺根数未知；T06–T11 未验收。

高清来源合法性/逐笔、真实同源 Web Locks/localStorage、本机真实读屏、Android/iOS 真机本轮 **not-run**；之前本地真实同源管理员策略阻断，不得计 pass。R11/R12/R35 原始 ZIP、R12 20SVG 仍缺失。R10 另有独立恢复记录，但不得据此声明连续历史全量。

后续优先 T01/T02 的 K:2/K:3 共享来源、M 四个未绑定微形、36 旧未匹配的逐笔和合法来源认证；本轮桥接不能替代正式资产认证。
