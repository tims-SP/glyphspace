# R199 · Root T03 · 真实 Chromium SVG 几何校验（隔离、非验收）

**日期：2026-10-29；轨道：原始 T03，不是 UI-01–UI-05。**

实际读取并独立复验 R198 累计 ZIP：2495 文件，SHA256 `6e2c7460154f08c347d7e0835d5f06aa6ad4fc04e669e76f066a006391f5ebe0`；父成员逐文件 SHA256 2495/2495 继承。

直接使用未修改的 R198/R197/R175/R160/R125 来源签发模块与冻结 R50/R54/R53 的151草案实例，生成 full/mini/focus 三视图 × 光学编辑前后，合计 150 个 SVG、906 实例组、918 Path。在本地独立系统 Chromium + Playwright 的 **about:blank** 真实 SVG DOM 中执行 `getBBox()`、`getScreenCTM()`、Path 属性、源键位、100×100 坐标和归一矩阵验证：**83/83 通过**。M/V 两实例矩阵按预期改变，其他149保持；全部实际几何仍在键帽内。

R125 解析式 stroke-inclusive 墨迹边界与 Chromium geometry-only `getBBox()` 对照：150/151实例差异 <0.01 键帽单位。唯一例外 `wb06/H/legacy-07` 约0.90434345，符合三条 `stroke-width=7`、局部 `scale(0.92)`、实例 `scale(0.14042597355)` 的完整 stroke 扩张宽度；这不是来源笔画认证。浏览器截图仅供审阅。

本轮实跑选定继承旧QA 901/901 + 新真实浏览器83/83 + 静态/冻结17/17 = **1001/1001**。累计 R199 ZIP 2508文件，SHA256 `8b0987baef9181773b01a3189e24effbc1842b7eb570bbd48e20e569bb584ff7`；Python zipfile 和系统 unzip **两套独立恢复**，各2508/2508 SHA、各1001/1001 QA，QA后文件SHA无变化。源码、原始JSON、截图、逐文件父SHA、双恢复审计在独立累计 ZIP 的 `v036_round199/`。

**不可外推：** 本轮浏览器是 about:blank，不是共享原点 Web Locks/localStorage；真实用户迁移、Android/iOS真机、真实读屏、完整历史全量QA均 not-run。T01正式认证0/25，T02正式永久ID0，T03未生产集成，T05缺根数未知，**T00–T11 0/12 Accepted**。R11/R12/R35原始ZIP及R12 20 SVG仍缺；合法同源高清原图字节/许可及K/E/B/J/R/X/V逐笔归属仍未解决。冻结V0.35 HTML、2008 JPEG、176旧编码、正式SVG、生产入口及用户Storage未动。

后续：优先T01/T02的M/V/K/E及其他高风险来源身份，T03隔离浏览器几何成果不得直接提升为正式生产认证。
