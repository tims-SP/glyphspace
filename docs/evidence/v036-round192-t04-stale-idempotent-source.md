# R192 · 原始 T04 · 幂等快路径来源新鲜度修复（隔离候选，非正式验收）

2026-10-28。**原始任务编号不变；T00–T11 0/12 Accepted。**

## 实际发现与修复

R189 核心在第一次 `sourceDigest()` 后异步执行 `buildPayload()`。如果旧版来源在此期间改变，而旧 shadow 恰好等于新 payload，原实现直接返回 `idempotent`，没有再次验证来源。这会把已经过期的来源误报为成功。R192 用实际 R189 ESM 与受控异步闸门复现旧缺陷，并新增独立 `scripts/r192_idempotent_freshness_core.mjs`，在幂等快路径重新计算来源摘要、读取来源原始字节、检查 shadow 与 journal 未并发改变；不改动原始 R189 核心。

测试覆盖来源在 buildPayload 期间改变、journal 插入、shadow 在第二次 digest 期间被修改、正常零写入幂等、首次过期拒绝、typed-slot null/空字符串恢复。**不是**原图认证、正式永久 ID、正式迁移或生产入口集成。localStorage 不具备原子 CAS，不能据此宣称竞态已完全消除。

## 可复验的本地记录

父 R191 ZIP SHA256：`d2d8b2b400daa5ba83011b9df007348927fa2a55c612af6fc69f616dc325453b`，2390/2390 文件逐项 SHA 一致。选定继承 QA 521/521，新增 Node 回归 36/36，新增 CI 等价烟测 13/13，新增静态冻结检查 18/18，合计 **588/588**。

R192 独立累计 ZIP：2402 文件，SHA256 `7e844d4126ed6b830088e9346f288509d317646d3d5eaa729cf91e0dfdb014c9`；Python zipfile 与系统 unzip 两次独立解压各 2402/2402 SHA，通过恢复后 588/588 QA，QA 后文件 SHA 零变化。ZIP 位于本次 ChatGPT 工作环境，不在 GitHub。

本地真实 Chromium 使用独立临时 127.0.0.1 原点，访问时 `ERR_BLOCKED_BY_ADMINISTRATOR`：**blocked/not-run**。R190 远端真实浏览器 CI 尚未独立核实；本轮新增 R192 Node CI 工作流的远端运行也尚未独立核实，均不计入通过数。完整历史全量 QA、真实屏幕阅读器、Android/iOS 真机、合法同源高清原图与逐笔审阅均未完成。

冻结 V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`、2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49` 已重新校验。176 旧编码、正式 SVG、生产入口及用户真实 localStorage 未修改。

R10 历史包已恢复，但 R11/R12/R35 原始 ZIP 与 R12 20SVG 仍缺失；不声称完整历史连续。T01 正式 0/25，T02 正式永久 ID 0，T05 真实缺根数未知。正式 T04 迁移未验收。

## 回滚

隔离 ZIP 只新增 `v036_round192/`；删除该目录即可恢复 R191，原核心不受影响。后续优先在授权真实同源浏览器验证 R192 幂等竞态，继续 T01/T02 原图与身份阻断。
