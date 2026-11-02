# R245F70 · Root T03 独立草案几何事务内核（非认证）

- **来源**：R245F69独立累计ZIP SHA256 `c6f0c002198299fdc7b84455ad7f354c32268dd96d32edbcdc7d42eb8f4f4321`，3821/3821成员逐SHA继承。F70累计3839成员ZIP SHA256 `3f2092029e44545e71d38489f908183ec621ab9220e6f85729e773229c6e1e02`。
- **实质实现**：[独立T03事务几何源码](../../scripts/r245f70_t03_draft_geometry_registry.js)，SHA256 `6a1af0726339479e044de7c595098d8df0d6c0a23cf887cbf45f1eafe77f4054`。从151条旧SVG只读草案几何导入，严格100×100、inkBBox草案、锚点、光学校正；按候选身份执行原子move/reorder与无正式SVG的M占位insert/remove，失败整批回滚，不按数组位置重映射。
- **隔离**：新增M占位仅 `draft-only/M/microframe-01`，`legacyInstanceId=null`、`paintedBBox=null`、`assetId=null`、`referenceShapeId=null`，不得当正式补图/永久ID/认证笔画。
- **QA**：真实Chromium `about:blank` 1280×800 DPR1和390×844 DPR2新增56/56；旧F69 39、F68 22、F67 63、F56 35、F65 98、T00 48，合计选定361/361。Python zipfile与系统unzip各3839/3839 SHA、各361/361 QA，QA后成员0漂移；历史全量QA not-run。
- **冻结**：V0.35 HTML `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`、2008 JPEG `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49` 均未变。176编码、正式SVG、生产入口、用户Storage未动。
- **正式状态**：Root T00–T11 **0/12 Accepted**；T01 0/25键认证、T02永久ID0、T03未生产集成、T04正式迁移未验收、T05缺根数未知。R11/R12/R35 ZIP和R12 20 SVG仍缺；合法同源高清/逐笔、真实同源、读屏、真机、历史全量均blocked/not-run。
- **回滚**：删除F70隔离候选并恢复F69父包即可；不涉及生产数据。
