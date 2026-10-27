# R178 · Root T04：旧v16来源快照过期门禁（隔离，非验收）

**日期：2026-10-28。原始任务：T04 存储与旧版迁移。正式状态：0/12 Accepted。**

R152 `verifyPlan` 只验证WeakMap曾签发的只读计划，不会在签发后重新读取v16存储。本轮真实Node22/FakeStore复现：更改K:2旧坐标后，旧签发验证仍为true；这不表示旧代码的只读计划本身发生了生产写入，但若被错误当作未来提交前门禁，会允许过期来源。

新增隔离模块 `v036_round178/source_freshness_gate.js`：模块加载时捕获R152签发器，不接受调用方伪造issuer；在受限独立loopback原点与协作Web Lock内再次验证签发，读取v16原始字节，计算SHA256，与计划sourceSHA核对，并在异步摘要前后比对原始字节。拒绝签发后变更、摘要期间变更、克隆计划、假issuer、缺失存储、非法原点及未执行回调的锁。**仅观察时刻有效，无commit/apply、不写用户数据、不批准永久ID，不保证返回后仍然新鲜。**

- 父ZIP R177：2189/2189逐文件SHA继承；SHA256 `b44a6720aeb7b27d4303affb4aa681cd93fbaf7030aad17534468da9eb82ecab`。
- R178累计ZIP：**2201文件**，SHA256 `4cb47c565f2fa6f3e1763cf1abf8ff8dcce6b2c51313dc5a5fb9cfc61fb5044e`。
- 新增Node QA **22/22**；实际重跑R177选定旧QA **1075/1075**，共**1097/1097**。
- Python zipfile与系统unzip双独立恢复各**2201/2201 SHA**、各**1097/1097 QA**，QA后全部SHA不变。
- 独立Chromium临时loopback原点返回 `net::ERR_BLOCKED_BY_ADMINISTRATOR`；真实共享原点**blocked/not-run**，未计入pass。
- 完整历史全量QA、Android/iOS真机、真实读屏均**not-run**；正式生产迁移**not-run**。
- 冻结V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc` 与2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49` 重新核对一致；176旧编码、正式SVG、生产入口及用户原有存储未修改。
- R10原始ZIP嵌套存在且SHA一致；R11/R12/R35原始ZIP及R12 20SVG仍缺。T01 0/25正式认证、T02正式ID 0、缺根数未知，T03尚未生产集成，T04仍未验收。

**结论：** T04新增了真实可复现的过期计划拒绝机制，但它只是隔离只读门禁；不能冒充真实同源迁移或T04 Accepted。下一步须在独立授权profile执行真实双标签Web Locks/localStorage测试，待T01/T02身份批准后再实现可回滚生产迁移。
