# V0.36 · R245F69 · Root T03 隔离预览状态封装

**状态：非正式验收，T03 accepted=false。** 父包R245F68 SHA256 `9cc7725e38ee6265270941ed4a47f0acf41564c77cadfbde70bf13ef1e1f64d3`，3802/3802成员逐SHA继承，未混合main的R246历史。

## 真实缺陷与修复

真实Chromium复现R245F68暴露可写`GlyphSpaceT03Preview.offsets` Map：直接`offsets.set('M-root-01',[0.5,0])`可让几何`snapshot`的x改变0.5，但三个SVG视图transform与几何revision不变。修复采用只读`get/has`兼容门面，`get`返回冻结光学数组副本；`getOptical`也返回冻结副本。旧的`setOptical`、`setPlacement`、reset和151条只读导出行为保持。

## 实际验证

- R245F68旧缺陷3/3复现；R245F69真实Chromium桌面1280×800 DPR1及移动模拟390×844 DPR2新增39/39。
- 继承F68 22/22、F67 63/63、F56 35/35、F65 98/98、T00 48/48；工作副本共305/305选定QA。
- 累计ZIP 3821成员 SHA256 `c6f0c002198299fdc7b84455ad7f354c32268dd96d32edbcdc7d42eb8f4f4321`；Python zipfile和系统unzip双独立恢复各3821/3821逐文件SHA，恢复后各305/305选定QA、QA后0漂移。
- 两个独立Chromium上下文151条非认证几何草案字节一致，SHA256 `b1abc3d88653b402c2fbe1f4569d41c50e85b83968482be577af44be2145de30`。

完整累计ZIP、QA与成员清单保存在本轮交付包，GitHub提交可复现补丁源码与证据。测试仅about:blank隔离profile；不是同源用户迁移、真机、真实读屏或原图逐笔认证。完整历史全量QA **not-run**。冻结V0.35 HTML、2008 JPEG、176编码、正式SVG、生产入口、用户Storage未修改。

## 整体停止门禁

原始T00–T11仍0/12 Accepted；T01 0/25键，T02批准永久ID0，T03生产未集成，T05缺根数未知。R11/R12/R35原始ZIP和R12 20SVG仍缺。不得发布或停止每小时任务。
