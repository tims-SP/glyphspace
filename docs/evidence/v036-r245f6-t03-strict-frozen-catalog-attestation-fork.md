# R245F6 · Root T03 冻结SVG目录逐字段来源绑定（隔离分叉，非正式验收）

2026-10-31。GitHub main仍为R246；其3054成员累计ZIP原始字节不可得，因此从实际验证的R245F5独立累计ZIP创建R245F6，**不是R247主线**。父ZIP SHA256 `e9a08e0ac401db814bd8fafd0ae5127edf902c8dcc4e0cd7db9cde95680faca0`，3090/3090逐成员SHA继承。

## 实际缺陷与实现

在冻结151实例/25键真实SVG目录上复现：R62 `auditCatalog` 可错误接受（1）SVG Path被替换、（2）草案assetId被替换、（3）byKey成员顺序变化、（4）仍处100×100内的transform偏移。旧验证只检查数量、几何边界与非认证标志，未将完整目录逐字段绑定到R50 Path和R54解析式inkBBox。

新隔离模块 `v036_r245f6/strict_legacy_geometry_attestation.mjs` 从冻结R50/R54源重建预期目录，对151实例每个字段、25键成员列表、来源摘要及未认证状态进行严格比对；仅当提供显式待审patch且R62安全光学校正可重演时才接受几何改动。QA真实读取冻结HTML与2008 JPEG原始字节，验证SHA；输入R50 JSON SHA `1d03c98a3dbd7074305e50cbb604447865ef2f9cde7786261aa9252b49860089`，R54 JSON SHA `65f3835499e64211e0f787cce7c2e33d18bea11c3d75204ee9e0f1eedf097f48`。

新增Node QA 25/25，继承选定QA 2125/2125，合计**2150/2150**。累计ZIP **3099成员**，SHA256 `be4e95ee257a6f9d61bfd11974bc69458f80b0f4fedf99556f94185d80674a5f`；Python与系统unzip两次独立解压各3099/3099 SHA，各2150/2150选定QA，QA后0文件漂移。完整历史全量QA未运行。

## 不得越过的验收边界

这是T03预集成的目录完整性门禁，**未集成正式单HTML、未批准任何永久ID，也未认证来源字形**。T01正式认证0/25键、T02批准ID0、T05真实缺根数未知，原始T00–T11仍0/12 Accepted。真实同源用户存储、真机、真实读屏、合法同源高清逐笔认证、仓库级verify_repo.py均not-run。R11/R12/R35原始ZIP和R12的20SVG仍缺；R10已于R164恢复。

冻结V0.35 HTML、2008原图、176编码、历史正式SVG、生产入口、用户原有localStorage均未修改。此分支不修改main；取得R246真实ZIP并复验后才可考虑移植。

外部同布局低清镜像仅发现网页线索（iwubi.net 08wubi.jpg、b.awei.pub wbxsj.jpg），没有验证高清原始字节或许可，**不能计为同源高清认证**。
