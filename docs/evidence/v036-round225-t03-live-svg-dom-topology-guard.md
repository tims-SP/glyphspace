# R225 · Root T03 · 隔离三视图SVG DOM拓扑与属性漂移守卫（未验收）

2026-10-30。原始任务为T03 SVG坐标内核，不是UI-track。父档案R224 ZIP SHA256 `a325e9beed8ea8e678f4057589168e8ece0596134845ff0f60201328ac353e72`；实际读取2821/2821父文件且SHA256逐文件一致。新累计ZIP 2834文件，SHA256 `07ac163dd8dedb93b2c8520b5fbdd98642f7beb97c1ed203c895f5b195a63f72`，Python zipfile及系统unzip两次独立恢复各2834/2834 SHA，恢复后各8169/8169选定断言通过、QA后0文件变化。

## 可重现的真实缺陷与修复

真实Chromium `about:blank`中，R224 `inspect()` 与 `apply([])` 错误接受五种DOM漂移：向已有SVG插入伪造`<g>`；对已有`<g>`添加`opacity=0`；SVG增加`transform:scale(.1)`；section增加`opacity:0`；重排现有SVG组。R225新隔离模块 `v036_round225/live_svg_optical_transaction.mjs` 对SVG子组身份/顺序、section的SVG身份/顺序、section/SVG属性及group非transform属性做冻结快照；在异步`issuer.propose`完成后、开始写transform前再次执行DOM稳定性验证。五种旧错误接受均被新实现拒绝，R224旧模块保留未改。

原R224 Chromium回归在R225新模块上重新运行3718/3718断言，覆盖75个SVG、453组、459路径、M/V两实例6组变换、第三视图写入失败回滚、路径篡改及非法墨迹越界。R225五组对抗回归17/17。额外实跑R223来源QA668/668、R223静态17/17、R224原Chromium3718/3718、R224静态14/14、R225 Chromium3718/3718、R225静态17/17，合计8169/8169。递归R224全选定5433套件曾尝试但超时，未计通过；完整历史全量QA未运行。

## 可复验文件

累计ZIP内 `v036_round225/` 包含新模块、`qa_dom_topology_adversarial.py`、`qa_live_chromium_r225.py`、`qa_static.py`、`run_r225_qa.py`、`R225_execution_report.md`、`R225_parent_2821_member_SHA256.json`、`R225_new_old_QA.json`、对抗QA及静态QA结果。独立ZIP外提供`R225_archive_member_SHA256.json`与`R225_double_independent_restore_QA.json`。

## 严格验收边界

这是隔离`about:blank`真实DOM验证，WebCrypto摘要通过Python桥接；并非真实安全同源Web Locks/localStorage，也未覆盖外部样式表或所有恶意monkeypatch。真实同源本地浏览器此前遭管理员策略阻断，本轮未重跑；真机、真实屏幕阅读器、完整历史全量QA均not-run。V0.35 HTML SHA `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc` 与2008 JPEG SHA `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49` 保持不变；176旧编码、正式SVG、生产入口及用户存储均未触碰。T01来源正式0/25、T02批准永久ID0、T05真实缺根未知，T03未生产集成；**T00–T11仍0/12 Accepted**。R11/R12/R35原始ZIP及R12 20SVG缺失，许可明确的同源高清原始字节及逐笔审阅未取得。
