# R245F66 · 原始 T00 冻结基线独立重放（非正式 Accepted）

本轮从 R245F65 隔离累计 ZIP 真读父包 SHA256 `d4f866225fd1f1baa0f6a8db4d9c6ad00ea18ff17cfd6575f308681a13ee5eb7`，3761/3761 继承成员 SHA 一致；前代 R245F64 3750/3750 一致。GitHub main 在 2026-11-02 核对为 `03c29e0fcc4b968224b9fdf37bc6d45b54da6b97`，R246 为另一条累计历史，不混合。

## 可重放技术证据

冻结 V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`，2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`。独立 Node VM 重新提取三份冻结 JSON 与原字节一致；真实 Chromium about:blank 检查 25 键、156 旧槽（151 可视、5 关联）、176 训练编码及 100×100 SVG，四视口/DPR（1440×900@1、390×844@2、844×390@2、320×568@3）共五张实际截图。新增 T00 QA 52/52；继承选定 QA 279+66+98=443/443；旧 R106 冻结 176 字三模式 3143/3143 在父工作副本通过。

新 R245F66 累计 ZIP **3777 成员**，SHA256 `c5a2ce9d2a11f9c361077a28321c835e8a403b39bbf081a8d3b8ec4935c5d6a5`。Python zipfile 与系统 unzip 两套独立恢复各 3777/3777 SHA，旧 443+新 52=495/495 选定 QA，各自独立恢复 T00 七文件 7/7，QA 后成员漂移 0。R106 在 Python 恢复目录执行超时，不计通过；unzip 恢复目录未运行 R106；完整历史全量 QA not-run。新 ZIP 内有 `v036_r245f66/qa_t00_formal_baseline.py`、`restore_t00_frozen.py`、QA JSON、五张截图、父成员 SHA 清单及审计。

## 严格验收边界

**T00 仍 `accepted=false`，Root 0/12 Accepted**。仅有合成旧 localStorage 测试样本，没有真实用户旧存储快照；V0.36 正式候选及其完整基线回归尚未验收。此轮不是 T01 原图认证（0/25）、T02 永久 ID 签发（0）、T03 生产集成、T04 真实迁移或 T10/T11 真机、真实读屏、file:// 离线发布。file:// 本地导航受管理员阻断；未访问用户存储。T05 缺根数仍未知。R10 原始 ZIP 已嵌入恢复，R11/R12/R35 原始 ZIP 和 R12 20 SVG 缺失。冻结生产 HTML、正式 SVG、176 编码及用户 Storage 均未修改。
