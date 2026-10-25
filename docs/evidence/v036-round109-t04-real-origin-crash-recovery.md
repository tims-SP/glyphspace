# V0.36 第109轮 · Root T04 GitHub真实隔离原点崩溃恢复（非正式验收）

- 日期：2026-10-25；原始任务T04为旧localStorage迁移。原始WBS和T00–T11编号未改，UI-01–05独立。
- **父ZIP实测**：R108 `51ee682e0df8ee4cde134b9a2b085be96959e6ed3435bd7c7e094bd02bfcbec5`，1459文件；R107→R108的1449/1449相同；R108→R109的1459/1459相同。R109 ZIP `d07f18b0d49bba080a896de22041a90077b8a22dbd4bd61a90c28fbe8f7ef3dc`，1468文件（不在GitHub）。Python zipfile和系统unzip独立恢复各1468/1468，QA后各1468/1468 SHA一致。
- **新代码**：`scripts/qa_v036_t04_disposable_origin.py` 在一次性loopback原点双标签内新增写pending后、写record后、发布head后三种崩溃恢复，pending状态拒绝并发提交/回滚，恢复后回滚验证。修改提交[053bb786](https://github.com/tims-SP/glyphspace/commit/053bb786cbb6088e4bd03e1c17ab7ca0e0da93cd)。
- **真实CI独立核验**：先行[run 40153502403](https://github.com/tims-SP/glyphspace/actions/runs/40153502403)在Ubuntu Chromium双标签真实Web Locks/localStorage通过11/11；新增[run 40156644345](https://github.com/tims-SP/glyphspace/actions/runs/40156644345)完整日志输出`T04 disposable origin 23 PASS; not production migration`，工作流/测试job均success。后者工件ID12584890814，GitHub元数据SHA256 `f8673646e124dbf9b17420696865cd977e8d75cb1d3b6355c30ff0a576f5ae18`；工件JSON未另行解压，23项来自日志。
- **本地QA**：新来源/状态边界16/16，继承R108 Node VM回滚10/10、R107静态26/26、R77 Node179/179、R105 Chromium about:blank170/170；Python和unzip两个恢复目录均分项重跑上述401项并在QA后逐文件SHA复验。R106完整浏览器回归和全历史全量QA仍not-run。
- **证据纠偏**：R108 ZIP内`v036_round108/R108_double_independent_recovery_QA.json`是1458文件、SHA `77803b1a49aaccf26a49d2a3c771f27003417ee2fcccd78659b27499ee94290e`的中间快照，不等于最终1459文件R108 ZIP；外部`第108轮_双独立恢复与新旧QA.json`才对应最终ZIP。R109保留旧证据字节并显式标记。
- **严格边界**：真实同源成功发生在GitHub Actions隔离原点，不是用户旧存储迁移；本地此前被管理员阻断，本轮未重测。T01 0/25、正式永久ID0、T03未正式集成、T04正式迁移not-run、T05未补图、T00–T11 **0/12 Accepted**。第10–12、35轮ZIP及第12轮20SVG、合法同源高清原图仍缺；Android/iOS真机及真实屏幕阅读器not-run。
- 冻结V0.35 HTML `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`、2008 JPEG `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`、176编码、正式SVG及用户localStorage未修改。
