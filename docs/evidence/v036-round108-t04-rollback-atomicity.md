# V0.36 第108轮 · Root T04 隔离回滚原子性修复（非正式验收）

- 日期：2026-10-25。父R107累计ZIP **1449文件**，SHA256 `3b5c30e922a9f58de189aa817f9369e768e4fed81dc9fedbe34b93a8ad43df5b`，本轮逐文件SHA继承 **1449/1449**。
- 发现真实代码缺陷：R107隔离事务`rollback()`先把`head`指向前驱，再调用`read()`；若前驱记录缺失或被篡改，函数虽抛错，却已经破坏最后一个可读修订的指针。
- R108隔离脚本先核验前驱记录存在、内容SHA256与schema，再写`head`；针对缺失和损坏前驱的四个拒绝/不变断言，以及修复后的成功回滚，共新增5项浏览器脚本断言。旧实现缺陷与新实现修复由Node VM合成存储/锁 **10/10** 复验，**不能冒充真实同源**。
- 继承R107静态26/26、R77 Node 179/179、R105 Chromium about:blank 170/170；R106完整176编码浏览器回归本轮尝试超时，不计pass。R108真实临时loopback Chromium再次返回`ERR_BLOCKED_BY_ADMINISTRATOR`，Web Locks/localStorage **blocked/not-run**。
- 新累计ZIP **1459文件**，SHA256 `51ee682e0df8ee4cde134b9a2b085be96959e6ed3435bd7c7e094bd02bfcbec5`；Python zipfile与系统unzip独立解压各 **1459/1459**，各自重跑上述4组定向QA、QA后1459/1459逐文件SHA一致。ZIP不在GitHub，不能把本页当作ZIP下载链接。
- GitHub新增[独立真实原点回滚回归脚本](../../scripts/qa_v036_t04_disposable_origin.py)，并修改[专用工作流](../../.github/workflows/v036-t04-disposable-origin.yml)执行并上传JSON；远端运行结果**待独立确认**，不得记为pass。GitHub CI脚本是隔离回归，不是V0.35用户存储迁移。
- 冻结V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc` 与2008参考JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`不变；176编码、正式SVG、生产入口及用户存储未动。
- T01 0/25键、T02正式永久ID0、T03生产未集成、T04真实迁移未验收、T05未补图；T00–T11 **0/12 Accepted**。第10–12、35轮ZIP及第12轮20SVG仍缺；同源高清原图/许可未取得，真机/读屏not-run。
