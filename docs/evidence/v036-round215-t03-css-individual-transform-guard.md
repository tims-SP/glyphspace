# R215 · Root T03 CSS独立变换与墨迹包络真实像素反例（隔离，非验收）

日期：2026-10-29。父包R214 SHA256 `d06b8400bece34bf9e6fb36ac1c88f7ff33df5e2ada15d2a04902d8de4a6c1da`，2701/2701逐成员SHA一致；本轮独立累计ZIP 2713成员，SHA256 `bd5dd91f5b9f34e8ab7729aefa96b933aa6112b6ebe3d7395c4143e3d54e9625`，Python zipfile/system unzip分别2713/2713 SHA，恢复后各311/311选定QA，QA后0文件变化。第一次合并双恢复任务超时，第二套unzip恢复的QA随后单独重跑通过；不冒称合并任务一次完成。

## 真正复现的缺陷

R213/R214仅审查CSS `transform`，忽略独立CSS `rotate`/`scale`/`translate`。真实Chromium中裁剪HTML祖先使用`rotate:45deg;border-width:40px 5px 0px 30px`，内部SVG使用`transform:rotate(-45deg)`抵消，祖先computed `transform:none`，SVG最终CTM轴对齐。R214错误接受旋转裁剪盒并按轴对齐扣边框，**40个真实黑色像素落在其宣称的保守上界之外**。证据：累计ZIP内`v036_round215/R215_chromium_QA.json`、`R215_R214_false_negative_40px_chromium.png`。

新增`v036_round215/individual_css_transform_gate.mjs`，沿SVG根到HTML根检查独立CSS变换；旋转、负/零缩放、3D缩放/位移、SVG根非轴对齐CSS transform失败关闭。正轴对齐缩放及2D平移在真实浏览器像素包络测试中通过。旧R214模块未修改。新的结果仍是**保守矩形上界，不是精确墨迹边界**。

## 实际QA

R214继承选定261/261（含旧版真实Chromium及906组冻结旧SVG几何）、R215新增真实Chromium31/31、冻结静态19/19，合计**311/311**。两个独立恢复目录均真实执行相同QA并逐文件SHA对照。完整历史全量QA：not-run。

真实独立127.0.0.1浏览器原点尝试返回`ERR_BLOCKED_BY_ADMINISTRATOR`；同源Web Locks/localStorage blocked/not-run。真实读屏、Android/iOS真机not-run。

## 任务与来源边界

严格归属**原始T03 SVG坐标内核**，不属于第36–40轮UI-01–UI-05。T03尚未生产集成，Root T00–T11仍0/12 Accepted；T01正式0/25、T02正式永久ID0、T05真实缺根数未知。R11/R12/R35原始ZIP及R12 20SVG仍缺；R10原件曾单独恢复但不构成完整历史链。同源合法高清原图原始字节、许可和逐笔认证仍缺。冻结V0.35 HTML、2008 JPEG、176旧编码、正式SVG、生产入口和用户存储均未修改。回滚直接使用R214累计ZIP。
