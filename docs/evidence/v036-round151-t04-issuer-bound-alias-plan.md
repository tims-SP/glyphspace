# R151 · Root T04 · 只读影子计划签发校验（非验收）

- 父基线：R150 本地累计 ZIP，1892 文件，SHA256 `51396c322a4a4ac7bd47b3aefb3b8bdcf8c7797b72dc353c1b9763f4a0d31d09`。
- 真实漏洞复现：R150 `verifyPlan` 对修改为 `sourceSlots=999`、重新计算 `planSHA` 且冻结顶层的伪造对象返回 true；它只能证明自一致，不能证明由 `planReadOnly` 签发。
- R151 实质修复：新增不导出的 `WeakMap`，仅 `planReadOnly` 在当前 realm 中登记真实返回对象，`verifyPlan` 先查签发对象身份，再核对已登记摘要/来源 SHA 与原始摘要。重建 JSON、structuredClone、同摘要新对象和外部重新签名均被拒绝。
- 局限：该登记不跨 JS realm，不是密码学签名；已签发计划也不证明上游 reader 代码/原图来源可信。用户生产迁移接口仍未开放。
- 新 Node 22 WebCrypto + FakeStore：**35/35 pass**；继承 R142 233、R143 87、R144 676、R145 379、R146 201、R147 14、R148 Node 29、R148 Chromium about:blank 9、R150 25，共 **1653/1653**。
- R150 授权 Chromium 真实原点 run [40393427271](https://github.com/tims-SP/glyphspace/actions/runs/40393427271)：旧 33/33、严格 v16 27/27、R150 影子计划 16/16；下载 artifact 已实际读取。
- R151 本地 Chromium：file:// 与 localhost 被 `ERR_BLOCKED_BY_ADMINISTRATOR` 阻断；本地真实同源 **blocked**。新增 R151 授权真实同源 Chromium CI [40402103656](https://github.com/tims-SP/glyphspace/actions/runs/40402103656) **22/22 pass**；artifact SHA256 `dba4bf50741c95633b055f4028cce883682479cb8c2eba3358b68033c5826d11` 已下载并逐项读取；仅合成数据预检，不是生产迁移。
- 历史 R10–12/R35 ZIP、R12 20SVG 仍缺；高清合法来源、逐笔来源认证、Android/iOS 真机、真实读屏、完整历史全量 QA 均未完成。
- 原始 T00–T11 **0/12 Accepted**；T01 **0/25**，正式永久 ID **0**，T04 正式迁移 **not-run**，T05 正式补图未完成；冻结 HTML/JPEG/176 编码/正式 SVG/用户存储不变。
