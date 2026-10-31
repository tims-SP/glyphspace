# R245F29 · 原始T03草案来源与变换一致性门禁（非正式验收）

2026-11-01。独立分叉：父R245F28 ZIP SHA256 `f02069e8268824786b73488b1a69246175e79f151653c86a72cf71f636bae86d`，3340/3340成员逐SHA继承；R245F29累计3349成员ZIP SHA256 `c0fd1ec988c49828f141fa00ece673a19f1a7c4bc039d0cd983c54f585e23622`。Python zipfile及系统unzip双独立恢复各3349/3349 SHA；每套旧新选定QA各268/268，QA后0漂移；完整历史全量QA not-run。

**实质问题：** 在R50冻结151条旧SVG Path + R54解析式inkBBox构建的R62隔离T03草案中，旧 `auditCatalog` 错误接受5种不一致：transform.tx改动未同步geometry；geometry.ox改动未同步transform；Path d字节变更；M键成员顺序被改；inkBBox与来源向量不一致。五类均已在真实Node运行中复现旧错误接受（不计入通过）。新增独立 `auditT03DraftCatalogIntegrity` 对151条旧实例逐项绑定来源Path/绘制属性、解析式inkBBox、100×100锚点/光学补偿/变换矩阵、25键成员归属；新门禁五类全部拒绝。新增 `safeSourceBoundOpticalPatches` 在旧R62事务补丁前后执行校验，合法光学修正通过。

本轮新增Node 24/24；继承R245F24 27、F25 17、F26 44、F27 76、F28 80，共244；合计268/268（选定QA，不是历史全量）。继承Chromium QA仅隔离about:blank；真实同源Web Locks/localStorage、读屏、Android/iOS真机、生产迁移均not-run/blocked。冻结V0.35 HTML、2008 JPEG、176旧编码、历史正式SVG、用户Storage均未修改。

**正式边界：** 这是原始T03的隔离预集成工具，不是T03 Accepted；T01正式25键认证0/25、T02永久ID批准0、T05缺根数未知，T00–T11仍0/12 Accepted。R246主线3054成员累计ZIP原始字节未取得；R11/R12/R35历史ZIP与R12的20 SVG仍缺；R10原ZIP在R164已恢复。合法同源高清原图及许可未建立，不能以旧Path/墨迹几何测试冒充原图认证。

本轮累计ZIP、父成员SHA清单、Node QA、两套恢复QA及恢复说明保存在隔离恢复包 `v036_r245f29/`（未向公开仓库提交二进制）。GitHub仅存本证据和状态文档；主线生产入口保持不动。
