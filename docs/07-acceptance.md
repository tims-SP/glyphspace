# 07 · V0.36验收标准：原始T00–T11 + UI-track

**R164 Root T00/T01/T02（原始R10历史ZIP真实恢复，非验收）：** 从Library取得原始第10轮ZIP 11,133,720字节，SHA `6a1552b45cfa3512d9fea2ab06df740a6adbb4b598369cd3ea8e214fee1c0ed0`，184/184原始成员与冻结HTML/JPEG SHA一致；与R163累计包同路径137一致、6同名历史字节不同、41原先缺失，保留原始ZIP嵌套不覆盖。R10 15证据=8暂映射+7未映射、8采框触边；7未映射标签与R96七微形7/7相符，均未认证。新增只读45/45、继承选定2143/2143，R163父2039/2039 SHA继承；R164累计ZIP2048文件SHA `ba42015efe35b702796266f23a458cf25fbf11e3a77bc4c56d3373eb678ec17a`，Python/unzip双独立恢复各2048/2048 SHA与2188/2188定向QA、QA后SHA不变。**R10不再缺失，仍缺R11/R12/R35及R12 20SVG**；完整历史全量/真同源/真机/读屏本轮not-run，正式T00–T11 0/12 Accepted、T01 0/25、正式ID0；冻结入口与用户存储未动。[R164证据](./evidence/v036-round164-t01-original-r10-archive-recovered.md)。

**R163 Root T03（隔离三视图DOM绘制预集成、非验收）：** 将R162 SHA绑定151草案SVG计划连接为full/mini/focus三种外部尺寸，共用100×100 viewBox、ID、Path和矩阵；仅返回detached DOM，拒绝getter/非法绘制/伪认证。真实Chromium about:blank DPR1/2共6组、900项fill DOM解析式BBox及156项alpha栅格采样通过；Node新增20/20、继承选定2117/2117、合计2143/2143。R162父2028/2028逐文件SHA继承，R163累计ZIP2039文件SHA `4a20d2335cb9f0fd557dd86d3a7b533d15a284467f3c42dd54fe97b0be56efc0`；Python/unzip双独立恢复各2039/2039 SHA、2143/2143 QA，QA后SHA不变。正式T00–T11仍0/12 Accepted、T01 0/25、正式ID0、T03未生产集成；R10–12/R35及R12 20SVG仍缺，高清合法原图/逐笔/真机/读屏/真实同源/完整历史全量本轮未通过或not-run，冻结入口与用户存储未动。[R163证据](./evidence/v036-round163-t03-three-view-source-bound-dom-renderer.md)。

**R162 Root T03（隔离实际绘制、非验收）：** 新增151草案实例SHA绑定的100×100 SVG安全绘制描述符；真实Chromium about:blank DPR2/3各151实例、153 Path，302次alpha墨迹及300次fill DOM解析式bbox核验通过，最大像素边缘误差0.49/0.33067 CSS px（非原图认证）。新增Node14/14、继承选定2101/2101、浏览器2/2；父R161 2016/2016 SHA继承，新ZIP2028文件SHA `bb5a007aed51cba3ff5b9391eca3d9bd9c21b7f3d64cf91db3f06a5bcecbcd96`；Python/unzip双独立恢复各2028/2028 SHA、2117/2117定向QA，QA后SHA不变。正式0/12 Accepted、T01 0/25、永久ID0、T03未生产集成；缺R10–12/R35和20SVG、高清许可/逐笔阻断不变；真实同源/真机/读屏/历史全量本轮not-run，冻结入口及用户存储不变。[R162证据](./evidence/v036-round162-t03-chromium-source-bound-svg-paint.md)。

**R161 Root T03（关联T08隔离预检、非验收）：** 新增151草案实例来源Path+真实解析式inkBBox+坐标/锚点/光学偏移的逐实例SHA256见证与变更影响清单；单实例调位仅该项签名过期，重排不变。新Node18/18、继承选定2083/2083；父R160 2007/2007逐文件SHA继承，新累计ZIP2016文件SHA `97327e64f2ac290edfe557fc3736b0c4c5855add2fec71735d0fdc685db65c4c`；Python/unzip双独立恢复各2016/2016 SHA与2101/2101定向QA、QA后SHA不变。完整历史全量/真实同源/真机/读屏本轮not-run；正式T00–T11仍0/12 Accepted，T01 0/25、正式ID0、T03未生产集成，缺R10–12/R35及20SVG、高清许可/逐笔阻断不变。冻结入口/176编码/用户存储未动。[R161证据](./evidence/v036-round161-t03-draft-geometry-change-witness.md)。

**R160 Root T03（隔离、非验收）：** 将R125三份SHA绑定真实冻结Path/解析式矢量inkBBox/151草案目录与R159数据描述符快照连接，建立151完整、路径SHA绑定、拒绝getter/身份漂移/未批准认证的不可变预集成计划。新Node30/30、旧选定2053/2053；父R159 1997/1997 SHA继承，新累计ZIP2007文件SHA `50892db856dbc26c52d9b18d330f818ee4fd391ed526ca2e861d780cabccaa6b`，Python/unzip双恢复各2007/2007 SHA与2083/2083定向QA、QA后SHA不变。完整历史全量QA/真实同源/真机/读屏本轮not-run；T00–T11 0/12 Accepted、T01 0/25、正式ID0、T03未生产集成；缺R10–12/R35及20SVG、高清许可/逐笔未解决，冻结入口/用户存储不变。[R160证据](./evidence/v036-round160-t03-source-bound-151-vector-snapshot.md)。


**R159 Root T03（隔离、非验收）：** 实际复现R154重复读取instanceId的getter TOCTOU：校验`validated`而注册`UNVALIDATED`。新增自有数据属性快照适配层，拒绝getter/继承字段，151草案几何与R154一致。新35/35、继承选定2018/2018；父R158 1987/1987 SHA继承，新累计ZIP1997文件SHA `27aaf806a767888c586feddd805a9253c7dab3d6088fd6603edea46188cccac6`，Python/unzip双恢复各1997/1997 SHA及2053/2053选定QA（QA后SHA不变）。完整历史全量QA/真同源/真机/读屏本轮not-run；T00–T11 0/12 Accepted，T01 0/25，正式ID0，T03未生产集成；缺R10–12/R35和20SVG、高清许可未解决，冻结入口/用户存储不变。[R159证据](./evidence/v036-round159-t03-accessor-snapshot-identity.md)。


**R158 Root T01/T02/T05（隔离、非验收）：** 从冻结2008 JPEG原始字节独立复算170/170原生RGB来源见证，生成12个无旧槽精确绑定裁框+2组E/K旧槽同框冲突的14张无损上下文复核卡与审阅图谱；K圈注/M小框/VX交叠/E空白框均保持待逐笔仲裁，不批准正式根或永久ID。新增81/81、继承选定1937/1937，Python/unzip双恢复各1987/1987 SHA、2018/2018选定QA且QA后SHA不变；父R157 1961/1961 SHA继承，新累计ZIP1987文件SHA `c0a439161e9d4745e941e120d38d763a8abe520abfa86bfea20e38aaf9bd8966`。完整历史全量QA/真同源/真机/读屏本轮not-run，T00–T11 0/12 Accepted、T01 0/25、正式ID0、真实缺根数未知；缺R10–12/R35及20SVG，合法高清许可未解决，冻结入口/用户存储未动。[R158证据](./evidence/v036-round158-t01-t02-native-14card-source-review.md)。

**R157 Root T02（隔离、非验收）：** 151旧可视槽→149不同原生裁框，E:1/E:8、K:2/K:3两组旧槽同框歧义；161个来源裁框中12个无旧槽精确绑定（M4/K1/B1/J1/R1/V2/X2），其中5个与旧槽局部ROI相交、7个不相交；这**不是12个已确认缺根**，不合并旧槽或批准永久ID。新36/36、继承选定1901/1901；父R156 1951/1951 SHA继承，新ZIP1961文件SHA `1c9d625892f1ae1fe3e761392862d793e574f51b02904c6bfba5b542e30ea070`，Python/unzip两套恢复各1961/1961 SHA、1937/1937选定QA且QA后SHA不变。完整历史全量QA、真机/读屏/真实同源本轮not-run；T00–T11仍0/12 Accepted，T01 0/25，正式ID0，历史缺包和许可/逐笔阻断不变。[R157证据](./evidence/v036-round157-t02-legacy-source-binding-ambiguity.md)。


**R156 非验收证据：** 170条来源观察对应161个不同原生JPEG裁框，8组精确同框别名共9条多余观察；这是来源证据等价，不能自动合并形态/UID或推断缺根数。新增42/42、继承1859/1859定向QA，Python/unzip双恢复各1951/1951 SHA及1901/1901 QA。T01 0/25、正式ID0、T00–T11 0/12 Accepted；历史全量QA、真机、读屏均not-run。[R156证据](./evidence/v036-round156-t02-content-addressed-source-evidence-identity.md)。


**R155 非验收门禁：** 170/170原生RGB来源核验、18条ROI重叠审计、双独立1942/1942 SHA及各1859/1859选定QA通过，只证明来源归属冲突被显式隔离；不得把ROI重叠推断为共享笔画或独立字根。T01 0/25、正式ID0、T00–T11 0/12 Accepted。完整历史全量QA/真机/读屏not-run。详见[证据](./evidence/v036-round155-t01-t02-native-pixel-ownership-graph.md)。


**R154 T03非Accepted：** 隔离注册表原型碰撞修复与151草案几何回归已验证（新24、选定旧1706、双恢复各1730），但正式ID/源图认证/生产集成/真机/读屏/历史全量均未验收；T00–T11 0/12。详见[证据](./evidence/v036-round154-t03-null-prototype-instance-registry.md)。

**R153 Root T04（隔离、非验收）：** 将R152独立raw来源绑定接入授权临时127.0.0.1双标签Chromium测试；本地ERR_BLOCKED_BY_ADMINISTRATOR=blocked，远端首跑40417492203因引用错误失败，已修复并启动40417922284（最终结果待复核）；继承定向1715/1715，父R152 1910/1910 SHA，新累计ZIP1918文件SHA `106319af615d7a5afb4c122306d649435137d7c502e1a084c7de45137c5b378d`，Python/unzip两套恢复各1918/1918 SHA、1715/1715 QA。完整历史全量QA not-run，T00–T11 0/12 Accepted，T01 0/25、正式ID0、正式迁移未完成；缺R10–12/R35及20SVG，许可/逐笔/真机/读屏未完成。 [证据](./evidence/v036-round153-t04-real-origin-raw-source-binding.md)。

**R152 T04非Accepted：**新27/27+继承1688/1688、两套独立恢复各1715/1715，仅为隔离来源一致性预检；R152真实同源not-run、正式迁移/回滚/永久ID/真机/读屏/源图认证未验收。原始T00–T11仍0/12。[证据](./evidence/v036-round152-t04-independent-raw-source-binding.md)。


**R151 增量门禁（非 Accepted）：**T04 只读计划必须区分“SHA 自一致”与“可信签发”。R150 的可自签伪造已复现；R151 同 realm WeakMap 签发门禁 Node 35/35，继承 1653/1653，不能作为跨 realm 可验证签名。本地 Chromium 真实同源 blocked；R151 授权真实同源 CI 40402103656 22/22 pass，但仅为合成数据预检。正式迁移、回滚、永久 ID、真机/读屏及源图认证仍须独立验收。


## R150 T04新增证据边界（非正式验收）

R149真实授权Chromium 33/33旧同源、27/27严格v16来源已独立下载artifact复验；R150新增只读旧槽别名影子计划与25/25 Node QA、1628/1628继承定向QA及1892/1892双独立恢复。R150本地真实同源blocked、远端pending。影子别名不是正式永久ID；真实用户数据未读取/写入，V0.35→V0.36生产迁移及回滚未验收；T00–T11仍0/12 Accepted。


## R149 T04新增证据边界（非正式验收）

R149将R148严格重复JSON键只读门禁接入授权临时127.0.0.1真实Chromium双标签WebCrypto/Web Locks/localStorage QA，远端运行 [40384582893](https://github.com/tims-SP/glyphspace/actions/runs/40384582893)待确认；本地同源blocked。旧定向1628/1628与双独立1881文件SHA恢复通过，不替代真实用户旧配置迁移、稳定正式ID、可回滚生产流程及T04 Accepted。T00–T11仍0/12 Accepted。

> 状态：**规则与证据边界已修订，项目未通过正式验收**。权威任务名称取自[历史原始WBS](./history/V0.36-P0-original.md)，不是隔离UI原型中的同名旧标签。详细输入和视口组合见 [12测试矩阵](./12-test-matrix.md)。

## 验收状态（不可跳级）

`planned → prototype → QA-passed → source-reviewed → integrated → accepted`；源图/字形`source-reviewed`和UI行为`QA-passed`是不同维度，不能互相转化。管理员阻断=blocked；没有运行=not-run；人审意见≠原图认证。

## 原始任务验收表

| 工作包 | 必须证明什么 | 当前结果 |
|---|---|---|
| **T00 基线冻结** | SHA不变、151旧可视/5关联/176编码旧行为、旧存储快照与恢复机制 | 基线在，正式候选全回归未做 |
| **T01 参考图清点** | 25键每个可辨形态逐图ID/分类、不可辨附证据、无未经登记形态 | **0/25正式认证**；第46轮仅审计候选阻断 |
| **T02 语义/永久ID** | root/variant/annotation/supplement/related分类、稳定instanceId/assetId及旧槽全映射 | 156ID草案；未正式绑定 |
| **T03 SVG坐标内核** | 100×100局部viewBox、真实inkBBox、锚点/ox/oy、标签独立区、三视图一致 | 隔离探索；未集成 |
| **T04 存储迁移** | 旧用户调位保留、schemaVersion+instanceId、失效签名、安全冲突/幂等/回滚 | R147授权临时原点合成v16部分来源双标签33/33通过；R148发现并隔离修复JSON重复来源键静默覆盖，Node29/29、Chromium about:blank仅解析9/9；本地真实同源blocked、R148远端同源not-run；**真实用户V0.35→V0.36正式迁移未验收** |
| **T05 完整性补图** | M键及全部25键有独立SVG实例且正式确认遗漏0 | 未完成 |
| **T06 轮廓一致性** | 全可辨形态逐笔/方向/宽重/变体/异源Path复核 | 未完成 |
| **T07 位置/碰撞** | 字根、字母、区号、圈注真实墨迹边界与stroke无未批准碰撞 | 未完成 |
| **T08 校准闭环** | 可新增参考形态，五维审批、Path/原图/坐标变更过期与证据导出闭环 | 隔离审阅页，未集成 |
| **T09 输入与三视图** | 完整/mini/单键共永久ID与Path；176编码、15识别码、PY/PU/QT、三学习模式 | 未集成新版本全回归 |
| **T10 视觉/设备** | 25键实际审图+真实Android/iOS、DPR/缩放、移动系统键盘、实际读屏 | **真机和读屏0** |
| **T11 发布冻结** | 完整单HTML离线、许可证来源、可回滚版本与完整验收报告 | 不具备发布条件 |

## 原图、几何与语义四类质量门禁

**覆盖率**：以每个referenceShape为分母，不以旧151实例、222暂定叶或156稳定ID草案为分母；不可辨必须单列。**语义准确性**：root/variant/annotation/supplement/related严格分类；不将圈注或补码第二键当正常字根。**视觉准确性**：逐笔审视、墨迹BBox、光学重量与相对几何。**技术稳定性**：增删实例不漂移、三视图同源、旧配置安全迁移。

原始规划建议：主根归一中心误差 ≤3/100，宽高偏差 ≤10%；高风险微根使用有证据的人工例外。此阈值不能替代逐笔认证，也不是第46轮已通过的测试。

### 必须出现的具体回归

* 全176原有编码对照；15种末笔字型识别码、PY/PU/QT三种补码、键名字、成字根；引导/进阶/盲打及盲打不泄漏下一键答案。
* GEO-01–06、DATA-01–03、REF-01/02、INPUT-01/02、UI-01、DIST-01与[12独立矩阵](./12-test-matrix.md)中的所有真实环境用例。
* 原始屏幕下限矩阵：320×568、375×667、390×844、430×932、844×390、1024×768、1440×900、1920×1080；DPR 1/2/3，键盘完整/折叠/迷你，真机Android Chrome与iOS Safari。
* 焦点/软键盘/系统缩放可达；真实VoiceOver/TalkBack/NVDA或等价屏幕阅读器测试，不能用浏览器AX树快照代替。
* V0.35旧存储加插入/重排/删除新字根的迁移、非法值、部分写入、真实共享原点双标签冲突、恢复默认与失败回滚。
* 离线`file://`完整运行（不能打开的环境记blocked）、无CDN、第三方路径许可与可分发审核。

## 第46轮已经核查的范围 ≠ 本章验收通过

第46轮独立ZIP `32c7130983d18965676f643d9fdd5d178047f749d2f0e4676cf7e56a67d7b5ce`，685/685文件SHA一致、663/663继承一致；静态26/26、Chromium about:blank 20/20和10组回归通过，证明审计层候选冲突隔离与历史一致性。**并未完成原图逐笔、永久ID生产绑定、T03/T05集成、用户真实数据迁移、真机/读屏。**

缺第10–12、35轮ZIP和第12轮20SVG，不能声称连续历史全部恢复。

## 发布否决规则

凡T00–T11任何任务未Accepted，或25键有未审对象、原图缺失数未知、正式SVG/编码被擅改、真实用户资料遭实验性写入、跨端控件不可达、法定素材许可不明，**均不得将V0.36标为完成或替换冻结index.html**。

## 验收证据最低字段

`taskId, testId, environment, sourceSHA, codeRevision, observed, expected, result(pass/fail/blocked/not-run), artifacts, reviewer, reviewedAt, remainingRisks`。所有统计必须带正确分母。自动测试不能替代真实逐笔或设备级证明。
