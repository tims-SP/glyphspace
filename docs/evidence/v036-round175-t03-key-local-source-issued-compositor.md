# R175 · Root T03：来源签发的25键局部SVG组合器（隔离，非正式验收）

日期：2026-10-28。原始WBS为 **T03 SVG坐标内核**，不是第36–40轮UI原型旧标签。正式T00–T11仍 **0/12 Accepted**；T01 0/25、正式永久ID 0、缺根数未知。

## 新实现与边界

在R169 SHA绑定的151个草案实例三视图适配器之上，新建 `v036_round175/key_local_source_compositor.mjs`（位于隔离累计ZIP），使每个键帽由**一个100×100 viewBox的SVG**承载独立`<g data-instance-id>`。25键/151组/153条原始Path；full、mini、focus三视图复用R169完全相同的Path、变换矩阵与实例ID，禁止跨键ID、重复ID、未知键、非法视图、getter/稀疏选择。没有将151草案提升为已认证形态，也没有修改生产`index.html`、176编码、历史正式SVG或用户存储。

## 实际QA

父ZIP为R174，SHA256 `65ce8d4305e8212e6638dd60fe7995bc85f042ead7f985014bc8f6363355e71d`；2151/2151成员逐文件SHA继承。新增Node **19/19**；Chromium真实浏览器`about:blank`载入由来源签发模块导出的实际SVG标记，DPR1/2/3×full/mini/focus九组 **99/99** 断言，检查25 SVG、151组、153可绘制Path、ID/键位隔离、100×100 viewBox及零网络资源。该浏览器测试**不代表在浏览器内直接执行ESM，不代表真实共享原点、真机或读屏**。实际重跑R174选定旧QA **1989/1989**，本轮合计 **2107/2107**。

累计ZIP **2165文件**，SHA256 `99efbb2097a587a19defe47f3c3ee710d7890c03523324ce7815141c68a5265d`。Python zipfile与系统unzip两套独立恢复各2165/2165 SHA、各2107/2107 QA，QA后SHA一致。完整历史全量QA not-run。

## 阻断与下一步

R10原始ZIP已恢复；R11/R12/R35原始ZIP和R12 20SVG仍缺。高清3508×2480第三方图片许可、逐笔原图认证、T02正式永久ID、T03生产集成均未完成。真实共享原点Web Locks/localStorage、Android/iOS真机、真实屏幕阅读器本轮not-run。下一步把隔离组合器接入授权的键帽宿主DOM进行位置/标签碰撞验证，继续T01/T02原图身份仲裁。**不得标记T03或其他Root任务Accepted。**

交付文件位于第175轮隔离累计ZIP的`v036_round175/`，包含源代码、Node/Chromium QA、父包SHA清单、报告、构建清单和缺档审计。GitHub仓库仅存证据与状态，不包含该57MB隔离ZIP。
