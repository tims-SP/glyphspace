# V0.36 R217 · Root T03：子组几何漂移拒绝（隔离非验收）

日期：2026-10-29。继承R216，父ZIP SHA256 `90b25d9800939d9b182998d1dc94c7f81694ff8e90cc38c7ad22a37dda5f310c`，2727/2727逐文件SHA一致。

## 可复现的真实缺陷
R216只在拖动前后比较根SVG `getScreenCTM()`。真实Chromium about:blank中，拖动期间分别修改子`<g transform>`、Path `d`、Path `stroke-width`，旧R216均错误接受（3/3）；根SVG CTM未变化。

## 新实现
隔离目录 `v036_round217/` 新增 `pointer_geometry_fingerprint.mjs` 与 `stable_pointer_group_guard.mjs`。在R216来源SHA绑定光学提案前后，比较子组屏幕CTM、SVG子树标记、`getBBox()`、祖先与后代的computed paint/layout样式；活跃动画或几何歧义失败关闭。漂移取消并消耗原令牌。不改Path、176旧编码、正式SVG、冻结V0.35 HTML、生产入口或用户存储。

## 实际QA与恢复
选定旧QA：R216 Node42+Chromium1522+静态24、R215 Chromium31+静态19、R214 Chromium40+静态18，共**1696/1696**。新增真实Chromium：151实例×3变换×DPR1/2=906稳定检查、8漂移拒绝、3旧缺陷复现，**917/917**；来源绑定Node **34/34**；静态 **20/20**；新增**971/971**；选定总计**2667/2667**。R216递归套件实际尝试超时，不能计入通过，完整历史全量QA not-run。

累计ZIP **2740**文件，SHA256 `6bb1302e283a41a17c6390ce5e9229efc8f4f5008b0a8748784540ba4166728d`；Python zipfile及系统unzip双独立解压各**2740/2740 SHA**、各**2667/2667 QA**，QA后0变化。隔离模块只在累计包中；仓库不切换生产入口。

## 形式验收边界
Root T00–T11 **0/12 Accepted**；T01正式参考图认证0/25键、T02批准永久ID0、真实缺根数未知。T03仍未生产集成。第10轮原ZIP已恢复，第11/12/35轮原ZIP及第12轮20SVG仍缺。合法同源高清原图原始字节/许可未取得；真实同源Web Locks/localStorage历史被管理员策略阻断，本轮not-run；真机/真实读屏not-run。不能用本轮CTM或DOM测试替代逐笔、来源或设备认证。
