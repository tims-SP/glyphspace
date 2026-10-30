# R231 · Root T03 · 真实浏览器指针事件接入（隔离，非验收）

2026-10-30。起点：R230累计ZIP 2900文件，SHA256 `7930431d36db4f28cab00fb0444b6eb203ce28f6b66ebef2ad798505ba39c6aa`。R231实际读取父ZIP并逐文件SHA继承2900/2900一致。

## 本轮实质变化

R230已经具有100×100 SVG、getScreenCTM逆矩阵、inkBBox与三视图事务API，但尚未绑定真实指针事件；冻结V0.35的`.rootglyph`在普通键盘中为`pointer-events:none`，实际鼠标点击会进入五笔训练。R231在**派生隔离HTML**新增独立`pointer_gesture_controller.mjs`，明确调用`arm()`后才允许真实浏览器pointerdown/pointerup命中绘制的字根，借助pointer capture和R230事务在完整/聚焦/迷你三视图同步光学位移。Escape、blur、pointercancel、lostpointercapture与卸载均取消令牌；越界失败关闭；disarm后普通训练点击恢复。没有自动启用或写入localStorage。

真实Chromium `page.mouse`而非仅JS直调，在1280×800 DPR1与390×844模拟DPR2执行：新指针50/50、新静态28/28、继承选定旧4020/4020，共4098/4098。父2900/2900 SHA一致；R231累计2912文件ZIP SHA256 `f283ee92bf297a1e99e402cfba34502c25a9ceb9aa7a50e61a36cc15b1abac82`；Python zipfile与系统unzip独立恢复均2912/2912 SHA、各4098/4098选定QA、QA后0变更。完整历史全量QA not-run。

## 不能外推的边界

测试使用隔离`about:blank`，390×844是Chromium移动视口模拟，不是真机。真实同源Web Locks/localStorage此前管理员策略阻断，本轮not-run；Android/iOS、真实屏幕阅读器、高清同源原始字节/许可及逐笔认证not-run。第10轮原始ZIP已恢复，第11、12、35轮原始ZIP和第12轮20SVG仍缺。T01正式来源0/25、T02批准永久ID0、T05真实缺根数未知，T03尚未生产集成；**T00–T11 0/12 Accepted**。原始任务编号及UI-01–UI-05分离不变。

冻结V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`、2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`、176旧编码、正式SVG、生产入口及用户原有存储未修改。回滚只需删除R231隔离目录/累计ZIP；父R230保持可恢复。
