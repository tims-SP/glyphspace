# R245F21 · Root T01/T02：E/K中立来源工作台异步竞态修复（隔离分叉，非认证）

**来源：** 实际读取R245F20累计ZIP，SHA256 `61d59cb708d845bcdb1cbbe3059e0832905e730765015613b43d9f211855f765`，3245/3245文件逐SHA继承一致。GitHub `main`仍为R246 `03c29e0fcc4b968224b9fdf37bc6d45b54da6b97`；R246 3054文件累计ZIP原始字节未取得，因此本轮只延续R245F20独立分叉，不宣称连续R247。

## 实际发现和修复

Chromium `about:blank`中对真实冻结2008 JPEG执行文件选择和SHA256验证，独立复现R245F20两项缺陷：

1. `File.text()`读取中立描记JSON时暂停；同一JPEG重新验证后恢复旧读取，旧版错误提交已经过期的草案。
2. 较早选择的有效JPEG在`File.arrayBuffer()`读取中暂停；随后选择无效JPEG且被拒绝；旧有效读取恢复后，旧版错误将`verified`恢复为true，覆盖最新文件选择。

R245F21在**文件选择时**预留source epoch，异步读取和解码完成前检查epoch；JSON导入同时检查来源epoch和最新导入请求序号；过期导入不得修改现有草案或新来源状态。错误来源禁用编辑和导出，合法旧未批准草案保留。只修改隔离E/K来源工作台，未触碰生产HTML、用户localStorage、176旧编码、正式SVG或2008参考JPEG。仓库提供可重现的`scripts/r245f21_source_epoch_patch.py`；实际完整候选、旧版复现脚本和浏览器QA随隔离累计ZIP交付。

## 真实QA、恢复和边界

- 旧版两项缺陷复现2/2（**缺陷证据，不计通过QA**）。
- 新Chromium 22/22；旧工作台57项在新候选上回归57/57；继承定向567/567；**选定646/646**。原生JPEG RGB裁框另计170/170。
- 新累计ZIP **3260成员**，SHA256 `6b08205f565e2bd6552554c9292f5dc645cda06b8e4d9adc468f72146c2bc971`；Python zipfile和系统unzip分别独立恢复3260/3260 SHA，分别重跑646/646选定QA与170/170 RGB，QA后0漂移。完整历史全量QA **not-run**。组合测试最初因浏览器测试顺序出现超时，不计通过；调整为新回归优先后两套独立恢复均通过。
- E/K仍为4组物理裁框、9条竞争来源观察，E:1/E:8历史否定保留，K来源身份未裁决。**不是新增4/9个正式字根**，未批准任何Path或永久ID。
- T01正式0/25键、T02批准永久ID0、T05真实缺根数未知、原始T00–T11仍0/12 Accepted。合法同源高清许可/逐笔认证、真实同源生产迁移、真实屏幕阅读器、Android/iOS真机和历史全量QA均not-run/blocked。
- 第10轮原始ZIP已复验；第11、12、35轮ZIP与第12轮20SVG仍缺。冻结V0.35 SHA `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`，原图SHA `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`均保持不变。

**恢复：** 在隔离空目录解压R245F21累计ZIP，执行`python3 v036_r245f21/run_selected_qa.py --no-write`及`python3 v036_r245f21/repro_r245f20_races.py --no-write`。只删除隔离目录即可回滚。不得将中立来源描记升级为正式身份。
