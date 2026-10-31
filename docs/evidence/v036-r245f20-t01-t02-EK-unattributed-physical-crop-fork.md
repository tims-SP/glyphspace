# R245F20 · Root T01/T02：E/K共享物理裁框中立描记（隔离分叉，非认证）

本轮实际读取R245F19父ZIP，SHA256 `b2a15a68826afbaa0f411948a4c02491755f23782df6175185e7489aa2f069ec`，3230/3230逐文件SHA一致。主线仍为R246（`03c29e0fcc4b968224b9fdf37bc6d45b54da6b97`）；R246 3054成员累计ZIP原始字节未取得，不能升级连续主线基线。

**实际进展：** 以冻结2008 JPEG（SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`）和R144来源注册表（SHA256 `cafa1c6eae872e1562109830faae5347094b41690c7bb63e5a4ce784a95e77bb`）独立重算170/170原生RGB裁框。R245F19的E/K九条来源观察由于4组完全共享物理裁框而零独占像素，按候选身份描记仍被阻断。本轮新增**中立物理裁框描记工具**：只在物理像素层记录人工笔画，严格禁止将笔画绑定为任何候选ID或签发永久ID。

四组明确登记为：E:1/E:8（历史否定，仍无效）；K-lower-left/K:2/K:3；K-lower-right/K:4；K-upper-left/K:0。4个物理裁框对应9个竞争来源观察，**不是4个或9个新增字根**。工具仅在用户手动载入并验证原始JPEG后启用；纯JS SHA256回退使隔离about:blank仍可真实核验原图字节。实际鼠标/指针可描记，导出JSON固定`claimedSourceObservationId=null`、`identityStatus=unresolved`、`formalCertification=false`、`approvedPermanentIds=0`。伪造来源、坐标、身份、审批标志或非法笔画均原子拒绝。无localStorage或外部依赖，原有R245F19 M别名工具未改。

**验证：** 新Chromium真实JPEG文件选择+四组真实pointer+导出导入及18种恶意导入：57/57；继承R245F19 35、R245F18 19、R245F17新修复14及来源63、R145 Python379，共旧510/510；旧新选定**567/567**，另有原生RGB170/170。累计ZIP **3245成员**，SHA256 `61d59cb708d845bcdb1cbbe3059e0832905e730765015613b43d9f211855f765`，Python zipfile与系统unzip双独立解压均3245/3245 SHA，分别真实复跑567/567 QA及170/170 RGB，QA后0漂移。完整历史全量QA not-run；R245F17旧版缺陷的预期失败未计pass。

**边界：** 这是人工审阅工具能力，不是原图笔画归属证明、合法同源高清认证、永久ID批准、正式SVG或T05补图。T01正式0/25、T02批准ID0、T05缺根数未知、Root T00–T11仍0/12 Accepted。R11/R12/R35原始ZIP及R12的20SVG仍缺；真实同源迁移、真实读屏、物理设备、合法高清许可逐笔、历史全量not-run/blocked。冻结V0.35 HTML、2008原图、176旧编码、正式SVG、生产入口及用户Storage均未修改。

**复验：** 累计ZIP内`v036_r245f20/`包含HTML候选、JSON来源契约、可复现构建脚本、浏览器QA、170裁框RGB审计、执行报告和恢复说明。运行`python3 v036_r245f20/run_selected_qa.py --no-write`，不得将中立草案导入正式字根身份表。
