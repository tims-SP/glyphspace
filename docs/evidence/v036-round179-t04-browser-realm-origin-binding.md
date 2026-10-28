# R179 · Root T04：浏览器执行原点绑定的只读来源证明（隔离，非验收）

**日期：2026-10-28；正式T00–T11：0/12 Accepted。**

R178 的只读来源过期门禁允许调用方注入 `origin`、`expectedOrigin`、`store`、`cryptoAPI` 和 `lockManager`。本轮在 Node22 VM 的非 loopback 模拟执行原点中，实际复现：传入伪造的 `http://127.0.0.1:17901` 及 FakeStore 后，R152 签发和 R178 验证均返回成功，`checkedOrigin` 却不是实际模拟执行原点。这是**证明来源的信任边界缺口**，不代表已发生生产数据写入。

新增隔离 `v036_round179/browser_realm_source_attestation.js`（源码SHA256 `7c97985ebf84b4dc4dd23702b2fb1397e477c3c91fc3341d92f4b9f7127fb64e`）。在读取任何 localStorage 前检查当前 `globalThis.location.origin` 和安全上下文，仅允许明确端口的 `http://127.0.0.1`；直接使用执行 realm 的 `localStorage`、`navigator.locks`、`crypto`，并将真实 Storage 缩减为只允许旧 v16 单键 `getItem` 的只读 facade。新入口不接受调用方注入原点、存储、锁或加密实现；无 `commit/apply`，不分配正式ID。

- 父R178累计ZIP：**2201/2201 SHA**继承；SHA256 `4cb47c565f2fa6f3e1763cf1abf8ff8dcce6b2c51313dc5a5fb9cfc61fb5044e`。
- R179累计ZIP：**2213文件**；SHA256 `87fddbac1512ab8f4b87f4f6fd59291ef88ad5a7c1aac13feaaebb5100be350f`。
- 新增Node22 VM 35/35，真实Chromium独立临时profile的 `about:blank` 非安全原点拒绝1/1；实际重跑R178选定旧QA 1097/1097；合计 **1133/1133**。
- Python zipfile及系统unzip独立恢复，各 **2213/2213 SHA**、**1133/1133 QA**，QA后逐文件SHA不变。
- 临时127.0.0.1浏览器页面实际返回 `net::ERR_BLOCKED_BY_ADMINISTRATOR`，**真实共享原点Web Locks/localStorage blocked/not-run**。Node VM不能冒充真实浏览器多标签验证；about:blank拒绝也不是同源迁移测试。
- 完整历史全量QA、Android/iOS真机、真实读屏、正式生产迁移和回滚均**not-run**。冻结V0.35 HTML、2008 JPEG、176旧编码、正式SVG、生产入口及用户原有存储未改。
- 第10轮原始ZIP已恢复；仍缺R11/R12/R35原始ZIP及R12 20 SVG。T01正式认证0/25、T02正式永久ID0、缺根数量未知，高清许可和逐笔审阅未完成。

**结论：** R179缩小了隔离只读预检的原点伪造面，但同realm恶意脚本仍不属于可信执行环境；不能把它当作正式迁移、安全提交证明或T04 Accepted。下一步需在独立授权真实loopback profile完成跨标签测试，并等待T01/T02正式身份批准后设计可回滚迁移。
