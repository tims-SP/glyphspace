# V0.36 R245F62 — Root T02 异步审阅导入会话隔离（隔离分支，非正式认证）

- 基线：R245F61 累计 ZIP SHA256 `93bfa399703ec9df57aba54c1fc38a429a700b49f3542d0f44aa48fb136e2e48`，3704/3704 成员逐 SHA 继承。
- 新累计 ZIP：3719 文件，SHA256 `23c8822d3ccec9681e3a6d874743e5fec9cc8bcb1d10673c44afb299334ac414`。仅在本轮隔离恢复包增加 15 文件；生产入口与正式 SVG 未修改。
- 真实 Chromium about:blank 复现旧 R245F61：`File.text()` 待决期间来源重置并重新验证、裁框往返、候选往返、筛选重建后，旧导入 4/4 错误恢复过期笔画。
- R245F62 使用来源 `loadEpoch`、审阅选择 `reviewSelectionEpoch` 与 `bindingKey()` 三重守卫，4/4 拒绝过期提交；正常导入 1/1 保留。
- 新浏览器 15/15 + 新静态 14/14 + 继承旧 QA 直接覆盖新 HTML 170/170 = **199/199**；Python zipfile / 系统 unzip 两个独立目录分别 3719/3719 SHA、199/199 QA、QA 后漂移 0。
- 测试使用合成已验证来源状态，不是私有高清 JPEG 逐笔认证；历史全量 QA not-run。
- T01 正式来源认证 0/25，T02 批准永久 ID 0，T05 真实缺根数未知，T00–T11 **0/12 Accepted**。
- 第 11/12/35 轮原始 ZIP、第 12 轮 20 SVG、R246 主线累计 ZIP 仍未取得。第 10 轮原包由 R164 恢复，本轮未重验。
- 正式来源许可、高清逐笔、生产迁移、真实读屏、Android/iOS 真机均 not-run。冻结 V0.35 HTML SHA `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`、2008 JPEG SHA `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`、176 旧编码、正式 SVG、用户 Storage 不变。

**下一步**：优先 K:2/K:3 共框笔画归属、M 四个未绑定形态及合法高清来源认证，不能用此事务修复替代 T01/T02 正式验收。