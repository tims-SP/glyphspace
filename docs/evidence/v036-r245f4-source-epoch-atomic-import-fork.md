# R245F4 · T01/T02 来源验证期间的异步导入竞态修复（隔离分叉，非认证）

## 可重复的缺陷

在 R245F3 工作台使用真实 Chromium `about:blank` 加载冻结 JPEG 字节，先启动有效的人工审阅意见 JSON 导入，拦截并延迟 `File.text()`，随后通过无效 JPEG 字节撤销来源认证，再放行文件读取。**旧版错误地把 1 条意见写入内存**，尽管 `imageReady=false`。这是 TOCTOU（检查与使用之间状态变化），不是来源逐笔认证。

## 修复

R245F4 独立工作台在来源验证开始时递增 `evidenceEpoch`；人工意见导入开始时捕获 epoch，在 `await file.text()` 之后及提交之前同时核对 epoch、`imageReady`、`sourceVerified`、`registryVerified`。来源撤销或**相同 JPEG 重新校验**均拒绝过期导入；失败不改变原有意见；全新合法导入仍通过。

代码、QA脚本及审计在独立累计ZIP的 `v036_r245f4/` 目录。没有修改正式 `index.html`、旧176编码、SVG或用户存储。

## 独立证据

- 父版 R245F3 ZIP SHA256 `cbb044d5697d2769a8ae3f7098d8d86dc0ea816983cd9880c114c7f489835f74`，**3073/3073**成员SHA继承。
- R245F4 累计ZIP **3083**文件，SHA256 `35e42f74ec7db39a96a96d5c7b0bb9fe3c8fba8a1227aeada19d21491c317b6b`。
- R239–R245旧QA 1387/1387；R245F1审计508/508；R245F2浏览器166/166；R245F3浏览器23/23；R245F4新增Chromium21/21，**选定合计2105/2105**。
- Python zipfile、系统unzip两套独立恢复各**3083/3083 SHA、2105/2105选定QA、0文件漂移**。
- 完整历史全量QA、真实同源生产迁移、合法同源高清、真实读屏、物理设备：**not-run**。

## 主线与正式验收边界

GitHub `main` 检查为 R246 / `03c29e0fcc4b968224b9fdf37bc6d45b54da6b97`，其累计ZIP预期3054文件、SHA256 `3f2c863af624bee7f9e2c96c3c0262fbb9af777924264612b49da2cc948da6fe`，**当前运行环境未取得该ZIP真实字节**。本轮仅继承R245F3，编号R245F4，不冒充R247连续主线，也不修改main。

T01正式认证0/25，T02批准永久ID0，T05真实缺根未知，T00–T11仍**0/12 Accepted**。R11/R12/R35原始ZIP及R12的20 SVG仍缺失。应优先取得R246 ZIP并独立复验后再移植分叉修复。
