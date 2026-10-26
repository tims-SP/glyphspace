# V0.36 第149轮 · Root T04：严格旧版来源真实同源预检（隔离，非验收）

## 任务与来源

Root **T04 存储与旧版迁移**（关联T00/T02/T03），与UI-01～UI-05无关。先读 `docs/STATUS.md`、`docs/history/V0.36-P0-original.md`、`docs/tasks/t00-t11.json`、`docs/11-traceability.md`、`docs/07-acceptance.md`、`AGENTS.md`；执行前 main SHA `2995b147a26b5291c3ff6f17ea836832d08823c0`。本地实际读取R148累计ZIP SHA `9b9c58ecd97cc1f68960ff4c70086148f197d1ec30704b9d4c8d0d6e490d35fa`，1875/1875逐文件SHA继承。

冻结V0.35 HTML SHA `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`；2008参考JPEG SHA `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`，两者原始字节未修改。GitHub新隔离文件 `scripts/v036_r148_strict_shadow.js` 与R148累计ZIP原件 **5944字节、SHA256 93095d5ef4ef85d8238b90b51f6fbc2e8968e6c5a51498e7503dccfe26b27fed 一致**；`scripts/qa_v036_t04_r149_strict_origin.py` 是新真实原点QA。

## 实际工作

扩展 `.github/workflows/v036-t04-disposable-origin.yml`：在授权GitHub Actions独立Chromium profile和随机127.0.0.1 HTTP原点，用两个真实标签页验证R148严格只读入口：WebCrypto SHA、Web Locks共享/独占锁竞争、localStorage及跨标签storage事件、G/K/X部分键模拟修改和22缺席键、重复JSON键（字面/转义/嵌套）拒绝、非法坐标/键长/来源SHA/默认值/原点拒绝、原始raw与无关sentinel保持。该测试不会连接用户生产origin、不会迁移用户资料或批准永久ID。

本地同样尝试独立Chromium真实原点，遭 `ERR_BLOCKED_BY_ADMINISTRATOR`，**blocked，不计通过**。本地重新运行R142–R148定向QA **1628/1628**（Python R142 233、R143 87、R144 676、R145 379、R146 201、Node R147 14、R148 Node 29、Chromium about:blank解析9）；R149本地前置冻结检查2通过，但浏览器同源0项运行。完整历史全量QA **not-run**。

授权远端测试运行： [GitHub Actions R149 real-origin QA](https://github.com/tims-SP/glyphspace/actions/runs/40384582893)。**必须以运行完成后的结果/产物为准；在完成前标记 pending，不计pass。**

## 累计恢复包

R149父包R148 **1875/1875**继承SHA一致；R149累计包 **1881文件**，SHA256 `a8f88dfbf54380e848c6610525d3272e9aeda69745f07247c707fe5635256259`。Python zipfile与系统unzip分别独立解压，两份各1881/1881文件SHA一致，实际重跑各1628/1628定向QA，QA后1881/1881 SHA一致。**不代表R10–12/R35历史连续性恢复**。

## 仍未验收

原始T00–T11 **0/12 Accepted**，T01正式认证 **0/25**，T02正式永久ID **0**，T03未生产集成，T04真实用户V0.35→V0.36迁移未完成，T05补图未完成，真实缺根数未知。第10–12轮、第35轮ZIP与第12轮20 SVG缺失；合法高清同源原图许可、逐笔认证、Android/iOS真机和真实屏幕阅读器QA均未完成。冻结入口、176旧编码、历史正式SVG、用户原有存储未改。
