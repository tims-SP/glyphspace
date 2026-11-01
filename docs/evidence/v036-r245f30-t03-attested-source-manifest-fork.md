# R245F30 · 原始 T03：冻结来源/矢量清单内容钉值（隔离预集成，非正式验收）

2026-11-01。继承R245F29父ZIP原始字节SHA256 `c0fd1ec988c49828f141fa00ece673a19f1a7c4bc039d0cd983c54f585e23622`，父3349/3349逐成员SHA与父清单一致；新累计3357成员ZIP SHA256 `6a727d8e14df67aebe6ed3f7e6b94c4a33448918ffbe1d3dde7d3dfb1113debf`。Python zipfile和系统unzip分别解压至空目录，各3357/3357 SHA一致；每套继承R245F24–F29选定QA 268/268、新R245F30 16/16，合计284/284，QA后0文件漂移。另有旧缺陷复现2/2，**不计入通过**。完整历史全量QA not-run。

## 发现并修复的真实缺陷

R245F29 `auditT03DraftCatalogIntegrity` 仅核对 `catalog.byId[].paths` 与传入的 `source.rows[].paths` 相等，以及两边 `sourcePathSHA256` 标签相等；**没有验证传入source本身是否是冻结R50的原始内容**。实际把M:0的Path d同时修改到catalog和source而保留原SHA标签，旧审计和旧补丁包装器均错误接受。新门禁先计算R50与R54解析后JSON规范化内容SHA256并对照钉值：

- R50 JSON文件原始SHA256：`1d03c98a3dbd7074305e50cbb604447865ef2f9cde7786261aa9252b49860089`；规范化内容SHA256：`c4fdd25a08a0670787b40c8cbe705516a4986c975fd377cfde5e99d7402f1ff1`。
- R54 JSON文件原始SHA256：`65f3835499e64211e0f787cce7c2e33d18bea11c3d75204ee9e0f1eedf097f48`；规范化内容SHA256：`e55e5252367ea88b7662dd3d6eac9f043d073a4a604cd6ab22315550eb4f6a07`。

对来源/矢量内容、Path、行顺序、来源SHA标签的协同篡改均失败关闭；保留151旧实例、25键、100×100/inkBBox/锚点/光学补偿的既有核验。旧补丁包装器的动态 `await import` 改为静态导入，减少预检与补丁间的异步窗口。Node-only隔离模块，不直接作为正式浏览器生产代码。

## 验收边界

R246主线提交仍为`03c29e0`，其3054成员累计ZIP原始字节未恢复；R245F30是R245F29隔离分叉，不得冒充R246连续主线。R10历史ZIP此前恢复，R11/R12/R35原ZIP与R12的20SVG仍缺。T01正式25键来源认证0/25、T02批准永久ID0、T05确认缺根数未知、T03未生产集成，原始T00–T11全部 `accepted=false`。合法同源高清逐笔、真实同源用户迁移、真实屏幕阅读器、Android/iOS真机、完整历史QA均未验收。继承浏览器QA仅`about:blank`。冻结V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`、2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`、176编码、正式SVG及用户Storage均未修改。

完整代码、两份独立解压QA、父ZIP逐文件SHA清单、执行报告及审计随隔离累计ZIP `v036_r245f30/` 保存；公开GitHub仅存文字证据与状态，不发布75MB二进制。
