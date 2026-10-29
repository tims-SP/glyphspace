# R226 · Root T03 · 外部CSS计算样式漂移失败关闭（隔离非验收）

2026-10-30。原始任务T03 SVG坐标内核，不属于UI-01至UI-05，也不是正式生产集成。GitHub main开始时R225 `e47f7e2d46140ae7a631daca8d2f0b3d2b3e2651`。真实读取R225 ZIP SHA256 `07ac163dd8dedb93b2c8520b5fbdd98642f7beb97c1ed203c895f5b195a63f72`，继承2834/2834成员SHA一致。

## 真实缺陷及隔离修复

真实Chromium about:blank中，R225原有DOM拓扑/属性守卫错误接受7种不修改原有节点属性的外部CSS变更：group opacity=0、path stroke-width=19px、svg display:none、section opacity=0、host transform:scale(.25)、path fill变色、svg filter:blur(3px)。新增`v036_round226/live_svg_optical_transaction.mjs`，对host、3个section、75个SVG、453个group和459个path捕获计算样式，防止外部样式表在光学校准前或异步提案期间改变绘制/布局。R225旧模块保留不改，7/7旧版错误接受与7/7新版拒绝在同一真实Chromium中独立复现。

R226新模块继续通过R225 151项来源SHA绑定、三视图原位transform、M/V更新、节点身份、路径不变、失败回滚、非法几何拒绝的3718/3718浏览器回归。R225选定旧QA8169/8169，新R226浏览器3718/3718、对抗30/30、静态16/16，合计**11933/11933选定QA**；不等于完整历史全量QA。

## 实际交付与双独立恢复

R226累计隔离ZIP SHA256 `473f99c16734dff9948a526ab44894caa2132057143315eff8c12ecbcbf50799`，**2849成员**，继承R225的2834/2834文件SHA。Python zipfile与系统unzip分别独立解压、逐文件SHA 2849/2849，并各重跑11933/11933选定QA，QA后文件变更0。恢复包内`v036_round226/`含新模块、对抗脚本、浏览器回归、静态QA、真实同源探测、父SHA清单、审计及执行报告。外置独立成员清单和双恢复QA可供复验。

独立临时Chromium profile访问127.0.0.1真实HTTP原点返回`ERR_BLOCKED_BY_ADMINISTRATOR`；Web Locks/localStorage同源验证标记**blocked**，绝不当作通过，用户原有存储未访问。真实屏幕阅读器、Android/iOS真机、高清同源来源许可/原始字节/逐笔认证、完整历史全量QA均not-run。

T01正式来源认证0/25键、T02批准永久ID0、T05真实缺根数未知，T03未生产集成，**原始T00–T11仍0/12 Accepted**。R11/R12/R35原始ZIP与R12 20SVG缺失。冻结V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`、2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`，176旧编码、正式SVG、生产入口和用户存储未改。

## 下一步

优先寻找经授权的真实共享原点浏览器profile验证Web Locks/localStorage；T01/T02继续追索许可明确的同源高清原始字节、M键四个微框、E/K与B/J/R/X/V逐笔身份。不能把CSS守卫或QA断言数量当作来源认证。
