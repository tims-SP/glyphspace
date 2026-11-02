# R245F74 · Root T03 · F73回滚修复累计恢复与真实Chromium验证

## 来源、继承与身份
- 基于R245F72累计ZIP，真实SHA256 a97e44a854c658166ab49e2d2295bcd67b9ae9ea6f00a3f4446fbd84aec0fcb9；3869/3869成员逐SHA对照原有清单一致。
- R245F73修复模块由远端分支源码字节重建，Git blob SHA 458761af9c4171e43d1c98cfff4c1fcd9d75ac97 与GitHub一致。
- 新累计R245F74 ZIP SHA256 eceb23c0162632f889a48ba82ffc4d4cb7ca45b8bcb4d1622cc78edb0e865f35，3889成员，继承3869/3869，新增20。ZIP仅在聊天交付，不进入公开Git仓库。

## 真实执行
- Node VM故障注入：5场景37/37断言，通过。修复第二个SVG setter先修改再抛异常后的回滚义务缺口；回滚不完整时桥接失败关闭。
- 新增Chromium about:blank 1280×800 DPR1和390×844 DPR2模拟：43/43；覆盖151候选/25键、M键两实例三视图、setter先写DOM后抛错、DOM与事务状态回滚、过期CAS及越界拒绝。
- 继承选定旧QA及新QA：651/651。F56运行完整120项，F65 98、F67 63、F68 22、F69 39、F70 56、F71 72、F72 53、T00 48、F74 43、F73 Node 37。
- Python zipfile与系统unzip两次独立恢复：各3889/3889 SHA，各651/651选定QA，QA后文件漂移0。
- 首次并发unzip QA运行超时，随后独立逐套重跑全部11套通过；超时运行不计pass。

## 冻结与验收边界
- V0.35冻结HTML SHA256 fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc、2008 JPEG SHA256 df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49，均本轮复验一致。
- 不改生产index.html、176编码、正式SVG或用户Storage。新几何候选不是原图逐笔认证。
- 真同源Web Locks/localStorage、真实读屏、Android/iOS真机、完整历史全量QA均not-run。
- 第11/12/35轮原始ZIP与第12轮20 SVG仍缺，Library名称检索未发现，不宣称连续历史完整。
- 正式T00–T11仍0/12 Accepted，T01 0/25，T02正式永久ID0，T03生产未集成，T05真实缺根数未知。
- 该分支继承R245F73隔离分支，不混合Root R246。不得自动发布或停止定时任务。
