# 11 · 任务—源码—证据—验收追踪

**R245F17 Root T01/T02（非认证）：** 旧来源校验并发Promise超时实测；私有JPEG字节/解码Image/Blob URL与latest-wins epoch修复。R245F16父3204 SHA一致；Chromium新14、来源63、旧R145 Python379，合计456/456选定QA；3213文件ZIP SHA `2c4090e7fd177a33c221190f145aa4aef886cd1228ef350d8979f468d57f68ea`，双独立恢复3213/3213 SHA和QA，0漂移。R246主线修复未继承，T01正式0/25、T02批准ID0、Root 0/12 Accepted，高清/真同源/真机/读屏/历史全量not-run。[证据](./evidence/v036-r245f17-t01-atomic-source-verification-fork.md)。


**R245F16 / 原始T01/T02（逐笔描记异步来源epoch隔离，非认证）：** 真读R245F15父ZIP SHA `abd45644160fc933bb7a1b83e9a16bb94e5932e6ba8ed012e6302785ab7b1a60`，3194/3194逐SHA继承。真实Chromium复现R245F4挂起File.text期间重新验证**相同SHA的2008 JPEG**，仍错误导入A:5一笔旧描记；R245F16为trace导入加入evidenceEpoch前后校验，旧错误接受→新拒绝，合法导入/失效来源/错误schema及原草案保留均通过。旧R245F4 21+旧R245F15 37+新Chromium 33=**91/91**选定QA；累计3204文件ZIP SHA `bc343a657e317838bcf289ccc058bdd1a49a37e70e09f79664638acf1d8db939`，Python/unzip双恢复各3204/3204 SHA与91/91 QA，QA后0漂移。仅隔离about:blank；R246主线M跨裁框修复**未继承**，R246 ZIP原始字节未得；T01 0/25、T02正式ID0、缺根未知、Root 0/12 Accepted；高清同源许可/真同源/真机/读屏/历史全量not-run，冻结入口/176编码/用户存储未动。[R245F16证据](./evidence/v036-r245f16-t01-source-trace-epoch-fork.md)。

**R245F15 / 原始T03（活体DOM校准预检，隔离非验收）：** 真实Chromium复现R245F14在SVG Path已被篡改后，合法M:0坐标编辑仍先写Storage再报告轮廓漂移；R245F15在滑块/JSON导入/重置前后检查full/focus/mini活体DOM，只有成功才持久化，失败回滚内存坐标且Storage不变。父R245F14 3181/3181 SHA继承；继承选定旧QA771/771、新37/37，合计**808/808**；累计3194文件ZIP SHA `abd45644160fc933bb7a1b83e9a16bb94e5932e6ba8ed012e6302785ab7b1a60`，Python/unzip双恢复各3194/3194 SHA与808/808 QA、0漂移。R245F13耗时穷举QA本轮超时不计通过，历史全量not-run。仅about:blank及隔离内存Storage，真实同源/读屏/真机/同源高清逐笔not-run；R246原始ZIP、R11/R12/R35及R12 20SVG仍缺。T01 0/25、T02正式ID0、T05缺根未知、Root 0/12 Accepted；冻结入口/176编码/用户Storage未动。[证据](./evidence/v036-r245f15-t03-live-dom-preflight-fork.md)。


**R245F14 / 原始T03（隔离校准inkBBox预提交门禁，非验收）：** Chromium真实复现R245F13在M:0 X=90时先保存隔离Storage、再发生几何漂移；R245F14在滑块及部分JSON导入写入前，先以151实例100×100解析式inkBBox验证完整投影快照，非法输入保留旧DOM/坐标/Storage并提示。R245F13父ZIP3170/3170逐SHA继承，旧772+新Chromium40=**812/812**分段选定QA；累计3181文件ZIP SHA `4354ed408d6b4b10ea245504cabef8e58b84cddc93a89e372511440bed1b8be8`，Python/unzip双独立3181/3181 SHA与各812/812 QA、QA后0漂移。仅about:blank及内存Storage，历史全量/真实同源/真机/读屏/同源高清逐笔not-run；R246原始ZIP、R11/R12/R35和R12 20SVG仍缺。T01 0/25、T02正式ID0、T05缺根未知、Root 0/12 Accepted，冻结生产入口/176编码/用户Storage未动。[证据](./evidence/v036-r245f14-t03-precommit-inkbbox-fork.md)。


**R245F13 / 原始T03（隔离校准事务提交前全视图验证，非验收）：** Chromium复现R245F12对结构合法但DOM未更新的旧事件先写151条CURRENT、后发现geometry drift，污染已提交几何。R245F13先核对full/focus/mini全部实例的来源Path、身份、DOM坐标和transform，再提交；异常回滚CURRENT。继承R245F12父ZIP3160/3160逐SHA，旧731/731+新41/41=**772/772**选定QA，另25键151实例逐项编辑还原；累计3170文件ZIP SHA `e8e02c2478215219aa1ffe96f01fe1f0b484e8cb61298c5be1307a62a3a98039`，Python/unzip双独立3170/3170 SHA与772/772 QA、0漂移。仅about:blank、内存Storage；完整历史、真实同源、读屏、真机、合法同源高清逐笔not-run。R246 ZIP原始字节及R11/R12/R35、R12 20SVG仍缺；T01正式0/25、T02批准ID0、T05缺根未知、Root 0/12 Accepted。冻结入口/176编码/用户Storage未动。[证据](./evidence/v036-r245f13-t03-atomic-calibration-transaction-fork.md)。


**R245F12 / 原始T03（旧校准与解析式SVG三视图闭环修复，隔离非验收）：** Chromium复现R245F11原有X/Y/尺寸校准会将解析式SVG改写旧translate/scale导致geometry drift；隔离候选通过151实例坐标快照、100×100 inkBBox校验后同步full/focus/mini matrix，原有重置和训练输入可用。R245F11父ZIP3151/3151逐SHA继承；新增Chromium51/51、继承680/680，选定731/731；累计3160文件ZIP SHA `46092b27bcc671aa72b0276d633a83354c382a2aeb2845215ee44e1934b8973c`，Python/unzip双独立各3160/3160 SHA与731/731 QA、QA后0漂移。仅about:blank、内存Storage；T01正式0/25、T02批准ID0、T05缺根未知、Root 0/12 Accepted。R246 ZIP及R11/R12/R35、R12 20SVG仍缺；真同源/真机/读屏/历史全量not-run，冻结入口/用户Storage未动。[R245F12证据](./evidence/v036-r245f12-t03-live-calibration-bridge-fork.md)。


**R245F11 / 原始T03（冻结V0.35真实DOM三视图解析式SVG内核隔离预集成，非验收）：** R245F10父ZIP3138/3138逐SHA继承；R50 151冻结Path + R54解析式inkBBox + R62 100×100锚点/光学矩阵，经R245F8双源原始字节钉值验证，接入独立V0.35应用副本的full/focus/mini实际DOM。隔离Chromium 1280×800、390×844、844×390新增46/46，选定旧新680/680；累计3151文件ZIP SHA `9dc745ba3d8a057af4e9dc7a98f83afec421c6afbc2e6fc52e5202536b7797fc`，Python/unzip双独立各3151/3151 SHA、680/680 QA及0漂移（unzip恢复组合wrapper超时后4套分开重跑通过）。候选使用内存Storage，不触碰用户现有存储；未替换生产入口、未认证原图/永久ID、未修改176编码。R246原始ZIP及R11/R12/R35、R12 20SVG仍缺；真实同源/真机/读屏/历史全量not-run，T03仍accepted=false，Root 0/12。[R245F11证据](./evidence/v036-r245f11-t03-live-analytic-geometry-fork.md)。

**R245F10 / 原始T00（冻结V0.35实际Chromium截图及键盘基线，独立分叉，非验收）：** 从R245F9真实ZIP3128/3128逐SHA继承；独立Chromium144在about:blank加载字节冻结V0.35 HTML，桌面1280×800、手机竖屏390×844、横屏844×390，3视口各两套独立context PNG逐字节一致；26键/零文档滚动/无JS异常，真实输入EEEE完成首题「月」。旧选定582+T00钉值10+新浏览器42=**634/634**，累计3138文件ZIP SHA `1953c645c8769afb1401a9fd29fac324a0f32a109d7af6e58c6eaa92f96273e6`，Python/unzip双恢复各3138/3138 SHA、634/634 QA、0漂移。固定随机种子仅限隔离测试；不等于原始历史设备截图/真机/真实同源/读屏/高清逐笔认证，T00仍accepted=false、Root 0/12，T01 0/25、T02 ID0、T05缺根未知。R246主线ZIP原始字节仍缺，R11/R12/R35及R12 20SVG仍缺；冻结HTML/176编码/正式SVG/用户存储未动。[R245F10证据](./evidence/v036-r245f10-t00-frozen-chromium-baseline-fork.md)。

**R245F9 / 原始T00（冻结基线外部SHA钉值，独立分叉，非验收）：** 从R245F8真实ZIP 3119/3119逐成员SHA继承；隔离复现R2旧验证器允许同步修改V0.35 HTML和T00 JSON后仍14/14错误通过。新增独立6份冻结字节SHA钉值及Node三快照逐字节重建，旧同步伪造新版拒绝。继承582/582+新10/10=592/592选定QA；R245F9累计3128成员ZIP SHA `d3d81e594527f24703697f5626bb34f29964142ca8fe297061a5f4edbcfe0f21`，Python/unzip双恢复各3128/3128 SHA、592/592 QA、0漂移。T00仍缺真实既有Storage样本/原始设备截图来源，accepted=false；Root 0/12，T01 0/25、T02批准ID0、T05缺根未知。R246主线ZIP字节缺失；R11/R12/R35及R12 20SVG缺失。真实同源/读屏/真机/高清逐笔/完整历史not-run；冻结HTML、2008 JPEG、176编码、正式SVG、生产入口、用户Storage未动。[R245F9证据](./evidence/v036-r245f9-t00-pinned-freeze-provenance-fork.md)。


**R245F8 / 原始T03（异步SHA字节快照竞态修复，隔离分叉，非认证）：** 真读R245F7累计ZIP SHA `a8d0c3aed1ae7c315c4a1bab742ad591bd508cb8dbb977ecce4112bcedbaa405`，3110/3110逐成员SHA继承。独立Node WebCrypto重现旧门禁在digest后/JSON解析前调用者同长度改写R50/R54原始buffer，将首项`金`改为`木`仍错误接受151实例伪目录；R245F8同步快照字节后同一伪造被拒绝，合法源即使调用者异步修改也正确接受。继承定向570/570+新增12/12=582/582；3119文件累计ZIP SHA `009310ce79cb62082150d2930ab4333d137d57e54cba86138dc2ef2c89d8a77e`，Python/unzip双独立恢复各3119/3119 SHA及582/582 QA、0漂移。R245F7完整选定2167曾尝试但超时，不计通过；本地Chromium导航blocked，历史全量/真实同源/读屏/真机/合法高清逐笔not-run。R246主线ZIP仍缺；R11/R12/R35及R12 20SVG仍缺。T01 0/25、T02批准ID0、T05缺根未知、Root 0/12 Accepted；冻结入口/176编码/用户Storage未动。[R245F8证据](./evidence/v036-r245f8-t03-atomic-byte-snapshot-fork.md)。

**R245F7 Root T03（冻结151 SVG输入原始字节钉定，独立分叉、非认证）：** 复现R245F6在source/vector/candidate三者一致被篡改时仍接受的来源自洽伪造；新增WebCrypto SHA256原始字节门禁，分别钉定R50/R54输入，并拒绝候选目录额外顶层权威字段。R245F6父ZIP3099/3099 SHA继承；旧选定2150/2150+新增Node17/17=2167/2167；R245F7累计3110成员ZIP SHA `a8d0c3aed1ae7c315c4a1bab742ad591bd508cb8dbb977ecce4112bcedbaa405`，Python/unzip双恢复各3110/3110 SHA与2167/2167 QA，QA后0漂移。Chromium独立127.0.0.1因管理员策略blocked（0通过），高清同源/真机/读屏/完整历史QA/生产集成not-run；R246主线ZIP未取得，保持独立分叉；Root T00–T11仍0/12 Accepted，T01 0/25、T02批准ID0、T05缺根未知，冻结入口/176编码/用户Storage未动。[R245F7证据](./evidence/v036-r245f7-t03-pinned-source-byte-fork.md)。


**R245F6 Root T03（151旧SVG目录逐字段来源绑定，隔离预集成，非认证）：** 复现R62旧auditCatalog错误接受Path替换、draft assetId替换、byKey成员顺序污染及微小transform偏移；新门禁按R50/R54冻结输入重建151实例/25键目录并逐字段核对，显式待审光学校正需重新安全推导。R245F5父ZIP3090/3090 SHA继承；新增Node25/25+旧选定2125/2125=**2150/2150**；R245F6累计3099成员SHA `be4e95ee257a6f9d61bfd11974bc69458f80b0f4fedf99556f94185d80674a5f`，Python/unzip双恢复各3099/3099 SHA与2150/2150 QA，QA后0漂移。R246原始ZIP仍缺，故为独立分叉；T03未集成正式HTML，T01认证0/25、T02正式ID0、T05缺根未知、Root 0/12 Accepted；真机/读屏/同源迁移/高清许可/历史全量/仓库verify_repo not-run。[R245F6证据](./evidence/v036-r245f6-t03-strict-frozen-catalog-attestation-fork.md)。


**R245F5 Root T01/T02（第三方高清候选字节取得与版权隔离，非认证）：** GitHub连接器真读 CNMan 2583×1363 JPEG 357376字节，SHA256 `ca0afcb4d3d2ee47d34bc78751b230917d0113ec58497135677265ecc449359b`；与冻结2008彩色1536×1086图不是同源高低清版，仓库声明权利归王码公司/请勿商用，禁止公开打包或签发正式SVG。真读R245F4父ZIP3083/3083 SHA，旧2105+新20=2125/2125选定QA，累计3090文件ZIP SHA `e9a08e0ac401db814bd8fafd0ae5127edf902c8dcc4e0cd7db9cde95680faca0`，Python/unzip双独立恢复各3090 SHA及2125 QA，0漂移。R246原始ZIP仍缺，故R245F5独立分叉；高清同源许可/逐笔、读屏/真机/历史全量not-run，T01 0/25、T02 ID0、T05缺根未知、Root 0/12 Accepted。冻结入口/176编码/用户Storage未动。[证据](./evidence/v036-r245f5-external-highres-rights-gate-fork.md)。


**R245F4 / 原始T01/T02（来源异步导入原子性，非验收）：** 真实Chromium复现R245F3的来源撤销与`File.text()`异步导入竞态；R245F4来源epoch复核阻断过期导入、同SHA重验亦阻断，保留已有草案。R245F3父3073/3073 SHA，R245F4累计3083双独立恢复SHA及2105/2105选定QA；main R246 ZIP缺字节，独立分叉未合并。T01 0/25、T02批准ID0、Root 0/12 Accepted。[证据](./evidence/v036-r245f4-source-epoch-atomic-import-fork.md)。


**R245F3（2026-10-31，Root T01/T02隔离分叉，非认证）：** 真实Chromium复现R245F2工作台可加载已改字节JPEG/已改内嵌注册表，却仍导出冻结来源SHA；新隔离工作台验证实际JPEG字节和内嵌注册表SHA后才显示并允许描记、导入/导出，支持file://手动原图校验与便携SHA256。R245F2父ZIP3065/3065继承；旧1387+F1审计508+F2浏览器166+新增23=**2084/2084**选定QA，额外新工作台旧浏览器回归166/166；累计3073文件ZIP SHA `cbb044d5697d2769a8ae3f7098d8d86dc0ea816983cd9880c114c7f489835f74`，Python/unzip双恢复各3073/3073 SHA与2084/2084 QA、QA后0漂移。main R246原始ZIP仍未取得，**非R247连续主线**。T01 0/25、T02批准ID0、T05缺根未知、T00–T11 0/12 Accepted；合法高清逐笔/真机/读屏/历史全量not-run。[证据](./evidence/v036-r245f3-source-byte-provenance-fork.md)。


**R245F2（2026-10-31，Root T01/T02隔离分叉，非R247、非认证）：** 从R245F1累计ZIP（3055/3055 SHA）独立继承，新增全25键来源像素/连线跨其他精确裁框失败关闭工作台；33/52跨来源风险案件逐案真实Chromium拒绝活体误描记及伪造导入，M04/06/07/08四个已知污染点拒绝，A:6端点合法但线段穿过A:2精确框时拒绝。继承旧1387+F1审计508+新增166=**2061/2061**选定QA，累计3065文件ZIP SHA `6ca8385ef8db6582f44044d6c85196f36dbe7cd4469150c48a0cbf9fcfeb0ecd`，Python/unzip双独立恢复各3065/3065 SHA、2061/2061 QA、QA后0漂移。GitHub main已有R246但原始累计ZIP未取得，**本分叉不冒充R247、不覆盖main**；同框别名暂保守拒绝描记，非笔画归属裁决。T01 0/25、T02批准ID0、T05缺根未知、T00–T11 0/12 Accepted；合法高清逐笔/真机/读屏/完整历史not-run。[证据](./evidence/v036-r245f2-allkey-cross-source-stroke-guard-fork.md)。


**R245F1（隔离审计分叉，非R247、非认证）：** GitHub main 已有R246，但本次运行未取得R246累计ZIP，不能冒充连续继承；以实测R245父包3044/3044 SHA创建独立证据分叉。25键170来源/52案件交集审计：86对裁框接触（8不同精确框交叠、10同框历史别名、68仅±7px上下文），33/52案件可能触及未列入本案的其他来源精确框；仅几何风险，不等于笔画错误或正式认证。旧选定1387+新508=1895/1895，累计3055文件ZIP SHA 9c416c40cf0d59967e87c59c206a1cfd1ed9dc7b8e0ec1e53a4df6131d38d548，Python/unzip双恢复各3055 SHA、1895 QA、0漂移。R246四个M shadow防护未被本分叉覆盖，需先取得R246原始ZIP再移植。T01 0/25、T02批准ID0、T05缺根未知、Root 0/12 Accepted；真机/读屏/高清许可/历史全量not-run。[分叉证据](./evidence/v036-r245f1-cross-source-pixel-ownership-fork.md)。


**R246 Root T01/T02（M四项来源像素跨候选污染修复，非认证）：** R245父ZIP3044/3044逐SHA继承；真实Chromium复现M-vis-04/06/07/08四项虽来源ID正确，但±7px上下文可描记其他候选精确裁框像素且导入仍接受。R246在活体描记/结束/导入三处保守隔离跨候选精确框像素，四项R245 4/4错误接受、R246 4/4拒绝，52案件映射不变；旧1387+新106=**1493/1493**选定QA。累计3054文件ZIP SHA `3f2c863af624bee7f9e2c96c3c0262fbb9af777924264612b49da2cc948da6fe`，Python/unzip双恢复各3054/3054 SHA及1493/1493 QA，QA后0漂移。仅隔离about:blank，**非来源逐笔认证**；高清许可、真实同源/真机/读屏/历史全量not-run，T01 0/25、T02批准ID0、T05缺根未知、Root 0/12 Accepted；冻结入口/176编码/用户Storage未动。[R246证据](./evidence/v036-round246-t01-t02-M-cross-crop-pixel-ownership.md)。


**R245 Root T01/T02（M四项来源案件身份绑定修复，非认证）：** 实际读取R244累计ZIP SHA `33e45a7924f10292e5e0794535e8a240b2cfebd913e55462b010c38844847d82`，3034/3034成员继承。真实Chromium复现R244把M shadow-04案件错误关联M-vis-01笔画且导出/导入仍接受；根因是4个shadow案件evidence原始ID与R144来源观察前缀不一致，且描记工具没有验证案件证据成员关系。R245只为M04/06/07/08建立显式别名，所有52案件描记与导入强制证据绑定、错误同键来源拒绝且保留旧草案。旧选定1299+新Chromium88=**1387/1387**；R245累计3044文件ZIP SHA `ae9b2181f8279db4e2fdebadc24f23da828193c0a6d6ebd806c06e44ce24626f`，Python/unzip双独立恢复各3044/3044 SHA及1387/1387 QA、QA后0漂移。仅隔离about:blank、非合法高清逐笔/正式SVG/真实读屏或真机；完整历史not-run，T01 0/25、T02批准ID0、T05缺根未知、Root 0/12 Accepted；冻结入口/176编码/用户Storage未动。[R245证据](./evidence/v036-round245-t01-t02-M-shadow-case-binding.md)。


**R244 Root T01/T02（原图笔画自由描记与自导出修复，非认证）：** 实际读取R243累计ZIP 3024/3024 SHA，真实Chromium复现R243允许130点描记完成但自身JSON导出无法导入（校验上限128点）；新增按住拖动的真实pointer自由描记、原生JPEG坐标连续采样、pointercancel/失焦取消、128点上限，保留点击两点再结束功能。旧选定1268+新Chromium 31=1299/1299；R244累计3034文件ZIP SHA `33e45a7924f10292e5e0794535e8a240b2cfebd913e55462b010c38844847d82`，Python与系统unzip双独立恢复各3034/3034 SHA、1299/1299选定QA，QA后0漂移。仅about:blank注入冻结JPEG，不是合法高清逐笔认证/正式SVG/真实读屏或真机；历史全量not-run，T01 0/25、T02正式ID0、T05缺根未知、Root 0/12 Accepted；冻结入口/176编码/用户Storage未动。[R244证据](./evidence/v036-round244-t01-t02-freehand-source-stroke-roundtrip.md)。


**R243 Root T01/T02（来源像素逐笔描记工具，非认证）：** R242父累计ZIP 3015/3015逐文件SHA一致；在R240 25键/170观察/52案件工作台新增人工笔画中心线描记、原生1536×1086坐标与裁框RGB SHA绑定、完整图/键位视图不变坐标、撤销与未批准JSON导入导出；10类伪造/越界输入拒绝且保留原内存。旧选定1227+新Chromium about:blank真实鼠标41=1268/1268 QA；R243累计3024文件ZIP SHA `eafddc9d9b028a97a55628d7326e771cd2dd63b6237757450b2292a235d24964`，Python/unzip双独立恢复各3024/3024 SHA、1268/1268 QA、QA后0漂移。仅两点M键测试草案，**不代表逐笔认证/正式SVG**；合法同源高清许可、真机/读屏/历史全量not-run；T01 0/25、T02正式ID0、T05缺根未知、Root 0/12 Accepted；冻结入口和用户Storage未动。[R243证据](./evidence/v036-round243-t01-t02-source-pixel-stroke-tracing.md)。


**R242 Root T01/T02（36个旧未匹配槽的原图逐项视觉分流，非认证）：** 真读R241父ZIP 3007/3007 SHA；冻结2008 JPEG与R144来源注册表钉SHA，36/36原裁框RGB及±7px上下文独立核验。人工低清视觉初筛6个右上圈注候选（D:1/E:7/F:2/H:4/J:4/N:7）、2个同框圈注边缘否定（E:1/E:8）、28项笔画归属未决；不自动改分类、Path或ID。旧1074+新153=1227/1227选定QA；R242累计3015文件ZIP SHA `d5020f167bc5d38dc0255678361de192384841d0a061c80c6ac583e0b8241527`，Python/unzip双恢复各3015 SHA与1227 QA，QA后0漂移。高清许可/逐笔、真实读屏/真机/历史全量not-run；T01 0/25、T02正式ID0、T05缺根未知、Root 0/12 Accepted；冻结入口和用户Storage未动。[R242证据](./evidence/v036-round242-t01-t02-36-unmatched-triage.md)。


**R241 Root T01/T02（M四个未绑定微形原图裁框上下文复核，非认证）：** 真读R240父ZIP 3000/3000 SHA；对M-vis-04/06/07/08原始裁框逐RGB SHA复验，实际并排审阅精确框与±7px上下文，发现低清原框边界邻近仍有深色笔画结构，不能把裁框当完整独立字根或直接生成Path。四项保持needs_highres、无替代裁框、无ID签发。旧R239 852+R240 190+新R241 32=1074/1074选定QA；R241累计3007文件SHA `9c720309427a10c86af633e1157c8b993474df14a37bf065b3df44b0bd21d8a4`，Python/unzip双独立恢复各3007/3007 SHA及1074/1074 QA、QA后0漂移。Chromium仅about:blank注入原始JPEG字节；合法同源高清逐笔、真机/读屏/历史全量not-run。T01 0/25、T02 ID0、T05缺根未知、Root 0/12；冻结入口/用户存储未动。[R241证据](./evidence/v036-round241-t01-t02-M-microform-context.md)。


**R240 Root T01/T02（25键原图人工复核工作台，非认证）：** 真实继承R239父ZIP 2989/2989 SHA，复验冻结2008 JPEG及R144注册表，170/170原生RGB裁框SHA；新增独立25键170观察/52待审案件审阅HTML（M12观察/8案件、无存储、仅导出未批准意见）。旧852+新190=1042/1042选定QA，Chromium为about:blank注入原始JPEG字节，file://被管理员阻断；R240累计3000文件SHA `4e6c646f9b48f3e66a7de681fb485bb5de84912498bbe746caf803235120a208`，Python/unzip双恢复各3000 SHA及1042 QA、QA后0漂移。T01认证0/25、T02批准ID0、T05缺根未知、Root 0/12；高清许可/逐笔、真机/读屏/完整历史not-run，冻结入口与用户存储未动。[R240证据](./evidence/v036-round240-t01-t02-source-review-workbench.md)。


**R239 Root T04（真实同源双标签并发恢复，非验收）：** 真实GitHub Actions独立127.0.0.1 Chromium Web Locks/localStorage/WebCrypto 22/22（run 41052963001），将R238 Node FakeStore并发冲突与恢复扩展至真实双标签；25键156旧槽仅合成数据。R238父ZIP 2984/2984逐SHA继承；R239累计2989文件SHA `1c00ab27ca12bb13d16b26d53e1cc3d37c1bb2c574756a1349c6d7ac08aa99c0`，Python/unzip双恢复各2989 SHA、852/852选定旧QA及QA后0漂移。本地真实同源仍管理员阻断；生产用户迁移、高清逐笔、真机/读屏/完整历史not-run。T04未Accepted，Root 0/12，T01 0/25、T02 ID0、T05缺根未知；冻结入口/176编码/用户存储未动。[R239证据](./evidence/v036-round239-t04-real-cross-tab-ci.md)。


**R238 Root T04（并发冲突隔离，非验收）：** 真读R237父ZIP SHA `68f84281940ed43892b71408e95ab3259268f5efdaa13e7f3db42366072a7d6a`，2976/2976逐成员继承；实际25键156槽签发+R192事务内核的Node私有Map双实例并发、崩溃日志、非协作写入冲突及恢复拒绝新增17/17，继承旧835/835，共852/852选定QA。R238累计2984文件SHA `28ea55adeb80a8309bb9d66ee077a4d559f9b7f8c54cfa76d0eb1698bf506580`，Python/unzip双恢复各2984 SHA及852 QA、QA后0漂移。本地真实同源仍blocked，R238真实浏览器not-run；生产迁移、高清逐笔、真机/读屏、历史全量not-run。T04未Accepted，Root 0/12，T01 0/25、T02 ID0、缺根未知；冻结入口及用户Storage未动。[证据](./evidence/v036-round238-t04-concurrent-recovery-conflict.md)。


**R237 / 原始T04追踪补充（非验收）：** 25键156旧槽合成v16编辑经实际R148/R152/R178/R179签发+R192事务核心验证；远端真实同源Chromium 24/24（[run 41037798793](https://github.com/tims-SP/glyphspace/actions/runs/41037798793)），本地管理员阻断；继承809+新增26=835/835选定QA，R236父2965 SHA继承、R237累计2976双独立恢复SHA/QA。未迁移用户数据、未批准永久ID，T02/T03依赖未Accepted，T04仍`accepted=false`，全部Root 0/12。[证据](./evidence/v036-round237-t04-fullslot-real-origin.md)。


**R236 Root T01/T02（高清坐标来源证据重算，非认证）：** 真实复现R235 crosswalk未钉SHA且只检查数量，篡改高清裁框四角/裁框ID/JPEG SHA仍错误接受3/3；新增R119/R156/R209/R218/R219来源字节钉值和独立重算门禁，逐字段复验161/161裁框JSON及161/161 CSV映射，旧3/3伪造新3/3拒绝。R235父ZIP2955/2955逐SHA继承，旧758+新51=809/809选定QA；R236累计2965成员ZIP SHA `126ed92fff3db578e6726abf41483e40f15ce35062e4b81b1ad7844f1edc6e30`，Python/unzip双独立各2965 SHA及809 QA、QA后0变化。仅来源投影证据完整性，非高清逐笔/许可/同源认证；T01 0/25、T02批准ID0、T05缺根未知、Root 0/12 Accepted，真实同源/真机/读屏/历史全量未验收，冻结入口与用户存储未动。[R236证据](./evidence/v036-round236-t01-t02-highres-provenance-replay.md)。


**R235 Root T01/T02（共享来源裁框扇入完整性审计，非认证）：** 真读R234父ZIP2947/2947 SHA，重建R156/R209/R218/R219证据图：166草案候选、170观察、161裁框；发现E1组/K3组共4个共享裁框扇入（9候选端点）。R209显式mustNotMerge只列2组，漏列K:0与K:4的2组，且K:2/K:3组漏列physical-lower-left第三候选；新增R235独立失败关闭门禁阻止所有共享裁框自动合并或签发ID，M四无旧槽候选仍隔离。旧717+新41=758/758选定QA，R235累计2955成员ZIP SHA `1e956e197b709c12e4f3d5eff67180e08cd95a7b9990b97abb99d4ff78b57542`，Python/unzip双独立各2955/2955 SHA及758/758 QA、QA后0变化。仅证据别名审计，非逐笔认证；T01 0/25、T02批准ID0、T05缺根未知、T00–T11 0/12 Accepted；高清许可/同源、真同源/真机/读屏/历史全量未验收，冻结入口、176编码、用户存储未动。[R235证据](./evidence/v036-round235-t02-source-crop-fanin-identity-guard.md)。


**R234 Root T01/T02（第三方3508×2480高清候选原始ZIP/JPEG独立字节复验，非认证）：** 已经GitHub连接器真实读取06wb仓库996823字节ZIP，独立SHA `fb7a9984...`、DEFLATE解出1348865字节JPEG SHA `47c5d53f...`、CRC `e90cbe82`、3508×2480均匹配R114；发现上游网页高清ZIP href全角括号与仓库实际半角括号文件名不一致。图片许可/官方来源未确认，原图字节只在连接器内存校验，未本地保存/打包/公开分发，逐笔未审。父R233 2939/2939 SHA继承；R234累计2947文件ZIP SHA `dce2085e82a92c3b75830d710d681f39e49e3df25366680244de3d537b6a5b22`，Python/unzip双独立2947/2947 SHA及来源定向旧新717/717 QA，QA后0变化；R233递归Chromium在unzip恢复超时不计入双恢复。T01正式0/25、T02永久ID0、缺根未知、T00–T11 0/12 Accepted；真同源/真机/读屏/高清逐笔/历史全量blocked或not-run，冻结入口、176编码及用户Storage未动。[R234证据](./evidence/v036-round234-t01-highres-byte-reverification.md)。

**R233 Root T03（退出校准后的残留click隔离，非验收）：** 真实Chromium CDP复现R232在触点未释放时disarm导致训练inputIndex误前进（390×844 DPR2、1280×800 DPR1）；R233追踪键盘指针ID，在disarm/dispose前安装限时click守卫，阻断已中止指针，下一次正常输入不受影响。继承旧220+新浏览器62+静态25=307/307选定QA；父R232 ZIP 2926/2926逐SHA，R233累计2939成员ZIP SHA `f55de3d71259ea75488b1cf5f3593c420e3e55ae8179b8da07fd7a860059c4f6`，Python/unzip双独立各2939 SHA及307 QA、QA后0变化。仅about:blank/CDP非真机；真同源blocked、读屏/高清逐笔/历史全量not-run；T01 0/25、批准ID0、T03生产未集成、缺根未知，Root 0/12 Accepted；冻结入口/176编码/用户Storage未动。[R233证据](./evidence/v036-round233-t03-post-disarm-ghost-click-guard.md)。

**R232 Root T03（真实触屏输入隔离修复，隔离非验收）：** 真实Chromium CDP touch复现R231校准模式误触触发训练输入2/2（390×844 DPR2、1280×800 DPR1）；R232按触点坐标命中字根、拦截三视图合成click、第二手指取消光学事务，显式disarm后触屏训练恢复。旧选定149+旧故障复现2+新触屏48+新静态21=220/220；R231父ZIP 2912/2912 SHA继承，R232累计2926文件ZIP SHA `b22ec8f6f711dcc651db624bbb8e1ab153babb2923ef39a2ac845cab05c0a1ca`，Python/unzip双独立各2926 SHA及220 QA、QA后0变化；unzip首次旧鼠标QA偶发失败，单独重跑及完整选定重跑通过。about:blank/CDP模拟触屏非真机；真实同源blocked/not-run，读屏/高清逐笔/历史全量not-run；T01 0/25、T02正式ID0、T03生产未集成、T05缺根未知，Root 0/12 Accepted；冻结入口、176编码及用户Storage未动。[R232证据](./evidence/v036-round232-t03-real-touch-input-isolation.md)。


**R231 Root T03（真实指针事件隔离接入，非验收）：** 复现R230只有JS beginDrag/finishDrag API而V0.35 .rootglyph禁用pointer-events，新增显式arm的真实Chromium pointerdown/up捕获与full/focus/mini光学事务，Escape/blur/cancel/越界失败关闭、disarm恢复普通输入；桌面DPR1/手机视口模拟DPR2真实page.mouse 50/50、新静态28/28、继承旧4020/4020，共4098/4098选定QA。父R230 2900/2900逐SHA继承，R231累计2912文件ZIP SHA `f283ee92bf297a1e99e402cfba34502c25a9ceb9aa7a50e61a36cc15b1abac82`，Python/unzip双独立各2912 SHA及4098 QA、QA后0变化。about:blank非真同源，正式T03生产未集成；T01 0/25、T02永久ID0、T05缺根未知、T00–T11 0/12 Accepted；真同源blocked/not-run、真机/读屏/高清逐笔/历史全量not-run，冻结入口及用户Storage未动。[R231证据](./evidence/v036-round231-t03-real-pointer-events.md)。


**R230 Root T03（冻结V0.35真实三视图指针→100×100/inkBBox光学校准，隔离非验收）：** R229父2888/2888逐SHA继承；真实Chromium 1280×800 DPR1及390×844 DPR2验证151旧可视实例inkBBox/ink-center、full/focus/mini指针逆CTM、事务同步、折叠重绘与失败拒绝；折叠full SVG隐藏导致空BBox的真实缺陷已修复。旧3949+新71=4020/4020选定QA，累计2900文件ZIP SHA `7930431d36db4f28cab00fb0444b6eb203ce28f6b66ebef2ad798505ba39c6aa`，Python/unzip双独立各2900 SHA与4020 QA、QA后0变化。真实同源blocked/not-run；T01 0/25、T02正式ID0、T05缺根未知，T00–T11 0/12 Accepted；生产/高清逐笔/真机/读屏/历史全量未验收，冻结入口及用户Storage未动。[R230证据](./evidence/v036-round230-t03-real-v035-pointer-inkbbox.md)。


**R229 Root T03（隔离V0.35三视图适配器安全卸载/重挂载，非验收）：** 实际Chromium复现R228 dispose后M/V偏移残留且无法再次挂载；R229先事务清除再断监听/释放标志，第三视图故障回滚并可重试。父R228 2876/2876逐SHA继承；旧选定3848+R228 58+R229新43=3949/3949定向QA，累计2888文件ZIP SHA `eaa5226d561f13343343ce2c7d8412853ab917739ccdd076f11a2b194d70cb26`，Python/unzip双独立各2888 SHA与3949 QA、QA后0变化。真实同源仍ERR_BLOCKED_BY_ADMINISTRATOR；T00–T11 0/12 Accepted、T01 0/25、T02正式ID0、T05缺根未知，生产/高清逐笔/真机/读屏/历史全量未验收，冻结入口及用户Storage未动。[R229证据](./evidence/v036-round229-t03-preview-lifecycle-atomic-dispose.md)。


**R228 Root T03（真实冻结V0.35应用三视图隔离光学校准接入，非验收）：** 不再只使用构造SVG演示视图；实际Chromium在冻结V0.35完整应用中验证151可视根/156旧槽，完整键盘、动态焦点、折叠迷你键盘的M/V预览偏移一致，重绘/折叠后同步；176旧编码和真实输入保持，4类非法编辑拒绝及第三视图写入故障回滚。R227父2863/2863 SHA继承，R228累计2876成员ZIP SHA `d9cd104fa5709a1a281d88bfda986e3088c0cced8e5b0383feee692e7197e1dd`，Python/unzip双独立各2876 SHA与3906/3906选定旧新QA、QA后0变化。about:blank隔离测试，真实同源仍ERR_BLOCKED_BY_ADMINISTRATOR，正式生产未集成；T00–T11 0/12 Accepted、T01 0/25、T02正式ID0、T05缺根未知，读屏/真机/高清逐笔/历史全量not-run，冻结入口及用户Storage未动。[R228证据](./evidence/v036-round228-t03-real-v035-runtime-preview.md)。


**R227 Root T03（隔离SVG轮廓计算样式漂移修复，非验收）：** R226遗漏stroke-linecap/join/dash、fill/clip-rule等CSS绘制属性，真实Chromium复现旧12/12错误接受，R227增加16个计算样式指纹，12/12正确拒绝；真实SVG仅dasharray变化产生3802个截图RGB差异像素。父R226 2849/2849逐SHA继承，R227累计2863成员ZIP SHA `2a86a5fcedcc29fcb93859f54611ca91589ea042fc1407327a50a4513fb11f1d`，Python/unzip双独立各2863/2863 SHA及3848/3848选定旧新QA、QA后0变化。递归旧套件超时不计pass，历史全量not-run；真实同源临时profile `ERR_BLOCKED_BY_ADMINISTRATOR`，读屏/真机/高清逐笔not-run；Root T00–T11 0/12 Accepted、T01 0/25、T02正式ID0、T05缺根未知，冻结入口与用户Storage未动。[R227证据](./evidence/v036-round227-t03-contour-style-guard.md)。

**R226 Root T03（隔离CSS计算样式漂移守卫，非验收）：** 实际继承R225累计ZIP 2834/2834逐文件SHA；真实Chromium复现R225对7类仅通过外部CSS样式表修改的错误接受（group透明度、path笔画宽度、SVG显示、section透明度、host变换、path填色、SVG滤镜），R226新隔离模块冻结host/3 section/75 SVG/453 g/459 path的计算样式，异步计划前后重检，旧7/7错误接受、新7/7拒绝；旧8169+新3718+对抗30+静态16=11933/11933选定QA，累计2849文件ZIP SHA `473f99c16734dff9948a526ab44894caa2132057143315eff8c12ecbcbf50799`，Python/unzip两次独立恢复各2849/2849 SHA及11933/11933 QA，QA后0变更。独立临时Chromium profile的127.0.0.1真实同源仍`ERR_BLOCKED_BY_ADMINISTRATOR`；T01 0/25、批准ID0、缺根未知、T00–T11 0/12 Accepted，正式生产未集成，读屏/真机/历史全量not-run，冻结入口/用户存储未动。[R226证据](./evidence/v036-round226-t03-computed-css-style-drift-guard.md)。

**R225 Root T03（隔离DOM拓扑/属性漂移修复，非验收）：** 真实Chromium复现R224对伪造SVG组、group opacity、SVG缩放、section隐藏、组重排五类错误接受；R225冻结组/视图DOM拓扑和非transform属性、异步计划后再次校验，五类均拒绝，旧三视图3718断言回归通过。父R224 2821/2821逐SHA继承；R225累计2834文件ZIP SHA `07ac163dd8dedb93b2c8520b5fbdd98642f7beb97c1ed203c895f5b195a63f72`，Python/unzip双独立各2834 SHA与8169/8169选定QA，QA后0变化；递归R224套件尝试超时不计pass、历史全量not-run。仍是about:blank+Python SHA桥接，真同源blocked/not-run、真机/读屏not-run，T01 0/25、正式ID0、缺根未知、Root T00–T11 0/12 Accepted；冻结入口及用户存储未动。[R225证据](./evidence/v036-round225-t03-live-svg-dom-topology-guard.md)。

**R224 Root T03（隔离DOM光学校准事务，非验收）：** R223父ZIP2812/2812逐SHA继承；R198 SHA绑定151旧Path草案在真实Chromium about:blank挂载25键×三视图=75 SVG/453 g/459 path，M/V两实例原位更新6组transform，453节点/Path及焦点不变；第三视图注入失败回滚、Path篡改/墨迹越界拒绝。旧1701+浏览器7场景3718断言+静态14=5433/5433选定断言，R224累计2821文件ZIP SHA `a325e9beed8ea8e678f4057589168e8ece0596134845ff0f60201328ac353e72`，Python/unzip双独立各2821 SHA与5433 QA，QA后0变化。about:blank SHA委托Python hashlib，真实同源仍管理员阻断；来源0/25、ID0、缺根未知、Root 0/12 Accepted，真机/读屏/历史全量not-run；冻结入口及用户存储未动。[R224证据](./evidence/v036-round224-t03-live-svg-optical-transaction.md)。

**R223验收边界：** 全25键参考矩形和161来源裁框的原生覆盖、36未匹配票据、M四独立未绑定裁框只属来源审阅，不代表真实缺根、笔画归属、正式ID或SVG生产集成。1701/1701选定QA、2812累计成员双独立恢复通过；真实同源blocked，许可/高清逐笔/真机/读屏/完整历史not-run；T00–T11仍0/12 Accepted，T01 0/25、T02批准ID0。


**R222原始Root T01/T02追踪（T05仅来源前置，非验收）：** 对R219冻结来源索引与2008 JPEG进行原生字节SHA核验，B/J/V/X 29裁框按真实像素的覆盖sourceCropId集合划分38个互斥成员组；多框覆盖B198/J66/V377/X100共741像素，其中V三重覆盖33像素。每组记录源坐标/RGB SHA与四邻域组件，4张审阅卡不进入键盘；不推断笔画、身份、缺根。R221父2785/2785 SHA、选定旧685+新331=1016/1016，R222累计2800双独立SHA/QA恢复。T01 0/25、ID0、缺根未知、Root 0/12 Accepted。 [证据](./evidence/v036-round222-t01-t02-disjoint-native-crop-membership.md)。

**R221 Root T01/T02（冻结JPEG原生裁框重叠像素归属，隔离非验收）：** 父R220累计ZIP2773/2773逐SHA继承；重新验证161/161原生裁框RGB与R219索引全字节SHA，B/J/V/X共8对裁框重叠，阈值100下6对有低清暗像素、按键去重B10/J8/V17/X1共36；V多框覆盖377像素且最多三重。V一对57px及X一对32px交集阈值140无暗像素，均不证明无真实笔画重叠或身份归属。旧628+新57=685/685选定QA，R221累计2785文件ZIP SHA `6ee6599610f3ade340bed5eb4345defc894eeaac097ba2a1f08706338b50e3ef`，Python/unzip双独立2785 SHA及685 QA、QA后0变更。高清原始字节/许可/逐笔未完成；正式T01 0/25、T02 ID0、缺根未知、Root 0/12 Accepted；真同源/真机/读屏/历史全量not-run。 [R221证据](./evidence/v036-round221-t01-t02-native-overlap-pixel-ownership.md)。

**R220原始Root T01/T02追踪（T05来源前置，非验收）：** 冻结2008 JPEG与R219 161原生裁框逐RGB SHA一致，M四未绑定来源独立；100阈值边缘深色100/161、B/J/V/X低清框几何交集8对，均只用于人工逐笔复核优先级，不能认证笔画或独立身份。R119 p95经验残差换算3高清像素启发式留白，不保证全覆盖。父R219 2762 SHA继承，选定旧588+新40=628 QA，R220累计2773文件双独立SHA/QA恢复。T01 0/25、ID0、缺根未知、Root 0/12 Accepted。 [证据](./evidence/v036-round220-t01-t02-native-crop-boundary-risk.md)。

**R219 Root T01/T02（25键高清候选坐标索引，隔离非验收）：** 基于R119真实ORB仿射与R156来源账本，新增25键170观察/161独立裁框的3508×2480候选坐标交叉表（原生RGB SHA、四角投影、整数包络、R209草案UID）。R119五组风险框误差<0.005高清像素；M四独立未绑定框及E/K同裁框异旧SVG身份仍隔离。R114/R119远端CI作业success已复核，但高清原始字节未落地本地、许可未确认、逐笔not-run。父R218 2751/2751 SHA，选定旧518+新70=588/588；R219累计2762成员ZIP SHA `5df9e395400857888a150791eb2c0e7db1ad0357e085a988bb8e075489fe6f0d`，Python/unzip双独立恢复各2762 SHA及588 QA。正式T01 0/25、永久ID0、缺根未知、Root 0/12 Accepted；真同源/真机/读屏/历史全量not-run。 [R219证据](./evidence/v036-round219-t01-t02-25key-highres-coordinate-crosswalk.md)。

**R218原始Root T01/T02追踪（非验收）：** R209 166个草案身份+R206 50票据/52关联建立可执行来源/许可/逐笔/语义/独立复核缺口门禁；25键M优先采集CSV、E/K两组同裁框异SVG冲突保持分离，166/166阻断且0正式ID。父R217 2740 SHA继承，选定旧229+新289=518/518，累计R218 2751成员双独立SHA/QA恢复。T01正式0/25、Root 0/12 Accepted，真同源/真机/读屏/完整历史not-run。[证据](./evidence/v036-round218-t01-t02-source-identity-readiness.md)。


**R217原始Root T03（非验收）：** R216根SVG CTM无法发现子组变换、Path d及CSS笔画变化；真实Chromium重现3个旧错误接受。新增只读子组几何指纹守卫，拖动前后验证组CTM/DOM/getBBox/计算样式，漂移取消令牌。父2727逐SHA，旧1696+新971=2667/2667；2740累计文件双独立SHA/QA复验。T03仍隔离、T00–T11 0/12 Accepted。[证据](./evidence/v036-round217-t03-pointer-group-geometry-drift.md)。

**R216原始T03（T08仅隔离输入前置）：** 新增真实浏览器指针client坐标到SVG 100×100局部坐标的逆CTM校准桥接，绑定R125/R160/R197的151历史草案路径SHA。25键Node42/42、Chromium about:blank 1510正向+12异常、静态24/24、继承311/311=1899/1899选定QA；2727成员双独立SHA/QA复验。仅草案光学校准，不是生产T03、正式T08或来源认证；T00–T11仍0/12 Accepted。[证据](./evidence/v036-round216-t03-pointer-to-optical-bridge.md)。

**R215 原始T03追踪（非验收）：** R214真实Chromium 40个已绘制黑像素落在CSS独立rotate裁剪的错误上界之外；R215隔离CSS个别变换守卫失败关闭。父2701 SHA继承、累计2713双独立SHA及311/311选定QA；非精确墨迹、非正式生产内核，T00–T11仍0/12 Accepted。[证据](./evidence/v036-round215-t03-css-individual-transform-guard.md)。


**R214 Root T03（SVG根视口裁剪保守上界，隔离非验收）：** R213未处理SVG根自身overflow，新增独立SVG viewport屏幕交集，保留原inkBBox，支持缩放及HTML+SVG双层裁剪；真实Chromium黑像素10000/19600/2500/0/200/4200案例，906旧SVG原始几何不变。父R213 2688/2688逐SHA继承，选定旧203+新Chromium40+静态18=261/261；累计2701文件ZIP SHA `d06b8400bece34bf9e6fb36ac1c88f7ff33df5e2ada15d2a04902d8de4a6c1da`，Python/unzip双独立恢复各2701 SHA与261 QA、QA后0变化。T03未生产集成、Root 0/12 Accepted、来源0/25、永久ID0、缺根未知；真实同源blocked，真机/读屏/历史全量not-run，冻结入口/Storage未动。[R214证据](./evidence/v036-round214-t03-svg-viewport-clipping.md)。

**R213 Root T03（缩放祖先overflow上界修复，隔离非验收）：** 真实Chromium发现R212在scale(.5)时屏幕可见500黑像素却报告仅10×15上界，漏掉真实墨迹；R213改用CSS subpixel border-box与屏幕缩放比率，scale(.5)修正为20×25，scale(2)为80×100，906旧SVG几何不变，旋转/透视等失败关闭。父R212 2675/2675 SHA继承，选定旧159+新44=203/203；累计2688文件ZIP SHA `5907af02850e0084528b3082f6524e9fd8750d20a88ecbcf9eeae7fb5aee7089`，Python/unzip双独立恢复各2688 SHA及203 QA、QA后0变化。T03未生产集成、Root 0/12 Accepted、来源0/25、永久ID0、缺根未知；同源blocked、真机/读屏/历史全量not-run；冻结入口/用户Storage未动。[R213证据](./evidence/v036-round213-t03-scaled-overflow-border-fix.md)。

**R212 Root T03（HTML overflow裁剪保守包络，隔离非验收）：** 修复R211一律拒绝合法overflow:hidden/clip/scroll祖先；新增真实Chromium矩形裁剪上界（保留原inkBBox，完全裁剪null），906旧SVG几何不变，截图黑像素10000→2000→0；父R211 2663/2663逐SHA继承，选定旧126+新33=159/159；累计2675文件ZIP SHA `4f4fd0283aa87dba0f95224c5e6afc5a11ca67b048ab8c263be5e79ce9e296ae`，Python/unzip双独立恢复各2675 SHA及159 QA、QA后0变化。R211递归670套件超时不计pass，完整历史全量not-run。T03未生产集成，Root 0/12 Accepted、来源0/25、永久ID0、缺根未知；同源blocked、真机/读屏not-run；冻结入口/用户Storage未动。[R212证据](./evidence/v036-round212-t03-rectangular-overflow-upper-bound.md)。
**R211 Root T03（HTML祖先绘制抑制，隔离非验收）：** 实际Chromium发现R210只检查SVG内祖先，HTML外层opacity=0/全裁剪时仍返回inkBBox，截图黑像素3200→0；新增HTML祖先computed-style失败关闭守卫。906组正常几何一致，11个外层反例拒绝（9个旧R210误接受），选定旧644+新Chromium14+静态12=670/670；父R210 2651/2651 SHA继承，R211累计2663文件SHA `ddc0127fe6317f1c9f336b00069766f5b1ea2ff5178be2e328024d4036a99739`，Python/unzip双独立恢复各2663 SHA及670 QA，QA后0变化。T03未生产集成，T01 0/25、永久ID0、Root 0/12 Accepted；同源blocked、真机/读屏/历史全量not-run；冻结入口及用户Storage未动。[R211证据](./evidence/v036-round211-t03-outer-html-ancestor-paint-gate.md)。

**R210 Root T03（有效绘制墨迹边界守卫，隔离非验收）：** 真实Chromium复现R200祖先opacity=0/全裁剪仍报告非空inkBBox，截图黑像素正常3200→不可见0；新增computed-style祖先/Path失败关闭守卫，906旧SVG组新旧正常几何一致、14/14对抗拒绝。父R209 2640/2640逐SHA继承；选定旧620+新Chromium12+静态12=644/644，R210累计2651文件ZIP SHA `12e329603696bd85991666c222e14f68124c920a8fb9effa2331661923433449`，Python/unzip双独立恢复各2651 SHA与644 QA、QA后不变。T03未生产集成，原始0/12 Accepted，来源0/25、永久ID0、缺根未知；同源blocked、真机/读屏/历史全量not-run；冻结入口/用户存储未动。[R210证据](./evidence/v036-round210-t03-effective-ancestor-paint-guard.md)。


**R209原始T01/T02追踪（T05依赖，非验收）：** R206 50票据→R208来源/旧SVG三向证据，166个独立草案候选（151旧可视+12无别名裁框+3 K混合），52条链接；E/K共享裁框各保留两旧Path身份，5关联槽排除，正式ID0。父2628/2628 SHA继承，选定旧554+新66=620/620，累计2640双独立SHA/QA；来源0/25、缺根未知、Root 0/12 Accepted。真同源blocked、真机/读屏/历史全量not-run。[证据](./evidence/v036-round209-t01-t02-typed-draft-identity-bridge.md)。


**R208原始T01/T02追踪（T05仅依赖证据，非验收）：** 冻结HTML 151实例/153 Path逐字节来源重算151 SHA，与R156 JPEG来源及R207匹配状态三向核对。36未匹配旧槽均有JPEG+旧SVG；15无旧别名观察分12纯无别名裁框与3 K混合裁框观察。E舟/用、K川/丨各同裁框但旧Path SHA不同，必须独立审阅，不能合并。父2613 SHA继承，累计2628双独立恢复各554/554选定QA；T01 0/25、永久ID0、缺根未知、Root 0/12 Accepted；真同源blocked，真机/读屏/历史全量not-run。[证据](./evidence/v036-round208-t01-t02-t05-three-way-source-vector.md)。


**R207原始T01/T02追踪（非验收）：** 156冻结旧槽=151可视+5关联；R156 155条带别名来源观察覆盖151可视槽（M四槽双观察），36/36旧未匹配槽均已有原图来源观察，不是没有来源；独立补充36来源证据字段，不改变R206 50票据ID或正式批准状态。旧424+新63=487/487，父2600 SHA继承、累计2613双独立恢复。正式0/12 Accepted、来源0/25、永久ID0、缺根未知；真同源blocked、真机/读屏/历史全量not-run。[证据](./evidence/v036-round207-t01-t02-legacy-source-reconciliation.md)。


**R206原始T01/T02追踪（非验收）：** 以R96/R156/R157/R196/R205原生来源建立12未绑定+36旧未匹配+2共享裁框冲突的50条非发布票据；K圈注/根身份分离待审、M四微框独立、E/K冲突不合并。R205父2586 SHA继承、累计2600双恢复424/424选定QA；没有永久ID批准或正式SVG、来源认证仍0/25，Root 0/12 Accepted；真同源blocked、真机/读屏/历史全量not-run。[R206证据](./evidence/v036-round206-t01-t02-semantic-arbitration-tickets.md)。


**R205 Root T01/T02追踪（非验收）：** 父R204 2569 SHA继承，原生JPEG 12未绑定裁框逐像素覆盖、6重叠区域RGB SHA、2同裁框冲突保留；旧306+新53=359/359、累计2586双独立恢复。来源0/25、正式ID0、缺根未知、Root 0/12 Accepted；无生产/Storage修改，真同源blocked、真机/读屏/历史全量not-run。[证据](./evidence/v036-round205-t01-t02-native-pixel-coverage.md)。

**R204 Root T01/T02（执行源码与历史审计字节锚，隔离非认证）：** 实际复现R203对R201/R202/R203可执行代码和R202历史审计/父清单共5类字节篡改仍误接受；新增父R203可信档案SHA绑定、执行前后失败关闭。父R203 2558/2558逐SHA继承，旧268+新增对抗26+静态12=306/306；累计2569文件ZIP SHA `a55b4b6a8e797e210496e45bf446b011913e394f06051863a3c39c874cb35c1b`，Python/unzip双独立恢复各2569 SHA和306 QA、QA后不变。T01 0/25、正式ID0、缺根未知、T00–T11 0/12 Accepted；真同源/真机/读屏/完整历史not-run，生产入口及用户Storage未动。[证据](./evidence/v036-round204-t01-t02-execution-and-audit-byte-anchor.md)。

**R203 Root T01/T02（协同伪造来源账本的SHA前置守卫，隔离非认证）：** 真实复现R202观察与裁框同时改用另一真实JPEG ROI并重算双SHA仍错误接受；R203将R156/R157/R174/R4/R196/R201及冻结JPEG/HTML共8个来源文件绑定已验证父档案SHA，先验后执行R202像素守卫与R201图重建，拒绝协同篡改及跨账本漂移。父R202 2547/2547逐SHA继承，旧240+新28=268/268，累计2558文件ZIP SHA `26058a5312341f0b6bc3dd1ca98fc72ea6a641be1477aa1de38200a0161457c3`，Python/unzip双独立恢复各2558 SHA和268 QA、QA后不变。T01 0/25、正式ID0、缺根未知、T00–T11 0/12 Accepted；真同源/真机/读屏/历史全量not-run，生产入口及用户Storage未动。[证据](./evidence/v036-round203-t01-t02-coordinated-ledger-provenance-gate.md)。
**R202 Root T01/T02（来源裁框原生像素与注册表互证，非认证）：** 复现R201接受伪造legacy:J:4观察坐标+真实像素SHA的证据链缺陷；R202新增失败关闭守卫，直接复核冻结JPEG 170观察+161裁框原生RGB与161组成员关系，M/V/K/E/B/J/R/X高风险单列。父R201 2535/2535逐SHA继承；旧199+新41=240/240选定QA，累计2547文件ZIP SHA `b02c6b499e4f29ae557880f22970a016bcd978286df7b8ce428b0baab72d02d2`，Python/unzip双独立恢复各2547 SHA与240 QA，QA后SHA不变。真实Chromium旧套件超时not-run，真同源/真机/读屏/历史全量not-run；T01 0/25、正式ID0、缺根未知、T00–T11 0/12 Accepted；生产入口/用户Storage未动。[证据](./evidence/v036-round202-t01-t02-native-crop-ledger-integrity.md)。

**R201（Root T01/T02，未验收）：** 170来源观察→161裁框→151旧可视别名；36旧未匹配、12无旧别名、2同裁框冲突、6原生矩形交叠、41历史高清审阅边分别分型；133个审阅分组（28个多观察）只作逐笔审阅队列，非身份合并。R200父2520/2520逐SHA继承、R201累计2535双独立恢复各300/300选定QA；递归1037超时不计通过；正式T01 0/25、T02永久ID0、全部T00–T11 0/12 Accepted。[证据](./evidence/v036-round201-t01-t02-source-identity-conflict-components.md)。

**R200 原始T03（真实Chromium含描边inkBBox隔离模块，非验收）：** 真读R199父ZIP2508/2508 SHA继承；真实浏览器 `about:blank` 对151草案实例×三视图×编辑前后共906组/918 Path按圆头stroke计算保守inkBBox，修正H:7 `getBBox()`忽略描边的0.90434345差异，最大解析式/真实DOM差0.000003706074；6种非法paint/CSS改动拒绝。实跑旧1001+新Chromium18+静态18=1037/1037；累计2520文件ZIP SHA `2940c4c28686599858acffb5c19fda47ce25605a8175fdfc7b4ed0c63beaba9d`，Python/unzip双独立恢复各2520 SHA与1037 QA。完整历史全量、真同源Storage、真机、真实读屏not-run；T00–T11 0/12 Accepted、T01 0/25、永久ID0、T03未生产集成、缺根未知，R11/R12/R35及R12 20SVG缺。冻结入口/用户Storage未动。 [证据](./evidence/v036-round200-t03-real-stroke-inclusive-dom.md)。


**R199 原始T03追踪（隔离非验收）：** R198父2495/2495逐SHA继承；R198来源签发151草案实例在真实about:blank Chromium三视图×编辑前后83/83 getBBox/getScreenCTM校验，150 SVG/906组/918 Path；H:7 stroke-inclusive几何口径差异已单列。选定旧901+新增83+静态17=1001/1001，R199累计2508文件双独立恢复各1001 QA。正式T01 0/25、T02永久ID0、T03未生产集成，真同源/真机/读屏/历史全量not-run；Root T00–T11仍0/12 Accepted。[证据](./evidence/v036-round199-t03-real-chromium-svg-geometry.md)。


**R198 原始T03追踪（非验收）：** R197父2482/2482 SHA继承，R198光学校正→25键三视图SVG隔离桥接；3视图各25 SVG/151实例/153 Path，M/V仅2矩阵变、其余149不变、全部Path属性不变；旧844+新57=901/901，累计2495双独立解压/QA与SHA复验。T02永久ID0、T01 0/25、T03未生产集成，真同源/真机/读屏/历史全量not-run，全部Root T00–T11 0/12 Accepted。[证据](./evidence/v036-round198-t03-source-bound-optical-three-view.md)。

**R197 Root T03（来源绑定151旧Path光学校正桥接，隔离非验收）：** R196父ZIP2469/2469逐SHA继承，R125/R160真实冻结矢量inkBBox绑定100×100光学编辑、M/V独立示例、来源/基线双SHA及非规范/越界/ID冲突拒绝；选定旧791+新Node35+静态18=844/844，累计R197 2482文件ZIP SHA `ce2c14605f9febdecff64243692db962b9c43247ac1c3dad23eedb2cb09b3769`，Python/unzip双独立恢复各2482 SHA和844 QA，QA后SHA不变。正式T03未生产集成，T01 0/25、永久ID0、缺根未知、T00–T11 0/12 Accepted；真同源/真机/读屏/完整历史not-run，R11/R12/R35和20SVG仍缺，冻结入口/用户Storage未动。[证据](./evidence/v036-round197-t03-source-bound-optical-preview.md)。


**R196 原始T01/T02追踪（T05仅关联、非验收）：** 父R195 2457/2457 SHA继承，冻结JPEG 170原生ROI SHA、R158 14审阅卡PNG/上下文RGB SHA、R174 41审阅边低清端点及R4 36旧槽未匹配、R157 12未绑定/2共享来源裁框的交叉一致性已实际重算。M/V/K/E风险排程，6原生矩形交叠只用于审阅；新34+静态18+选定旧739=791/791，R196累计2469文件ZIP SHA `ac99a7e7f36a9af57b3bc0ca2c120d7e6dc6ccb460913eaaf1efc9e85dc7a024`，Python/unzip双独立恢复各2469 SHA与791 QA。高清JPEG未本地读取、逐笔/许可未认证，T01 0/25、正式ID0、缺根未知、T00–T11 0/12 Accepted，缺R11/R12/R35及20SVG；生产入口和用户Storage未动。[证据](./evidence/v036-round196-t01-t02-exact-source-review-frontier.md)。

**R195 Root T04（25键/156旧槽全量v16来源隔离预演，非验收）：** 实际复验R194父ZIP2447/2447逐文件SHA，使用原R148/R152/R178/R179与R192事务核心，对冻结V0.35 25键156坐标槽全部作合规1单位编辑，签发156别名/156编辑；另测M键局部覆盖、来源不变、幂等、崩溃恢复、克隆/过期/非法来源拒绝。Node私有Map+模拟锁46/46、静态22/22、实跑选定旧671/671，共739/739；R195累计2457文件ZIP SHA `6ba77588da4a7e19b2622d9da722474e3b4be910cbd2b727ee6ac663fbe2895c`，Python/unzip双独立恢复各2457/2457 SHA和739/739 QA。真实浏览器本地管理员阻断，本轮真实浏览器not-run；正式迁移/真机/读屏/历史全量not-run，T00–T11仍0/12 Accepted，T01 0/25，永久ID0，缺根未知；R11/R12/R35与R12 20SVG缺，冻结入口/用户Storage未动。[证据](./evidence/v036-round195-t04-full25-v16-source-rehearsal.md)。

**R194 Root T04：首次在授权真实Chromium执行完整R148/R152/R178/R179来源签发链+R192隔离事务核心，双标签30/30，run 40712389404、artifact SHA256 56fb43276363bcd023fcf9f128f7b6e0650ac77ab7633b58b54c741eec3de42f；R193父2417/2417 SHA继承，R194累计2447文件ZIP SHA256 35eeaf4d0f9bf6b350dc915269ad46f1428d829594cfe8c3bf1894cd51734839，Python/unzip双独立恢复各2447/2447 SHA和671/671选定新旧QA。本地Chromium管理员阻断；远端使用合成v16来源与隔离profile，正式迁移/永久ID/真机/读屏/历史全量not-run。T00–T11仍0/12 Accepted，T01 0/25，缺根未知，R11/R12/R35和R12 20SVG仍缺，冻结生产入口及用户Storage未动。** [证据](./evidence/v036-round194-t04-real-issuer-r192-chromium.md)。

**R193 Root T04（真实Chromium幂等快路径竞态，隔离非验收）：** 独立核实此前R190真实浏览器15/15与R192 Node13/13的原始CI artifact；新增同一R192 ESM在127.0.0.1双标签Web Locks/localStorage/WebCrypto的异步来源变化回归，远端真实Chromium 15/15 success（run 40703055405，artifact SHA `0c8dc9e0a5cba157a4365aa34c153d9d624704b07ceb462a2343620792fe6592`）。R192父ZIP2402/2402逐SHA继承，R193累计2417文件ZIP SHA `88d7258d80cc83aed15b17fa8c97482202dd6d113b49454c610b15896003e6d7`，Python/unzip双独立恢复各2417 SHA、600/600选定新旧QA且QA后SHA不变。本地真实Chromium管理员阻断；浏览器仅合成签发，不是完整R148/R152/R178/R179或正式迁移。T00–T11仍0/12 Accepted，T01 0/25，永久ID0，缺根未知，R11/R12/R35与20SVG缺失；生产入口及用户Storage未动。[证据](./evidence/v036-round193-t04-real-chromium-stale-idempotent.md)。

**R192原始T04追踪（非验收）：** **R192 Root T04（幂等快路径来源过期拒绝，隔离非验收）：** 实际R189旧ESM复现buildPayload异步期间来源变化后仍返回idempotent；R192候选核心二次来源SHA+原始字节读回并检查shadow/journal。R191父ZIP2390/2390逐SHA继承；新Node36/36+CI等价烟测13/13+静态18/18、选定旧521/521，总计588/588；累计2402文件ZIP SHA `7e844d4126ed6b830088e9346f288509d317646d3d5eaa729cf91e0dfdb014c9`，Python/unzip双独立恢复各2402/2402 SHA及588/588 QA，QA后SHA不变。本地真实Chromium ERR_BLOCKED_BY_ADMINISTRATOR=blocked，远端R190/R192 CI未独立核实；正式T00–T11仍0/12 Accepted、T01 0/25、正式ID0、缺根未知，R11/R12/R35与R12 20SVG缺，冻结生产入口及用户Storage未动。[证据](./evidence/v036-round192-t04-stale-idempotent-source.md)。


**R191 Root T04（Storage同步异常回滚，隔离非验收）：** 父R190 ZIP2379/2379 SHA继承；Node私有Map写入故障29/29、静态18/18、选定旧474/474，共521/521；累计2390文件ZIP SHA `d2d8b2b400daa5ba83011b9df007348927fa2a55c612af6fc69f616dc325453b`，Python/unzip双独立恢复各2390/2390 SHA与521/521 QA，QA后SHA不变。真实Chromium临时127.0.0.1仍ERR_BLOCKED_BY_ADMINISTRATOR=blocked/not-run，R190远端CI unverified。正式T00–T11 0/12 Accepted、T01 0/25、永久ID0、缺根未知；R11/R12/R35与R12 20SVG缺，冻结入口及用户Storage未动。[证据](./evidence/v036-round191-t04-storage-quota-fault-matrix.md)


**R190 Root T04（真实同源SHA异步竞态CI基础设施，隔离非验收）：** R189父ZIP2360/2360成员SHA继承，新增19成员，累计2379文件ZIP SHA `ee13e558617a268763fd6a5869532bf13ad851e6a6b15091b50fdb110babe1c0`；Python/unzip双独立恢复各2379/2379 SHA及474/474选定新旧QA（旧456+新静态18），QA后SHA一致。新增同一R189 ESM真实Chromium双标签Web Locks/localStorage/WebCrypto第三次来源SHA延迟竞态测试与CI工作流；**本地Chromium管理员阻断、远端CI结果未独立核实，浏览器0项计pass**；完整真实R148/R152/R178/R179签发链浏览器测试not-run。正式T00–T11仍0/12 Accepted，T01 0/25、永久ID0、缺根未知；R11/R12/R35及20SVG仍缺，冻结入口与用户Storage未动。[证据](./evidence/v036-round190-t04-real-browser-async-readback-infrastructure.md)。


**R189 Root T04（异步来源SHA读回竞态修复，隔离非验收）：** Node复现R187在第三次来源摘要计算期间外部修改旧v16来源后仍提交过期影子；R189 SHA后读回原始来源字节，变化则拒绝并回滚。R188父ZIP2342/2342 SHA继承；新Node竞态14/14+真实签发Map47/47+静态17/17，选定旧378/378，总计456/456；累计2360文件ZIP SHA `6daddf37eb4c8df9990ee750650d4e9b934f1cbe309d240538fa6a29b1d71946`，Python/unzip双独立恢复各2360 SHA及456 QA。真实同源本地blocked、远端not-run；正式0/12 Accepted、T01 0/25、永久ID0、缺根未知；R11/R12/R35及20SVG缺，冻结入口与用户Storage未动。[证据](./evidence/v036-round189-t04-async-source-digest-readback.md)。


**R188 Root T04（真实签发链接入R187 typed-slot v3，隔离非验收）：** 真实读取R187父ZIP2325/2325 SHA继承；实际R148/R152/R178/R179签发与R187核心连接，Node47/47+静态26/26+实跑旧305/305=378/378；累计2342文件ZIP SHA `b2c13aad18a87e0da0b43ece78d5ad0541f3a96c7557694209c5a24316b07471`，Python/unzip双独立恢复各2342 SHA、378 QA，QA后SHA一致。本地真实Chromium ERR_BLOCKED_BY_ADMINISTRATOR=blocked/not-run，远端R188真实CI not-run；生产迁移/历史全量/真机/读屏not-run。T00–T11仍0/12 Accepted、T01 0/25、永久ID0、缺根未知；R11/R12/R35及20SVG仍缺，冻结入口/用户Storage未动。[证据](./evidence/v036-round188-t04-actual-issuer-typed-slot-bridge.md)。


**R187 Root T04追踪（非验收）：** R187 Root T04（typed-slot v3隔离恢复，非验收）：复现R186 `before??''`将不存在的shadow与空字符串视为同一SHA，导致非协作空字符串被回滚覆盖；新v3 typed-slot SHA拒绝该冲突，旧v2日志失败关闭。R186父ZIP2310/2310 SHA继承；R187累计2325文件SHA `6f35d9e783986ab16245fcdca7e567808bcab3411cc299aa4252c99361b22ae3`，Python/unzip双独立恢复各2325 SHA、305/305选定新旧QA、QA后SHA一致；本地旧270+新Node18+静态17=305/305。远端真实Chromium同一ESM双标签17/17（CI 40654063434，artifact SHA `cebf673d75c26e179860574bf6bf80e99f0c39efe31558ff962e6d6efa091ff3`），但使用合成来源计划，非R148真实签发浏览器验证；本地浏览器管理员阻断。完整历史、真机、读屏、生产迁移not-run；T00–T11仍0/12 Accepted，T01 0/25、正式ID0、缺根未知；R11/R12/R35和20SVG仍缺，冻结入口及用户Storage未动。 [证据](./evidence/v036-round187-t04-typed-storage-slot-recovery.md)。

**R186 Root T04（非协作影子写入冲突防护，隔离非验收）：** R185父ZIP2289/2289 SHA继承；新增v2 before/next双SHA日志与回滚/恢复冲突拒绝，外部写入不被静默覆盖。Node真实签发65/65+异步竞态16/16+静态20/20+选定旧169/169=270/270；累计2310文件ZIP SHA `0897ac244652dd7fa93038c5717967e8d8a47b61599abf11015ef85ba289b456`，Python/unzip双独立恢复各2310 SHA、270 QA，QA后SHA一致。本地真实Chromium管理员阻断，远端CI/历史全量/真机/读屏not-run；T00–T11仍0/12 Accepted、T01 0/25、永久ID0、缺根未知；R11/R12/R35及20SVG缺，冻结入口与用户存储未动。[证据](./evidence/v036-round186-t04-noncooperative-shadow-conflict.md)。


**R185 Root T04（真实来源签发隔离事务桥接，非验收）：** 实际读取R184父ZIP2271文件并逐项2271/2271 SHA继承；连接原样R148/R152/R178/R179签发与R183共享ESM事务核心，旧v16源只读、隔离影子日志可回滚、127.0.0.1原点先于Storage校验。新增Node40/40+静态21/21+选定旧215/215=276/276；R185累计2289文件SHA `18450dde7b141cb58888f1f2608c76cd0d3dcd71ce97e32aa088a09872fb8b38`，Python/unzip双独立恢复各2289 SHA及276 QA、QA后SHA不变。本地真实Chromium ERR_BLOCKED_BY_ADMINISTRATOR=blocked，远端真实CI not-run；正式T00–T11仍0/12 Accepted、T01 0/25、正式ID0、缺根未知，R11/R12/R35及20SVG缺；生产入口/用户Storage未动。[证据](./evidence/v036-round185-t04-actual-source-issued-disposable-bridge.md)。

**R184 Root T04（真实浏览器故障分支QA修复，非验收）：** R183真实同源CI 40630751605失败：测试复用相同payload走幂等分支，未触发故障；修复后CI 40635880938成功，实际Chromium同一ESM双标签25/25，原始artifact 12793257183 SHA独立核验。R183父ZIP2257/2257 SHA继承，R184累计2271文件ZIP SHA `1404f851ae798a32c5e5698448755c4ddc838421c4920fee85b11f13b3ad23fa`，本地选定旧170+新21+静态24=215/215，Python/unzip双独立恢复各2271 SHA与215 QA。真实迁移/来源认证/真机/读屏/历史全量仍未验收，T00–T11保持0/12 Accepted、T01 0/25、永久ID0、缺根未知；冻结生产入口及用户存储未动。[证据](./evidence/v036-round184-t04-real-browser-fault-branch-fix.md)。

**R183 Root T04（跨Node/浏览器同一ESM隔离事务核心，非验收）：** 新增可注入存储/锁/SHA/签发验证的纯ESM隔离核心及真实R148/R152/R178签发桥接；Node新44/44+真实旧签发17/17，实际重跑选定旧109/109=170/170。R182父ZIP2247/2247逐文件SHA继承，R183累计2257文件ZIP SHA `65526b6e12e03f8fd6a83f9a458e5a492180fe6fd23e4134575c561395ccd185`，Python/unzip双独立恢复各2257/2257 SHA、170/170 QA，QA后SHA不变。本地真实127.0.0.1 Chromium管理员阻断，真实浏览器not-run；远端同一ESM CI工作流已提交，结果尚未核实。历史全量/真机/读屏not-run；正式T00–T11仍0/12 Accepted、T01 0/25、正式ID0、缺根未知；R11/R12/R35和R12 20SVG仍缺，生产入口/用户存储未动。[证据](./evidence/v036-round183-t04-shared-disposable-transaction-core.md)。

**R182 Root T04（真实同源隔离暂存与回滚，非验收）：** 重新核实R181远端真实浏览器原语CI 16/16（run 40619051747），新增R182远端真实127.0.0.1 Chromium独立隔离暂存/回滚/崩溃重载/过期来源/损坏journal QA 24/24（run 40624848783），两份CI原始artifact ZIP SHA与内部JSON均独立校验；R181父ZIP2234/2234 SHA继承，R182累计2247文件SHA `0d44faa8e833f67eea49cc314c92559e4224055780dc9b9f25b6e729ae1e5b23`，Python/unzip双独立恢复各2247/2247 SHA及109/109本地选定QA。R180递归1181旧QA超时不计通过，完整历史全量not-run。本地真实浏览器仍管理员阻断，R182额外26项本地浏览器草案未运行。**远端fixture不是R180生产迁移代码的直接执行**；无正式永久ID、无用户存储写入，T00–T11仍0/12 Accepted，T01 0/25，缺根未知，R11/R12/R35及R12 20SVG仍缺。[证据](./evidence/v036-round182-t04-real-same-origin-disposable-quarantine.md)。


**R181追踪补充（原始T04，非验收）：** 独立同源浏览器Web Locks/storage事件/WebCrypto验证脚本与CI工作流已入仓；本地真实浏览器被管理员阻断，远端结果未核实；静态12+选定旧1181=1193/1193，R180父2224/2224 SHA、R181累计2234双独立恢复各1193 QA；不替代真实生产迁移。T00–T11仍0/12 Accepted。[证据](./evidence/v036-round181-t04-real-same-origin-browser-infrastructure.md)。

**R180 Root T04（私有Map隔离影子与崩溃回滚，非验收）：** 真实读取R179父ZIP2213文件、逐文件2213/2213 SHA继承；新增Node-only内存隔离影子事务：复用R148/R152/R178来源签发与SHA验证，支持v16别名/编辑快照、幂等重放、失败回滚、模拟崩溃后重启恢复及来源更新后只回滚影子不覆盖v16源；无永久ID、无浏览器localStorage写入。新增Node48/48+实跑R179选定旧1133/1133=1181/1181；累计2224文件ZIP SHA `5155e490d3ec295d6f1cf6868ca0dc92397525123262f9058237c41fb44bce5f`，Python/unzip双独立恢复各2224/2224 SHA、1181/1181 QA，QA后SHA一致。模拟锁/模拟原点不是真同源；R179管理员阻断，本轮真同源not-run；历史全量/真机/读屏/正式迁移not-run。原始T00–T11仍0/12 Accepted、T01 0/25、正式ID0、缺根未知，R11/R12/R35及20SVG仍缺；冻结入口和用户存储未动。[R180证据](./evidence/v036-round180-t04-disposable-quarantine-rollback.md)。

**R179 Root T04（浏览器realm真实原点绑定，隔离只读非验收）：** Node VM复现R178接受调用方伪造loopback原点/存储并给出正面来源见证；新增R179浏览器realm绑定入口，在读取localStorage前拒绝非127.0.0.1安全原点，只从当前realm取得单键只读存储/Web Locks/WebCrypto。新35/35+真实Chromium about:blank拒绝1/1+实跑R178选定旧1097/1097=1133/1133；R178父2201/2201 SHA继承，R179累计2213文件SHA `87fddbac1512ab8f4b87f4f6fd59291ef88ad5a7c1aac13feaaebb5100be350f`，Python/unzip双独立恢复各2213/2213 SHA、1133/1133 QA，QA后SHA一致。真实loopback仍ERR_BLOCKED_BY_ADMINISTRATOR=blocked/not-run，历史全量/真机/读屏/正式迁移not-run；T00–T11仍0/12 Accepted，T01 0/25、正式ID0、缺根未知，R11/R12/R35与20SVG仍缺，冻结入口/用户存储未动。[R179证据](./evidence/v036-round179-t04-browser-realm-origin-binding.md)。


**R178 Root T04（只读来源快照过期防护，非验收）：** 复现R152已签发计划在旧v16存储K:2被修改后仍通过旧verifyPlan；新增R178独立只读门禁，在协作Web Lock内重新核对真实源SHA，拒绝过期、异步竞态、克隆计划及假issuer。Node22新增22/22、实跑R177选定旧1075/1075；R177父2189/2189 SHA继承，R178累计2201文件SHA `4cb47c565f2fa6f3e1763cf1abf8ff8dcce6b2c51313dc5a5fb9cfc61fb5044e`，Python/unzip双独立恢复各2201/2201 SHA、1097/1097 QA，QA后SHA一致。真实loopback Chromium仍ERR_BLOCKED_BY_ADMINISTRATOR，真同源blocked；完整历史/真机/读屏not-run，生产迁移not-run。正式T00–T11仍0/12 Accepted，T01 0/25、永久ID0、缺根未知，R11/R12/R35与20SVG仍缺，冻结入口/用户存储未动。[R178证据](./evidence/v036-round178-t04-legacy-source-freshness-gate.md)。


**R177 Root T03（关联T07仅墨迹隔离预检，非验收）：** 真实Chromium about:blank分别渲染151草案实例至256/384px透明Canvas，25键每分辨率409对同键alpha交集检查，0墨迹重叠、0空白/边界裁切、0对3px内近接；仅草案/两分辨率，不等于原图/stroke/正式T07。R176父ZIP2181/2181 SHA继承，R177累计2189文件SHA `b44a6720aeb7b27d4303affb4aa681cd93fbaf7030aad17534468da9eb82ecab`，Python/unzip双恢复各2189/2189 SHA、1075/1075选定QA，QA后SHA不变。R176递归2820项尝试超时不计pass，历史全量/真同源/真机/读屏not-run。正式0/12 Accepted，T01 0/25、正式ID0、缺根未知，R11/R12/R35与20SVG缺、许可/逐笔未完成，冻结入口/用户存储未动。[R177证据](./evidence/v036-round177-t03-real-ink-alpha-collision-preflight.md)。

**R176 Root T03（关联T07仅隔离前置预检，非验收）：** R175来源签发25键/151草案实例/153旧Path完整复用，新增字母/区号独立标签带与单HTML真实DOM宿主、full/mini及聚焦同源克隆。首次844×390纵向溢出120px，新增横屏左右分栏后8视口×DPR1/2/3×双模式零纵横滚动；Chromium about:blank真实DOM 50组×14=700/700，来源静态13/13，实际重跑R175选定旧2107/2107，合计2820/2820。父ZIP2165/2165 SHA继承；新累计2181文件SHA `c687d56e8674632735fd03143cc2aa15450c6439224f27e9917cdee41cf15d55`，Python/BusyBox双独立恢复各2181/2181 SHA与2820/2820 QA，QA后SHA不变。file://管理员阻断；真同源/真机/读屏/完整历史全量not-run。组BBox标签无交叠≠真实墨迹/stroke认证，T03未生产集成、T07未达依赖；正式0/12 Accepted、T01 0/25、正式ID0、缺根未知；R11/R12/R35与R12 20SVG仍缺，许可/逐笔未完成，冻结入口/用户存储未动。[R176证据](./evidence/v036-round176-t03-keycap-host-real-dom-preflight.md)。


**R175 Root T03（来源签发25键局部SVG组合器，隔离非验收）：** 实际复验R174父ZIP2151文件、2151/2151 SHA继承；R169 SHA签发151草案实例重新组合为25个100×100 SVG、151独立g、153原始Path，full/mini/focus三视图共用矩阵/路径/ID，拒绝跨键/重复/非法选择。新增Node19/19、Chromium about:blank实际SVG绘制DPR1/2/3×3视图99/99，重跑R174选定旧1989/1989，合计2107/2107；累计ZIP2165文件SHA `99efbb2097a587a19defe47f3c3ee710d7890c03523324ce7815141c68a5265d`，Python/unzip双独立恢复各2165/2165 SHA及2107/2107 QA，QA后SHA一致。浏览器验证为序列化SVG绘制，非真实同源/真机/读屏或生产ESM执行；历史全量not-run。正式T00–T11仍0/12 Accepted、T01 0/25、正式ID0、缺根未知；R11/R12/R35及R12 20SVG缺失，高清许可/逐笔认证未完成，冻结入口/用户存储未动。[R175证据](./evidence/v036-round175-t03-key-local-source-issued-compositor.md)。


**R174 Root T01/T02（关联T05，41对来源双框离线逐笔审阅工作台，非验收）：** 实际读取R173父ZIP2138项并逐文件2138/2138 SHA继承；以冻结2008 JPEG和R171 170观察、R172 41对审阅框、R173高清像素历史证据建立41对/16键原生双框来源注册表，82次原生ROI RGB SHA重算一致；新增独立单HTML可交互人工审阅（仅内存笔记/导出未批准JSON，无localStorage、网络或正式审批入口）和41格低清来源联系图。E:1/E:8旧否定、K:2/K:3阻断不解除；未重新读取高清JPEG，许可未确认。新增静态138+Chromium about:blank 98=236/236，实际重跑R173选定继承1753/1753；累计ZIP2151文件SHA `65ce8d4305e8212e6638dd60fe7995bc85f042ead7f985014bc8f6363355e71d`，Python/unzip双独立恢复各2151/2151 SHA、1989/1989 QA，QA后SHA一致。历史全量/真同源/真机/读屏not-run；T00–T11仍0/12 Accepted、T01 0/25、正式ID0、缺根未知；R11/R12/R35及R12 20SVG仍缺，冻结入口/用户存储未动。[R174证据](./evidence/v036-round174-t01-t02-frozen-native-41-pair-review-workbench.md)。


**R173 Root T01/T02（关联T05，真实3508×2480高清像素41对审阅ROI拓扑，非验收）：** GitHub Actions 40557130807独立临时runner实际读取SHA锁定高清JPEG，41对中10对审阅框完全同几何、20对为R172 p95余量新增；灰度<160时34/41共享ROI有暗像素、12/41存在跨两侧独占区域的8连通暗组件，新增20对中13有暗像素、10有桥接候选。**像素拓扑不等于逐笔归属或字根身份，许可未确认；远端仅内存处理，不向仓库/ZIP发布JPEG。** R172父ZIP2126/2126 SHA继承，R173累计2138文件SHA `00051c8856b1d73338a2e41cdecba892f22c8d90ffcfb76d7e39c0752490c103`；新增隔离65/65+远端日志一致性58/58+继承选定1630/1630=1753/1753，两套独立恢复各2138/2138 SHA和1753/1753 QA，QA后SHA不变。完整历史全量/真同源/真机/读屏not-run；正式T00–T11 0/12 Accepted、T01 0/25、正式ID0、缺根未知，R11/R12/R35及R12 20SVG仍缺；冻结入口/用户存储未动。[R173证据](./evidence/v036-round173-t01-highres-41-overlap-pixel-topology.md)。


**R172 Root T01/T02（关联T05，170项高清审阅ROI配准不确定性余量，非验收）：** 真读R171父ZIP2116文件并逐文件2116/2116 SHA继承；以R119真实99内点/22格仿射配准的p95残差0.9552低清px计算3高清px审阅余量，170项/25键的同键投影裁框原有21对交叠、余量新增20对、合计41对，**仅审阅交叠非笔画/根身份认证，p95不保证覆盖全部笔画**。新增399/399、继承选定1231/1231，R172累计2126文件ZIP SHA `c5534e9c0eabb3be3ca79e3aac8873646e5327017b83b7a43b570633373e2e9b`，Python/unzip双独立恢复各2126/2126 SHA、1630/1630 QA，QA后SHA不变。高清原始JPEG本地未落地/许可未确认，完整历史全量/真同源/真机/读屏not-run；T00–T11 0/12 Accepted，T01 0/25，正式ID0，缺根未知；缺R11/R12/R35和20SVG，冻结入口/用户存储未动。[R172证据](./evidence/v036-round172-t01-t02-highres-uncertainty-roi-envelope.md)。


**R171 Root T01/T02（关联T05，高清候选历史调和与170来源ROI仿射投影，非验收）：** 纠正R170对1479×843简繁ZIP“新发现”的认识：R114早已在独立CI解压并核验ZIP/JPEG SHA和尺寸，R171重新经GitHub连接核实R114/R119两次CI jobs均success；优先源仍是R114的3508×2480简体JPEG（SHA `47c5d53f6cf57ac67c957c6510a3e2696072c3ce63e73024ed025367f31c600e`）。本地真读冻结2008 JPEG并重算170/170原生ROI RGB SHA，使用R119真实仿射矩阵为25键170条观察生成高清坐标审阅框，非高清像素逐笔认证。新875/875+选定旧356/356；R170父2106/2106 SHA继承，R171累计2116文件ZIP SHA `3e853216819bc3f770aaffe2cf8012f29218f93d620b6daaea7ad2c5d62fb5c4`，Python/unzip双独立恢复各2116/2116 SHA、1231/1231 QA且QA后SHA不变。高清JPEG本地未落地、许可未确认、完整历史全量/真同源/真机/读屏not-run；T00–T11 0/12 Accepted，T01 0/25，正式ID0，缺根未知；缺R11/R12/R35和20SVG，冻结入口/用户存储未动。[R171证据](./evidence/v036-round171-t01-t02-source-candidate-reconciliation-170-affine-rois.md)。


**R170 Root T01/T05（官方高分辨率候选ZIP元数据+M未绑定低清SVG掩码隔离研究，非验收）：** 通过GitHub连接读取06wb资源ZIP359250字节（blob `542ee2067965b2d5498ad211dfd763ca0e7f6447`，内含 `zgjwt_jf_1479x843.jpg` 416166声明字节），但原图JPEG未落地/解压/独立SHA或许可核验，**不得称为合法同源高清图**。M4项未绑定中M04归属阻断、M06/07/08仅低清阈值像素掩码SVG研究，正式补图0。R169父2094/2094 SHA继承；R170累计2106文件SHA `d3fbd466fabee4bcb58c9eaceae4fd1df43b7cb923d02c64250295c247ae8d8d`，新23/23+选定旧333/333、Python/unzip双独立恢复各2106/2106 SHA和356/356 QA，QA后SHA不变。历史全量/真同源/真机/读屏not-run；T00–T11仍0/12 Accepted、T01 0/25、正式ID0、缺根未知，缺R11/R12/R35和20SVG，冻结入口/用户存储未动。[R170证据](./evidence/v036-round170-t01-t05-official-source-candidate-and-m-mask.md)。

**R169 Root T03（来源签发三视图适配器，隔离非验收）：** R168父ZIP2083/2083 SHA继承；新增R125固定SHA的R50/R54/R53原始字节同步快照签发边界，拒绝伪造plan/registry与异步输入TOCTOU，连接R160/R162/R163的151草案实例、25键和三视图。新增Node17/17+实际重跑选定旧316/316；R169累计ZIP2094文件SHA `a428e4ae95cfc039b052c877b269211a8a226b2a96f4132d9fbf7713676181b5`，Python/unzip双独立恢复各2094/2094 SHA、333/333 QA及QA后SHA一致。真实localhost Chromium `ERR_BLOCKED_BY_ADMINISTRATOR`，共享原点迁移blocked/not-run；历史全量/真机/读屏not-run。T00–T11仍0/12 Accepted、T01 0/25、正式ID0、缺根未知，缺R11/R12/R35及20SVG；冻结入口/用户存储未动。[R169证据](./evidence/v036-round169-t03-source-issued-three-view-boundary.md)。

**R168 Root T00/T01/T02/T03（原始R8→R50冻结SVG来源连续性，非验收）：** 真读R167父ZIP2075文件、嵌套原始R10 ZIP184文件、原始R8 151 SVG草案与156 ID注册表、R9 15证据及后期R50 151 Path；151/151实例ID/键/旧槽/字符/坐标/Path一致，5关联项隔离，149个普通Path SHA可直接重算，H:6/H:7两个特殊部件来源SHA单列不伪造。新28/28+实际重跑选定旧288/288；R168累计ZIP2083文件SHA `3ca7a8f727bd28790816a96f6ecd342a946891203a40ddbdd55c4d4087625f0f`，父2075/2075 SHA继承，Python/unzip双独立恢复各2083/2083 SHA及316/316选定QA，QA后SHA不变。完整历史全量/真同源/真机/读屏not-run；原始T00–T11仍0/12 Accepted、T01 0/25、正式ID0、缺根未知，R11/R12/R35及20SVG仍缺，冻结入口/用户存储未动。[R168证据](./evidence/v036-round168-t00-t03-original-r8-r50-source-lineage.md)。


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
