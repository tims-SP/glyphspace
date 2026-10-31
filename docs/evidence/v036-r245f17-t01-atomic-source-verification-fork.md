# R245F17 · T01/T02 来源校验并发原子性（独立分叉，非认证）

父R245F16累计ZIP SHA256 `bc343a657e317838bcf289ccc058bdd1a49a37e70e09f79664638acf1d8db939`，3204/3204文件逐SHA继承；新R245F17累计ZIP 3213文件，SHA256 `2c4090e7fd177a33c221190f145aa4aef886cd1228ef350d8979f468d57f68ea`。Python zipfile与系统unzip双独立恢复各3213/3213 SHA一致、各456/456选定QA、QA后0文件漂移。隔离工作台HTML SHA256 `d2ce90792f0ac0ef0463e8cf3969af48bd54d2c1fd1fccb127a153cea0f2f172`。

## 真实缺陷与修复

Chromium about:blank中，R245F16并发执行有效JPEG验证与无效JPEG验证时，旧实现共用全局Image的onload/src，第一项Promise超过3.5秒未完成（预期旧缺陷），无效校验后registryVerified仍为true。R245F17使用私有字节快照、独立候选Image/Blob URL、evidenceEpoch latest-wins门禁；失败时三个验证标志一起清零；文件读取/自动fetch增加请求epoch。未提交笔画草案随来源重验取消，已有未批准记录保留。

新代码并发四种顺序、恢复、缓冲区篡改隔离、25键与描记API **14/14 Chromium通过**；原图25键/170观察/52案件及M四项跨框拒绝 **63/63 Chromium通过**；R145 Python原始RGB SHA/非认证门禁 **379/379**；总计**456/456选定QA**。旧缺陷超时不计通过，历史全量QA not-run。

## 验收边界

本轮未获得R246主线3054文件ZIP原始字节，不含R246主线M跨裁框修复；此包不可冒充R247连续主线。R11/R12/R35 ZIP及R12 20 SVG仍缺。合法同源高清来源与许可、逐笔形态归属、真实同源Web Locks/localStorage、真读屏、真机均not-run/blocked。T01正式0/25，T02批准永久ID0，T05缺根未知，Root T00–T11 **0/12 Accepted**。冻结V0.35 HTML、2008 JPEG、176编码、正式SVG、生产入口、用户存储未修改。
