# R238 · Root T04：156槽双实例并发与非协作写入冲突（隔离非验收）

2026-10-30。起始GitHub main：`de6754a59e36524bcc8d78bac1769c12025d8807`。实际读取R237父ZIP SHA256 `68f84281940ed43892b71408e95ab3259268f5efdaa13e7f3db42366072a7d6a`，2976/2976成员逐SHA继承。

本轮以实际R148/R152/R178/R179签发+R192事务核心、25键156旧槽的**私有Node Map**验证两个独立桥接实例并发stage：一次disposable_staged、一次idempotent；crash-after-journal后的其他实例被拒绝；非协作写入shadow后恢复拒绝并保留冲突字节及journal；恢复合法前值后可回滚；伪造journal拒绝；旧来源跨实例变化拒绝。新增17/17，继承R237选定835/835，总计852/852。不是实际用户迁移或真实Web Locks。

R238累计ZIP **2984文件**，SHA256 `28ea55adeb80a8309bb9d66ee077a4d559f9b7f8c54cfa76d0eb1698bf506580`；Python zipfile和系统unzip两次独立恢复各2984/2984 SHA及852/852选定QA、QA后0文件变化。父ZIP逐文件继承2976/2976。

本地系统Chromium144真实loopback仍`ERR_BLOCKED_BY_ADMINISTRATOR`；R238真实浏览器并发脚本已准备但**not-run**，R237远端24/24不能冒充R238结果。完整历史全量QA、真机、读屏、高清原图逐笔、真实用户迁移not-run。T01正式认证0/25、T02批准ID0、T05缺根数未知、原始T00–T11 **0/12 Accepted**；R11/R12/R35原始ZIP及R12 20SVG缺失。冻结V0.35 HTML、2008 JPEG、176编码、正式SVG和用户Storage未动。

R238代码、QA与成员SHA清单随独立累计ZIP交付，尚未将R238测试脚本提交为GitHub Actions工作流。此项不构成T04验收。
