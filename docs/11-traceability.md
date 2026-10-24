# 11 · 任务—源码—证据—验收追踪

> 本表基于[V0.36-P0原始工作分解](./history/V0.36-P0-original.md)、可用的第46轮独立档案及仓库两份HTML。**“已有证据”不等于“正式验收”**。资料未上传GitHub时必须注明外部档案而非编造仓库文件路径。

| ID | 原始工作包 | 已有事实/证据 | 缺失的正式验收 | 完成 |
|---|---|---|---|---|
| T00 | 基线冻结 | GitHub `index.html` SHA冻结；旧151可视+5关联、176条编码 | 未来候选发行版的双版本回归与可逆恢复 | 否 |
| T01 | 参考图清点 | 第41–46轮离线证据、冲突账本；第46轮ZIP 685文件 | 同源原件逐笔验证、所有25键穷尽审计、正确缺失数 | 否，**0/25** |
| T02 | 语义与ID | 第3、44轮156条稳定ID**草案**；历史类别冲突 | 永久ID/asset ID/reference ID、类别、旧槽映射、schema集成 | 否 |
| T03 | **SVG坐标内核** | 第62–65轮隔离SVG内核、151草案/149资产三视图；第65轮浏览器发现`getBBox`漏stroke并补充真实墨迹包络核验（证据在GitHub evidence文档及外部累计ZIP） | 永久ID/来源认证依赖未满足，未正式集成，完整生产回归未完成 | 否 |
| T04 | 存储与旧版迁移 | 第32轮Node/FakeStore演练 | 真正同源、多标签页/Web Locks/localStorage事务和授权回滚验证 | 否 |
| T05 | **完整性补图** | 原始P0问题矩阵识别M等高风险 | 25键真实参考形态完全建模、独立SVG资产及实例、确认缺失0 | 否 |
| T06 | 轮廓一致性 | 历史字体/SVG轮廓来源审计 | 逐笔形态、笔画重量、异源部件人工签署 | 否 |
| T07 | 位置与碰撞 | 旧几何坐标/个别隔离碰撞检查 | 真实墨迹BBox+stroke、标签/圈注碰撞、所有状态无未批准冲突 | 否 |
| T08 | 校准工作台闭环 | 第41–46轮离线人工审阅/导入工作台 | 新形态登记→分类→五维审批→过期失效→正式发布的闭环 | 否 |
| T09 | 学习视图与输入回归 | 冻结V0.35 176编码、旧三视图、UI-track焦点原型 | 三视图统一资产及几何、三学习模式与特殊取码全回归 | 否 |
| T10 | 视觉和设备验收 | Chromium about:blank隔离桌面/手机预览测试 | Android/iOS实体设备、软键盘、读屏与完整浏览器原点 | 否 |
| T11 | 发布冻结 | 目前只有V0.35正式入口、V0.36隔离原型 | 发布候选单HTML、完整版权来源、QA/回滚、冻结版本 | 否 |

## 并行 UI-track：不占用T编号

| 编号 | 方向 | 当前证据 | 未决 |
|---|---|---|---|
| UI-01 | 全屏零主体滚动与界面减法 | V0.34已完成模拟尺寸布局改造；仍非全真实环境 | 大字体/软键盘/真机可触达 |
| UI-02 | 物理QWERTY渐进键盘/字母帽 | 第36–40轮隔离HTML、Chromium交互 | 与T02/T03正式身份几何合并 |
| UI-03 | 焦点字根放大/分页/高亮 | 第36–40轮隔离原型 | 校正候选数据、实际移动与读屏 |
| UI-04 | 收起键盘后辅助迷你键盘 | V0.34基本版；V0.36拟统一状态源 | 盲打无剧透、输入状态一致 |
| UI-05 | 无障碍与输入途径 | 第38–40轮AX/导航实验 | VoiceOver/TalkBack/NVDA真实验收 |

## 证据寻址与阻塞

- GitHub版本：[冻结HTML](../index.html)、[UI-track原型](../preview/v0.36/index.html)。
- 第46轮独立隔离档案：`字间_V0.36_第四十六轮隔离分支恢复包_继承第45轮_缺第35轮及第10至12轮.zip`；ZIP SHA256：`32c7130983d18965676f643d9fdd5d178047f749d2f0e4676cf7e56a67d7b5ce`。**此ZIP未纳入当前仓库**。
- 独立复验：685/685逐文件SHA匹配、继承663/663、10组QA日志通过；`ERR_BLOCKED_BY_ADMINISTRATOR`阻断真实同源测试，不能记为通过。
- 来源缺失：第10–12轮及第35轮ZIP、第12轮20个SVG。外部资料未收齐时，历史链条标记不完整。

只有证据、正式集成与真实环境验收同时具备，才允许把任何T项改为完成。

## 第66轮 T03隔离来源绑定补充（2026-10-23）

第64轮三视图DOM适配器未强制检查第63轮冻结草案的Path/变换/成员绑定；第66轮增加全模型SHA256核验及不可变快照。Chromium about:blank 43/43，新旧QA 25/25+1/1组，两次独立解压各996/996通过。详情：`docs/evidence/v036-round66-t03-source-bound-renderer.md`（仓库证据，不含ZIP）。T03仍未正式集成、T04真实同源被管理员阻断、T01 0/25，T00–T11 0/12 Accepted。

## 第67轮 T02→T03只读桥接（2026-10-23）

第44/45/46轮156条历史证据与第63轮151条几何草案建立逐实例只读交叉账本；五条关联不渲染。新发现H:6/H:7缺历史Path哈希，草案SVG不得自动转为正式来源绑定。K/E/B/V旧阻断维持。两次独立解压各1006/1006，新增27/27与继承26组QA通过。详见 `docs/evidence/v036-round67-t02-t03-crosswalk.md`。原始T02/T03仍未集成/未验收，T00–T11 0/12 Accepted。

## 第68轮 H:6/H:7 提取部件来源核验（T02→T03）

冻结HTML的`EXTRACTED_COMPONENT_D`为H:6/H:7提供了可重算的历史Path字节与来源元数据，分别对应一条轮廓和三条描边；第33/50/63/67轮来源SHA/草案资产哈希一致。**不改变**第67轮历史`fontGlyphPathHashV035=null`的事实，也不将路径来源等同原图逐笔认证、正式永久ID或已核验分发许可。第68轮ZIP 1016文件，SHA256 `d077e82ea340675759862d156f9bb937c8bbd1833cb49717b9ce71749e877d05`，两种独立解压及新旧QA通过；T02/T03未正式集成，0/12 Accepted。见 `docs/evidence/v036-round68-h-extracted-component-provenance.md`。

## 第69轮 T01→T02 36条未匹配来源证据门禁（非正式验收）

原始JPEG和各键原生裁片对36条历史采框逐像素一致（36/36），但第45轮未对36条建立有效裁框绑定（0/36）；第46轮门禁25仅审阅、8否定阻断、2命名空间阻断、1共享来源阻断。K:3在第43轮历史分类与第46轮新阻断之间的差异已显式保留，K:2/K:3、E:1/E:8、B:7/V:4不可自动提升。累计ZIP1030文件，两种独立解压各1030/1030及新旧QA通过。详情：`docs/evidence/v036-round69-unmatched36-pixel-provenance.md`。正式认证0/25、永久ID正式分配0、原始任务0/12 Accepted。

## 第70轮 T01→T02 全151候选采框原始JPEG证据（非正式验收）

第45轮115暂定裁框及第69轮36历史未绑定框全部从原始JPEG独立重算，151/151与25键PNG逐像素一致；5关联不计独立形态。K:2/K:3和E:1/E:8各为一组同源同框，但仍分别保留共享来源阻断和历史否定；B:7/V:4命名空间阻断不变。新增25/25防篡改QA；父1030/1030继承，累计ZIP1042文件，双重解压及旧QA均通过。详见 `docs/evidence/v036-round70-all151-jpeg-provenance.md`。**没有**原图逐笔认证、正式ID、正式T03集成或T04真同源事务，0/25键、0/12 Accepted。

## 第71轮 原始T01/T05 M键裁框隔离诊断（非验收）

8个M候选裁框两两不重叠，但原生JPEG暗像素连通分量在阈值140/160下同时进入07/08两框，在100/120下不连通，不能据此判定独立字根或笔画归属。新补PNG字节级SHA门禁（修复解码后RGB检查忽略尾部附加字节），新18/18、旧25/25+19/19+16/16+27/27 QA通过；父1042/1042继承，第71轮1053文件双解压各1053/1053。详见 `docs/evidence/v036-round71-m-candidate-boundary-graph.md`。原始T01/T05均未Accepted，M缺根数未知，原始T00–T11 0/12 Accepted。

## 第72轮 T02/T03隔离运行时门禁（非正式验收）

第63轮151 SVG实例、第67轮156身份阻断及第70轮151 JPEG裁框账本首次在同一只读HTML运行时通过SHA256及旧槽、草案资产、inkBBox、几何和视图成员交叉绑定。139仅审阅+12可视阻断+5关联；K/E同框冲突、B/V命名空间阻断继续保留。Chromium about:blank 77/77，父1053/1053继承，累计ZIP1067文件双解压及新旧QA均通过。详见 `docs/evidence/v036-round72-t02-t03-runtime-source-gate.md`。**T02永久ID正式分配0、T03正式内核未集成，T00–T11仍0/12 Accepted；真实同源/真机/读屏not-run。**

## 第73轮 T02→T03候选不透明身份预集成（非验收）

从151个SVG草案与156条来源门禁建立151个一次性随机UUIDv4候选UID、5条关联仅保留别名；候选UID不从旧槽/显示字推导，来源/资产/几何签名绑定。25键插入/删除/重排影子编辑不漂移既有身份或几何；新增97/97 Node QA，继承77/77 Chromium about:blank与18/18+25/25+19/19+16/16+27/27旧QA。第72轮1067/1067继承，第73轮1077文件双解压及解压后QA通过。证据：`docs/evidence/v036-round73-opaque-candidate-uid-shadow.md`。候选UID**不是正式永久ID**，T01 0/25、T02正式分配0、T03正式集成未完成、T00–T11 0/12 Accepted；同源存储blocked，真机/读屏not-run。

## 第74轮 T01/T05 全25键跨框连通风险核验（非正式验收）

151旧可视槽位（5关联排除）在25键内形成409个候选配对；基于原始JPEG/PNG字节SHA与裁框RGB SHA，四档8邻接扫描标记25对（2完全同框、23不相交但共享暗色分量），16持续、9阈值敏感。仅供人工审阅，不解除K/E/B/V来源阻断，不代表M键8新候选已认证。新增34/34 QA与7组旧QA通过，第73轮1077/1077继承，第74轮1088/1088双重独立解压及QA后SHA一致。证据：`docs/evidence/v036-round74-all25-component-ambiguity.md`；正式0/25键、0/12 Accepted，真实同源blocked、真机/读屏not-run。

## 第75轮 Root T04 只读迁移预检（非验收）

旧156条索引坐标经来源SHA与旧身份交叉验证，映射为151个候选UID和5条仅关联隔离记录；合成三条调位3/3无损，其中M:4关联调位单独保留，不提升为正式字根。额外v16_v033/v15_XQU_only合成profile通过；未登记调位漂移被拒绝。新增48/48 Node QA、继承八组QA，父1088/1088继承，第75轮累计1101/1101两次独立解压与QA后SHA通过。证据：`docs/evidence/v036-round75-t04-readonly-uid-migration-preflight.md`。**这不是真实浏览器迁移**：隔离HTTP/Chromium原点探针超时，Web Locks/localStorage事务blocked/not-run；T01 0/25、T02正式ID 0、T04未Accepted，原始T00–T11仍0/12 Accepted。

## 第76轮 T04追踪：Root T04 隔离事务与恢复预演（2026-10-24，非正式验收）

- 继承第75轮1101/1101文件SHA；新增151候选UID+5关联的合成预览两阶段提交，模拟独占锁、日志恢复、回滚、篡改与多模拟tab冲突。新增Node **70/70**、继承 **9/9组**QA通过。
- 第76轮累计ZIP **1111文件**，SHA256 `036d42a90875b30dfc475fbbd4feaccdc2b4a775f6ecf05486f58365db66b76d`；两次独立解压各1111/1111并复跑新旧QA、QA后SHA一致。ZIP不在GitHub，详见 `docs/evidence/v036-round76-t04-isolated-journal.md`。
- 临时127.0.0.1 Chromium profile导航超时、未获得DOM；真实Web Locks/localStorage事务 **blocked/not-run**。真机/读屏not-run；T01 **0/25**、永久ID正式分配0、原始T00–T11 **0/12 Accepted**，生产入口与用户存储未改。

## 第77轮 Root T03/T07前置隔离几何（2026-10-24，非正式验收）

第63轮151草案SVG来源字节SHA门禁下，新增100×100 inkBBox锚点（5种）、ox/oy光学校正、撤销、不可变来源绑定的预览导出导入与同键草案矩形碰撞检查；原transform几何151/151一致。新增179/179 Node QA及旧10/10组QA通过，父1111/1111继承，第77轮1122文件累计ZIP双解压各1122/1122、QA后SHA一致。仅T03隔离代码和T07前置检查，未认证参考图、标签碰撞、永久ID或生产集成；T00–T11仍0/12 Accepted，T01 0/25，真同源/真机/读屏not-run。证据：`docs/evidence/v036-round77-t03-anchor-optical-preview.md`。

## 第78轮 T02/T03 隔离UID与几何适配追踪（2026-10-24）

第73轮151个候选UID与第77轮100×100、inkBBox、五锚点/光学偏移模块已在**隔离运行时**按冻结来源SHA一对一绑定。新增50/50 QA；第77轮11组旧QA继承通过；父ZIP1122/1122文件继承，累计ZIP1131文件、双独立解压1131/1131与复跑通过。详见 `docs/evidence/v036-round78-candidate-uid-geometry-bridge.md`。正式永久ID仍0、T01 0/25、T03正式生产集成未完成，所有T项accepted=false；真实同源/真机/读屏本轮not-run。候选UID不代表原图逐笔认证。

## 第79轮 T04 旧坐标—候选UID几何修订隔离日志（2026-10-24）

第75轮旧156条（151候选UID+5关联隔离）迁移预检、第76轮事务协议与第78轮UID几何预览现由独立FakeStore版本日志贯通；支持多修订、幂等、回滚、模拟并发及崩溃恢复，来源摘要和几何合法性失败关闭。新QA38/38，旧12/12组；父1131/1131继承，累计1141文件、ZIP SHA256 `7da4350b7f2e9fc69500038c8b7e7045450fea31aa60457cc8af77ad94eabddc`，两次独立解压与复跑均通过。证据：`docs/evidence/v036-round79-t04-uid-geometry-revision-journal.md`。**仅Node合成存储，非真实共享原点；T04未Accepted**。T01 0/25、正式永久ID 0、T00–T11 0/12 Accepted；真机/读屏not-run，冻结生产入口未改。

## 第80轮 Root T04 模拟多标签页UID三方合并（2026-10-24）

基于第79轮候选UID几何版本日志，新增共同祖先三方合并：M/K/V不同候选UID的并发调位可保留彼此编辑；同UID分歧、未知祖先、篡改负载失败关闭。仅FakeStore和模拟独占锁；新QA24/24、旧13/13组；父1141/1141继承，累计ZIP1151文件、SHA256 `26285567c81a302cd9dcb9b96bb57a39a8a57110bf98d948a1ff7a8412142185`，双独立解压/QA后SHA一致。证据：`docs/evidence/v036-round80-t04-disjoint-uid-three-way-rebase.md`。真实Web Locks/localStorage事务仍blocked/not-run，正式T04未验收；T01 0/25、T02正式ID 0、T00–T11 0/12 Accepted；真机/读屏not-run。

## 第81轮 Root T01 全25键候选来源位置归并（2026-10-24；非正式验收）

- 基于第80轮父ZIP 1151/1151文件SHA继承，重新核验原始JPEG 151个旧可视裁框与M键8个暂存候选，共159观察记录、153个不同来源裁框位置。M有4个与旧槽完全同框、4个未绑定旧槽；E:1/E:8与K:2/K:3各同框冲突保持阻断。36条旧未绑定与25对跨框风险保持待审。
- 新增25键原生像素审阅清单与M/K/E/B/J/R/X/V重点审阅图；新QA 400/400，继承14/14组旧QA；第81轮累计ZIP1164文件，SHA256 `211e8e0f3c4d5c5808cfaa87969dfa7cbf9d9dd5872a7a6cfad6c77966f0b6f9`，Python zipfile/system unzip双重独立恢复各1164/1164，解压后新旧QA及文件SHA一致。ZIP不在GitHub。
- **153是候选裁框位置数，不是字根数量或认证形态数。** T01正式0/25、T00–T11仍0/12 Accepted，真实缺根数未知；同源高清原图/许可、第10–12与35轮历史包、第12轮20SVG仍缺；真同源存储blocked/not-run，真机/读屏not-run。冻结入口、176编码、正式SVG及用户存储未动。证据：`docs/evidence/v036-round81-t01-25key-source-location-inventory.md`。

## 第82轮 Root T01 原生JPEG审阅草案导出与来源失败关闭（2026-10-24；非验收）

第81轮159条观察及25键位置清单已接入只读单HTML原生JPEG像素工作台；可在原始1536×1086像素上记录ROI和分类草案并导出JSON。独立验证器对JPEG字节SHA、清单SHA、裁框RGB哈希、ROI边界和身份字段失败关闭；不允许草案冒充正式认证。新Chromium about:blank 18/18、新Python负例24/24、继承15组QA通过；父1164/1164 SHA继承，第82轮1181文件双重独立解压及QA后SHA一致，ZIP SHA256 `c1755737b727e6616538a0ade8eaf562fc4c76708aa9331ecf5fcd8a4d369796`。直接`file://`导航blocked；真同源存储、真机/读屏not-run。原始T01 0/25，永久ID正式0，T00–T11 0/12 Accepted。证据：`docs/evidence/v036-round82-t01-native-pixel-review-workstation.md`。

## 第83轮 Root T01 → T05来源草案可信边界（2026-10-24，非验收）

发现第82轮可选来源清单路径存在自洽伪造草案绕过；第83轮隔离门禁固定R81清单/JPEG两份字节SHA，重算159裁框RGB并给ROI附原生像素SHA，Pillow/OpenCV各159/159匹配，353/353新QA和17组继承QA通过。父1181/1181继承、累计1193文件ZIP双恢复及QA后SHA一致。2017年CC BY-SA图仅为独立次级来源元数据，未取得原始二进制，不能用于2008同源逐笔认证。T01 0/25、T02正式永久ID 0、T00–T11 0/12 Accepted；真同源/真机/读屏not-run。证据：`docs/evidence/v036-round83-t01-pinned-source-and-roi-pixel-seal.md`。

## 第84轮 Root T01/T02/T05 · M键4个未绑定来源观察的隔离身份（2026-10-24，非正式验收）

- 真实读取第83轮1193文件累计ZIP，1193/1193逐文件SHA继承；第55轮M键8观察、第81轮来源清单和第73轮151候选UID交叉绑定。M vis-01/02/03/05四个同框观察复用旧UID，vis-04/06/07/08四个未绑定观察获得独立**影子候选UID**，不是4个正式新增字根或正式永久ID；151旧候选UID及5关联项不变。
- 新124/124正负例及第83轮353/353与此前17组QA重新通过；累计ZIP1203文件 SHA256 `9e95931ab39c37261aee085ee66d9e1c9cf763dca3248ce46b7d175736af0956`，Python zipfile和系统unzip双独立解压各1203/1203、QA后SHA一致。ZIP本体不在GitHub，见 `docs/evidence/v036-round84-m-unbound-shadow-candidate-ids.md`。
- 原始T00–T11仍**0/12 Accepted**、T01 **0/25正式认证**、T02正式永久ID **0**，真实缺根数未知。第10–12、35轮ZIP与第12轮20SVG仍缺；同源高清原图未获。独立127.0.0.1 Chromium同源导航`ERR_BLOCKED_BY_ADMINISTRATOR`，真实Web Locks/localStorage **blocked/not-run**；真机/读屏not-run。冻结HTML/176编码/正式SVG/用户存储未动。

## 第85轮 T01/T05 · M键边界来源审计（非验收）

8个M裁框中6个存在跨框暗像素诊断标记，vis-02右、vis-04左优先人工复框；不证明裁框错误或独立字根。父1203/1203继承，新1214文件双解压及定向新旧QA通过，完整继承QA尝试超时。T01正式0/25、T05未正式补图、T00–T11仍0/12 Accepted。证据：`docs/evidence/v036-round85-m-native-border-context.md`。

## 第86轮 Root T01/T05 · M vis-02原生裁框候选修复（2026-10-24）

第85轮1214/1214父成员SHA继承；原生JPEG可视核验发现M vis-02旧框右侧截断可见竖笔，建立向右5像素列的**未批准**候选框及来源哈希，vis-04左侧归属不明继续隔离。新增20/20 QA，5组定向旧QA双恢复通过；累计ZIP1223文件、SHA256 `af6260dbda45957892d844d5af1a2f2a3d494547b1b89f82c774971d2cd3a84a`，Python/unzip双独立恢复与QA后SHA一致。全历史QA not-run，真同源blocked/not-run、真机/读屏not-run。**T01 0/25、T05未正式补图、T00–T11 0/12 Accepted**。证据：[R86](./evidence/v036-round86-m-vis02-unapproved-crop-handoff.md)。

## 第87轮 Root T01/T02/T05 · M来源影子身份到非可渲染候选的隔离桥接（2026-10-24）

以第73/81/84/86轮SHA锁定证据，交叉校验151旧候选UID、5关联隔离、M键4旧UID别名+4未绑定影子UID；4影子均保持source_pending、不可渲染且不具有正式Path/inkBBox/永久ID。R86 vis-02扩框仍仅是未批准证据。新38/38+12/12、继承16组，父1223/1223、累计1236文件双解压各1236/1236与恢复后QA/文件SHA一致。详见 [R87](./evidence/v036-round87-m-source-shadow-nonrenderable-bridge.md)。**不满足T01正式认证、T02永久ID、T03正式内核或T05补图完成；T00–T11 0/12 Accepted。** 真同源blocked、真机/读屏not-run，历史缺口未补。

## 第88轮 T01/T05 K/E冲突来源分区证据（非验收）

2008 JPEG及R81来源清单固定SHA下，K/E 6个独立人工定位ROI经Pillow/OpenCV原生RGB交叉验证；K:2/K:3同框及E:1/E:8失效同框不解除，K:4语义对应风险单列。新增78/78 QA，继承+新增19组；第87轮1236/1236继承、第88轮1243文件ZIP双独立解压各1243/1243，QA后SHA一致。证据：[R88](./evidence/v036-round88-ke-source-roi-collision-review.md)。T01正式0/25，T02永久ID正式0，T05未完成，T00–T11 0/12 Accepted；真同源、真机、读屏not-run。

## 第89轮 T01/T02/T05 K:4异源Path与ROI坐标纠偏（非验收）

历史K:4来源绝对框`[1127,462,24,22]`与R88上下文ROI`[1125,460,29,26]`严格区分，四边额外226原生像素各自SHA封存；冻结V0.35 `〢` Path两竖形与右下来源轮廓差异保留为逐笔待审，不产生正式身份。父1243/1243继承、累计1253文件双解压各1253/1253及各8组QA通过；证据：[R89](./evidence/v036-round89-k4-frozen-path-native-source-crosscheck.md)。T01 0/25、正式永久ID 0、T00–T11 0/12 Accepted；真同源/真机/读屏not-run。

## 第90轮 Root T01/T02/T05 · E来源空间排除（非正式验收）

2008原生JPEG/R81/R88固定SHA下，对E键9个旧槽逐项复核；E:1/E:8共用失效来源框（368像素，5个RGB均值<160，仅描述性），R88上排微形与圈注上下文分别相交240/66像素，不可自动重绑；E:7继续blocked_invalidated。新增82/82 QA，父1253/1253继承，第90轮1270文件ZIP双独立恢复及各9组新旧QA/QA后SHA通过。见 [R90](./evidence/v036-round90-e-invalid-source-spatial-exclusion.md)。**0/25来源认证、0正式永久ID、0/12 Accepted**；同源存储blocked，真机/读屏not-run。

## 第91轮 Root T03 隔离UID→SVG三视图DOM集成（非验收）

R63 Path与R73候选UID经R78来源校验，将内存几何/五锚点/ox/oy编辑实际同步到Chromium full/mini/single SVG `<use>`。新DOM QA27/27、继承十组，父1270/1270 SHA继承、累计1283文件ZIP双解压及恢复后QA/逐文件SHA一致。仅 `about:blank`，不是正式T03生产集成或T09学习引擎全回归。见 [R91证据](./evidence/v036-round91-t03-live-uid-three-view-dom.md)。T00–T11仍0/12 Accepted。

## 第92轮 T03 · DOM成员与资产来源门禁（非正式验收）

R91的全局UID数量检查不能防止SVG href、跨键UID或Path被篡改；R92隔离Chromium中先复现3个漏洞，再加25键逐项成员/顺序、149资产Path/描边及三视图transform一致性验证，修复撤销/导入的内存事务及键帽真实click/Enter/Space绕过包装层的问题。新29/29、R91旧27/27、继承10组；父1283/1283 SHA继承，第92轮1296成员双解压/QA后SHA一致。详见 [R92证据](./evidence/v036-round92-t03-dom-provenance-attestation.md)。正式T03生产集成、来源逐笔认证、真同源存储、真机及读屏仍未验收；T00–T11 0/12 Accepted。

## 第93轮 Root T03 · SVG片段ID全局来源门禁（2026-10-24；非验收）

- Chromium实际复现R92漏洞：在可信defs之前注入同名fragment ID，`<use>.getBBox()`绘制几何被替换，但R92 attest仍通过。R93在整个document检查149规范ID唯一性、`getElementById`指向规范defs节点，并拒绝额外base[href]；非法DOM修改在编辑/切键前失败关闭。
- 新Chromium12/12、R92回归29/29、R91回归27/27、继承10组定向QA通过。第92轮1296/1296逐文件继承，第93轮累计1308文件，SHA256 `ea618a9dffc1e03f5aad5affa63de7a13f1e5d0da75e4059ef5a7b31b8e57480`；Python zipfile/system unzip双独立恢复各1308/1308，恢复后QA/文件SHA一致。ZIP本体不在GitHub，见 [R93证据](./evidence/v036-round93-t03-document-fragment-identity.md)。
- 仍非正式T03生产集成；T01 0/25、T02正式ID 0、T00–T11 0/12 Accepted；真同源/真机/读屏not-run，冻结入口/用户存储未动。

## 第94轮 Root T03 · SVG实际绘制与声明几何的一致性门禁（非验收）

R93允许在可信defs的g上添加transform，使真实Chromium SVG `<use>.getBBox()` 宽82→164却仍attest通过；CSS覆盖Path透明度也可绕过旧门禁。R94以严格SVG属性集合、规范节点身份、computed style和computed transform对照修复。新Chromium 18/18、R91 27/27、R92 29/29、R93 12/12、定向继承10组；第93轮1308/1308继承，第94轮1319成员ZIP SHA256 `2dcbc8880ab8adde82a8693c5c05f163d81c1476763a10d57d925d4a296df4fc`，两次独立解压各1319/1319并复跑QA、后SHA一致。仍仅about:blank隔离，不是逐笔认证、正式T03生产集成或T10真机/读屏验收。见 [R94证据](./evidence/v036-round94-t03-computed-svg-paint-integrity.md)。原始T00–T11 0/12 Accepted。

## 第95轮 Root T01/T02（关联T05）· K键物理来源与旧槽身份分离（非验收）

2008原生JPEG四个K物理ROI独立SHA封存、Pillow/OpenCV交叉验证；5旧槽分账，K:1仅关联，K:2/K:3共享裁框继续阻断，K:3没有独立来源ROI，K:4「〢」与右下原图可见轮廓需逐笔复核，右上圈注未分类。新增仅审阅来源身份仲裁（禁止借框/升级/伪造许可）。新36/36及R81/R86–R94十组定向旧QA；第94轮1319/1319继承，第95轮ZIP1331文件SHA256 `7deea5a9de203a1cefee6f52ca988f7d26c5588b6b0316a68fab42c2b1dd6db0`，双解压与两次QA后SHA均1331/1331。详见 [R95证据](./evidence/v036-round95-k-physical-source-identity-arbitration.md)。**0/25正式来源认证、0正式永久ID、0/12 Accepted**；真同源存储blocked，真机/读屏not-run，缺档与高清原图许可未补齐。

## 第96轮 Root T01/T02 七微形物理来源观察（非验收）

B/J/R/X/V五键7个历史未映射微形ROI已绑定原生JPEG像素SHA与独立**审阅观察ID**，但无正式referenceShapeId/assetId/instanceId；B:7/V:4命名空间阻断维持，重叠旧槽不代表身份同一。父第95轮1331/1331继承，第96轮1340文件双恢复各12组新旧QA通过；详见[第96轮证据](./evidence/v036-round96-seven-microform-source-crosswalk.md)。T01 0/25、T02正式ID 0、T05未补齐、T00–T11 0/12 Accepted；真实同源/真机/读屏not-run。

## 第97轮 Root T07 · 变换后SVG矩形碰撞与stroke边界（非验收）

第94轮隔离HTML真实Chromium DOM的`<use>.getBBox()`不含自身transform，直接使用会把全25键同键409/409对误判为相交；新增CTM变换后BBox审计，完整/mini各151及M单键4实例、每视口824对，两个视口均0个变换后矩形相交。H:7 stroke必须用来源绑定inkBBox单列，不能以Chromium未描边的getBBox认证实际墨迹。R97新旧13组QA在两份独立恢复环境通过；父1340/1340 SHA继承，累计1348文件ZIP SHA256 `bb744069860dd24c51e5fe08a6c81e63ff7b94768c3fae822533a7e8cb08d0d5`双解压1348/1348及QA后SHA一致。见[第97轮证据](./evidence/v036-round97-t07-transformed-svg-bbox-preflight.md)。**T07仍未正式Accepted**，真实笔画/标签/圈注/真机/读屏/同源存储未验收；T00–T11仍0/12 Accepted。

## 第98轮 Root T07 · 屏幕空间stroke/键头/跨键碰撞预检（2026-10-25；非验收）

第97轮1348/1348逐文件SHA继承；R98使用Chromium `getScreenCTM()`把草案inkBBox投影至CSS像素坐标，扩展检查跨键、键头、SVG裁切、键格外溢与H:7描边包络。8视口×DPR1/2/3=24个模拟上下文，7344实例、19776同键及523968跨键配对，隔离草案矩形重叠/越界0；3类主动DOM篡改均被检测。320px完整/mini键格约24.7 CSS px，触控目标风险待真实UI/设备审查。14组新旧QA在两份独立解压环境均通过；累计ZIP1359文件，SHA256 `1e1aeeac3c0dd321f5e2f22d26eb00e133ef6f6ecc7087c46dc3e231155da7ed`，ZIP不在GitHub。见[R98证据](./evidence/v036-round98-t07-screen-space-stroke-header-crosskey.md)。**T07尚未正式集成/认证，T01 0/25、T00–T11 0/12 Accepted**；真同源/真机/读屏未验收，历史缺口未补。
