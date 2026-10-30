# R230 · Root T03 — 冻结V0.35真实三视图指针→100×100光学校准与inkBBox（隔离，非验收）

- 2026-10-30 11时（Asia/Shanghai）读取main六份强制文档及原V0.35问题矩阵，R229父累计ZIP SHA256 `eaa5226d561f13343343ce2c7d8412853ab917739ccdd076f11a2b194d70cb26`，2888/2888成员逐SHA继承一致。
- 新增隔离`v036_round230/live_v035_pointer_ink_adapter.mjs`及派生`V035_R230_T03_pointer_ink_preview.html`（代码交付于本轮累计ZIP，**非仓库正式生产入口**）。将真实Chromium getScreenCTM逆矩阵指针手势接入冻结V0.35完整键盘、聚焦放大、折叠迷你三视图；使用151旧可视槽的100×100 SVG `getBBox({fill:true,stroke:true})`和ink-center锚点；三视图事务同步、失败回滚、卸载恢复。发现折叠时full SVG隐藏导致getBBox为空并修复为仅对可绘制视图做墨迹包络校验。
- 桌面1280×800 DPR1及手机390×844 DPR2的真实Chromium `about:blank`浏览器QA **46/46**；R230静态 **25/25**，R229旧 **101/101**，R227旧 **3848/3848**，本轮选定旧新 **4020/4020**。完整历史全量QA **not-run**。
- 累计ZIP 2900成员，SHA256 `7930431d36db4f28cab00fb0444b6eb203ce28f6b66ebef2ad798505ba39c6aa`；Python zipfile和系统unzip两个独立全新解压各2900/2900 SHA、各4020/4020 QA、QA后0文件变化。首次合并执行超时，第二套QA随后独立完成。
- `getBBox`仅为浏览器绘制几何，不是2008原图逐笔/许可认证。T01正式0/25，T02批准永久ID0，T05真实缺根未知；Root T00–T11 **0/12 Accepted**，T03仍非生产集成。真实同源Web Locks/localStorage此前被管理员阻断，本轮CLI尝试超时：**blocked/not-run**；真实读屏、Android/iOS真机、高清逐笔、完整历史QA均not-run。
- 第10轮原始ZIP曾于R164恢复；第11/12/35轮原始ZIP及第12轮20SVG仍缺；合法同源3508×2480高清原始字节/许可未取得。冻结V0.35 HTML、2008 JPEG、176旧编码、正式SVG、生产入口、用户Storage未动。UI-01至UI-05独立，不冒充Root T03/T05。

本轮证据仅证明隔离T03技术进展，不满足原始T03正式验收退出条件。
