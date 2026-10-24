# 09 · 历史演化与变更记录

## 2026-10-23 · 第65轮 T03 隔离浏览器描边墨迹门禁（非正式验收）

Chromium SVG `getBBox` 漏计描边，H:07草案宽高各低估6.44；新增真实DOM描边/三视图核验。父ZIP970/970继承，累计ZIP981文件，两次独立解压981/981并复跑QA。T00–T11仍0/12 Accepted，T01 0/25，正式入口不变。详情见 `docs/evidence/v036-round65-t03-browser-stroke-geometry.md`。

> **最新经核验进度第46轮**；原始V0.36任务编号已据[历史任务全文](./history/V0.36-P0-original.md)纠正，后期键盘实验使用独立UI轨道。

> 文档是**可追溯阶段摘要**，不是完整Git变更日志。部分历史ZIP缺失，明确保留空缺。

## 截至2026-10-22

### V0.35（冻结正式入口）

- 练习网页为单文件HTML，包含06版训练逻辑、字根键盘、拆分提示、辅助页面和旧版浏览器设置存储。
- HTML文件SHA256：`fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`。
- 页面内部标题仍含V0.34，不是未冻结或已发布V0.36的证据。

### V0.36早期阶段（隔离数据与来源）

- 第2轮：T00冻结来源快照，保留25键、156实例（151可视+5关联）、176编码的校验结果；开始T01参考图证据链。
- 第3轮：156稳定ID草案。
- 第4–9轮：原图候选与36旧未匹配实例、圈注/误框排除、跨轮采框修正等审计（具体以隔离包记录为准）。
- **不可重建区间**：第10–12轮ZIP、第12轮20 SVG仍缺失；不能声称连续可验。
- 第35轮ZIP亦缺失，影响完整累积链条的证明。

### V0.36交互原型（未正式合并）

- 第36轮：T03/T05渐进键盘独立原型，移动端字母键帽+焦点字根分页。
- 第38–40轮：物理行列、触摸/键盘焦点、无障碍方面的隔离改进。
- 当前仓库 `preview/v0.36/index.html` 继承第40轮实验入口，不是第45轮完整网页。

### V0.36证据审计（持续隔离）

- 第41轮：B/J/R/V/X七未映射微形的原图人工复核工作台。
- 第42轮：严格离线审阅意见导入与全批拒绝校验；意见仅在页面内存。
- 第43轮：36旧实例跨轮来源冲突清单，历史失效8、跨轮冲突2、其他待核26。
- 第44轮：156实例来源交叉账本，151可视=115暂定+36未匹配，5关联独立记账。
- **第45轮**：151/151裁片RGB哈希核验；新增K:2「川」与K:3「丨」引用同一参考候选框的来源冲突；25键审阅图集。正式认证仍0/25。
- 第45轮663文件隔离归档ZIP SHA256：`cddff2926b296fe86d7ef20f52d4b7e8348b3c0e6936c483bd84b651e6079935`。

### GitHub项目建立

- 2026-10-22：仓库 `tims-SP/glyphspace` 首次发布V0.35冻结完整学习HTML、V0.36第40轮交互预览、README与简要进度。
- 本次文档补全：首次系统记录愿景、原则、需求、架构、数据/字根证据、UI、路线图、验收、ADR与Agent规则。**仅文档变更，不代表V0.36功能新增或验证完成。**

## 更新规则

每次新增条目至少说明：日期/提交、变化的**真实对象**、验证方式、尚存风险及是否正式集成。不能以发布了报告或重复阈值测试代替字根认证；缺失的历史包不得由推测补写。

### 第46轮（T01隔离来源审计，不是正式字根发布）

- 实际读取第45轮663文件ZIP，继承663/663 SHA一致；第46轮独立恢复档案共685文件，SHA256 `32c7130983d18965676f643d9fdd5d178047f749d2f0e4676cf7e56a67d7b5ce`。
- 新增K:2「川」/K:3「丨」同一参考候选`2008-K-vis-03`的**双向fail-closed阻断**，保留原证据且不做任何正式字根绑定。
- 分类139人工审阅、2本轮新增阻断、8旧否定、2B/V候选冲突、5关联，合计156条。
- 静态证据门禁26/26，Chromium about:blank静态审阅20/20、旧回归10组记录通过；独立同源导航因管理员策略被阻断，真实多标签事务/读屏没有验收。
- T01正式认证仍0/25键；第10–12和第35轮ZIP/第12轮20SVG缺失。

### 2026-10-22仓库文档错误纠正

- 原始[V0.36-P0 12任务全文](./history/V0.36-P0-original.md)和[V0.35 25键问题总清单](./history/V0.35-root-audit-original.md)被归档到仓库。
- 正式恢复T03 SVG坐标内核、T05完整性补图及T06–T11全量职责；第36–40轮渐进键帽原型划归并行UI-01–UI-05。
- 新增六实体数据架构、25键逐项矩阵、项目证据追踪、Gate A–D用例、许可证溯源规则、自动只读静态校验与CI入口。
- 只修订文档/静态验证工具；冻结V0.35 HTML、176编码、历史SVG及真实用户存储未修改。

## 2026-10-23 · 第66轮（原始T03，隔离原型）

- 新增完整151草案实例来源模型SHA256挂载前门禁和深冻结快照，修复浏览器渲染器可接受被改写Path的缺陷；非正式来源认证。
- 981/981父包继承、996/996双重独立解压，新Chromium 43/43，25组旧QA+1组新QA在两次解压后通过。
- T04一次性同源profile导航被管理员阻断；用户原有存储未接触，正式任务仍0/12 Accepted。

- 2026-10-23 / 第67轮：原始T02/T03隔离来源—身份—几何桥接；发现H:6/H:7历史Path哈希缺口，保留K/E/B/V门禁，27/27新增QA，996/996父继承、1006/1006双解压。证据：`docs/evidence/v036-round67-t02-t03-crosswalk.md`。无正式验收/生产入口变更。

- 2026-10-23 · 第68轮：T02/T03隔离来源纠偏，冻结V0.35中H:6/H:7专用`EXTRACTED_COMPONENT_D`与历史第33/50/63/67轮哈希双向验证，新增16项防篡改QA；累计ZIP1016文件双重独立解压和继承QA通过。非2008原图认证，非正式集成；0/12 Accepted。

- 2026-10-23 · 第69轮：原始T01/T02对36条旧未匹配历史裁框完成原始JPEG→键PNG逐像素哈希复核（36/36）；区分第43轮旧分类与第46轮最新阻断门禁，明确第45轮36条未绑定。累计ZIP1030文件双重独立解压复验及新旧QA通过；不认证任何字根、不修改正式入口，0/12 Accepted。证据：`docs/evidence/v036-round69-unmatched36-pixel-provenance.md`。

- 2026-10-23 · 第70轮：原始T01/T02全151旧可视槽位JPEG原始裁框证据交叉核验（115暂定+36历史未绑定，5关联排除），全156行冲突门禁保持K/E/B/V阻断。新QA25/25、旧19/19+16/16+27/27，父1030/1030 SHA继承，累计1042文件双重独立解压及QA通过。**仅像素来源，不是逐笔或身份认证**；原始T00–T11仍0/12 Accepted。证据：`docs/evidence/v036-round70-all151-jpeg-provenance.md`。

- 2026-10-23 · 第71轮：原始T01/T05隔离M键8候选裁框跨框像素连通图；M:07/08在灰度阈值140/160共享暗色连通分量、100/120不共享，提示低清JPEG采框边界无法自动认证笔画。修复PNG尾部字节篡改未被解码RGB核验拒绝的缺陷；新18/18、旧25/25+19/19+16/16+27/27 QA，父1042/1042继承、累计1053/1053双解压通过。仅来源风险证据，正式0/25键、0/12 Accepted，冻结入口未改。

## 2026-10-23 · V0.36第72轮（Root T02→T03隔离来源门禁）

将151个旧SVG草案实例与156行身份门禁、151行JPEG裁框来源账本在同一隔离三视图HTML内做运行时来源SHA/旧槽/几何一致性核验，12可视阻断实例淡化、5关联不渲染；Chromium about:blank 77/77，继承旧QA通过；第71轮1053/1053继承，第72轮累计1067文件、两次独立解压及QA后SHA一致。未正式集成或认证；0/12 Accepted。证据：`docs/evidence/v036-round72-t02-t03-runtime-source-gate.md`。

## 2026-10-23 · 第73轮 Root T02/T03 隔离候选身份预集成

新增151个一次性随机不透明候选UID及来源/几何绑定，5关联不提升，25键影子插入/删除/重排保持已有身份与几何；新97/97 Node QA、旧77/77+18/18+25/25+19/19+16/16+27/27 QA。父1067/1067继承，累计ZIP1077文件双重独立解压及复跑QA通过。证据`docs/evidence/v036-round73-opaque-candidate-uid-shadow.md`。非正式永久ID，未改生产入口/存储，0/12 Accepted。

## 2026-10-24 · 第74轮 Root T01/T05 25键跨框连通风险审计

在2008冻结JPEG、25键原生PNG和151历史裁框字节/像素校验基础上，新增409组候选对的4阈值8邻接审阅：25组风险（K/E两组同框、23组跨框连通，16持续、9敏感）。这是低清来源的风险定位，不认证任何形态、不推断缺根数。新增34/34 QA、继承7组QA，父1077/1077逐文件SHA继承，累计1088文件双重独立解压及QA后SHA一致；真实同源blocked、真机/读屏not-run，0/25键、0/12 Accepted。证据：`docs/evidence/v036-round74-all25-component-ambiguity.md`。

## 2026-10-24 · 第75轮 Root T04 隔离旧坐标→候选UID迁移预检

新增156旧记录到151候选UID+5关联隔离的只读、来源绑定桥接；合成3条调位全部保留（含1条关联调位隔离），V0.33/V0.15旧profile通过；拒绝未登记坐标漂移。新增48/48 QA，继承八组QA；父1088/1088逐文件继承、累计ZIP1101文件Python/system unzip两次独立解压及QA后SHA均一致。真实同源探针超时，事务blocked/not-run；未接触用户存储。证据：`docs/evidence/v036-round75-t04-readonly-uid-migration-preflight.md`。正式T00–T11仍0/12 Accepted。

## 2026-10-24 · 第76轮 Root T04 隔离事务与恢复预演（2026-10-24，非正式验收）

- 继承第75轮1101/1101文件SHA；新增151候选UID+5关联的合成预览两阶段提交，模拟独占锁、日志恢复、回滚、篡改与多模拟tab冲突。新增Node **70/70**、继承 **9/9组**QA通过。
- 第76轮累计ZIP **1111文件**，SHA256 `036d42a90875b30dfc475fbbd4feaccdc2b4a775f6ecf05486f58365db66b76d`；两次独立解压各1111/1111并复跑新旧QA、QA后SHA一致。ZIP不在GitHub，详见 `docs/evidence/v036-round76-t04-isolated-journal.md`。
- 临时127.0.0.1 Chromium profile导航超时、未获得DOM；真实Web Locks/localStorage事务 **blocked/not-run**。真机/读屏not-run；T01 **0/25**、永久ID正式分配0、原始T00–T11 **0/12 Accepted**，生产入口与用户存储未改。

## 2026-10-24 · 第77轮 Root T03 100×100锚点与光学校正隔离内核

新增来源字节SHA绑定的151实例草案几何内核、五种ink锚点、独立光学偏移、预览撤销及签名导入导出；增加T07草案矩形碰撞前置检查（默认0对，合成移动可检出）。新增179/179 QA、继承10/10组QA；父1111/1111继承，累计ZIP1122文件，两种独立解压各1122/1122并复跑QA后SHA一致。非正式生产集成/原图认证；真同源/真机/读屏not-run，T01 0/25、T00–T11 0/12 Accepted。证据：`docs/evidence/v036-round77-t03-anchor-optical-preview.md`。

### 2026-10-24 · 第78轮（T02/T03隔离候选UID几何桥接）

- 在隔离模块中将151候选UID绑定第77轮100×100 inkBBox/锚点/光学校正内核；外部API拒绝旧索引和草案ID，导入失败保持原预览不变。未认证形态不升级。
- 新增50/50测试、继承11组旧QA；第77轮父包1122/1122 SHA继承；累计1131文件，ZIP SHA256 `48fe5a2b6cda30d1ef72ce09454a9ddd78ab55dfdf1d0360f6ccd669cc6e55c9`；两次独立解压与新旧QA通过。
- T00–T11 0/12 Accepted；T01 0/25；真实同源、真机、读屏not-run。生产HTML及用户存储未动。

## 2026-10-24 · 第79轮 Root T04 候选UID几何隔离修订日志

第75轮151候选UID+5关联的旧坐标迁移计划与第78轮几何预览首次通过可逆版本日志连接；新增仅FakeStore可用的两阶段提交、模拟并发/故障恢复、版本回滚、上下文SHA和非法UID/认证拒绝。新增38/38 Node QA、继承12/12组QA；父1131/1131逐文件继承，累计1141文件ZIP SHA256 `7da4350b7f2e9fc69500038c8b7e7045450fea31aa60457cc8af77ad94eabddc`，双独立解压与QA后SHA通过。真实同源blocked/not-run、真机/读屏not-run；原始T00–T11仍0/12 Accepted。详见 `docs/evidence/v036-round79-t04-uid-geometry-revision-journal.md`。

## 2026-10-24 · 第80轮 Root T04 隔离候选UID三方合并

第79轮日志上的过期模拟标签页编辑现在可按共同祖先进行三方合并：不同UID保留彼此修改，同UID分歧/未知祖先拒绝。新增24/24 Node QA，继承13/13组旧QA；父1141/1141 SHA继承，累计1151文件ZIP SHA256 `26285567c81a302cd9dcb9b96bb57a39a8a57110bf98d948a1ff7a8412142185`，双独立解压及QA后SHA一致。仅FakeStore模拟，不代表真实同源存储、原图或正式T04验收；T00–T11仍0/12 Accepted。证据：`docs/evidence/v036-round80-t04-disjoint-uid-three-way-rebase.md`。

## 第81轮 Root T01 全25键候选来源位置归并（2026-10-24；非正式验收）

- 基于第80轮父ZIP 1151/1151文件SHA继承，重新核验原始JPEG 151个旧可视裁框与M键8个暂存候选，共159观察记录、153个不同来源裁框位置。M有4个与旧槽完全同框、4个未绑定旧槽；E:1/E:8与K:2/K:3各同框冲突保持阻断。36条旧未绑定与25对跨框风险保持待审。
- 新增25键原生像素审阅清单与M/K/E/B/J/R/X/V重点审阅图；新QA 400/400，继承14/14组旧QA；第81轮累计ZIP1164文件，SHA256 `211e8e0f3c4d5c5808cfaa87969dfa7cbf9d9dd5872a7a6cfad6c77966f0b6f9`，Python zipfile/system unzip双重独立恢复各1164/1164，解压后新旧QA及文件SHA一致。ZIP不在GitHub。
- **153是候选裁框位置数，不是字根数量或认证形态数。** T01正式0/25、T00–T11仍0/12 Accepted，真实缺根数未知；同源高清原图/许可、第10–12与35轮历史包、第12轮20SVG仍缺；真同源存储blocked/not-run，真机/读屏not-run。冻结入口、176编码、正式SVG及用户存储未动。证据：`docs/evidence/v036-round81-t01-25key-source-location-inventory.md`。

## 2026-10-24 · 第82轮 Root T01 原生像素证据草案工具

新增25键/159观察原始JPEG像素定位、ROI标注、非正式审阅JSON导出及独立失败关闭验证器；不发布源图到GitHub，不更改生产资产或用户存储。新增Chromium about:blank 18/18、Python负例24/24、继承15组旧QA；父1164/1164继承，累计ZIP1181文件、SHA256 `c1755737b727e6616538a0ade8eaf562fc4c76708aa9331ecf5fcd8a4d369796`，Python/system unzip双恢复QA及SHA通过。`file://`被管理员策略阻断；T01仍0/25，原始T00–T11仍0/12 Accepted。见 `docs/evidence/v036-round82-t01-native-pixel-review-workstation.md`。

## 2026-10-24 · 第83轮 Root T01来源清单固定与ROI像素签封

复现第82轮隔离审阅草案可选清单伪造绕过，新增严格原始JPEG与R81清单SHA固定、159条原生RGB裁框复算、ROI原生像素签封与许可/认证冒充拒绝；Pillow/OpenCV各159/159一致，353/353新增QA、17组旧QA通过。父1181/1181继承，累计ZIP1193文件、SHA256 `d28dec3bc9118b334f0ffdcf724ad307c265b08b2756f3a421bb57d7d3366aa6`，双独立解压及QA后SHA通过。独立CC BY-SA 2017图只发现元数据，未获得原件，不能替代2008同源高清。T01仍0/25，T00–T11仍0/12 Accepted；同源存储/真机/读屏not-run。证据：`docs/evidence/v036-round83-t01-pinned-source-and-roi-pixel-seal.md`。

## 第84轮 Root T01/T02/T05 · M键4个未绑定来源观察的隔离身份（2026-10-24，非正式验收）

- 真实读取第83轮1193文件累计ZIP，1193/1193逐文件SHA继承；第55轮M键8观察、第81轮来源清单和第73轮151候选UID交叉绑定。M vis-01/02/03/05四个同框观察复用旧UID，vis-04/06/07/08四个未绑定观察获得独立**影子候选UID**，不是4个正式新增字根或正式永久ID；151旧候选UID及5关联项不变。
- 新124/124正负例及第83轮353/353与此前17组QA重新通过；累计ZIP1203文件 SHA256 `9e95931ab39c37261aee085ee66d9e1c9cf763dca3248ce46b7d175736af0956`，Python zipfile和系统unzip双独立解压各1203/1203、QA后SHA一致。ZIP本体不在GitHub，见 `docs/evidence/v036-round84-m-unbound-shadow-candidate-ids.md`。
- 原始T00–T11仍**0/12 Accepted**、T01 **0/25正式认证**、T02正式永久ID **0**，真实缺根数未知。第10–12、35轮ZIP与第12轮20SVG仍缺；同源高清原图未获。独立127.0.0.1 Chromium同源导航`ERR_BLOCKED_BY_ADMINISTRATOR`，真实Web Locks/localStorage **blocked/not-run**；真机/读屏not-run。冻结HTML/176编码/正式SVG/用户存储未动。

## 2026-10-24 · 第85轮 Root T01/T05 M键裁框边界审计

新增8个M候选的原生JPEG跨框暗像素坐标与4px上下文RGB签封；6/8有诊断标记，不自动扩框/分根/认证。新增45/45及定向继承R84/R83/R82/R81 QA通过，完整继承QA尝试超时。父1203/1203继承，新ZIP1214文件SHA256 `d1bcd4fe6ba44a8efcf6680c6028604380b7875cdcbb3ba950a4134db18628f5`，双独立恢复及QA后SHA一致。T01 0/25、T00–T11 0/12 Accepted。见 `docs/evidence/v036-round85-m-native-border-context.md`。

## 2026-10-24 · 第86轮 Root T01/T05（非验收）

原始2008 JPEG M vis-02旧框右侧截断可见竖笔，新增向右5原生像素列的**未批准**来源裁框提案与哈希门禁；vis-04左侧像素归属不明，保留原框。新增20/20 QA，继承5组定向旧QA；父1214/1214继承、累计ZIP1223文件、SHA256 `af6260dbda45957892d844d5af1a2f2a3d494547b1b89f82c774971d2cd3a84a`，双独立解压各1223/1223及QA后SHA一致。未修改冻结HTML、176编码、正式SVG/裁框/UID/用户存储；全量历史QA本轮not-run，T01 0/25、T00–T11 0/12 Accepted。证据：`docs/evidence/v036-round86-m-vis02-unapproved-crop-handoff.md`。

## 2026-10-24 · 第87轮 Root T01/T02/T05 隔离来源影子桥接

将151旧候选UID、M键4旧UID别名/4未绑定影子UID、25键来源清单与R86未批准裁框证据接入固定SHA只读模块，增加纯内存笔记的防冒充导入/导出。影子候选**不生成SVG、不分配正式永久ID、不可渲染**。新增38/38 Node+12/12 RGB QA，16组继承QA；父1223/1223继承，新累计ZIP1236文件 SHA256 `c50653e2bb980a289fb0287d7edb05f99d30f3f671112ec86cb39880e366e89f`，两次独立解压及恢复后18组QA/文件SHA均通过。真实同源blocked、真机/读屏not-run；正式T01 0/25、T00–T11 0/12 Accepted。见 [R87](./evidence/v036-round87-m-source-shadow-nonrenderable-bridge.md)。

## 2026-10-24 · 第88轮（原始T01/T05，隔离证据）

- 新增K/E六ROI原生JPEG来源位置与像素SHA/Pillow-OpenCV交叉核验；保留K/E同框阻断，K:4右下可见形态语义对应待审，不修改正式字形。
- 新QA78/78，19组继承与新增QA；父1236/1236，累计ZIP1243文件、SHA256 `76690664e16bd08d77bbbc4dda1699df20d1178d51b9ae5ed011ee1d402b5d9a`，双解压和QA后SHA通过。外部ZIP不在GitHub；T00–T11仍0/12 Accepted。

## 2026-10-24 · 第89轮（原始T01/T02/T05，隔离来源纠偏）

- 交叉比对冻结K:4 `〢` Path与2008 JPEG右下来源构形；纠正R88 ROI不等于K:4历史框的坐标误认，四边新增226原生像素签封，保持来源认证阻断。
- 新QA51/51、继承7组；父1243/1243，累计ZIP1253文件 SHA256 `c9700baf3730fbe1eee234bd5af8cf2e6f10434698b3b0507dd7dd12f3cbb2f0`，双独立解压/恢复后8组QA与SHA通过。证据：[R89](./evidence/v036-round89-k4-frozen-path-native-source-crosscheck.md)；T00–T11仍0/12 Accepted。

## 2026-10-24 · 第90轮（原始T01/T02/T05，E键失效来源空间排除）

- 逐项复核E键9个旧可视槽，固定2008 JPEG/R81/R88来源SHA，E:1/E:8同框失效与E:7圈注语义阻断保持；新增邻接ROI交叠证据，不自动修正历史框。
- 新QA82/82、继承8组；父1253/1253继承，累计ZIP1270文件 SHA256 `7e694c91b8f424390314ea7e92c3c7819536a14551290cc7ad95fba8aa1d52f2`；Python/unzip两次独立解压及QA后1270/1270 SHA通过。完整历史QA未运行。详见 [R90](./evidence/v036-round90-e-invalid-source-spatial-exclusion.md)；原始T00–T11仍0/12 Accepted。

## 2026-10-24 · 第91轮 原始T03候选UID几何与三视图SVG DOM隔离贯通

第64/66轮三视图Path渲染与第77/78轮UID锚点/光学校正合并为真实Chromium SVG DOM编辑；100×100来源SHA门禁，三视图同UID transform同步和原子回滚。新QA27/27、旧十组定向QA，父1270/1270继承、1283文件ZIP双解压复验。仅隔离技术证据，T03未Accepted、真同源/真机/读屏未运行。见 [R91证据](./evidence/v036-round91-t03-live-uid-three-view-dom.md)。

## 2026-10-24 · 第92轮（Root T03；隔离非验收）

- Chromium实证R91允许伪造SVG href、跨键UID替换和Path修改仍通过全局数量门禁；R92新增严格逐键/资产/Path/transform审计及原子内存导入/撤销，真实click/Enter/Space统一经过包装层。
- 新29/29 Chromium、旧R91 27/27、旧10组QA通过；父1283/1283继承、累计1296成员两种解压和QA后SHA一致。ZIP不在GitHub。详见 [R92](./evidence/v036-round92-t03-dom-provenance-attestation.md)。
- 原始T00–T11仍0/12 Accepted；冻结正式入口/旧编码/用户存储不变。

## 2026-10-24 · 第93轮（Root T03，隔离非验收）

R92文档级SVG fragment ID冲突漏洞经Chromium真实绘制包围盒复现，R93加入全document唯一ID/规范defs解析和base[href]门禁。新12/12、R92 29/29、R91 27/27及继承10组定向QA通过；父1296/1296继承、累计1308文件双恢复与QA后SHA一致。证据：[R93](./evidence/v036-round93-t03-document-fragment-identity.md)。正式T03仍未集成，T00–T11 0/12 Accepted。

## 2026-10-24 · 第94轮（Root T03，隔离SVG实际绘制来源门禁）

- 复现R93实际Chromium `<defs><g transform=scale(2)>` 使getBBox宽82→164仍通过attest，以及CSS Path opacity=0未被察觉；新增节点属性/身份、computed paint/transform检查。
- 新18/18、R91 27/27、R92 29/29、R93 12/12、继承10组QA通过；父1308/1308继承、累计1319文件ZIP SHA256 `2dcbc8880ab8adde82a8693c5c05f163d81c1476763a10d57d925d4a296df4fc`，双恢复和QA后SHA一致。ZIP本体不在GitHub。证据：[R94](./evidence/v036-round94-t03-computed-svg-paint-integrity.md)。正式T03未集成、T00–T11仍0/12 Accepted。

## 2026-10-24 · 第95轮（Root T01/T02，K键物理来源身份仲裁）

- 新增4个原生JPEG K物理ROI与5旧槽分离的可复验审计；K:3没有独立来源ROI，K:2/K:3继续双阻断；K:4冻结「〢」来源差异及圈注语义未解决。隔离仲裁拒绝借框、非法认证/许可/ID提升；不产生正式SVG或永久ID。
- 新QA36/36、R81/R86–R94十组定向旧QA通过；父1319/1319 SHA继承，累计ZIP1331文件SHA256 `7deea5a9de203a1cefee6f52ca988f7d26c5588b6b0316a68fab42c2b1dd6db0`，Python/unzip双独立恢复各1331/1331且QA后SHA一致。完整历史QA not-run；真实同源浏览器导航blocked，真机/读屏not-run。证据：[R95](./evidence/v036-round95-k-physical-source-identity-arbitration.md)。T00–T11仍0/12 Accepted。

## 2026-10-24 · 第96轮（隔离来源账本，非发布）

Root T01/T02（关联T05）：对B/J/R/X/V七个微形建立原始JPEG来源锚定的独立物理观察ID；新增旧槽裁框交叠交叉账本，保留B:7/V:4阻断。新增35/35 QA、旧11组、双独立恢复1340/1340；不认证字根、不改冻结入口。详见[证据](./evidence/v036-round96-seven-microform-source-crosswalk.md)。

## 2026-10-24 · 第97轮隔离T07 CTM碰撞预检

真实Chromium确认直接`use.getBBox()`产生同键409/409对假碰撞，独立修正为CTM映射；两视口各306实例、824对，转换后0矩形相交，H:7描边单列。父1340/1340继承，累计1348文件ZIP SHA256 `bb744069860dd24c51e5fe08a6c81e63ff7b94768c3fae822533a7e8cb08d0d5`，双独立恢复各13组新旧QA及文件SHA通过。非生产/非来源认证，正式T00–T11仍0/12 Accepted。见[证据](./evidence/v036-round97-t07-transformed-svg-bbox-preflight.md)。

## 2026-10-25 · 第98轮 Root T07屏幕坐标碰撞检查（非验收）

新增真实Chromium CSS屏幕坐标的跨键、字母键头、SVG/键格边界与H:7草案stroke包络检查；24个模拟视口/DPR上下文，3类篡改负例。父R97 1348/1348继承、R98累计1359/1359双恢复及各14组定向QA通过。320px隔离完整键盘键格仅约24.7 CSS像素，标记触控风险。正式T07/源图/真机/读屏/同源存储仍未验收。见[R98证据](./evidence/v036-round98-t07-screen-space-stroke-header-crosskey.md)。
