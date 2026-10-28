# R190 · Root T04 · R189 异步来源 SHA 读回的真实浏览器验证基础设施

日期：2026-10-28。**隔离候选；非正式验收。**

## 真实资产与继承

R189父ZIP SHA256 `6daddf37eb4c8df9990ee750650d4e9b934f1cbe309d240538fa6a29b1d71946`；实际读取并验证2360/2360个成员的SHA256。R190累计ZIP包含2379个成员（2360父成员原样继承、19个新增成员），SHA256 `ee13e558617a268763fd6a5869532bf13ad851e6a6b15091b50fdb110babe1c0`。Python与系统unzip分别独立解压，均2379/2379 SHA一致；两套恢复后均执行选定旧新QA 474/474，通过后SHA不变。完整历史全量QA未运行。

## 本轮实际实现

新增 `scripts/r190_source_readback_browser.py` 及 `.github/workflows/r190-t04-source-readback-browser.yml`。测试使用全新临时Chromium profile、真实127.0.0.1双标签、Web Locks、localStorage、WebCrypto和**同一份**R189 ESM事务核心。在第三次来源SHA计算时用可控Promise暂挂，另一个标签修改合成来源，再恢复摘要，检查拒绝过期提交、影子回滚、日志清理、来源/无关键保护及跨context隔离。

**严格区分**：这个远端浏览器测试使用合成来源计划，并非R148/R152/R178/R179完整来源签发链；完整链的独立浏览器脚本已放入R190累计ZIP，但本地因管理员策略阻断，尚未运行。测试没有访问任何真实用户存储或正式生产入口。

## 实际测试与未运行边界

- R189选定旧新QA实跑456/456；R190新增静态及冻结合同18/18；合计474/474（**不包含浏览器测试**）。
- 本地真实Chromium导航到临时127.0.0.1返回 `net::ERR_BLOCKED_BY_ADMINISTRATOR`，本地浏览器0项通过。
- R190 GitHub Actions工作流已提交；**远端运行结果和原始artifact尚未独立核实，状态unverified，不计pass**。
- 冻结V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`、2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`复核一致；176旧编码、正式SVG、生产入口和用户存储未修改。
- R10原始ZIP已于R164恢复；R11、R12、R35原始ZIP及R12的20SVG仍缺；同源高清原图许可、逐笔认证、真机、真实读屏、完整历史QA均未完成。

## 正式状态

原始T00–T11 **0/12 Accepted**；T01来源正式认证0/25键、T02永久ID批准0、T03未生产集成、T04正式迁移未验收、T05正式补图未完成且缺根数量未知。UI-01至UI-05不冒充原始T03/T05。

下一轮首先独立核实R190 GitHub Actions真实浏览器CI与原始产物；成功后再推进R148/R152/R178/R179完整签发链真实同源测试及正式T04依赖。不得因静态QA或合成来源浏览器成功而修改accepted。
