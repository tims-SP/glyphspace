# 项目状态：GlyphSpace / 字间 V0.36

> **核对日期：2026-10-24**。仓库正式网页仍是V0.35冻结版本；GitHub保留第46轮基线，并登记已独立复验的第89轮隔离累计ZIP（ZIP本体不在GitHub）。这不是已发布的V0.36版本。

## 当前唯一可信发布入口

- `index.html`：V0.35冻结正式学习网页；SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`。
- `preview/v0.36/index.html`：第40轮独立的移动/桌面渐进键盘实验。预览不包含正式完整学习系统，不能替代根目录入口。
- V0.35冻结SVG、176条原编码、真实用户`localStorage`从未获授权修改；文档修复不修改上述资源。


## 第66轮独立进展（非发布、非正式验收）

- 原始**T03**：修复第64轮浏览器适配器未绑定第63轮来源门禁的问题。现在挂载前校验151旧可视实例完整草案模型SHA256，深拷贝并冻结，拒绝路径、stroke、几何、变换、键位成员与旧槽位的意外漂移；不认证原图或永久ID。
- 第66轮累计ZIP **996文件**，SHA256 `29735c2ce105e93c0ad843ff3d894c81329f0808810865d35454e055f8fc3690`；父第65轮981/981逐文件SHA继承一致，Python zipfile与系统unzip两次独立解压各996/996并复跑新旧QA。新Chromium about:blank 43/43，旧QA25/25组通过。ZIP本体不在GitHub，详见 `docs/evidence/v036-round66-t03-source-bound-renderer.md`。
- T04一次性profile+127.0.0.1同源导航被管理员策略阻断（blocked），真实Web Locks/localStorage事务**not-run**；真机/读屏**not-run**。原始T00–T11仍**0/12 Accepted**，T01**0/25**，真实缺根数未知。

## 第65轮独立累计进展（非发布、非正式验收）

- 第65轮ZIP：`字间_V0.36_第六十五轮隔离累计恢复包_继承第64轮_历史缺口未补齐.zip`，**981文件**，SHA256 `f9a61e9cad2022e48e943bead7766c8645ef9c31b69810728f385ede9d27f6c4`；第64轮970/970继承SHA一致，Python zipfile和系统unzip两次独立解压各981/981并复跑新旧QA通过。**GitHub不包含ZIP原始字节**，证据详情见 `docs/evidence/v036-round65-t03-browser-stroke-geometry.md`。
- 原始T03隔离渲染的实际问题：Chromium SVG `getBBox()` 不含stroke，H:07描边草案宽高各低估6.44/100局部单位；新增描边包络与三视图真实DOM核验，Chromium 22/22、独立Python1738/1738、旧浏览器54/54、旧Python1719/1719、继承21/21组通过。**仍未正式集成，不代表字形认证**。
- 第62轮证据SHA遗漏已在提交 `fca24e7b3b5d01031e2be23a3d6e5b8798ff431b` 修复。原始T00–T11仍**0/12 Accepted**；T01仍**0/25**，真实缺根数未知；第10–12、35轮历史缺口仍在；真机、读屏、同源存储QA仍not-run。

## GitHub原有基线档案：第46轮

- 文件：`字间_V0.36_第四十六轮隔离分支恢复包_继承第45轮_缺第35轮及第10至12轮.zip`（**当前公开GitHub仓库未收录此ZIP**）。
- ZIP SHA256：`32c7130983d18965676f643d9fdd5d178047f749d2f0e4676cf7e56a67d7b5ce`。
- **685个文件**，继承第45轮**663/663**逐项SHA一致；最终独立解压**685/685** SHA一致。
- 第46轮新增：T01 **fail-closed来源冲突隔离**，不改变任何正式字形、稳定身份与旧原始证据。**139条仅可人工审阅+2条K新阻断+8条旧提议否定+2条B/V命名空间冲突+5条关联=156**；对应151条历史可视实例。
- K:2「川」和K:3「丨」共同引用`2008-K-vis-03`框(10,69,21,24)；两条审计候选使用资格均已阻断。E:1/E:8空白误框仍失效。身份仍待逐笔确定。
- **测试边界**：第46轮隔离静态/证据门禁26/26、Chromium about:blank审阅20/20及旧回归日志合计10组通过；真浏览器共享原点尝试返回`ERR_BLOCKED_BY_ADMINISTRATOR`，记为**blocked**而非通过。

上述独立档案位于前次交付的文件工作区，本仓库只保存可复制的状态与核验信息；不要对GitHub上不存在的ZIP创建链接。

## 原始字根系统任务：T00–T11（编号已纠正）

| ID | **原始含义** | 当前已知状态 | 正式验收 |
|---|---|---|---|
| T00 | 冻结V0.35基线 | SHA/151旧可视/5关联/176编码源快照与隔离QA存在 | 尚未完成最终版回归 |
| T01 | 参考图25键逐形态清点 | 到第46轮完成候选来源冲突审计 | **0/25键，缺根数未知** |
| T02 | 语义root/variant等分类与永久ID | 156条稳定ID草案 | 未集成，未认证 |
| T03 | **SVG 100×100坐标内核** | 第65轮隔离DOM描边墨迹/锚点/三视图门禁 | **正式内核未集成** |
| T04 | 旧版localStorage迁移、可逆保存 | Node/FakeStore独立演练 | 真实共享原点QA **0** |
| T05 | **原图完整性补图** | M键等风险审计、暂定形态清单 | 未完成正式补图 |
| T06 | 轮廓一致性 | 历史字体/SVG候选路径材料 | 未完成逐笔认证 |
| T07 | 定位与碰撞 | 局部实验与旧位置数据 | 25键完整几何碰撞未验收 |
| T08 | 校准工作台闭环 | 第41–46轮隔离审阅/导入实验 | 正式闭环未集成 |
| T09 | 三视图与输入回归 | V0.35旧版练习引擎仍冻结 | 集成后完整QA未执行 |
| T10 | 全键视觉与真实设备验收 | 隔离Chromium模拟记录 | 真机Android/iOS、真实读屏QA **0** |
| T11 | 单HTML发布冻结 | 无V0.36正式候选 | 未发布 |

**注意：** 第36–40轮文件旧标签“T03/T05”对应**并行UI原型**，不能覆盖上述真正的T03/T05。[两条轨道的映射说明](./14-ui-change-control.md)。

## 并行UI工作流（非T编号）

- UI-01：全屏零主体滚动与界面减法，V0.34有模拟验收，真机/软键盘仍未正式验收。
- UI-02/03：第36–40轮字母键帽、焦点字根放大、分页和视觉层级，有**隔离原型**。
- UI-04：折叠键盘后mini拆字键盘，V0.34有基线；与T09新数据同源集成未完成。
- UI-05：焦点导航和语义实验已做；**真实屏幕阅读器仍未验收**。

## 仍然阻塞

1. 第10–12轮和第35轮完整ZIP、第12轮20个SVG**缺失**；无法声明历史连续归档。
2. 同源高清JPEG**原始字节未取得或合法来源未确认**，小图放大不能生成未存在的笔画。
3. B/J/R/X/V七微形、36旧未匹配与K/E来源冲突尚未逐笔确认；实际缺根未知。
4. 真实共享原点Web Locks/localStorage事务和真实读屏QA均0；导航被管理员策略阻断。
5. T03坐标内核、T05补图、T06–T11尚未全部正式集成与验收。

## 下轮实际执行起点

先核实第46轮ZIP原始字节及其日志，再寻找缺失历史包/高清同源图。优先解决字根身份和永久ID/几何，再进行独立真实同源存储及三视图集成。**未能真实执行的验证标not-run/blocked；不新造“已通过”状态。** 真实任务定义与验收顺序见 [tasks](./tasks/t00-t11.json)、[roadmap](./06-roadmap.md)及[traceability](./11-traceability.md)。

## 第67轮隔离桥接进展（2026-10-23；非验收）

- 原始T02/T03：第44轮156草案、第45轮扩展证据、第46轮来源阻断及第63轮151几何数据实现只读交叉账本。151旧可视+5关联分别保留，**H:6/H:7缺历史Path哈希绑定**，不得将第63轮草案SVG自动视为正式来源资产。
- 第67轮累计ZIP 1006文件，SHA256 `693eea7737e0ae55d819de842214433682e959d6068b6cba5c95deab87b0bafd`；父第66轮996/996逐文件SHA继承一致；Python zipfile及系统unzip两次解压各1006/1006，新增27/27及继承25/25+1/1 QA均通过。ZIP不在GitHub。
- T01正式认证0/25、永久ID正式分配0、T00–T11 Accepted仍0/12；真机/读屏/真实同源存储not-run。详见 `docs/evidence/v036-round67-t02-t03-crosswalk.md`。

## 第68轮 H键提取部件Path来源纠偏（2026-10-23，非正式验收）

- 原始T02→T03：H:6「具头」与H:7「皮头」虽然历史`fontGlyphPathHashV035=null`，但冻结HTML另有`EXTRACTED_COMPONENT_D`来源。第68轮将其与第33/50/63/67轮的Path SHA及草案资产哈希逐项比对，两项均一致；保留历史普通字体Path字段未绑定，不将提取部件来源等同2008原图身份认证。
- 第68轮累计ZIP 1016文件，SHA256 `d077e82ea340675759862d156f9bb937c8bbd1833cb49717b9ce71749e877d05`，继承第67轮1006/1006；Python zipfile与系统unzip两次独立解压各1016/1016，新增16/16、上轮27/27及历史25/25+1/1组QA通过。ZIP本体不在GitHub。
- 许可仍待独立核验；25键原图正式认证0/25，T00–T11仍0/12 Accepted；真实同源存储/真机/读屏not-run。详见 `docs/evidence/v036-round68-h-extracted-component-provenance.md`。

## 第69轮 36条旧未匹配来源像素核验（2026-10-23，非验收）

- 原始T01→T02：36条历史提议裁框从2008原始JPEG字节重算RGB SHA256并与对应键位PNG逐像素比对，36/36一致；但第45轮36条 `sourceCropBox` / `candidateCropRGBSHA256` 均为null，历史裁框**不可升级为正式来源绑定**。
- 第43轮旧分类26待核+8否定+2命名空间冲突；第46轮有效门禁为25仅审阅+8否定阻断+2命名空间阻断+1共享来源阻断（K:3与K:2共享来源）。
- 第69轮累计ZIP1030文件，SHA256 `3459c84bb6eb6c2cdf19c01fcf1a96fe8ac80fee33127ffaf86dddf35cc65d4f`，父第68轮1016/1016继承，两次独立解压各1030/1030，解压后新19/19、旧16/16+27/27+43/43 QA通过；ZIP本体不在GitHub。
- T01正式认证0/25、缺根数未知、T02永久ID正式分配0、原始T00–T11仍0/12 Accepted；真机/读屏/真实同源存储not-run。详见 `docs/evidence/v036-round69-unmatched36-pixel-provenance.md`。

## 第70轮全151旧可视槽位原始JPEG来源核验（2026-10-23；非验收）

- 原始T01→T02：从2008 JPEG原始字节独立重算115条第45轮暂定裁框及36条历史未绑定裁框，151/151与对应键位PNG原生RGB像素一致；另5条为关联项。只证明裁框像素来源，**不证明151个独立字根或逐笔身份**。
- 全156行交叉审计维持K:2/K:3同框共享来源阻断、E:1/E:8历史否定、B:7/V:4命名空间阻断；正式永久ID分配0。
- 第70轮累计ZIP1042文件，SHA256 `9ed222ce9b3f62d22593cf4036fd30f3d859ab4afae7aff14ff648596da40d2a`；父第69轮1030/1030逐文件SHA继承，两次独立解压各1042/1042并重新运行新25/25、旧19/19+16/16+27/27 QA，解压后文件SHA仍一致。ZIP本体不在GitHub，见 `docs/evidence/v036-round70-all151-jpeg-provenance.md`。
- T01仍0/25键正式认证，缺根数未知；原始T00–T11仍0/12 Accepted。真同源存储、真机、读屏not-run；冻结入口及176编码未修改。

## 第71轮 M键候选边界来源风险（2026-10-23；非验收）

- 原始T01/T05：第55轮M键8候选原生像素8邻接图发现07/08在阈值140/160跨框连通、100/120不连通；来源分割对阈值敏感，不能确认笔画独立身份。
- 新增PNG原始字节SHA绑定，修复尾部附加字节仍被解码RGB检查接受的问题；新QA18/18、继承QA25/25+19/19+16/16+27/27。第71轮ZIP1053文件，SHA256 `554a3f58f5398464caead8e4714f4bcaa0804985473f5e9640109fb2661caa66`，父1042/1042继承，Python与系统unzip双重解压各1053/1053并复跑QA；ZIP本体不在GitHub。证据见 `docs/evidence/v036-round71-m-candidate-boundary-graph.md`。
- T01正式认证0/25，真实缺根数未知，T00–T11仍0/12 Accepted；真实同源存储、真机、读屏not-run，冻结生产入口及用户存储未修改。

## 第72轮 T02→T03隔离运行时来源门禁（2026-10-23；非验收）

- 将第63轮151 SVG草案、第67轮156身份门禁、第70轮151 JPEG来源证据在同一隔离HTML内按三份SHA256及旧槽/几何/资产/门禁逐项绑定；139仅审阅、12可视阻断、5仅关联不绘制。原始T02/T03未正式集成。
- 第72轮累计ZIP **1067文件**，SHA256 `7b19740ab91973338e12241ab7fa0ae47f72966eae04758c45db8493cb69f23a`；父第71轮1053/1053继承；Python zipfile与系统unzip两次独立解压各1067/1067、QA后SHA仍一致；Chromium about:blank **77/77**及第71/70/69/68/67轮旧QA均通过。ZIP本体不在GitHub。详见 `docs/evidence/v036-round72-t02-t03-runtime-source-gate.md`。
- 原始T00–T11 **0/12 Accepted**、T01 **0/25**、正式永久ID **0**、真实缺根数未知；真同源存储、真机、读屏均not-run。冻结生产入口/176编码/用户存储未动。

## 第73轮 T02/T03不透明候选UID预集成（2026-10-23；非验收）

- 151个随机UUIDv4候选UID与旧槽别名分离；5条仅关联不赋独立UID，来源/几何/阻断摘要绑定。25键影子插入/删除/重排保持其他候选身份与几何稳定，**不等于正式永久ID分配**。
- 第72轮1067/1067父文件SHA继承，第73轮ZIP1077文件，SHA256 `e7ba8266abb96b716662cd297a1f7b3f27602adcf7ae65d27c49d7d93ee03b7e`；两次独立解压各1077/1077并复跑7组新旧QA（新97/97，旧77/77、18/18、25/25、19/19、16/16、27/27），ZIP不在GitHub。证据：`docs/evidence/v036-round73-opaque-candidate-uid-shadow.md`。
- T01仍0/25键、正式永久ID 0、原始T00–T11仍0/12 Accepted；真实同源导航blocked，真机/读屏not-run；生产入口与用户存储未动。

## 第74轮 Root T01/T05 全25键候选跨框连通风险审计（2026-10-24；非正式验收）

- 从第73轮1077文件累计ZIP逐项继承SHA，核验2008 JPEG与25键PNG原始字节、151个历史候选裁框像素；同键409组配对发现25组需审阅风险（2同框K/E、23跨不相交裁框共享暗色连通分量；16四档持续、9阈值敏感）。**这是审阅线索，不能作为笔画身份认证或根数量统计**。
- 新QA34/34、继承第67–73轮7组QA通过；累计ZIP1088文件，SHA256 `ea5572a037424c333f5d18c02286535a34ed6f69e34320e952f265308240fd7e`，Python zipfile与系统unzip两次独立解压均1088/1088，QA后SHA一致。外部ZIP不在GitHub。详见 `docs/evidence/v036-round74-all25-component-ambiguity.md`。
- T01仍0/25正式认证、真实缺根未知；M新候选07/08风险未解决，K/E/B/V门禁不解除，T00–T11仍0/12 Accepted。同源导航blocked、真实存储not-run，真机/读屏not-run；历史缺第10–12、35轮ZIP及第12轮20SVG，冻结入口/176编码/用户存储未动。

## 第75轮 Root T04 旧坐标→候选UID只读迁移预检（2026-10-24；非验收）

- 以第74轮累计ZIP为父（1088/1088 SHA继承），新增第19–21轮旧156索引坐标负载与第73轮151个候选UID的**只读**桥接；5个仅关联记录独立隔离保留。合成3条调位**3/3**无损，其中1条关联调位未被错误提升；另测V0.33/V0.15旧profile。检测未登记调位的静默漂移。
- 新Node QA **48/48**、含旧QA **9/9组**；累计ZIP **1101文件** SHA256 `f809b54708efa819a1b9e0092a9e48b3458eefb596be0b86e53af24c88228607`；Python zipfile与系统unzip各1101/1101、两次QA后SHA一致。ZIP本体不在GitHub，见 `docs/evidence/v036-round75-t04-readonly-uid-migration-preflight.md`。
- 真实127.0.0.1隔离Chromium profile原点探针**超时**，Web Locks/localStorage真实事务**blocked/not-run**；真机/读屏not-run，用户原有存储未动。T01 **0/25**、正式永久ID **0**、原始T00–T11仍 **0/12 Accepted**。第10–12、35轮历史ZIP及第12轮20SVG仍缺失；冻结生产入口/176编码未修改。

## 第76轮 Root T04 隔离事务与恢复预演（2026-10-24，非正式验收）

- 继承第75轮1101/1101文件SHA；新增151候选UID+5关联的合成预览两阶段提交，模拟独占锁、日志恢复、回滚、篡改与多模拟tab冲突。新增Node **70/70**、继承 **9/9组**QA通过。
- 第76轮累计ZIP **1111文件**，SHA256 `036d42a90875b30dfc475fbbd4feaccdc2b4a775f6ecf05486f58365db66b76d`；两次独立解压各1111/1111并复跑新旧QA、QA后SHA一致。ZIP不在GitHub，详见 `docs/evidence/v036-round76-t04-isolated-journal.md`。
- 临时127.0.0.1 Chromium profile导航超时、未获得DOM；真实Web Locks/localStorage事务 **blocked/not-run**。真机/读屏not-run；T01 **0/25**、永久ID正式分配0、原始T00–T11 **0/12 Accepted**，生产入口与用户存储未改。

## 第77轮 Root T03锚点/光学校正隔离预演（2026-10-24；非验收）

- 第63轮151草案几何经原始JSON SHA锁定，新增五种ink锚点、ox/oy光学校正、单实例移动/撤销、预览SHA导入导出及草案矩形碰撞预检；151/151旧几何与transform反推一致，默认草案墨迹矩形碰撞0对。**不是正式SVG内核集成、逐笔原图或T07完整碰撞验收**。
- 第76轮父ZIP1111/1111逐文件继承，第77轮累计ZIP1122文件SHA256 `314c5dd3033923f20a959a8df8e555e95460d975284f2df72e59528ecb357e2b`；Python zipfile及系统unzip两次独立解压各1122/1122，新增Node 179/179、旧10/10组QA在两次恢复环境均通过，QA后SHA一致。ZIP不在GitHub，见 `docs/evidence/v036-round77-t03-anchor-optical-preview.md`。
- T01仍0/25、永久ID正式分配0、原始T00–T11仍0/12 Accepted；真同源存储本轮not-run（此前管理员阻断），真机/读屏not-run，生产入口与用户存储未动。

## 第78轮 T02/T03 候选UID—100×100几何运行时桥接（2026-10-24；非正式验收）

- 真实读取第77轮累计ZIP（1122文件，SHA256 `314c5dd3033923f20a959a8df8e555e95460d975284f2df72e59528ecb357e2b`），逐文件1122/1122继承；新增独立T02/T03隔离模块：外部几何接口只使用151个不透明候选UID，不再允许旧槽位/历史草案instanceId作为可编辑身份；25键几何、inkBBox、锚点及光学校正绑定第63轮字节SHA与第73轮注册表SHA。**仍非正式永久ID、来源认证或生产集成**。
- 新增50/50 Node QA，继承第77轮11组QA通过；累计第78轮ZIP 1131文件，SHA256 `48fe5a2b6cda30d1ef72ce09454a9ddd78ab55dfdf1d0360f6ccd669cc6e55c9`；Python zipfile和系统unzip各1131/1131独立恢复、两份均重跑12组新旧QA、QA后SHA无变化。ZIP本体不在GitHub。
- T01 0/25，正式永久ID 0，T00–T11 0/12 Accepted。缺第10–12、35轮ZIP与第12轮20 SVG，高清原图及许可未补；真实同源存储、真机、读屏本轮not-run。冻结V0.35、176编码、正式SVG及用户存储未动。证据：`docs/evidence/v036-round78-candidate-uid-geometry-bridge.md`。

## 第79轮 Root T04 候选UID几何修订隔离事务（2026-10-24；非正式验收）

- 将第75轮156条旧坐标映射（151候选UID+5关联隔离）、第76轮事务思想及第78轮UID几何桥接接入可逆多修订日志。FakeStore/模拟锁**专用**，不提供真实localStorage写入适配器；支持模拟两阶段提交、恢复、回滚、并发冲突与来源篡改拒绝。新QA **38/38**，继承 **12/12组**QA通过。
- 第78轮父ZIP **1131/1131**逐文件SHA继承；第79轮累计ZIP **1141文件**，SHA256 `7da4350b7f2e9fc69500038c8b7e7045450fea31aa60457cc8af77ad94eabddc`。Python zipfile与系统unzip两次独立解压各1141/1141、QA后SHA均一致。ZIP本体不在GitHub；见 `docs/evidence/v036-round79-t04-uid-geometry-revision-journal.md`。
- 真实共享原点事务仍**blocked/not-run**，真机/读屏not-run；T01 0/25、正式永久ID 0、T00–T11 **0/12 Accepted**。第10–12、35轮完整ZIP及第12轮20SVG缺失，冻结入口、176编码和用户存储未修改。

## 第80轮 Root T04 隔离候选UID三方合并（2026-10-24，非验收）

- 基于第79轮不可变候选UID几何日志，增加共同祖先三方合并：不同UID过期编辑可安全合并，同UID分歧、未知祖先失败关闭；仅FakeStore/SimulatedExclusiveLocks，不是真实浏览器迁移。
- 第79轮父ZIP1141/1141逐文件SHA继承；第80轮累计ZIP1151文件，SHA256 `26285567c81a302cd9dcb9b96bb57a39a8a57110bf98d948a1ff7a8412142185`；新增Node 24/24及旧13/13组QA通过；Python/system unzip双独立恢复各1151/1151及QA后SHA一致。
- **原始T00–T11仍0/12 Accepted；T01仍0/25，正式永久ID0，真实缺根数未知。** 真同源存储blocked/not-run、真机/读屏not-run。历史第10–12、35轮ZIP及第12轮20SVG缺失；生产入口、原图、176编码和用户存储未修改。证据：`docs/evidence/v036-round80-t04-disjoint-uid-three-way-rebase.md`。

## 第81轮 Root T01 全25键候选来源位置归并（2026-10-24；非正式验收）

- 基于第80轮父ZIP 1151/1151文件SHA继承，重新核验原始JPEG 151个旧可视裁框与M键8个暂存候选，共159观察记录、153个不同来源裁框位置。M有4个与旧槽完全同框、4个未绑定旧槽；E:1/E:8与K:2/K:3各同框冲突保持阻断。36条旧未绑定与25对跨框风险保持待审。
- 新增25键原生像素审阅清单与M/K/E/B/J/R/X/V重点审阅图；新QA 400/400，继承14/14组旧QA；第81轮累计ZIP1164文件，SHA256 `211e8e0f3c4d5c5808cfaa87969dfa7cbf9d9dd5872a7a6cfad6c77966f0b6f9`，Python zipfile/system unzip双重独立恢复各1164/1164，解压后新旧QA及文件SHA一致。ZIP不在GitHub。
- **153是候选裁框位置数，不是字根数量或认证形态数。** T01正式0/25、T00–T11仍0/12 Accepted，真实缺根数未知；同源高清原图/许可、第10–12与35轮历史包、第12轮20SVG仍缺；真同源存储blocked/not-run，真机/读屏not-run。冻结入口、176编码、正式SVG及用户存储未动。证据：`docs/evidence/v036-round81-t01-25key-source-location-inventory.md`。

## 第82轮 Root T01 原生像素逐形态审阅草案（2026-10-24；非正式验收）

- 基于第81轮159观察/25键/153候选裁框，新增隔离单HTML原生JPEG像素工作台、ROI标注与审阅草案JSON导出；新增独立来源/裁框/ROI/永久ID伪造拒绝校验器。**工作台草案不是正式字根认证**。
- 父第81轮ZIP1164/1164逐文件SHA继承；第82轮累计ZIP**1181文件**，SHA256 `c1755737b727e6616538a0ade8eaf562fc4c76708aa9331ecf5fcd8a4d369796`；Python zipfile与系统unzip双独立解压各1181/1181、QA后SHA一致；新Chromium about:blank **18/18**、新Python **24/24**、继承15组旧QA通过。ZIP本体不在GitHub。
- `file://`真实导航本轮实际返回`ERR_BLOCKED_BY_ADMINISTRATOR`，记blocked；真实同源Web Locks/localStorage、真机/读屏not-run。**原始T00–T11仍0/12 Accepted，T01正式0/25，真实缺根数未知**；无合法高清原图、历史第10–12/35轮完整ZIP及第12轮20SVG。冻结入口/176编码/正式SVG/用户存储未动。见 `docs/evidence/v036-round82-t01-native-pixel-review-workstation.md`。

## 第83轮 Root T01来源信任边界修复（2026-10-24；非正式验收）

- 复现第82轮审阅草案验证器在调用方自带伪造清单时可被绕过的来源绑定问题；新增隔离严格验证器固定JPEG与R81清单原始SHA，Pillow/OpenCV两套独立解码器各159/159裁框RGB SHA一致，ROI原生像素签封并拒绝冒充认证。
- 父第82轮1181/1181逐文件继承；第83轮累计ZIP1193文件，SHA256 `d28dec3bc9118b334f0ffdcf724ad307c265b08b2756f3a421bb57d7d3366aa6`；双独立解压各1193/1193，新增353/353和旧17组QA在两份恢复环境通过，QA后SHA一致。ZIP本体不在GitHub。
- 发现Wikimedia Commons一份2017年CC BY-SA 4.0**不同来源**字根图元数据，原件二进制未取得，不是2008同源高清原图。缺第10–12/35轮完整包和第12轮20SVG；同源存储、真机、读屏not-run。
- **T01 0/25正式认证，真实缺根数未知；T02正式永久ID 0；T00–T11 0/12 Accepted。** 冻结入口、176编码、正式SVG、用户存储不变。详见 [第83轮证据](./evidence/v036-round83-t01-pinned-source-and-roi-pixel-seal.md)。

## 第84轮 Root T01/T02/T05 · M键4个未绑定来源观察的隔离身份（2026-10-24，非正式验收）

- 真实读取第83轮1193文件累计ZIP，1193/1193逐文件SHA继承；第55轮M键8观察、第81轮来源清单和第73轮151候选UID交叉绑定。M vis-01/02/03/05四个同框观察复用旧UID，vis-04/06/07/08四个未绑定观察获得独立**影子候选UID**，不是4个正式新增字根或正式永久ID；151旧候选UID及5关联项不变。
- 新124/124正负例及第83轮353/353与此前17组QA重新通过；累计ZIP1203文件 SHA256 `9e95931ab39c37261aee085ee66d9e1c9cf763dca3248ce46b7d175736af0956`，Python zipfile和系统unzip双独立解压各1203/1203、QA后SHA一致。ZIP本体不在GitHub，见 `docs/evidence/v036-round84-m-unbound-shadow-candidate-ids.md`。
- 原始T00–T11仍**0/12 Accepted**、T01 **0/25正式认证**、T02正式永久ID **0**，真实缺根数未知。第10–12、35轮ZIP与第12轮20SVG仍缺；同源高清原图未获。独立127.0.0.1 Chromium同源导航`ERR_BLOCKED_BY_ADMINISTRATOR`，真实Web Locks/localStorage **blocked/not-run**；真机/读屏not-run。冻结HTML/176编码/正式SVG/用户存储未动。

## 第85轮 Root T01/T05 · M键裁框原生边界（2026-10-24，非验收）

- 8个M候选裁框新增原始JPEG内外相邻像素诊断，6/8出现跨框暗像素；vis-02右和vis-04左优先复框，不能自动判定缺根、笔画或SVG。原始裁框/候选UID不变。
- 父第84轮1203/1203 SHA继承；第85轮1214文件ZIP SHA256 `d1bcd4fe6ba44a8efcf6680c6028604380b7875cdcbb3ba950a4134db18628f5`，双独立解压各1214/1214，恢复后定向QA和SHA通过。新45/45，旧R84 124/124、R83 353/353、R82静态24/24、R81 400/400通过；完整继承QA尝试超时，不计pass。
- T01 0/25、正式永久ID0、T00–T11 0/12 Accepted；真实同源存储blocked/not-run，真机/读屏not-run，历史10–12/35轮ZIP与第12轮20SVG及同源高清图仍缺。冻结入口、176编码、正式SVG和用户存储不变。证据：`docs/evidence/v036-round85-m-native-border-context.md`。

## 第86轮 T01/T05 · M vis-02裁框候选修复（2026-10-24，非正式验收）

原始2008 JPEG可视核验表明M vis-02（旧槽M:1）原裁框右侧截断可见竖笔；新增**未批准的证据框提案**[1045,585,26,23]，在原[1045,585,21,23]基础上右延5原生像素列，未改任何正式裁框/UID/SVG。vis-04左侧两点归属仍不明，不自动扩框。新增20/20 QA、旧第81–85轮5组定向QA在两次恢复环境通过；**全量历史QA本轮not-run**。第85轮父ZIP1214/1214继承；第86轮累计ZIP1223文件SHA256 `af6260dbda45957892d844d5af1a2f2a3d494547b1b89f82c774971d2cd3a84a`，Python/system unzip双恢复各1223/1223、QA后SHA一致。ZIP不在GitHub，见 [R86证据](./evidence/v036-round86-m-vis02-unapproved-crop-handoff.md)。T01正式0/25、T02正式永久ID0、T00–T11仍0/12 Accepted；真同源blocked/not-run、真机/读屏not-run，历史ZIP与高清同源原图缺口未解决。

## 第87轮 Root T01/T02/T05 · M键非可渲染影子来源桥接（2026-10-24；非正式验收）

第86轮父ZIP1223/1223 SHA继承，新增隔离模块将第73轮151候选UID、第81轮25键来源、第84轮M键4别名+4影子UID及第86轮未批准vis-02裁框提案按固定原始SHA绑定。4影子观察**无SVG Path、inkBBox、正式assetId/instanceId或可发布几何**，不能当作4个新根；vis-02旧框保持不变。新增Node38/38、原生RGB12/12，继承16组QA；累计ZIP1236文件 SHA256 `c50653e2bb980a289fb0287d7edb05f99d30f3f671112ec86cb39880e366e89f`，Python/system unzip双恢复各1236/1236，恢复后各18组QA与文件SHA通过。ZIP仅在外部交付，不在GitHub。第10–12、35轮历史ZIP/第12轮20SVG仍缺；真实同源导航管理员阻断，Web Locks/localStorage blocked/not-run，真机/读屏not-run。**T01 0/25、正式永久ID 0、T05未补完、T00–T11 0/12 Accepted**。冻结HTML、176编码、正式SVG及用户存储不变。证据：`docs/evidence/v036-round87-m-source-shadow-nonrenderable-bridge.md`。

## 第88轮 Root T01/T05 K/E原生像素冲突审阅（2026-10-24，非正式验收）

第87轮1236/1236父文件SHA继承；从2008 JPEG原始字节为K/E共享来源问题登记6个独立ROI证据框，Pillow/OpenCV RGB交叉一致。K:2/K:3、E:1/E:8共享来源阻断不解除；K:4历史标签与可见右下构形对应仍待分类，圈内区域不得自动算字根。新增78/78 QA、共19组新旧QA；累计ZIP1243文件SHA256 `76690664e16bd08d77bbbc4dda1699df20d1178d51b9ae5ed011ee1d402b5d9a`，Python/system unzip双独立恢复各1243/1243、QA后SHA不变。外部ZIP不在GitHub。**T01 0/25、正式永久ID 0、T05未补完、T00–T11 0/12 Accepted**；真同源/真机/读屏本轮not-run，历史缺口与许可问题未解除。证据：[R88](./evidence/v036-round88-ke-source-roi-collision-review.md)。

## 第89轮 Root T01/T02/T05 · K:4冻结Path与原图来源交叉证据（2026-10-24，非验收）

- 冻结`〢`字体Path为两条竖形，2008原图右下构形的可见底部需逐笔确认；K:4历史绝对框为`[1127,462,24,22]`，不是R88审阅上下文`[1125,460,29,26]`。R88框四边扩展左2/上2/右3/下2，新增226原生像素，已分别SHA封存。**来源差异不能自动判定字根身份。**
- 父第88轮1243/1243继承；新QA51/51、旧第81/83–88轮7组，新旧共8组；第89轮累计ZIP **1253文件**、SHA256 `c9700baf3730fbe1eee234bd5af8cf2e6f10434698b3b0507dd7dd12f3cbb2f0`，Python/system unzip双独立解压各1253/1253、恢复后各8组QA及QA后SHA通过。ZIP不在GitHub。见 [R89](./evidence/v036-round89-k4-frozen-path-native-source-crosscheck.md)。
- **T01正式0/25、T02正式永久ID0、T05未正式补图、T00–T11 0/12 Accepted**；真实缺根数未知；历史缺包、高清许可未解；真实同源/真机/读屏本轮not-run。冻结入口/176编码/正式SVG/用户存储未动。

## 第90轮 Root T01/T02/T05 · E键失效来源空间排除（2026-10-24，非正式验收）

- 原始JPEG/R81清单/R88 ROI三份固定SHA交叉验证E键9个历史可视槽。E:1/E:8共享失效框[452,223,16,23]，368像素仅5个RGB均值<160；E顶部微形/圈注上下文ROI与失效框分别交叠240/66像素，**不能自动重绑**。E:7继续blocked_invalidated，语义未认证。
- 新增只读空间排除门禁及82/82新QA；继承8组历史QA，父第89轮1253/1253继承；累计ZIP1270文件SHA256 `7e694c91b8f424390314ea7e92c3c7819536a14551290cc7ad95fba8aa1d52f2`，Python/system unzip双独立解压1270/1270、两份环境各9组QA及QA后SHA通过。ZIP本体不在GitHub；详见 [R90](./evidence/v036-round90-e-invalid-source-spatial-exclusion.md)。
- T01正式0/25、永久ID正式0、原始T00–T11 **0/12 Accepted**；完整历史QA not-run，真同源存储 blocked/not-run，真机/读屏not-run。历史第10–12、35轮ZIP及第12轮20SVG缺失，合法同源高清原图仍缺。冻结V0.35、176编码、正式SVG及用户存储未修改。
