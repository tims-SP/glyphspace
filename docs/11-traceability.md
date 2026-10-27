# 11 · 任务—源码—证据—验收追踪

**R168 Root T00/T01/T02/T03（原始R8→R50冻结SVG来源连续性，非验收）：** 真读R167父ZIP2075文件、嵌套原始R10 ZIP184文件、原始R8 151 SVG草案与156 ID注册表、R9 15证据及后期R50 151 Path；151/151实例ID/键/旧槽/字符/坐标/Path一致，5关联项隔离，149个普通Path SHA可直接重算，H:6/H:7两个特殊部件来源SHA单列不伪造。新28/28+实际重跑选定旧288/288；R168累计ZIP2084文件SHA `1bb96c5dcd658230aee4cfd0836e1c04e74479e6a6d0a3b72ab3b5a1a54a2ef4`，父2075/2075 SHA继承，Python/unzip双独立恢复各2084/2084 SHA及316/316选定QA，QA后SHA不变。完整历史全量/真同源/真机/读屏not-run；原始T00–T11仍0/12 Accepted、T01 0/25、正式ID0、缺根未知，R11/R12/R35及20SVG仍缺，冻结入口/用户存储未动。[R168证据](./evidence/v036-round168-t00-t03-original-r8-r50-source-lineage.md)。


**R167 Root T00/T01/T02（原始R10历史快照分歧门禁，非验收）：** 真读R166父ZIP2066文件和嵌套R10原始184文件，核对137同名同SHA、6同名异SHA、41累计根路径缺失；R10依赖的原始R9 evidence.json及R8 151旧SVG草案仅在R10原包内，8条旧Path SHA来源一致、7条无旧映射。新39/39+实际重跑选定旧249/249；R167累计ZIP2075文件SHA `f0ebd556f75e48cb09aef569054aa6b0c8f5dff62bed74a8647bf268c5504286`，Python/unzip双独立恢复各2075/2075 SHA、288/288选定QA及QA后SHA不变。2358递归选定全套/完整历史全量/真同源/真机/读屏本轮not-run；原始T00–T11仍0/12 Accepted、T01 0/25、正式ID0、缺根未知；R11/R12/R35与R12 20SVG仍缺，冻结入口和用户存储未动。[R167证据](./evidence/v036-round167-t00-t01-original-r10-fork-lineage.md)。

**R166 Root T01/T02（关联T05，原生裁框交叠来源分区，非验收）：** R10 V/X两组原框均无交叠，R96扩框后V共享57像素（57/57原在R10 V-vis-06）、X共享32像素（原在两旧框各16）；meanRGB<185下V 4暗像素均在R10 V-vis-06原框，阈值敏感，**不代表笔画/字根归属**。父R165 2057/2057 SHA继承，新108/108、继承选定2250/2250；R166累计ZIP2066文件SHA `a0bd753dd2d2be8b95c3cfdb8bf05bb98bde02998b9ef7c94ea63bee6f1a0832`，Python/unzip双独立恢复各2066/2066 SHA与2358/2358选定QA、QA后SHA不变。完整历史全量/真同源/真机/读屏not-run；正式T00–T11仍0/12 Accepted、T01 0/25、永久ID0、缺根未知；R11/R12/R35和R12 20SVG仍缺，冻结入口及用户存储未动。[R166证据](./evidence/v036-round166-t01-t02-r10-r96-overlap-provenance-partition.md)。

**R165 Root T01/T02（关联T05，R10→R96原生裁框谱系，非验收）：** 真读R164父ZIP2048文件与嵌套R10原始ZIP、冻结2008 JPEG，复核R10 7个未映射标签与R96物理观察：标签7/7相同，但**原生裁框0/7相同**；7个R10裁框均严格包含于R96对应框，后者合计新增338原生像素、移除0；固定meanRGB<185诊断新增V:06 3暗像素/V:07 4暗像素，V两框重叠57像素其中4暗像素（归属未定），X重叠32像素其中0暗像素。新62/62、继承选定2188/2188，父2048/2048 SHA继承；R165累计ZIP2057文件SHA `19cf88860967c4c7eec8f73b7e654d0dc8c34022bc72d5b4456e11a2cfa37a3e`，Python/unzip双独立恢复各2057/2057 SHA、2250/2250 QA且QA后SHA不变。原图/身份/缺根均**未认证**，T00–T11仍0/12 Accepted、T01 0/25、正式ID0；R11/R12/R35和R12 20SVG仍缺，真同源/真机/读屏/完整历史全量QA本轮not-run；冻结入口与用户存储未动。[R165证据](./evidence/v036-round165-t01-r10-r96-native-pixel-crop-lineage.md)。

**R164 Root T00/T01/T02（原始R10历史ZIP真实恢复，非验收）：** 从Library取得原始第10轮ZIP 11,133,720字节，SHA `6a1552b45cfa3512d9fea2ab06df740a6adbb4b598369cd3ea8e214fee1c0ed0`，184/184原始成员与冻结HTML/JPEG SHA一致；与R163累计包同路径137一致、6同名历史字节不同、41原先缺失，保留原始ZIP嵌套不覆盖。R10 15证据=8暂映射+7未映射、8采框触边；7未映射标签与R96七微形7/7相符，均未认证。新增只读45/45、继承选定2143/2143，R163父2039/2039 SHA继承；R164累计ZIP2048文件SHA `ba42015efe35b702796266f23a458cf25fbf11e3a77bc4c56d3373eb678ec17a`，Python/unzip双独立恢复各2048/2048 SHA与2188/2188定向QA、QA后SHA不变。**R10不再缺失，仍缺R11/R12/R35及R12 20SVG**；完整历史全量/真同源/真机/读屏本轮not-run，正式T00–T11 0/12 Accepted、T01 0/25、正式ID0；冻结入口与用户存储未动。[R164证据](./evidence/v036-round164-t01-original-r10-archive-recovered.md)。

**R163 Root T03（隔离三视图DOM绘制预集成、非验收）：** 将R162 SHA绑定151草案SVG计划连接为full/mini/focus三种外部尺寸，共用100×100 viewBox、ID、Path和矩阵；仅返回detached DOM，拒绝getter/非法绘制/伪认证。真实Chromium about:blank DPR1/2共6组、900项fill DOM解析式BBox及156项alpha栅格采样通过；Node新增20/20、继承选定2117/2117、合计2143/2143。R162父2028/2028逐文件SHA继承，R163累计ZIP2039文件SHA `4a20d2335cb9f0fd557dd86d3a7b533d15a284467f3c42dd54fe97b0be56efc0`；Python/unzip双独立恢复各2039/2039 SHA、2143/2143 QA，QA后SHA不变。正式T00–T11仍0/12 Accepted、T01 0/25、正式ID0、T03未生产集成；R10–12/R35及R12 20SVG仍缺，高清合法原图/逐笔/真机/读屏/真实同源/完整历史全量本轮未通过或not-run，冻结入口与用户存储未动。[R163证据](./evidence/v036-round163-t03-three-view-source-bound-dom-renderer.md)。

**R162 Root T03（隔离实际绘制、非验收）：** 新增151草案实例SHA绑定的100×100 SVG安全绘制描述符；真实Chromium about:blank DPR2/3各151实例、153 Path，302次alpha墨迹及300次fill DOM解析式bbox核验通过，最大像素边缘误差0.49/0.33067 CSS px（非原图认证）。新增Node14/14、继承选定2101/2101、浏览器2/2；父R161 2016/2016 SHA继承，新ZIP2028文件SHA `bb5a007aed51cba3ff5b9391eca3d9bd9c21b7f3d64cf91db3f06a5bcecbcd96`；Python/unzip双独立恢复各2028/2028 SHA、2117/2117定向QA，QA后SHA不变。正式0/12 Accepted、T01 0/25、永久ID0、T03未生产集成；缺R10–12/R35和20SVG、高清许可/逐笔阻断不变；真实同源/真机/读屏/历史全量本轮not-run，冻结入口及用户存储不变。[R162证据](./evidence/v036-round162-t03-chromium-source-bound-svg-paint.md)。

**R161 Root T03（关联T08隔离预检、非验收）：** 新增151草案实例来源Path+真实解析式inkBBox+坐标/锚点/光学偏移的逐实例SHA256见证与变更影响清单；单实例调位仅该项签名过期，重排不变。新Node18/18、继承选定2083/2083；父R160 2007/2007逐文件SHA继承，新累计ZIP2016文件SHA `97327e64f2ac290edfe557fc3736b0c4c5855add2fec71735d0fdc685db65c4c`；Python/unzip双独立恢复各2016/2016 SHA与2101/2101定向QA、QA后SHA不变。完整历史全量/真实同源/真机/读屏本轮not-run；正式T00–T11仍0/12 Accepted，T01 0/25、正式ID0、T03未生产集成，缺R10–12/R35及20SVG、高清许可/逐笔阻断不变。冻结入口/176编码/用户存储未动。[R161证据](./evidence/v036-round161-t03-draft-geometry-change-witness.md)。

**R160 Root T03（隔离、非验收）：** 将R125三份SHA绑定真实冻结Path/解析式矢量inkBBox/151草案目录与R159数据描述符快照连接，建立151完整、路径SHA绑定、拒绝getter/身份漂移/未批准认证的不可变预集成计划。新Node30/30、旧选定2053/2053；父R159 1997/1997 SHA继承，新累计ZIP2007文件SHA `50892db856dbc26c52d9b18d330f818ee4fd391ed526ca2e861d780cabccaa6b`，Python/unzip双恢复各2007/2007 SHA与2083/2083定向QA、QA后SHA不变。完整历史全量QA/真实同源/真机/读屏本轮not-run；T00–T11 0/12 Accepted、T01 0/25、正式ID0、T03未生产集成；缺R10–12/R35及20SVG、高清许可/逐笔未解决，冻结入口/用户存储不变。[R160证据](./evidence/v036-round160-t03-source-bound-151-vector-snapshot.md)。


**R159 Root T03（隔离、非验收）：** 实际复现R154重复读取instanceId的getter TOCTOU：校验`validated`而注册`UNVALIDATED`。新增自有数据属性快照适配层，拒绝getter/继承字段，151草案几何与R154一致。新35/35、继承选定2018/2018；父R158 1987/1987 SHA继承，新累计ZIP1997文件SHA `27aaf806a767888c586feddd805a9253c7dab3d6088fd6603edea46188cccac6`，Python/unzip双恢复各1997/1997 SHA及2053/2053选定QA（QA后SHA不变）。完整历史全量QA/真同源/真机/读屏本轮not-run；T00–T11 0/12 Accepted，T01 0/25，正式ID0，T03未生产集成；缺R10–12/R35和20SVG、高清许可未解决，冻结入口/用户存储不变。[R159证据](./evidence/v036-round159-t03-accessor-snapshot-identity.md)。


**R158 Root T01/T02/T05（隔离、非验收）：** 从冻结2008 JPEG原始字节独立复算170/170原生RGB来源见证，生成12个无旧槽精确绑定裁框+2组E/K旧槽同框冲突的14张无损上下文复核卡与审阅图谱；K圈注/M小框/VX交叠/E空白框均保持待逐笔仲裁，不批准正式根或永久ID。新增81/81、继承选定1937/1937，Python/unzip双恢复各1987/1987 SHA、2018/2018选定QA且QA后SHA不变；父R157 1961/1961 SHA继承，新累计ZIP1987文件SHA `c0a439161e9d4745e941e120d38d763a8abe520abfa86bfea20e38aaf9bd8966`。完整历史全量QA/真同源/真机/读屏本轮not-run，T00–T11 0/12 Accepted、T01 0/25、正式ID0、真实缺根数未知；缺R10–12/R35及20SVG，合法高清许可未解决，冻结入口/用户存储未动。[R158证据](./evidence/v036-round158-t01-t02-native-14card-source-review.md)。

**R157 Root T02（隔离、非验收）：** 151旧可视槽→149不同原生裁框，E:1/E:8、K:2/K:3两组旧槽同框歧义；161个来源裁框中12个无旧槽精确绑定（M4/K1/B1/J1/R1/V2/X2），其中5个与旧槽局部ROI相交、7个不相交；这**不是12个已确认缺根**，不合并旧槽或批准永久ID。新36/36、继承选定1901/1901；父R156 1951/1951 SHA继承，新ZIP1961文件SHA `1c9d625892f1ae1fe3e761392862d793e574f51b02904c6bfba5b542e30ea070`，Python/unzip两套恢复各1961/1961 SHA、1937/1937选定QA且QA后SHA不变。完整历史全量QA、真机/读屏/真实同源本轮not-run；T00–T11仍0/12 Accepted，T01 0/25，正式ID0，历史缺包和许可/逐笔阻断不变。[R157证据](./evidence/v036-round157-t02-legacy-source-binding-ambiguity.md)。


**R156 Root T02来源证据身份（非验收）：** 170来源观察→161原生裁框证据，8组精确同框、9条别名；sourceCropId与evidenceObservationId仅为可复算来源证据，不是referenceShapeId/assetId/instanceId。M/K/E同框不合并字形，V/X部分交叠不传递等价。新42/42+旧1859/1859；双恢复各1951/1951 SHA、1901/1901定向QA。T00–T11 0/12 Accepted，T01 0/25，正式永久ID0。 [R156证据](./evidence/v036-round156-t02-content-addressed-source-evidence-identity.md)。


**R155 Root T01/T02（隔离、非验收）：** 冻结2008 JPEG原生170/170裁框RGB SHA独立复验；25键建立18条同键ROI重叠边（2旧槽重复：E:1/E:8、K:2/K:3；8同框别名：K4/M4；6旧槽局部重叠；2未绑定物理观察互相重叠：V57像素/X32像素），跨键0。像素相交不等于笔画归属或字根认证；正式0/25键、永久ID0、缺根数未知。父R154 1931/1931 SHA继承，新累计ZIP1942文件SHA `99f0c1315800dccceec75331cf01eba86989be01abf788e602e660a0a8c69125`，Python/unzip双独立恢复各1942/1942 SHA及1859/1859选定QA（旧1730+新129），QA后SHA不变；完整历史全量QA not-run。R10–12/R35及20SVG仍缺，合法高清许可/逐笔/真机/读屏未完成；冻结入口/用户存储不变，T00–T11 0/12 Accepted。 [证据](./evidence/v036-round155-t01-t02-native-pixel-ownership-graph.md)。


**R154 Root T03（隔离、非验收）：** 实际复现R48普通对象注册表遇`__proto__`实例ID时自有键丢失、原型被覆盖；新增零原型不可变安全注册表，151草案实例几何与旧R48逐项一致，增删/重排稳定。新Node 24/24、继承定向1706/1706；父R153 1918/1918 SHA继承，新累计1931文件ZIP SHA `ea6340b4207aa8e9b223140bbdc47436bfa9092814579fea102ca2bc0457b051`，Python/unzip两套独立恢复各1931/1931 SHA、1730/1730 QA且QA后SHA不变。R153授权Chromium CI 40418102420最终success、R153 22/22；R154真实同源not-run，完整历史全量QA not-run。正式T00–T11仍0/12 Accepted，T01 0/25、正式ID0、T03未集成；缺R10–12/R35及20SVG、高清许可/逐笔/真机/读屏未完成，冻结入口/用户存储不变。[证据](./evidence/v036-round154-t03-null-prototype-instance-registry.md)。

**R153 Root T04（隔离、非验收）：** 将R152独立raw来源绑定接入授权临时127.0.0.1双标签Chromium测试；本地ERR_BLOCKED_BY_ADMINISTRATOR=blocked，远端首跑40417492203因引用错误失败，已修复并启动40417922284（最终结果待复核）；继承定向1715/1715，父R152 1910/1910 SHA，新累计ZIP1918文件SHA `106319af615d7a5afb4c122306d649435137d7c502e1a084c7de45137c5b378d`，Python/unzip两套恢复各1918/1918 SHA、1715/1715 QA。完整历史全量QA not-run，T00–T11 0/12 Accepted，T01 0/25、正式ID0、正式迁移未完成；缺R10–12/R35及20SVG，许可/逐笔/真机/读屏未完成。 [证据](./evidence/v036-round153-t04-real-origin-raw-source-binding.md)。

**R152原始T04（隔离、非验收）：R151 WeakMap只能验证当前realm计划签发，不能验证注入reader与原始存储raw相符。R152实际复现R151接受伪SHA、伪编辑、漏键和转义重复JSON键，新增独立raw SHA/坐标/键/编辑校验及只读reader facade。Node新27/27、继承1688/1688；R151父1902/1902 SHA，R152累计1910文件ZIP SHA `2ed630217d3b85a20d18eba07d636d31fe93885212d50eb0a2861ea8a19b62e4`，Python/unzip两次独立恢复各1910/1910 SHA及1715/1715定向QA。R152真实同源not-run，完整历史QA not-run；原始T00–T11仍0/12 Accepted，T01 0/25、正式ID0、T04正式迁移未完成；缺R10–12/R35和R12 20SVG，高清许可/逐笔/真机/读屏未完成。** [证据](./evidence/v036-round152-t04-independent-raw-source-binding.md)。


**R151 Root T04（非验收）：**累计 ZIP SHA `f7770b71a7f0aa52eaff20c4afee5481624e6ac7796c4eabf9b5a139d82a78aa`；父1892/1892继承、双独立恢复各1902/1902 SHA及1688/1688定向QA（完整历史全量not-run）。R150 影子计划可被调用者重新计算 SHA 后伪造，R151 采用私有 WeakMap 仅允许同 realm 原始签发对象通过 verifyPlan；Node 35/35、继承 1653/1653；本地真实同源 blocked，R151 远端真实同源 CI 40402103656 22/22 pass，仍非正式迁移。生产迁移/永久 ID 未通过，T00–T11 仍 0/12 Accepted。详见 [证据](./evidence/v036-round151-t04-issuer-bound-alias-plan.md)。


## R150 原始T04追踪（隔离，非验收）

R149授权Chromium严格来源27/27及旧同源33/33真实CI已复核artifact；R150新增严格v16来源→旧槽别名影子计划，SHA绑定、不可变、缺席键保留、拒绝正式ID提前绑定；Node25/25、继承1628/1628，父1881/1881 SHA继承，新1892文件累计ZIP SHA `51396c322a4a4ac7bd47b3aefb3b8bdcf8c7797b72dc353c1b9763f4a0d31d09`，Python/unzip各1892/1892 SHA及1653/1653 QA。R150本地同源blocked、远端CI pending；完整历史QA not-run。正式T00–T11仍0/12 Accepted，T04生产迁移未完成，缺历史原件和许可/逐笔/真机/读屏。[证据](./evidence/v036-round150-t04-immutable-legacy-alias-shadow-plan.md)


## R149 原始T04追踪（隔离，非验收）

R149 Root T04：R148 5944字节严格旧v16只读门禁SHA一致接入GitHub Actions授权127.0.0.1双标签真实Chromium回归；远端运行 [40384582893](https://github.com/tims-SP/glyphspace/actions/runs/40384582893)尚待最终结论，不得计pass。本地ERR_BLOCKED_BY_ADMINISTRATOR=blocked，继承R142–R148 1628/1628定向QA通过；父R148 1875/1875逐文件SHA继承，R149累计1881文件ZIP SHA `a8f88dfbf54380e848c6610525d3272e9aeda69745f07247c707fe5635256259`，Python/unzip独立恢复各1881/1881 SHA和1628/1628 QA，完整历史QA not-run。正式T00–T11 0/12 Accepted，T01 0/25、永久ID0、T04生产迁移未验收；冻结入口/编码/用户存储未动。[证据](./evidence/v036-round149-t04-strict-real-origin-shadow-preflight.md)

## R148 原始T04追踪（2026-10-27，隔离非验收）

R148 Root T04（关联T00/T02）实际复现R147旧v16来源JSON重复G键被JSON.parse静默覆盖、即使raw SHA匹配仍被接纳；隔离增加重复对象键（含转义等价键）失败关闭扫描、冻结25键156槽默认值SHA、部分键/原始raw/来源签名门禁。父R147 ZIP1865/1865逐文件SHA继承；新R148累计1875文件，ZIP SHA `9b9c58ecd97cc1f68960ff4c70086148f197d1ec30704b9d4c8d0d6e490d35fa`，Python zipfile/unzip两套独立恢复各1875/1875 SHA及1628/1628定向QA（旧1590、新Node29、Chromium about:blank仅解析9）。本地真实同源仍管理员blocked；R148远端真实同源not-run、真机/读屏0、完整历史QA not-run。缺R10–12/R35和R12 20SVG、高清许可/逐笔；T00–T11 0/12 Accepted，T01 0/25、正式永久ID0、T04生产迁移未完成，冻结入口/176编码/用户存储未改。 [证据](./evidence/v036-round148-t04-strict-legacy-v16-source-duplicate-key-gate.md)


## 第147轮 · Root T04 冻结v16局部来源双标签影子读取

R147 Root T04（关联T00/T02）新增冻结V0.35 v16局部坐标来源只读影子测试：从SHA锁定HTML提取25键156旧坐标，在GitHub Actions授权临时127.0.0.1原点双标签读取G/K/X三键、22缺席键与3条模拟编辑，保留原始raw及无关sentinel，来源SHA变化拒绝；真实Chromium 33/33（run 40365890296）通过。容器本地真实同源仍ERR_BLOCKED_BY_ADMINISTRATOR；新Node WebCrypto/FakeStore 14/14、R142–R146继承1576/1576；父R146 ZIP 1855/1855逐文件SHA继承，新R147累计1865文件，Python/unzip双独立恢复各1590/1590本地定向QA与1865/1865 SHA前后不变。ZIP SHA bebcacaafadb23734dc11bb76ac095af21c744fa7b2c2e6fbec65c54c8153f70。真实用户存储未触碰；该CI仅合成数据预检，生产V0.35→V0.36迁移、正式永久ID、T03集成均未验收；历史R10–12/R35 ZIP和R12 20SVG仍缺，高清合法许可/逐笔/真机/读屏/完整历史QA未完成；T00–T11 0/12 Accepted、T01 0/25。 [证据](./evidence/v036-round147-t04-real-origin-v16-partial-shadow.md)

## 第146轮 · Root T02来源—身份交叉核验

R146 Root T02（关联T01/T04/T05）只读交叉核验R73/R75的151个草案UID与R145的170条原生物理来源观察：151旧可视槽各一草案UID；M同框别名4、M未绑定影子4、K4及B/J/R/V/X微形7，共15条未绑定物理观察（不是已确认缺根）；36旧未匹配属于151旧槽子集；5条related关联不生成独立UID。重算170/170原生RGB SHA；新201/201，继承R142–R145共1375/1375，每套1576/1576；父R145 1847/1847 SHA继承，新ZIP 1855文件，Python zipfile与unzip两套独立恢复各1855/1855 SHA且QA后不变。ZIP SHA e01168b3a786903568a8d6173d544f967affd2beb4f71304275d2790764287eb。R10–12/R35及R12 20SVG仍缺，合法同源高清许可/逐笔/真实同源/真机/读屏/历史全量QA未通过；T00–T11仍0/12 Accepted、T01 0/25、正式永久ID0；冻结入口/2008 JPEG/176编码/正式SVG/用户存储未动。 [证据](./evidence/v036-round146-t02-170-source-151-draft-uid-crosswalk.md)

## 第145轮 · Root T01/T02 全来源观察逐条待审覆盖（关联T05）

R145复核R144父ZIP 1839/1839逐文件SHA，170条来源观察中58条关联特定案件、112条无特定案件但仍待审（均非字根/缺根数）；新增逐观察来源审阅失败关闭门禁与379/379新QA，继承R142/R143/R144共996/996定向QA；Python zipfile与unzip双独立恢复各1847/1847 SHA、1375/1375 QA及QA后SHA一致。累计ZIP SHA `4eec6b3b80561532dc79a4915d392a4cfc7506e50cd92d6d01e8b62ec40d68a3`。正式T01 0/25、永久ID0、T05未完成、T00–T11 0/12 Accepted；R10–12/R35及20SVG缺失，高清许可/原字节/逐笔/真同源/真机/读屏/历史全量QA未通过；冻结HTML/JPEG/176编码/正式SVG/用户存储未动。 [证据](./evidence/v036-round145-t01-t02-observation-review-coverage.md)

## 第144轮 · Root T01/T02 来源逐键追踪（关联T05）

R144实际核验R143父ZIP 1830/1830 SHA；按25键登记170来源记录（151旧可视槽、8 M候选、4 K来源、7微形；其中M同框别名不重复计入151），36旧未匹配为别名。12相交分量+36旧未匹配+4 M影子形成52个review-only案件，**不等于缺根数**。新676/676、继承957/957定向QA，Python/unzip双恢复各1839/1839文件SHA与1633/1633 QA；ZIP SHA `fc2a2257e9d17d031e7a012e7712987deeffc0110eea6e8ac301333fe635bba0`。R10–12/R35及20SVG缺失，高清候选许可未核，真实同源R108回放管理员阻断，真机/读屏/历史全量QA not-run；T01 0/25、正式永久ID0、T05未完成、T00–T11 0/12 Accepted；冻结生产入口/176编码/用户存储不变。[证据](./evidence/v036-round144-t01-t02-keywise-source-review-queue.md)


## 第143轮 · Root T01/T02/T05 M原始裁框与候选修订的不可变来源追踪

- R143聚焦M键8个来源观察的**原生裁框版本谱系**：4条旧槽完全同框别名+4条不可渲染影子观察；M-vis-02旧M:1框21×23与R86未批准的26×23证据候选框分离，新增115原生像素且RGB SHA不同，禁止将旧别名自动升级为候选框；M-vis-04左侧2像素归属仍未定。新87/87、继承R142/R141/R140/R81/R86/R87定向953/953，Python/unzip双独立恢复各1830/1830文件SHA、各1040/1040 QA且QA后SHA一致；父R142 1821/1821逐文件SHA继承，R143累计ZIP SHA `5b50c4141fdcebbbf42dda3c3e140426788f9cbcdd16f4449522d26ea55e833b`。正式T00–T11仍0/12 Accepted、T01 0/25、正式永久ID0、T05未完成，真实缺根数未知；历史R10–12/R35 ZIP及R12 20SVG未恢复，合法同源高清/逐笔/真同源迁移/真机/读屏/完整历史全量QA仍未通过。冻结HTML、2008 JPEG、176编码、正式SVG、用户存储未修改。 [证据](./evidence/v036-round143-t01-t02-t05-m-crop-evidence-lineage.md)

## 第142轮 · Root T01/T02 全25键物理来源集合（关联T05，隔离、非验收）

- R142将R81 159、R95 K物理观察4、R96微形7合并为25键**170/170原生RGB SHA复核**；R69 36旧未匹配仅作别名交叉核验。全源同键采框相交**18边**（10完全同框、8部分相交），12待审分量涉及28观察，其余142观察在本轮集合内无相交；B1/E1/J1/K5/M4/V4/X2。此为物理来源几何，不证明同一/独立字根、笔画归属或永久ID。父R141 1813/1813 SHA继承，R142累计1821文件ZIP SHA `7c7cf8f7d1036f32fe7e6a89f4d65455a38db4c30ac3d2bbd08b8f0d3876be37`；Python/unzip双独立恢复各1821/1821 SHA、各新233+旧733=966/966定向QA。正式T00–T11仍0/12 Accepted、T01 0/25、正式ID0、T05未完成；历史R10–12/R35和20SVG缺失、高清许可/逐笔/真同源/真机/读屏/历史全量QA未通过。冻结入口、176编码、正式SVG、用户存储未动。[证据](./evidence/v036-round142-t01-t02-full-25key-physical-source-universe.md)


## 第141轮 · Root T01/T02 来源冲突图追踪（隔离）

- R141 Root T01/T02（关联T05）：冻结2008 JPEG、R81 159、R96 7及R69 36条原生裁框**202/202 SHA复核**；7候选与旧槽来源相交图为12节点/8边/5分量。新发现V:4与V-vis-06、V-vis-07三方共有原生矩形[644,662,3,11]共33像素；V:4仍blocked_namespace。X-vis-03经X-vis-02连通旧X:0但**不能传递为身份相同**。父R140 1803/1803逐文件继承，R141累计1813文件ZIP SHA `bbef7887976f9c932439ce803ce7aee0e39bffc5b1b13d3a1804ef30862a9493`，Python/unzip双独立恢复各1813/1813 SHA、各新237+旧484=721/721定向QA。正式T00–T11仍0/12 Accepted、T01 0/25、永久ID0、T05未完成；缺R10–12/R35及20SVG、高清许可未明、真同源/真机/读屏/完整历史QA未验收；冻结入口、176编码、正式SVG和用户存储未动。 [证据](./evidence/v036-round141-t01-t02-source-overlap-component-graph.md)

## 第140轮 · Root T01/T02 候选对来源归属门禁（隔离）

- R140 Root T01/T02（关联T05）发现R96七个来源微形候选之间的两组**此前未单列**ROI交叠：V-vis-06/07原生57像素（灰度≤160/192/224分别2/3/6暗像素），X-vis-02/03原生32像素（0/0/0）。此为来源审阅候选对，不证明笔画归属或独立字根。R139父1793/1793逐文件SHA继承，R140累计1803文件ZIP SHA `3128d7d725071ef7904bd88bf0d56f73998c3e993a08c1739177b725ecb4c204`；Python zipfile/unzip双独立恢复各1803/1803 SHA、各新25+旧489=514/514定向QA；QA产生2个__pycache__文件均清理后SHA一致。T00–T11仍0/12 Accepted、T01 0/25、正式永久ID0、T05未完成；R10–12/R35及20SVG仍缺、许可未核、真实同源/真机/读屏/完整历史QA未验收；冻结入口、176编码及用户存储不变。 [证据](./evidence/v036-round140-t01-microform-pair-native-overlap.md)


## 第139轮 · Root T03 挂载后DOM完整性证据（隔离）

- R139 Root T03：R138仅在提交前后查重，后续宿主脚本仍可修改symbol/Path或搬移已挂载节点。本轮隔离新增私有R138包装的`GlyphSpaceR139.mountWatched`、MutationObserver和同步`assertIntact`/`dispose`；临时属性改写、外部同名ID插入再移除、SVG几何改写、节点搬移均被失效检测，普通无冲突DOM变更仍可保留。Chromium 144 `about:blank`新24/24、R132–R138旧120/120定向QA；父R138 1784/1784逐项SHA继承，R139累计1793文件ZIP SHA `344f5adfbb307de298a27e19d8dcfb890fe0bd839800f22ee507c1904c24db72`，Python/unzip双独立恢复各144/144 QA及QA后1793/1793 SHA一致。非恶意脚本沙箱、非生产集成、非来源认证；T00–T11仍0/12 Accepted，T01 0/25、正式ID0、T05未完成，R10–12/R35及R12 20 SVG缺失；真同源迁移blocked，真机/读屏/完整历史QA not-run；冻结入口、176编码、用户存储不变。 [证据](./evidence/v036-round139-t03-postcommit-dom-integrity-watch.md)


## 第138轮 · Root T03 宿主DOM symbol ID碰撞原子挂载守卫（隔离、非验收）

- R138在Chromium 144真实复现R137宿主DOM预置同名symbol导致错误字形：两个`gs134-1-def-1`，字根BBox被替换为100×100。新增私有受控`mountInto`，提交前宿主ID冲突检测、同步DOM提交、提交后复核及失败回滚；预置冲突拒绝且0半挂载，正常151字根×3视图453 SVG/453唯一symbol ID。新22/22+继承R132–R137 98/98；父R137 1776/1776逐文件SHA继承，R138累计1784文件ZIP SHA `e2df22e36096a664a9fa592f15a9b0f3e2b8c1fa6f7679279e898afc498dc3ee`，Python/unzip两套独立恢复各120/120 QA、QA后1784/1784 SHA一致。仅隔离技术修复，不能防御挂载后外部脚本改DOM，未来源认证/生产集成；T00–T11仍0/12 Accepted、T01 0/25、正式ID0、T05未完成；历史R10–12/R35与20SVG仍缺，真同源/真机/读屏/历史全量QA未通过；冻结入口/176编码/用户存储不变。[证据](./evidence/v036-round138-t03-host-dom-symbol-id-commit-gate.md)


## 第137轮 · Root T03 固定审阅草案SHA，拒绝调用者自签摘要（隔离、非验收）

- R137实际复现R136可被调用者通过修改Path/fill并重新计算SHA绕过字节来源约束；新增私有`GlyphSpaceR137.mountPinned(raw,view,ids)`，内置R134冻结派生草案SHA `89c6bbaac319f4f59d81c18ea5d0cbbb42899558c7ba7cf65fc81107de020f8a`，拒绝自签变更。151条冻结Path原始来源哈希逐项一致；Chromium 453个SVG、453唯一symbol ID。新21/21与继承77/77定向QA，R136父1768/1768 SHA继承；R137累计1776文件ZIP SHA `edfe5508884a5b50a2145f89f9ea47b5651a7333e3eb01cf04bf71df1bb0ecfb`，Python/unzip两套独立恢复各98/98 QA、1776/1776 SHA一致。未生产集成、未认证2008原图；T00–T11 0/12 Accepted、T01 0/25、正式永久ID0、T05未完成；R10–12/R35及R12的20 SVG仍缺，真同源/真机/读屏/完整历史QA未通过；冻结入口/176编码/用户存储未动。[证据](./evidence/v036-round137-t03-pinned-manifest-digest.md)

## 第136轮 · Root T03私有SHA验证渲染入口（隔离，非验收）

- R136 Root T03私有SHA验证渲染入口：将R132–R135源代码封入词法私有对象，只公开R136 mountVerified(raw,sha,view,ids)，旧R134可变manifest绕过入口不再公开，若已有旧全局API则失败关闭；Chromium about:blank 151字根×3视图=453 SVG、453唯一symbol ID；新20/20、继承R132 21+R133 12+R134 10+R135 14=57/57，Python/unzip两套独立恢复各77/77、1768/1768 SHA一致；父R135 1760/1760逐文件继承，R136 ZIP SHA a60486ed2af060f774450669d6c81e3ad99edab089a46f62b33d9144470d3806。仅隔离技术证据，未生产集成、未来源认证，T00–T11仍0/12 Accepted，T01 0/25、正式ID0、T05未完成；缺R10–12/R35及20 SVG，高清许可/真实同源迁移/真机/读屏/完整历史QA未解；冻结HTML、176编码、用户存储不变。 [证据](./evidence/v036-round136-t03-private-verified-renderer.md)

## 第135轮 · Root T03 SHA验证后不可变与H:7真实stroke paint（隔离、非验收）

- R135 Root T03实测发现R134的SHA验证manifest仍可在校验后修改嵌套strokeWidth并被挂载（WeakSet仅绑定对象身份）；隔离新增递归深冻结与受控挂载入口，路径和光学校正后置篡改被拒。Chromium 144 about:blank对H:7三视图×800/1600/3200px共9次真实stroke paint bbox测量，9/9与解析式inkBBox在分辨率量化+0.08/100容差内一致，9/9错误宽度负对照被拒。新14/14、继承175/175定向QA，两套独立Python/unzip恢复各189/189，QA副作用审计并还原后各1760/1760 SHA一致；父R134 1753/1753继承，R135 ZIP SHA dbc54639aa409d773aa39316c91bad1fe040b9ae6756d6413fb7ed1c67072c43。旧R134 API仍可绕过受控入口，未生产集成；完整历史QA not-run，T00–T11 0/12 Accepted、T01 0/25、正式ID0、T05未完成；R10–12/R35及20SVG缺失，高清许可、真实同源/真机/读屏未验收；冻结HTML、176编码和用户存储未动。 [证据](./evidence/v036-round135-t03-immutable-manifest-and-h7-stroke-paint.md)。

## 第134轮 · Root T03 SHA绑定解析式三视图SVG挂载（隔离、非验收）

- R134串联R125的151条真实冻结Path解析式inkBBox/100×100光学校正、R132符号闭包与R133跨SVG命名空间；独立Chromium about:blank同时挂载full/mini/focus 453/453实例及453个唯一symbol ID。450个fill-only绘制BBox最大归一化误差0.000310/100；H:7 stroke例外未计入450分母（浏览器BBox不含stroke，差约0.9044/100），待独立paint测试。原始manifest UTF-8 SHA校验、篡改拒绝和反序ID稳定通过。新10/10+继承165/165；父R133 1742/1742 SHA继承，R134累计1753文件，ZIP SHA 3c9e9fc821afbed248fe45d20018e41c5fe1818be12a928bae0a1cf5f2fbd274，Python/unzip双独立恢复各175/175 QA、1753/1753 SHA一致。完整历史QA not-run；T03仅隔离预集成，T01 0/25、正式ID0、T05未完成、T00–T11 0/12 Accepted；R10–12/R35及20SVG仍缺、许可/真同源迁移/真机/读屏未验收，冻结入口/176编码/用户存储未动。[证据](./evidence/v036-round134-t03-sha-bound-three-view-mount.md)。


## 第133轮 · Root T03 跨SVG挂载命名空间修复（隔离、非验收）

- R133 Root T03发现并复现R132隔离SVG跨实例默认ID冲突：两个不同符号同挂DOM，原始BBox宽10/80被错误绘制为10/10；新增每次调用唯一命名空间与内部ID/ARIA IDREF安全重映射，修复后10/80。冻结V0.35主键盘25个有根键位、151旧可视字根同时挂载，151/151本地symbol ID唯一、151/151原生BBox一致，5个对抗用例通过。新增12/12+继承定向153/153，两套独立Python/unzip恢复各165/165、1742/1742文件SHA一致；父R132 1734/1734 SHA继承，R133 ZIP SHA `bd866c1e436d8f3d9412fc4e3e47f2543c17f3f8bc806c07a307da8d0a64bbc4`。完整历史QA not-run，T00–T11仍0/12 Accepted、T01正式0/25、正式ID0、T03未生产集成、T05未完成；R10–12/R35 ZIP与R12的20SVG仍缺，许可、真实同源迁移、真机读屏未验收；冻结入口/176编码/用户存储未动。 [证据](./evidence/v036-round133-t03-cross-svg-mount-namespace-collision.md)。


## 第132轮 · Root T03 SVG symbol递归依赖闭包（关联T04，隔离、非验收）

- 本轮新增隔离SVG引用解析器：递归闭包、唯一局部ID、菱形共享依赖、循环/缺失/重复ID/外链及危险节点失败关闭；开发中修复分支汇合局部ID冲突。冻结V0.35真实Chromium `about:blank` 仅计主键盘26物理键（Z旧可视0），其他25键**151/151**自包含引用闭包且**151/151**原生getBBox四分量相同；15个对抗用例，新增21/21，继承R131/R130/R125/R123定向132/132，每套153/153。父R131 **1722/1722**逐文件SHA继承，R132累计**1734文件** ZIP SHA `670c139b1017a793ae6e84155874a633cbd94a602b24dd25f4eb00a1b28d184c`，Python/unzip双独立解压及QA后各1734/1734 SHA一致、各153/153。T04临时独立profile访问127.0.0.1仍被`ERR_BLOCKED_BY_ADMINISTRATOR`阻断，不计通过。完整历史QA not-run；**T00–T11仍0/12 Accepted**，T01 0/25、正式ID0、T03未生产集成、T05未完成，缺历史R10–12/R35及20 SVG、高清许可、真实同源迁移、真机读屏；冻结入口/176编码/用户存储未动。[证据](./evidence/v036-round132-t03-symbol-dependency-closure.md)。


## 第131轮 · Root T03隔离绘制符号依赖证据（非验收）

- 第131轮 Root T03（关联T07）隔离修复浏览器诊断的跨SVG `<use>`→`<symbol>`悬空依赖：新增本地`<defs>`克隆与唯一href绑定，独立Chromium 2 contexts×11对×2尺寸×4模式=176次渲染，396/396历史字段一致；两套恢复分别复测新守卫50/50与精选旧QA282/282，最终ZIP 1722/1722双解压SHA一致、最终各104/104 QA。父R130 1712/1712 SHA继承；第131轮ZIP SHA `f67fed7b5d62d01cf1d50336c66451aefcdfa46c429bcbeec6cbdfc3ce077549`。R129完整953与候选恢复R130完整505曾尝试但超时，**不计pass**。不能证明渲染波动唯一根因或跨设备稳定；T03未集成，T00–T11 0/12 Accepted，T01 0/25、正式ID0、T05未完成；历史R10–12/R35 ZIP和20SVG缺失，真实同源迁移/真机/读屏/许可仍未解，冻结入口及用户存储未动。[证据](./evidence/v036-round131-t03-self-contained-symbol-replay.md)。


## 第130轮 · Root T01/T02来源语义与T03绘制碰撞交叉证据（非验收）

- 第130轮 Root T01/T02/T03：2008 JPEG J:4原生裁框[1005,397,24,32]是包含圈和双竖笔的复合来源区域；R81 J:4来源账本仍为`blocked_invalidated`及`round69Unbound=true`。冻结V0.35源码明确H/J/K区位竖笔是说明性徽记，独立Chromium验证H/J/K分别为1/2/3笔且每键有1圈；R129 J:4/marker1的648/648墨迹重叠不能当作新增独立字根、碰撞已批准或源图认证。新增30/30来源语义QA，精选继承475/475 QA；Python/unzip两套独立恢复最终各505/505，候选1710/1710文件SHA一致，最终1712/1712文件双恢复SHA及新增30/30通过。R129完整953项定向QA未重跑、历史全量QA not-run；Chromium首次重放出现L:1和J:4短暂像素差异，失败已记录，重试才通过。R129父1698/1698继承，R130累计1712文件ZIP SHA `e7d0d0fda95ca938cba1e49359ce3507356e6c65a9cb25d383c0a3cede7c0bb3`。正式T01 0/25、正式永久ID0、T03未生产集成、T05未完成、T00–T11仍0/12 Accepted；历史缺包/20SVG、高清许可、真实同源迁移、真机读屏仍未解，冻结入口及用户存储未动。 [证据](./evidence/v036-round130-t01-j4-zone-badge-source-role-conflict.md)。


## 第129轮 · Root T03区位徽记绘制顺序与J:4根墨迹全包含（隔离，非验收）

- 冻结V0.35真实Chromium DOM 9组BBox候选+2阴性对照，400/800px分别渲染字根、徽记、原始及反向绘制顺序：5组真实像素交叠且绘制顺序敏感，4组所测分辨率无交叠；**J:4/marker1在800px下648/648字根墨迹像素落入区位徽记墨迹区域，反向顺序648像素变化**。此为必须复核的视觉归属风险，不是错误字根或已认证根；新增失败关闭碰撞复核门禁，不自动白名单。父R128 1679/1679 SHA继承，R129累计**1698文件** ZIP SHA `a7facaeaa26667d36dd0584d443b2e8b63abfbed8f24ec0c4a5c1a591286e732`，Python/unzip双独立恢复各新61+旧892=**953/953定向QA**、QA后1698/1698 SHA一致；完整历史全量QA not-run。T01 0/25、正式ID0、T03未集成、T05未完成、T00–T11 **0/12 Accepted**；历史缺包、许可、真同源迁移、真机读屏仍未解决；冻结入口/176编码/正式SVG/用户存储未动。[证据](./evidence/v036-round129-t03-zone-badge-paint-order-and-root-containment.md)。

## 第128轮 · Root T03标注/字根实际绘制像素交集（隔离）

- 冻结V0.35 SHA绑定的真实Chromium DOM双遮罩实测，第127轮9组BBox候选经400/800px、220/245阈值核验为5组真实像素交叠、4组无交叠；2组阴性对照为0。交叠可能为预期徽记覆盖，不等于正式碰撞判定。新增73/73、继承819/819；父R127 1663/1663 SHA继承，第128轮累计1679文件，ZIP SHA `0606855e57ec7e83c8240cc25148802d1aef654833e36933eab6a98605e940b0`；Python/unzip两套独立恢复各892/892及QA后1679/1679 SHA一致。完整历史QA、真实设备/读屏、真实同源迁移、来源逐笔均not-run；原始T00–T11仍0/12 Accepted，T03未集成。[证据](./evidence/v036-round128-t03-frozen-dom-paint-mask-intersection.md)。

## 第127轮 · Root T03补充追踪（2026-10-26，非验收）

- 第127轮 Root T03隔离新增冻结V0.35真实SVG圈注/区位徽记包络：Chromium about:blank从原页面DOM实测25键39个标注（7根圈/补码框、32区位徽记），对R125解析式墨迹240对及R126文字标签78对比较；6键H/J/L/N/Q/Y存在9组**保守BBox交叠候选**（非真实涂色碰撞），7组预期根圈叠加单列，标签交叠0/78，越界0/39。新Chromium39/39+Node30/30+继承750/750，两套Python/unzip独立恢复各819/819、1663/1663后验SHA一致；R126父1652/1652继承，R127 ZIP SHA `f2692f705f93b26b3e722c86b61725dcc22b506d2c1eda95b29f32347eb6eb6e`。**仍非正式验收**：T01 0/25、正式ID0、T03未集成、T05未完成、原始T00–T11 0/12 Accepted；历史R10–12/R35和20SVG缺失、许可/真机/读屏/正式迁移/全量历史QA未完成，冻结入口及用户存储未动。 [证据](./evidence/v036-round127-t03-frozen-svg-annotation-paint-envelopes.md)。


## 第126轮 · Root T03 字母/区号保留区几何证据（隔离）

- **第126轮 Root T03隔离新增字母/区号保留区实测**：从SHA冻结V0.35源码取25键区号与P/Q特殊字母坐标，在独立Chromium about:blank实测50个SVG文字BBox，与151旧实例解析式墨迹进行302对几何比较；直接交叠0/302，但R:5距字母仅0.782472/100，按1/100安全间距有1/302预警。新浏览器50/50+Node19/19+继承681/681，两套各750/750；R125父1641/1641 SHA继承，R126累计ZIP1652文件SHA `d8707b50a0249052fb74d208d2f6b135e3be6c7727255862badba7c20661e3d2`，Python/unzip两套各1652/1652 SHA一致。**仍仅隔离**：T01 0/25、正式ID0、T03未集成、T05未完成、T00–T11 0/12 Accepted；历史缺包、许可、真同源/真机/读屏/完整历史QA未解；冻结入口/176编码/用户存储未动。[证据](./evidence/v036-round126-t03-chromium-label-reservation-clearance.md)。


## 第125轮 · Root T03 解析式矢量BBox与R124光学校正守卫联接（隔离）

- **第125轮 Root T03隔离实质修复**：将R54解析式矢量墨迹BBox（151旧形态/153真实Path）SHA绑定R50 Path与R53几何，再接入R48/R124光学校正越界判定；151中145条与R50近似BBox存在非零差异（最大0.4841016564源单位、0.105布局单位）。新Node24/24+独立Python157/157+继承500/500，每套681/681；R124父1629/1629继承、R125 ZIP1641文件SHA `b64d144b0c4f79ce113330e4399db4a2fae3916e277e595e402d9a45893955cb`，Python/unzip两套各1641/1641后验SHA一致。**仍仅隔离实现**：正式T03未集成、T01 0/25、正式ID0、T05未完成、原始T00–T11 0/12 Accepted；历史R10–12/R35及20SVG缺失，真同源/真机/读屏/历史全量QA未运行。冻结入口/176编码/用户存储未动。[证据](./evidence/v036-round125-t03-sha-bound-analytic-vector-optical-guard.md)。


## 第124轮 · Root T03 光学校正后墨迹越界守卫（隔离实现，非正式验收）

- 发现R48 SVG坐标解析器只限制目标geometry，未限制光学校正ox/oy之后的真实inkBBox；冻结151条Path草案逐项注入ox=200均可在旧解析器中越出100×100。新增隔离守卫拒绝越界、验证锚点重构、保留未认证来源标记；**151/151**原始几何与旧矩阵一致、**151/151**恶意偏移拒绝、**151/151**小偏移往返。新增22/22 + 继承478/478，两套Python/unzip独立恢复各500/500 QA与1629/1629 SHA一致；父R123 1620/1620继承，新ZIP SHA256 `1b2ece4a2a2486aaf078b0fc27136c7a02f3c24b30a959832a03c9deb509aec9`。
- 本轮未生产集成；R50 Canvas inkBBox并非精确矢量边界，不能宣称T03 Accepted。T01 0/25、正式ID0、T05未完成、T00–T11 **0/12 Accepted**；历史R10–12/R35与20SVG缺失，真实同源仍被管理员策略阻断，真机/读屏/正式迁移未运行。冻结HTML/176编码/正式SVG/用户存储未动。[证据](./evidence/v036-round124-t03-optical-envelope-guard.md)。


## 第123轮 · Root T01/T02 M相邻候选最小割来源证据（关联T05，非验收）

- 冻结2008 JPEG/R81清单SHA绑定；M03/04五阈值4/8邻接最小割均0；M05/06仅阈值176连通（4邻接割4、8邻接割8）；M07/08在144/160/176的4邻接割1/1/2、8邻接割2/2/3，8邻接割像素位于原图x=1039、y=658–660。新28/28+旧450/450，两套Python/unzip恢复各478/478 QA及1620/1620后验SHA；R122父1610/1610继承，R123 ZIP SHA256 `20d5aa05ff4b26e0b5d7e46b4d2818df73b66983f184bebeb646db3f8be86812`。只是阈值脆弱桥接，不是逐笔归属或字根拆分证据。T01 0/25、正式永久ID0、T05未完成、T00–T11 0/12 Accepted；缺历史第10–12/35轮与20SVG，高清许可/真机/读屏/正式迁移未解，冻结入口/176编码/用户存储未动。 [证据](./evidence/v036-round123-t01-m-pair-min-cut-bottleneck.md)。


## 第122轮 · Root T01/T02 M-vis-04/08阈值隔离与邻根拓扑（关联T05，非认证）

- 冻结2008 JPEG/R81来源SHA绑定：M04原框[1017,623,14,13]在阈值96分裂、128–176可隔离且左伸2原生像素；M08原框[1040,653,12,15]在96分裂、128可隔离且底伸2像素，144–176因邻近墨迹连通触及隔离ROI边界而阻断。低清M07/08共享连通分量3/5档、M05/06仅1/5档、M03/04为0/5；R117高清5/5与本轮低清3/5是不同分辨率测量。**无笔画归属、裁框、身份或正式SVG认证。**
- R121父ZIP SHA `c3be0c550f467c94aaf38e38a0f855752eca44e0d6b9dac0ad29931270df4711`，1595/1595逐文件继承；R122累计**1610文件** SHA256 `e1b878d2c23ea2db07db1c27959911d9208a6e505ad5dad842af762f31f210bc`。新增30/30、继承420/420，两套Python/unzip恢复各450/450定向QA，QA后各1610/1610 SHA一致；完整历史QA not-run。
- T01正式0/25、T02正式永久ID0、T05未完成、原始T00–T11 **0/12 Accepted**。第10–12/35轮与20SVG仍缺；高清许可、真实迁移、真机/读屏未解；冻结入口/176编码/正式SVG/用户存储未动。[证据](./evidence/v036-round122-t01-m04-m08-source-topology.md)。

## 第121轮补充：Root T01/T02 → T05 M-vis-02墨迹包络（2026-10-25；非正式验收）

M-vis-02旧框[1045,585,21,23]经固定ROI五阈值连通分量重算，右侧墨迹超出4–5原生像素，未批准包络[1053,587,18,21]。父R120 1582/1582 SHA继承，R121累计1595文件，Python/unzip双独立恢复各420/420定向QA及1595/1595 SHA一致；ZIP SHA256 `c3be0c550f467c94aaf38e38a0f855752eca44e0d6b9dac0ad29931270df4711`。**非原图逐笔/字根/永久ID/补图认证**；T01 0/25、T02正式ID0、T05未完成、T00–T11 0/12 Accepted。历史缺包、高清许可、真实迁移、真机、读屏仍未解决。[证据](./evidence/v036-round121-t01-m02-component-envelope.md)。

## 第120轮 · Root T01/T02 全25键原生裁框边缘审计（关联T05；非验收）

- 第120轮读取冻结2008 JPEG及R81来源清单，**151/151旧可视+8/8 M暂存**逐框原生RGB SHA核验，25键旧来源均有记录；五阈值四侧边界审计标记**81/151**旧框为墨迹延续待复核（不是确认错误/缺根），M-vis-02右侧、M-vis-04左侧、M-vis-08底侧优先；K/E/B/V身份阻断未解。新46/46、继承354/354；父R119 1572/1572继承，新累计**1582文件** ZIP SHA256 `81fd92d03b6b5f92dd827a10ea2bf5a12116e6ea0c91524475d088aa0cbffd84`；Python/unzip两套各400/400定向QA、QA后各1582/1582 SHA一致。完整历史全量QA not-run；T01 **0/25**、正式ID **0**、T00–T11 **0/12 Accepted**。历史10–12/35与20SVG仍缺，许可/真机/读屏/正式迁移未解；冻结入口和用户存储未动。[证据](./evidence/v036-round120-t01-all-key-native-crop-edge-census.md)。

## 第119轮 · Root T01/T02真实高低清跨来源配准（关联T05；非验收）

- GitHub Actions [40196733036](https://github.com/tims-SP/glyphspace/actions/runs/40196733036)真实高清ZIP/JPEG SHA固定：133低清非图像ORB描述子、101比值匹配、99内点、22/25空间格；中位0.0636低清像素、95分位0.9552。M-vis-02、M-vis-07/08、K/E风险框实际投影与尺寸比例最大角点差0.126高清像素；**非逐笔/身份/许可认证**。
- 父R118 1560/1560逐文件继承，R119累计1572文件SHA256 `d2a160a86764c2b903241d3b9efdb49b756544411f13d55a03a0f46f21efa898`；双独立恢复与QA后各1572/1572 SHA一致，各354/354定向QA。完整历史全量QA not-run；两次SHA阻断的失败CI未计通过。
- T01 0/25、正式ID0、T05未完成、原始T00–T11 0/12 Accepted；历史10–12/35轮及20SVG、高清许可、真机读屏和正式迁移仍缺。[证据](./evidence/v036-round119-t01-real-cross-source-orb-registration.md)。

## 第118轮 · Root T01/T02高低清特征配准前置（非正式认证）

- 本轮新增SIFT/RANSAC来源坐标仿射配准器，冻结2008 JPEG来源SHA通过，**仅源图派生合成仿射7/7 QA**；904内点、中位误差0.1171为合成测试，不是3508×2480高清跨图实测。真实高清原始字节本地不可得，**真实跨来源配准not-run**，不批准裁框/字根/永久ID。
- 父R117 **1551/1551**逐文件SHA继承，R118累计**1560文件** SHA256 `287e93524cd698319bb502d5517c4c806f84c04f5fbc440185f7a6a89bbee993`；Python/unzip双独立恢复及QA后各1560/1560一致，每套新7+旧340=**347/347**定向QA；完整历史全量QA not-run。
- T01 **0/25**、正式永久ID **0**、T05未完成、T00–T11 **0/12 Accepted**。高清许可未确认，缺第10–12/35轮与第12轮20SVG；真实迁移/真机/读屏not-run；冻结入口/176编码/正式SVG/用户存储不动。[证据](./evidence/v036-round118-t01-affine-registration-preflight.md)。

## 第117轮 Root T01/T02→T05严格边界证据（非验收）

- M-vis-02高清五阈值直接跨界接触30/34/34/37/37，严格框内连通扩框像素166/177/180/186/190；M07/08持续连通仅属来源拓扑，不能决定笔画归属/字根身份。
- 父1540/1540 SHA继承；R117累计1551文件，SHA256 `a7aa36bcf6e994da9a93430881202649310bb48ebf5b5e8714bc357c7f1b0cca`，双独立恢复与QA后1551/1551，定向新旧各340/340；远端[真实高清CI](https://github.com/tims-SP/glyphspace/actions/runs/40187583179) success。
- T01 0/25、T02正式ID0、T05未完成，原始T00–T11 0/12 Accepted。版权、精确配准、历史缺包、真机、读屏、真实迁移仍未解决。[证据](./evidence/v036-round117-t01-m-strict-seam-topology.md)。


## 第116轮补充：Root T01/T02 高清M键墨迹连通（2026-10-25；非认证）

独立[CI 40183270210](https://github.com/tims-SP/glyphspace/actions/runs/40183270210)在固定SHA高清3508×2480 JPEG真实像素上计算五阈值8连通：M-vis-02右扩暗像素166/177/180/186/190均与旧框相连；M03/04无跨框连通，M05/06仅阈值176连通，M07/08五阈值均连通。旧框截断风险进一步得到物理证据，但**不批准**笔画归属、扩框、身份、SVG。新增20+旧311=331项每套通过，R115父1529/1529继承，R116累计1540文件双独立解压及QA后SHA一致。T01 0/25、永久ID0、原始0/12 Accepted；版权、历史包、真机读屏、正式迁移缺口不变。[证据](./evidence/v036-round116-t01-m-highres-ink-connectivity.md)。

## 第115轮补充：Root T01/T02 高分辨率原始像素与安全导入（2026-10-25；非验收）

R115 [CI 40178902354](https://github.com/tims-SP/glyphspace/actions/runs/40178902354)成功重新取得高清ZIP/JPEG真实原始字节并分析21个M/K/E风险ROI；M vis-02旧图右扩5像素对应高清ROI暗像素186（仅观察），K:2/K:3和E:1/E:8依旧共用物理RGB，不解除来源阻断。R114通用ZIP导入器合成路径穿越漏洞复现，R115拒绝；新增15/15+继承296/296，父1519/1519逐文件继承，新1529成员双独立恢复及QA后SHA一致。T01正式0/25、T02永久ID0、T05未完成、原始0/12 Accepted；缺版权、历史包、真机读屏、正式迁移。[证据](./evidence/v036-round115-t01-highres-roi-pixel-triage.md)。

## 第114轮补充：Root T01/T02 高清来源候选（2026-10-25；非正式验收）

R114从06wb社区镜像发现标称官方的3508×2480高清简体字根图ZIP；GitHub Actions 40175565336实际下载、解压并核验原始ZIP/JPEG SHA256。与冻结1536×1086参考图整图+四象限dHash仅4/320位差异，属于高度相似排版候选，**不是逐笔/同源原始字节/版权认证**。新31/31、继承R113 34+R112 36+R96 35+R95 36+R84 124，两套Python/unzip独立恢复各296/296；R113父1509/1509逐文件继承，R114累计1519文件，ZIP SHA256 `a24303d1e53c4643f7c8a7bbf3c68925c1225a4f76b4918dc1ba6f0aeb5af50c`。原始T00–T11 0/12 Accepted、T01 0/25、正式永久ID0，历史10–12/35轮与20SVG仍缺，未获合法再分发许可，高分辨率原图不入仓/ZIP。 [证据](./evidence/v036-round114-t01-highres-source-candidate.md)。

## 第113轮补充：Root T02/T04 影子UID与冻结默认坐标来源门禁（2026-10-25；非正式验收）

R111在151+5计数合法时允许Q:0/K:2候选UID互换、在默认坐标被投毒时静默漏记用户覆盖；R113两项旧缺陷实际复现，新门禁绑定冻结V0.35 Chromium默认25键156槽、R46/R73/R75、2008 JPEG和HTML字节SHA，拒绝替换并保留5条关联隔离。新34项及6组旧310项在两份独立解压环境各344/344通过，父1498/1498继承、累计1509/1509及QA后SHA一致。正式永久ID0、T01 0/25、T04真实迁移not-run、原始0/12 Accepted。[证据](./evidence/v036-round113-t02-source-bound-uid-shadow.md)。

## 第112轮补充：Root T01/T02 原图坐标系显式转换（2026-10-25；非正式验收）

R46旧槽原始框属于key-local坐标，而R81清单是native-JPEG坐标；R112读取25键referenceRect分别变换并核验原生JPEG RGB，151旧可视与R73候选UID、36旧未匹配与R69、M八观察与R84、七微形与R96、K四物理观察与R95均一致。新增36项失败关闭测试，两种独立解压各310项定向新旧QA通过；父1488/1488继承、R112累计1498/1498 SHA及QA后复验通过。K/E/B/V/M冲突未解除，正式来源认证0/25、永久ID0、T00–T11 0/12 Accepted；不等于T05补图。[证据](./evidence/v036-round112-t01-t02-native-coordinate-frame-identity.md)。

## 第111轮补充：Root T04/T02 局部v16来源无损隔离（2026-10-25；非正式验收）

R110严格完整25键准入无法保留V0.35真实接受的局部v16坐标配置；R111在只读候选门禁中显式区分sourceKeys/absentKeys，不为缺失键生成用户编辑，保留源SHA并拒绝重复键/未知键/非法数值。真实Chromium about:blank内存存储四组局部案例与旧页行为一致，新增60/60；旧定向QA五组405项通过。父1477/1477继承，新ZIP1488成员双独立解压及QA后SHA一致；正式永久ID0、T01 0/25、T04真实用户迁移not-run、原始0/12 Accepted。详见[证据](./evidence/v036-round111-t04-partial-v16-readonly-preservation.md)。

## 第110轮补充：Root T04/T02 冻结旧页浏览器快照准入（2026-10-25；非正式验收）

真实Chromium about:blank执行原始V0.35 HTML，内存localStorage合成输入复现部分v16被接受、坏v16阻断v15回退两项兼容风险；新增严格只读完整快照准入与151候选UID+5关联隔离影子映射。30/30新QA、16+10+179+170项旧QA在Python/unzip两份独立恢复中通过，父1468/1468继承、新累计1477/1477、QA后成员SHA不变。真实同源用户迁移**not-run**，T01 0/25、T02正式ID0、全部0/12 Accepted。见[证据](./evidence/v036-round110-t04-v035-browser-storage-shadow.md)。

## 第109轮补充：Root T04 真实原点预检（2026-10-25；非正式验收）

独立核验R108 CI 11/11（run 40153502403），并新增pending/record/head三阶段崩溃与恢复的真实Chromium双标签CI 23/23（run 40156644345，commit 053bb786）。此处真实原点仅为GitHub Actions临时127.0.0.1，不是本地profile或V0.35用户迁移；旧用户迁移仍not-run。R108父1459/1459逐项SHA继承，R109累计1468文件，Python/unzip两次独立恢复各1468/1468，恢复后新16+旧385项QA通过。R108 ZIP内1458成员QA为中间快照，外部最终复验才对应1459；不篡改旧档案。正式T04仍未Accepted，T00–T11 0/12；见[证据](./evidence/v036-round109-t04-real-origin-crash-recovery.md)。


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

## 第99轮 T03/T07 独立草案SVG像素绘制复验（非正式验收）

151候选UID × 400×400及800×800 = 302/302 Chromium alpha实际渲染非空且草案包络误差不超过一栅格像素；H:7真实stroke纳入，三种主动像素篡改3/3检出。父R98 1359/1359继承，R99 ZIP 1366文件 SHA256 `7fe43e62975b1e1b339f46674d452c519a3ad6b6d130e448e8c2f670d12f4fea`，双独立解压及14组定向旧QA通过。仅验证草案Path渲染，不认证2008来源形态、标签圈注或生产集成；原始任务0/12 Accepted。详见[第99轮证据](./evidence/v036-round99-t03-t07-raster-alpha-ink-envelope.md)。

## 第100轮 T00/T01/T05 归档链及M来源审计（非正式验收）

工作区第90–99轮10份真实ZIP逐个SHA/成员核验，第90→99轮9次父文件继承一致；R99 1366/1366继承后R100累计1373文件、SHA256 `f90595913cb0469809897a0dab9c20a84628fff2b61e032d2506b5e691cc559c`，双独立恢复各1373/1373且QA后SHA一致。M键8个候选ROI原始JPEG裁框、PNG原始字节与RGB重算均8/8一致，4个仍无旧槽、无正式Path/assetId；**正式新增字根0**。缺第10–12、35轮ZIP和第12轮20SVG；原始T00–T11仍0/12 Accepted，T01 0/25、缺根数未知。真实同源存储blocked/not-run，真机/读屏not-run。证据：[R100](./evidence/v036-round100-archive-chain-m-provenance.md)。

## 第101轮 T01/T02/T05 M键候选扩框像素归属（非正式验收）

R100父1373/1373逐文件SHA继承，R101累计ZIP1385文件 SHA256 `e40cae7e5932df6c2784bd977d1c511a5d7a4609e7002b509f10b72ef3795cd2`；Python zipfile/system unzip两次独立恢复及各自新旧QA通过。2008 JPEG/R55/R84来源绑定的8个M观察，6个未批准复框备选揭示3组交叠像素归属（M03/M04 2×13、M05/M06 4×18、M07/M08 2×17），保留未决不提升任何正式字根、Path或永久ID。新增58/58、旧R84 124/124、R86 20/20、R99 Chromium 302/302双恢复重跑通过。当前环境缺R90 ZIP，R100外部十包链本轮复跑blocked。T01 0/25、缺根未知、T00–T11 0/12 Accepted；同源存储/真机/读屏未验收。详见[证据](./evidence/v036-round101-m-native-source-ownership.md)。

## 第102轮 T01/T02/T05 M键扩框交叠像素证据（2026-10-25）

对R101三组交叠独立读取原始JPEG：M03/04仅几何交叠（五阈值暗像素0），M05/06、M07/08含暗像素候选且后者连通性阈值敏感；不认定共享笔画，不解除来源阻断。新增52/52、继承R101 58/58、R84 124/124、R86 20/20、R100局部、R99 Chromium302/302通过。父1385/1385继承，R102累计1397文件双恢复与QA后SHA全一致。历史十包链因R90缺失blocked，正式认证T01 0/25、原始任务0/12 Accepted。见[证据](./evidence/v036-round102-m-native-overlap-topology.md)。

## 第103轮 Root T03 SVG祖先绘制完整性隔离修复（2026-10-25）

R94 computed SVG style校验未覆盖key-cell、key-row、view、layout、body等祖先绘制属性，真实Chromium复现opacity:0后实际像素改变而getBBox不变、R94 attest仍通过。R103隔离门禁新增祖先绘制链快照，9类攻击拒绝，新增26/26；父R102 1397/1397 SHA继承、R103 1410文件双独立恢复与各8组定向QA（612项）通过，QA后SHA一致。**T03未生产集成，原始T00–T11仍0/12 Accepted**；T01 0/25、T02正式ID 0、真实同源存储/真机/读屏未验收。详见 [R103证据](./evidence/v036-round103-t03-ancestor-paint-integrity.md)。

## 第104轮 Root T03 伪元素遮挡缺陷（2026-10-25；非验收）

R103祖先普通computed style无法发现CSS `::before`/`::after`遮挡；真实Chromium五类攻击改变截图像素但`getBBox`不变、R103仍attest通过。R104隔离门禁增加祖先伪元素绘制/层叠签名，新增25/25；父1410/1410继承，R104累计1425文件SHA256 `3840ac7eaeea34c66d3c251dd8906117d92de2f5536b34256d26b6afad275289`，Python/unzip四次分段独立恢复，QA前后各1425/1425 SHA一致，9组637项定向QA通过。完整历史QA not-run；真实同源存储blocked/not-run，真机/读屏not-run。**T03未生产集成，T01 0/25、T02正式ID0、T00–T11 0/12 Accepted**。[证据](./evidence/v036-round104-t03-pseudo-element-occlusion.md)。

## 第105轮 Root T03/T07 事务性碰撞预检（2026-10-25，非验收）

真实Chromium复现R104允许同键候选墨迹包络重叠而attest仍通过；R105在DOM/overlay提交前执行25键151候选UID、409对完整事务碰撞检查，151/151主动碰撞拒绝且状态无部分写入，新增170/170 Chromium QA。父R104 1425/1425 SHA继承，R105累计ZIP 1433成员SHA256 `2ffa0ecc3b72bee3ef7d2a24d76431f3619c29b5734ed7dbf513388b0b7d876a`，Python/unzip双恢复及各5组定向新旧QA（702项）、QA后SHA均通过。**只是隔离草案矩形门禁，不是原图逐笔、描边/标签/圈注或正式T07验收；T03/T07未生产集成，T01 0/25，T02正式ID0，T00–T11 0/12 Accepted。** [证据](./evidence/v036-round105-t03-t07-transactional-collision.md)。

## 第106轮 Root T00/T09冻结176编码行为基准（2026-10-25；非正式验收）

R105父1433/1433逐文件SHA继承；冻结V0.35 HTML只在测试时内存注入选题钩子，真实Chromium about:blank逐字对照176训练条目，在引导/进阶/盲打528案例中执行输入状态机，新增3143/3143 QA。继承R105 170、R104 25、R103 26、R77 179、R99 302定向QA通过。R106累计ZIP1439文件 SHA256 `55e96b14b2a969e33b7e6b9e39fa132d0836062bbbb4d3fe9104d044d2de26c0`；Python/unzip两份独立恢复各重跑新3143+旧179+170并在QA后1439/1439成员SHA一致。此项只补充T00旧行为可复用回归证据，**不是T09正式新三视图集成**；原始T00–T11仍0/12 Accepted，T01 0/25、T02正式ID0；同源存储blocked/not-run，真机/读屏not-run，历史缺口不变。[证据](./evidence/v036-round106-t00-176-browser-oracle.md)。

## 第107轮 Root T04 真实原点预检路径（非正式验收）

新增可复现的独立loopback HTTP原点双标签Web Locks/localStorage事务脚本，覆盖提交、并发冲突、崩溃恢复、回滚和记录篡改；本地Chromium被管理员策略阻断，真实事务**blocked/not-run**。独立GitHub Actions烟测workflow已提交，运行结果待核验。新静态26/26、旧R77 179/179、R105 170/170；R106完整旧QA本轮超时未计通过。R106父1439/1439继承，R107累计1449成员双独立解压与QA后SHA一致；完整历史QA not-run。详见[第107轮证据](./evidence/v036-round107-t04-disposable-origin-preflight.md)。T04未真实迁移验收，T00–T11仍0/12 Accepted。

## 第108轮 · Root T04 隔离回滚前驱验证（非正式验收）

R107的隔离`rollback()`先变更head再读前驱，前驱缺失/篡改会破坏最后可读指针；R108在Web Lock内先校验前驱record SHA256/schema再更新head。Node VM合成存储/锁旧缺陷复现+新修复10/10；R107静态26/26、R77 Node179/179、R105 Chromium about:blank170/170在两份独立恢复中通过。父R107 1449/1449逐项继承，R108累计ZIP1459文件、SHA256 `51ee682e0df8ee4cde134b9a2b085be96959e6ed3435bd7c7e094bd02bfcbec5`，Python/unzip两次独立恢复及QA后SHA一致。真实临时loopback仍被管理员策略阻断，远端CI结果待独立核验；R106完整回归本轮超时不计pass。**不是生产迁移**，T04未Accepted、T01 0/25、全部0/12 Accepted。详见[证据](./evidence/v036-round108-t04-rollback-atomicity.md)。
