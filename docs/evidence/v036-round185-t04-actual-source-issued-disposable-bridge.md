# R185 · Root T04：真实来源签发到共享事务核心的隔离适配器（非正式验收）

2026-10-28。先读取main六份规范与R184累计ZIP原始字节，SHA256 `1404f851ae798a32c5e5698448755c4ddc838421c4920fee85b11f13b3ad23fa`，逐文件继承 **2271/2271 SHA**。

本轮在独立累计档案 `v036_round185/` 实现 `realm_issued_disposable_bridge.mjs`，将**原样继承**的R148真实v16严格读取、R152同realm WeakMap签发、R178来源SHA新鲜度、R179真实浏览器原点绑定和R183共享ESM事务核心连接。执行原点必须是127.0.0.1安全上下文，触碰Storage前先拒绝非法原点；只读旧v16来源，写入只允许两个`__glyphspace_disposable_`影子/日志键，Web Locks独占包裹事务，签发与来源SHA在锁内复核。输出只有旧槽别名和显式编辑，不分配永久ID，不提供正式迁移入口。

Node私有Map使用冻结V0.35的156项ROOT_COORDS与上述五个真实历史模块，新增**40/40**；包括真实签发、克隆计划拒绝、原点拒绝先于Storage、来源过期、不同revision的实际故障回滚、崩溃恢复、损坏日志拒绝、旧来源保护。来源/脚本静态**21/21**，选定旧QA **215/215**，合计本地 **276/276**。R184父2271项全部SHA继承，R185累计 **2289** 文件，ZIP SHA256 `18450dde7b141cb58888f1f2608c76cd0d3dcd71ce97e32aa088a09872fb8b38`；Python zipfile与系统unzip两套独立恢复均2289/2289 SHA、276/276 QA且QA后SHA不变。

已编写真实Chromium双标签脚本，覆盖R148/R152/R178/R179/R183**同一份模块**的签发、Web Locks争用、localStorage隔离、故障和跨文档恢复；本地实际启动后导航返回 `net::ERR_BLOCKED_BY_ADMINISTRATOR`，因此真实浏览器为 **blocked/not-run**，远端CI亦 **not-run**，不得计为通过。完整历史全量QA仍not-run。

正式原始T00–T11保持 **0/12 Accepted**；T01 **0/25** 正式来源认证、T02正式永久ID **0**、真实缺根数unknown。R11/R12/R35原始ZIP和R12 20SVG仍缺，高清图第三方许可、逐笔、正式T03集成、正式T04迁移、Android/iOS真机和真实读屏仍未完成。冻结V0.35 HTML、2008 JPEG、176旧编码、正式SVG、生产入口与用户原有Storage均未修改。

累计档案与独立复验报告保存在本轮会话交付文件；移除隔离`v036_round185/`即可回退R184。GitHub此证据文档记录本轮本地真实QA，不将未执行的浏览器CI冒充成功。
