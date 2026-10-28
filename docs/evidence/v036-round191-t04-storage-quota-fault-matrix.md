# R191 · Root T04 · Web Storage 写入异常回滚矩阵（隔离非验收）

日期：2026-10-28。工作轨道：原始 T04（不是 UI-03/UI-05）。

## 可复验资产

- 父 R190 ZIP：`ee13e558617a268763fd6a5869532bf13ad851e6a6b15091b50fdb110babe1c0`，2379成员；逐项读取CRC、SHA256，**2379/2379原字节继承**。
- R191累计ZIP：`d2d8b2b400daa5ba83011b9df007348927fa2a55c612af6fc69f616dc325453b`，2390成员，新增11项。
- 两次独立恢复：Python ZipFile与系统unzip各2390/2390 SHA，分别实际重跑521/521选定QA，QA后所有文件SHA不变。
- 新增Node私有Map同步异常注入：29/29；新增静态冻结门禁18/18；实际重跑R190选定旧QA474/474；合计521/521。具体源码、逐成员SHA审计、异常日志与QA JSON在R191累计ZIP的`v036_round191/`目录。
- 实际启动Chromium全新临时127.0.0.1来源签发双标签测试，导航被`net::ERR_BLOCKED_BY_ADMINISTRATOR`阻断；真实浏览器本轮**blocked/not-run**。R190远端CI结果仍未独立核实，不能计pass。

## 新的安全覆盖

针对真实R189事务核心，在独立Map注入同步Web Storage失败：journal首次写入失败、shadow写入失败、提交时journal删除失败、恢复时shadow写入失败、恢复时journal删除失败、二次恢复、损坏journal拒绝、来源过期拒绝、旧来源键禁止写入。覆盖事务前、中、后不同写入点的失败原子性与恢复能力。**这是模拟同步异常，并非真实浏览器QuotaExceededError/权限异常证据。**

## 验收边界

正式T00–T11仍**0/12 Accepted**，T01认证0/25键、T02永久ID批准0、T03未生产集成、T04正式迁移未验收、T05真实缺根数未知。R11/R12/R35原始ZIP及R12 20SVG仍缺；完整历史QA、原图许可及逐笔认证、Android/iOS真机与真实读屏均not-run。冻结V0.35 HTML SHA `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`、2008 JPEG SHA `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`复核一致；176旧编码、正式SVG、生产入口和用户原有localStorage未改。

下一轮应优先在独立授权真实同源profile运行完整R148/R152/R178/R179签发链、R189事务核心及配额异常测试；同时继续T01/T02的M/K/E/B/J/R/X/V来源身份复核。