# R245F19 · Root T01/T02 · M键同物理裁框别名人工描记解阻（非认证）

2026-10-31。独立分支继承R245F18；未修改main或冻结生产入口。

**真实父包：** R245F18累计ZIP SHA256 `3cfbcfd15c8006a3beb7bfa9f9aacfc67501785eb0e205f356c8252463e9ff2e`，3220/3220成员SHA一致。本轮R245F19累计ZIP 3230文件，SHA256 `b2a15a68826afbaa0f411948a4c02491755f23782df6175185e7489aa2f069ec`，Python zipfile和系统unzip两次独立恢复各3230/3230 SHA、选定QA510/510、170/170原图裁框RGB SHA及QA后0漂移。完整历史全量QA not-run。

**来源实质发现：** R144 25键170来源观察中17条因裁框重合而零独占像素。R245F18把M键四对「候选来源观察/历史索引来源观察」完全相同的物理JPEG裁框视为互斥，旧Chromium 4/4无法描记。R245F19对明确的M-vis-01↔legacy:M:0、02↔M:1、03↔M:2、05↔M:3四对，仅在nativeRect完全一致且RGB SHA完全一致时豁免对方的像素排除；8条M来源观察可进行**人工未批准笔画描记**。E:1/E:8和K七条共享裁框仍严格阻断，未作身份合并。M-vis-04/06/07/08四个未绑定微形保持隔离。

**QA：** 新Chromium about:blank 35/35（旧缺陷复现、4组M双向像素归属、4组手工笔画/导入回环、E/K保持拒绝、K伪造导入不污染旧草案）；旧R245F18 19/19、R245F17固定候选14/14、来源63/63、R145 Pillow379/379。R245F17旧版预期超时不计入通过。170/170原始JPEG裁框独立重算RGB SHA。冻结JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`。

**严格边界：** 仅低清冻结图几何与人工描记能力，绝非高清合法同源逐笔认证；没有新正式Path、永久ID、确认缺根数或T01 Accepted。T01 0/25、T02批准ID0、T05缺根未知、T00–T11 0/12 Accepted。真实同源Storage/Web Locks、真实读屏、Android/iOS物理设备、历史全量QA均not-run。R246原始3054文件ZIP未取得；R11/R12/R35 ZIP及R12 20 SVG仍缺。176旧编码、历史SVG、V0.35冻结HTML、原JPEG、用户Storage及生产入口未修改。

**恢复：** 以R245F18父ZIP为输入，使用R245F19累计ZIP内`v036_r245f19/patch_r245f19.py`及`qa_r245f19.py`、`audit_r245f19.py`独立复验。所有输出仍为review-only，禁止自动认证/合并。
