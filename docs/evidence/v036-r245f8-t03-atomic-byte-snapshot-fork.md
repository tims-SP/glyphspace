# 字间 V0.36 · R245F8 · Root T03 原始字节快照竞态修复（隔离分叉）

**R245F8 / 原始T03（异步SHA字节快照竞态修复，隔离分叉，非认证）：** 真读R245F7累计ZIP SHA `a8d0c3aed1ae7c315c4a1bab742ad591bd508cb8dbb977ecce4112bcedbaa405`，3110/3110逐成员SHA继承。独立Node WebCrypto重现旧门禁在digest后/JSON解析前调用者同长度改写R50/R54原始buffer，将首项`金`改为`木`仍错误接受151实例伪目录；R245F8同步快照字节后同一伪造被拒绝，合法源即使调用者异步修改也正确接受。继承定向570/570+新增12/12=582/582；3119文件累计ZIP SHA `009310ce79cb62082150d2930ab4333d137d57e54cba86138dc2ef2c89d8a77e`，Python/unzip双独立恢复各3119/3119 SHA及582/582 QA、0漂移。R245F7完整选定2167曾尝试但超时，不计通过；本地Chromium导航blocked，历史全量/真实同源/读屏/真机/合法高清逐笔not-run。R246主线ZIP仍缺；R11/R12/R35及R12 20SVG仍缺。T01 0/25、T02批准ID0、T05缺根未知、Root 0/12 Accepted；冻结入口/176编码/用户Storage未动。[R245F8证据](./evidence/v036-r245f8-t03-atomic-byte-snapshot-fork.md)。

## 真实复现

R245F7 `bytesOf` 只创建共享底层ArrayBuffer的Uint8Array视图。摘要API异步执行时，调用者仍可改写原始buffer。Node/WebCrypto确定性测试先对原始R50/R54字节求SHA，再在Promise返回前把第一项 `glyph: 金` 同长度替换为 `glyph: 木`；同时使用被篡改的对象重建目录。旧R245F7门禁**错误接受151/151实例**，证明digest与JSON.parse之间存在TOCTOU竞态。

## 修复与界限

新增 `v036_r245f8/snapshot_byte_geometry_attestation.mjs`，在任何await之前复制输入ArrayBuffer/TypedArray有效视图范围到独立Uint8Array；digest与JSON.parse使用同一不可被调用者更改的快照。历史R245F7文件保持原样；新接口仍调用R245F6的151实例/25键严格目录比对，且不批准永久ID、字根轮廓、版权或发布。原始T03依赖T02未Accepted，生产单HTML未集成。

## 真实验证

父R245F7 ZIP SHA256 `a8d0c3aed1ae7c315c4a1bab742ad591bd508cb8dbb977ecce4112bcedbaa405`，3110/3110 SHA继承；冻结V0.35 HTML SHA `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`，2008 JPEG SHA `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`，R10原始ZIP SHA `6a1552b45cfa3512d9fea2ab06df740a6adbb4b598369cd3ea8e214fee1c0ed0` 均独立一致。继承定向旧QA 508+20+25+17=570，新QA 12，合计582/582；Python zipfile及系统unzip分别独立解压3119/3119 SHA，并各自重跑582/582，0漂移。累计ZIP SHA256 `009310ce79cb62082150d2930ab4333d137d57e54cba86138dc2ef2c89d8a77e`。

R245F7完整选定2167 QA尝试超时，**未完成**；本地Chromium `data:` 导航返回 `net::ERR_BLOCKED_BY_ADMINISTRATOR`，浏览器验证blocked。真实同源Web Locks/localStorage、屏幕阅读器、Android/iOS、合法高清逐笔、完整历史全量QA、生产迁移均not-run。R246 ZIP真实字节未取得，不能冒充R247主线。R11/R12/R35 ZIP及R12 20SVG仍缺。

原始T00–T11全部 `accepted=false`，正式0/12。T01来源0/25，T02正式永久ID0，T05真实缺根数未知。没有修改冻结V0.35 HTML、2008原图、176编码、正式SVG、生产入口或用户Storage。
