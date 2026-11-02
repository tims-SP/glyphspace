# R245F54 · Root T04 真实独立浏览器同源事务证据（非正式验收）

日期：2026-11-02。轨道：Root T04（存储与旧版迁移），不是UI-01–UI-05。**正式T00–T11仍0/12 Accepted**。

## 原始证据与测试

- GitHub main 六份基准文档先行核对；R245F53父累计ZIP SHA256 `ea7bbc4827073952068c26ca7a9f34e9dba74b0eb75830bc9e774f8049587bb0`，**3586/3586**继承成员逐SHA一致；冻结V0.35 HTML和2008 JPEG哈希匹配。
- 本地容器独立127.0.0.1 Chromium测试遭管理员策略`net::ERR_BLOCKED_BY_ADMINISTRATOR`：**blocked，不计通过**。
- 授权VPS独立临时profile + Chromium 141 + Playwright 1.56.1 + 随机127.0.0.1端口：真实两标签、真实Web Locks、StorageEvent、localStorage。25键/156旧槽均采用**合成编辑数据**；跨标签锁排队、提交、幂等、崩溃日志、跨标签恢复、非合作写入冲突拒绝、来源过期拒绝、无关键保留、profile销毁等 **33/33通过**，再次新profile重跑亦33/33通过。
- 实际执行脚本：[r245f54_real_origin_156slots.js](../../scripts/r245f54_real_origin_156slots.js) SHA256 `cd58ba8d609297e20640c2cbd911242e3bc339696130cb46e040a12adc8ba87e`；[原始QA JSON](./v036-r245f54-T04-real-origin-QA.json) SHA256 `ac7165fc35a255a2187020069dbe58323097d5aef83b732ce39e8b116c4521cc`。合成来源SHA `fa890b6dbdbc4530ac8cf6b1f7b00b08985dad44cdc931b31f7a78406d9fd402`。
- 实际R194模块7/7 SHA与R245F53父ZIP中相应源码逐字节一致。此项验证了真实浏览器语义，而非Node模拟锁。
- R245F50–F53选定旧Chromium QA实际复跑：348+175+217+20=**760/760**；完整历史全量QA **not-run**。
- R245F54累计ZIP SHA256 `97013f27a78bab79492bcf30474663460ff994bc8d7d2da67eebab3dc530dd9f`，**3597文件**（3586继承+11新增）；Python zipfile与系统unzip两套独立恢复各**3597/3597 SHA、3586/3586父SHA、760/760选定QA、0漂移**。真实同源33项在授权VPS独立profile执行，**未在本地双恢复重跑**（管理员策略阻断），不能把760+33说成两套恢复各793。

## 不能据此批准的内容

这不是用户真实旧数据迁移，不会对真实用户Storage写入。测试仅在新临时profile写入合成旧键；真实生产迁移、正式稳定ID绑定、回滚发布均未执行。T04 **accepted=false**。T01 0/25、T02批准永久ID0、T05缺根未知；正式T03 inkBBox仍未集成。第11/12/35轮历史ZIP、第12轮20SVG和R246主线累计ZIP缺失；高清来源许可与逐笔认证、真实读屏、Android/iOS真机未完成。冻结V0.35 HTML、2008 JPEG、176编码、正式SVG、生产入口保持不动。

## 后续

T01/T02完成合法同源逐笔和正式ID签发后，T03正式集成；再以隔离授权profile执行T04真实旧数据迁移、回滚、并发和错误隔离正式验收。此次33项可作为T04浏览器底层事务证据，**不能替代正式T04验收**。
