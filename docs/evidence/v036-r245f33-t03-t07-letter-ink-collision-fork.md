# R245F33 · 原始T03/T07：三视图字母与SVG墨迹碰撞隔离修复（非认证）

## 真实基线与父档案
- 2026-11-01重新读取main的STATUS、原始P0、T00–T11任务账本、追踪表、验收规范、AGENTS。main head `03c29e0fcc4b968224b9fdf37bc6d45b54da6b97`，记录R246；R246累计3054成员ZIP SHA `3f2c863af624bee7f9e2c96c3c0262fbb9af777924264612b49da2cc948da6fe`仍未取得原始字节，不能宣称连续继承。GitHub releases为空。
- 实际读取R245F32累计ZIP SHA256 `ca4a830f00624a89579e6845f8246da1586b43f984ae6f79900eb96a9bf50458`，ZIP成员原始字节与解压后逐成员3376/3376 SHA256一致。
- 冻结V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`，2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`重新核对一致。

## 真实Chromium问题与修复
- 旧R245F32独立三视图将字母绝对定位覆盖SVG上缘。通过Chromium实际 `getBoundingClientRect()` 比较字母矩形与151旧字形实例墨迹矩形，完整+迷你两视图共检测到：1280×800 40处、390×844 51处、320×640 76处相交。
- 新R245F33仅修改独立导出器的键帽布局，给字母独立高度条带，SVG仍用100×100 viewBox；151 Path、instanceId草案、inkBBox、锚点、光学校正、变换矩阵、R50/R54来源原始字节SHA均保持一致。移动端来源SHA文本换行与高度压缩也得到修复。
- 三种视口Chromium新QA 107/107，字母与SVG墨迹矩形相交0、25键切换及151实例全/迷你一致，水平和垂直溢出0，JS异常0、外部请求0。均为about:blank模拟视口，非物理设备/读屏/真实同源。
- 继承R245F24–F32选定QA 385/385重新执行，本轮合计492/492。完整历史全量QA not-run。
- 新累计ZIP 3389成员 SHA256 `dcbf5d1d22937e3c7e8eedba19e8f337d700b1f4090ecaa0deb4927c45885ce3`；Python zipfile及系统unzip两次独立恢复各3389/3389 SHA256，恢复后各107/107新Chromium与23/23旧T03 QA，QA后0文件漂移。

## 正式验收边界
T00–T11编号不漂移，全部accepted=false（0/12）。T01来源正式0/25键，T02永久ID批准0，T05缺根数量未知。T03/T07仅隔离预集成，不代表生产集成或正式验收。R11/R12/R35历史ZIP、R12 20SVG仍缺；合法同源高清原图/许可、真实同源Web Locks/localStorage、真实读屏和Android/iOS真机均未通过。冻结生产HTML、176旧编码、正式SVG和用户存储未修改。

源码、截图、逐文件SHA和双独立恢复QA保存在R245F33独立累计ZIP；GitHub只提交技术证据/状态，不声称仓库包含完整累计ZIP源码。
