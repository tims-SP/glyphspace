# R189 · Root T04 异步来源SHA读回防护（非正式验收）

日期：2026-10-28。真实Node私有Map复现R187第三次旧来源SHA异步计算期间，外部修改来源后R187仍提交过期影子数据；R189在SHA完成后再次读取原始来源字节，发生变化则拒绝并沿既有回滚路径恢复旧影子，保留旧来源及其他存储。仅修复该类TOCTOU，不提供localStorage原子CAS，也不代表正式生产迁移安全。

父R188 ZIP 2342/2342逐文件SHA继承；新Node竞态14/14、R148/R152/R178/R179真实签发私有Map47/47、静态17/17、实际重跑选定旧378/378，合计456/456。R189累计2360文件ZIP SHA256 `6daddf37eb4c8df9990ee750650d4e9b934f1cbe309d240538fa6a29b1d71946`，Python zipfile及系统unzip两套独立恢复各2360/2360 SHA、456/456 QA，QA后SHA一致。

本地临时127.0.0.1 Chromium仍返回 `ERR_BLOCKED_BY_ADMINISTRATOR`，真实共享原点本轮blocked/not-run；远端真实同源not-run；完整历史全量QA、Android/iOS真机、真实读屏not-run。T00–T11 0/12 Accepted，T01 0/25正式认证，T02正式ID0，缺根数未知。R10已恢复，R11/R12/R35原始ZIP及R12 20SVG仍缺，高清来源许可未确认。冻结V0.35 HTML、2008 JPEG、176编码、正式SVG、生产入口和用户原有Storage未改。

下一步：独立授权真实同源profile验证R189完整来源签发及异步来源竞态，并继续M/K/E/B/J/R/X/V逐笔来源审阅。
