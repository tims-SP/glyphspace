# 第104轮 · Root T03 SVG祖先伪元素遮挡门禁（非正式验收）

日期：2026-10-25。**原始T00–T11编号及accepted状态均不改变，正式验收0/12。**

## 实际缺陷与隔离修复

真实Chromium在第103轮隔离HTML中复现：对`.key-cell`、`.key-row`、`.view`或`body`添加`::before`/`::after`伪元素遮挡层，SVG `getBBox()`不变，祖先普通computed style门禁仍允许`attest()`。五类CSS负例改变真实截图像素（分别8803、304290、26067、71415、507708个RGB像素），R103全部错误放行。

第104轮隔离HTML在SVG祖先链的普通样式与结构基线之外，新增`::before`/`::after` computed paint/compositing签名。五类伪元素遮挡均被R104失败关闭；编辑、撤销、导入及三视图操作继续正常。真实Chromium about:blank新增QA **25/25**。这是明确的隔离绘制缺陷修复，不是源图逐笔认证、生产集成或一般性的DOM/CSS安全证明。

## 父包、QA、恢复

- 实际读取R103累计ZIP：**1410文件**，SHA256 `bdd1f42c847c01bc98b278294b7a6074550e293c9e4b977f601dc4fe75ef8874`；继承**1410/1410**逐文件SHA一致。
- R104独立累计ZIP（不上传公开GitHub）：**1425文件**，SHA256 `3840ac7eaeea34c66d3c251dd8906117d92de2f5536b34256d26b6afad275289`。
- 新旧定向QA：R104 25、R103 26、R102 52、R101 58、R84 124、R86 20、R99 Chromium 302、R94 18、R93 12；**9/9组、637项通过**。完整历史全量QA **not-run**。
- Python zipfile与系统unzip两种方法分别进行**两次独立恢复**，按0–5及5–9两段执行9组QA；四份恢复环境在QA前后均**1425/1425**成员SHA一致。首次尝试整批恢复QA超时，**不计通过**；最终改用四次独立分段复验全部通过。
- 冻结V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`、2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49` 在最终ZIP内再次一致；176旧编码、正式SVG及用户存储未改。

## 未解决事项

临时独立Chromium profile访问127.0.0.1时实际返回`ERR_BLOCKED_BY_ADMINISTRATOR`；Web Locks/localStorage真实同源事务为**blocked/not-run**，未触碰用户原有存储。真实Android/iOS与屏幕阅读器为**not-run**。缺第10–12/35轮ZIP、第12轮20SVG、合法同源高清图；T01正式来源认证仍**0/25**、真实缺根数未知、T02正式永久ID **0**。T03仍未生产集成，原始T00–T11 **0/12 Accepted**。

隔离累计包内`v036_round104/`包含HTML、源码、QA、父文件SHA账本、缺口清单及恢复脚本；回滚仅删除此隔离目录，不修改冻结正式入口。
