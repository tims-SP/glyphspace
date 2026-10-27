# R160 · Root T03 来源绑定的151实例SVG矢量快照（隔离、非正式验收）

日期：2026-10-27。轨道：Root T03（100×100 SVG坐标内核），关联T00/T02。UI-01至UI-05未改变原任务编号。

## 实际代码与新增能力

R159 自有数据描述符快照接受调用者提供的任意 inkBBox，缺少真实冻结 Path 来源绑定。R160 新增 `v036_round160/source_bound_vector_snapshot.mjs`（在隔离累计ZIP内），将 R125 已有的 R50 Path 原始字节、R54 解析式矢量 inkBBox 和 R53 151实例草案目录的三个 SHA 绑定来源与 R159 不执行 getter 的快照门禁连接。只允许完整151条已知草案ID、逐条真实 Path SHA 匹配、100×100范围内光学校正；拒绝漏项/插入/重复、来源路径漂移、getter/继承属性、未批准来源认证及生产发布标记。返回零原型、不可变的预集成计划。与 R125 逐项几何一致，不改变冻结生产入口。

**边界：** 151是冻结草案，不是已认证根总数；解析式边界只对既有受支持SVG绘制子集成立，非渲染像素精确。正式referenceShapeId/assetId/instanceId、25键逐笔源图认证、生产T03集成均未完成。R125 SHA绑定注册表不是原图来源许可证明。

## 实际校验

父R159累计ZIP：1997文件，SHA256 `27aaf806a767888c586feddd805a9253c7dab3d6088fd6603edea46188cccac6`，逐文件继承1997/1997一致。R160新Node QA 30/30、继承定向2053/2053，合计2083/2083。新累计ZIP 2007文件，SHA256 `50892db856dbc26c52d9b18d330f818ee4fd391ed526ca2e861d780cabccaa6b`；Python zipfile 与系统 unzip 两次独立恢复均2007/2007 SHA、2083/2083定向QA，QA后2007/2007 SHA不变。完整历史全量QA not-run。

冻结V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`，2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`。正式SVG、176旧编码、用户localStorage均未修改。

## 未解决阻断

缺R10–12/R35历史ZIP与R12 20SVG，不能宣称连续历史；合法同源高清原图再分发许可及逐笔认证未完成。真实同源浏览器、Android/iOS真机、真实读屏及完整历史QA本轮not-run。T01 0/25、正式永久ID 0、T03未生产集成，T00–T11仍0/12 Accepted。下一轮优先M/K/E/V/X逐笔身份与许可来源，不把几何一致性当字根认证。
