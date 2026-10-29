# 项目状态：GlyphSpace / 字间 V0.36

**R218 Root T01/T02（来源证据→独立身份晋级前置检查，隔离非验收）：** R217累计ZIP 2740/2740逐SHA继承；基于R209 166草案身份及R206 50票据/52链接，新增逐候选缺失证据门禁、25键M优先来源采集队列和12类身份篡改/3份来源字节篡改拒绝；166/166仍blocked、M四无旧别名、E/K两组同裁框异SVG分离。选定旧229+新289=518/518，R218累计2751文件ZIP SHA `f4766f9b7760f3bf2df7c3383f4ec24bd3cead0ab4b6b9a008e00a106969b3d0`，Python/unzip双独立恢复各2751 SHA与518 QA、QA后0变化。T01 0/25、永久ID0、缺根未知、Root 0/12 Accepted；合法同源高清原始字节/许可未取得；真实同源/真机/读屏/历史全量not-run，冻结入口与用户Storage未动。[R218证据](./evidence/v036-round218-t01-t02-source-identity-readiness.md)。


**R217 Root T03（子组几何漂移失败关闭，隔离非验收）：** 真实Chromium复现R216在子g transform、Path d及stroke-width变化时错误接受3/3次拖动；新增子组CTM、SVG子树、getBBox、computed style和动画拒绝守卫。父R216 2727/2727逐SHA继承；选定旧1696/1696+新971/971=2667/2667；累计2740文件ZIP SHA `6bb1302e283a41a17c6390ce5e9229efc8f4f5008b0a8748784540ba4166728d`，Python/unzip双独立恢复各2740 SHA及2667 QA，QA后0变化。R216递归套件超时不计pass；完整历史QA not-run。T03未生产集成、Root 0/12 Accepted、T01 0/25、T02批准ID0、缺根未知；真同源/读屏/真机not-run，冻结入口/Storage未动。[R217证据](./evidence/v036-round217-t03-pointer-group-geometry-drift.md)。

**R216 Root T03（真实指针坐标→100×100光学校准隔离桥接，非验收）：** 实际继承R215 2713/2713 SHA并重跑旧311/311；新增真实Chromium `getScreenCTM()` 逆映射，覆盖151旧草案实例×5种CSS变换×DPR1/2=1510次坐标断言及12次异常拒绝，Node来源绑定42/42、静态24/24，合计选定1899/1899。首次发现SVGMatrix无`is2D`属性并修复；R197→R160→R125绑定的草案光学移动不写DOM/Storage。R216累计2727文件ZIP SHA `90b25d9800939d9b182998d1dc94c7f81694ff8e90cc38c7ad22a37dda5f310c`，Python/unzip双独立恢复各2727 SHA与1899 QA、QA后0变化。T03未生产集成、Root 0/12 Accepted、T01来源0/25、T02永久ID0、缺根未知；R10历史原包R164已恢复，R11/R12/R35和R12 20SVG仍缺，真同源/真机/读屏/完整历史not-run；冻结入口/用户Storage未动。[R216证据](./evidence/v036-round216-t03-pointer-to-optical-bridge.md)。

**R215 Root T03（CSS独立变换真实像素漏包修复，隔离非验收）：** 真实Chromium复现R214在rotate:45deg+内层反向旋转+不对称边框的HTML裁剪下错误接受，40个黑像素位于宣称上界之外；新增独立CSS rotate/scale/translate失败关闭守卫，允许已验证正轴对齐缩放/2D平移。父R214 2701/2701 SHA继承，选定旧261+新Chromium31+静态19=311/311；累计2713成员ZIP SHA `bd5dd91f5b9f34e8ab7729aefa96b933aa6112b6ebe3d7395c4143e3d54e9625`，Python/unzip双独立恢复各2713 SHA和311 QA，QA后0变化。合并双恢复任务中途超时，第二套单独重跑通过。Root 0/12 Accepted、来源0/25、永久ID0、缺根未知；真同源blocked、真机/读屏/历史全量not-run，冻结入口/Storage未动。[R215证据](./evidence/v036-round215-t03-css-individual-transform-guard.md)。


**R214 Root T03（SVG根视口裁剪保守上界，隔离非验收）：** R213未处理SVG根自身overflow，新增独立SVG viewport屏幕交集，保留原inkBBox，支持缩放及HTML+SVG双层裁剪；真实Chromium黑像素10000/19600/2500/0/200/4200案例，906旧SVG原始几何不变。父R213 2688/2688逐SHA继承，选定旧203+新Chromium40+静态18=261/261；累计2701文件ZIP SHA `d06b8400bece34bf9e6fb36ac1c88f7ff33df5e2ada15d2a04902d8de4a6c1da`，Python/unzip双独立恢复各2701 SHA与261 QA、QA后0变化。T03未生产集成、Root 0/12 Accepted、来源0/25、永久ID0、缺根未知；真实同源blocked，真机/读屏/历史全量not-run，冻结入口/Storage未动。[R214证据](./evidence/v036-round214-t03-svg-viewport-clipping.md)。

**R213 Root T03（缩放祖先overflow上界修复，隔离非验收）：** 真实Chromium发现R212在scale(.5)时屏幕可见500黑像素却报告仅10×15上界，漏掉真实墨迹；R213改用CSS subpixel border-box与屏幕缩放比率，scale(.5)修正为20×25，scale(2)为80×100，906旧SVG几何不变，旋转/透视等失败关闭。父R212 2675/2675 SHA继承，选定旧159+新44=203/203；累计2688文件ZIP SHA `5907af02850e0084528b3082f6524e9fd8750d20a88ecbcf9eeae7fb5aee7089`，Python/unzip双独立恢复各2688 SHA及203 QA、QA后0变化。T03未生产集成、Root 0/12 Accepted、来源0/25、永久ID0、缺根未知；同源blocked、真机/读屏/历史全量not-run；冻结入口/用户Storage未动。[R213证据](./evidence/v036-round213-t03-scaled-overflow-border-fix.md)。

**R212 Root T03（HTML overflow裁剪保守包络，隔离非验收）：** 修复R211一律拒绝合法overflow:hidden/clip/scroll祖先；新增真实Chromium矩形裁剪上界（保留原inkBBox，完全裁剪null），906旧SVG几何不变，截图黑像素10000→2000→0；父R211 2663/2663逐SHA继承，选定旧126+新33=159/159；累计2675文件ZIP SHA `4f4fd0283aa87dba0f95224c5e6afc5a11ca67b048ab8c263be5e79ce9e296ae`，Python/unzip双独立恢复各2675 SHA及159 QA、QA后0变化。R211递归670套件超时不计pass，完整历史全量not-run。T03未生产集成，Root 0/12 Accepted、来源0/25、永久ID0、缺根未知；同源blocked、真机/读屏not-run；冻结入口/用户Storage未动。[R212证据](./evidence/v036-round212-t03-rectangular-overflow-upper-bound.md)。
**R211 Root T03（HTML祖先绘制抑制，隔离非验收）：** 实际Chromium发现R210只检查SVG内祖先，HTML外层opacity=0/全裁剪时仍返回inkBBox，截图黑像素3200→0；新增HTML祖先computed-style失败关闭守卫。906组正常几何一致，11个外层反例拒绝（9个旧R210误接受），选定旧644+新Chromium14+静态12=670/670；父R210 2651/2651 SHA继承，R211累计2663文件SHA `ddc0127fe6317f1c9f336b00069766f5b1ea2ff5178be2e328024d4036a99739`，Python/unzip双独立恢复各2663 SHA及670 QA，QA后0变化。T03未生产集成，T01 0/25、永久ID0、Root 0/12 Accepted；同源blocked、真机/读屏/历史全量not-run；冻结入口及用户Storage未动。[R211证据](./evidence/v036-round211-t03-outer-html-ancestor-paint-gate.md)。

**R210 Root T03（有效绘制墨迹边界守卫，隔离非验收）：** 真实Chromium复现R200祖先opacity=0/全裁剪仍报告非空inkBBox，截图黑像素正常3200→不可见0；新增computed-style祖先/Path失败关闭守卫，906旧SVG组新旧正常几何一致、14/14对抗拒绝。父R209 2640/2640逐SHA继承；选定旧620+新Chromium12+静态12=644/644，R210累计2651文件ZIP SHA `12e329603696bd85991666c222e14f68124c920a8fb9effa2331661923433449`，Python/unzip双独立恢复各2651 SHA与644 QA、QA后不变。T03未生产集成，原始0/12 Accepted，来源0/25、永久ID0、缺根未知；同源blocked、真机/读屏/历史全量not-run；冻结入口/用户存储未动。[R210证据](./evidence/v036-round210-t03-effective-ancestor-paint-guard.md)。


**R209 Root T01/T02（类型化草案身份桥接，T05仅关联，非验收）：** 真读R208累计ZIP 2628/2628 SHA继承；151旧SVG可视槽+12无旧别名裁框+3 K混合观察形成166个`draft-only/`非正式候选，50条R206票据原ID连接52条边，E/K同裁框异Path继续独立；R50冻结Path交叉验证阻断内存Path伪造。旧554+新51+静态15=620/620；R209累计2640文件ZIP SHA `89c8eed7d8dfbf85b29d68565e33c1d577d79d82be73584534944c5c9c0d81df`，Python/unzip双独立恢复各2640 SHA及620 QA。T01正式0/25、永久ID0、缺根未知、Root 0/12 Accepted；同源blocked、真机/读屏/历史全量not-run；冻结入口及用户Storage未动。[R209证据](./evidence/v036-round209-t01-t02-typed-draft-identity-bridge.md)。


**R208 Root T01/T02（T05依赖三向来源审计，隔离非认证）：** 实际从冻结HTML重新抽取151旧SVG实例/153 Path并重算151 Path SHA，联合R156 JPEG 170观察/161裁框与R207 156旧槽匹配状态：36/36未匹配旧槽同时有JPEG观察及旧SVG（未匹配≠缺SVG）；15无旧别名观察=12个纯无别名裁框+3条共享旧槽K裁框的观察，不能推断15新增根；E:1舟/E:8用及K:2川/K:3丨各共用一JPEG裁框却对应不同旧SVG Path SHA，继续阻断。父R207 2613逐SHA继承，选定旧487+新50+静态17=554/554；R208累计2628文件ZIP SHA `200db5147697b9686bee3fd1073464707105bd060f821c24eda815364a02dc46`，Python/unzip双恢复各2628 SHA与554 QA。T01认证0/25、永久ID0、缺根未知、Root 0/12 Accepted；同源blocked、真机/读屏/历史全量not-run；生产入口/用户Storage未动。[R208证据](./evidence/v036-round208-t01-t02-t05-three-way-source-vector.md)。


**R207 Root T01/T02（156旧槽与R156来源观察纠错，隔离非认证）：** 真实联读T00冻结156槽、R113坐标、R156 170观察/161裁框与R206 50票据，发现36/36“未匹配旧槽”实际上各有冻结JPEG来源观察（未匹配≠无来源，更不等于已认证）；新增156槽映射与36条证据交叉表，保留R206 ticketId，5关联槽隔离、M:0–M:3双观察保留、E:1/E:8同裁框不合并。父R206 2600/2600 SHA继承，旧424+新48+静态15=487/487，累计2613文件ZIP SHA `1b69983adafb0d4b972a9411ef2b3f849add4279fa1626505daae9ec5ce76e2a`，Python/unzip双恢复各2613 SHA及487 QA。T01正式0/25、永久ID0、缺根未知、Root 0/12 Accepted；真同源blocked、真机/读屏/历史全量not-run；冻结入口与用户Storage未动。[R207证据](./evidence/v036-round207-t01-t02-legacy-source-reconciliation.md)。


**R206 Root T01/T02（50条来源语义仲裁票据，隔离非认证）：** R205父2586/2586逐SHA继承；12无旧别名裁框、36旧槽未匹配、2组E/K同裁框冲突建立50条review-*票据（非永久ID），K圈注待审、M四微框分立；R157宽松邻接与R205精确原生矩形交叠口径不同，R206独立重算并拒绝伪造。选定旧359+新49+静态16=424/424；累计2600文件ZIP SHA `0b3edc0d8241278a1bb8ffd023638622a41d9d09c94811b4e972859c6460bcae`，Python/unzip双独立恢复各2600 SHA及424 QA、QA后不变。T01 0/25、永久ID0、缺根未知、Root 0/12 Accepted；真同源blocked、真机/读屏/历史全量not-run；R11/R12/R35与R12 20SVG仍缺。[R206证据](./evidence/v036-round206-t01-t02-semantic-arbitration-tickets.md)。


**R205 Root T01/T02（原生JPEG未绑定裁框像素覆盖，隔离非认证）：** 父R204 2569/2569逐SHA继承；冻结JPEG 12未绑定裁框原生面积累计3626像素，其中2908像素不在同键旧裁框矩形内（非笔画归属），6原生重叠与R196一致，E/K同裁框冲突仍未决。B未绑定252像素中198与B:7矩形重叠；M四未绑定各180/182/168/180像素与旧M矩形不交叠。选定旧306+新53=359/359；累计2586文件ZIP SHA `a4f5688e6884d98560570cf2fbed5923b52f33dc7be144c9bf12fdbb31ff2080`，Python/unzip双独立恢复各2586 SHA和359 QA，QA后不变。T01正式0/25、永久ID0、缺根未知、T00–T11 0/12 Accepted；真同源blocked、真机/读屏/完整历史not-run，生产入口/用户Storage未动。[证据](./evidence/v036-round205-t01-t02-native-pixel-coverage.md)。

**R204 Root T01/T02（执行源码与历史审计字节锚，隔离非认证）：** 实际复现R203对R201/R202/R203可执行代码和R202历史审计/父清单共5类字节篡改仍误接受；新增父R203可信档案SHA绑定、执行前后失败关闭。父R203 2558/2558逐SHA继承，旧268+新增对抗26+静态12=306/306；累计2569文件ZIP SHA `a55b4b6a8e797e210496e45bf446b011913e394f06051863a3c39c874cb35c1b`，Python/unzip双独立恢复各2569 SHA和306 QA、QA后不变。T01 0/25、正式ID0、缺根未知、T00–T11 0/12 Accepted；真同源/真机/读屏/完整历史not-run，生产入口及用户Storage未动。[证据](./evidence/v036-round204-t01-t02-execution-and-audit-byte-anchor.md)。

**R203 Root T01/T02（协同伪造来源账本的SHA前置守卫，隔离非认证）：** 真实复现R202观察与裁框同时改用另一真实JPEG ROI并重算双SHA仍错误接受；R203将R156/R157/R174/R4/R196/R201及冻结JPEG/HTML共8个来源文件绑定已验证父档案SHA，先验后执行R202像素守卫与R201图重建，拒绝协同篡改及跨账本漂移。父R202 2547/2547逐SHA继承，旧240+新28=268/268，累计2558文件ZIP SHA `26058a5312341f0b6bc3dd1ca98fc72ea6a641be1477aa1de38200a0161457c3`，Python/unzip双独立恢复各2558 SHA和268 QA、QA后不变。T01 0/25、正式ID0、缺根未知、T00–T11 0/12 Accepted；真同源/真机/读屏/历史全量not-run，生产入口及用户Storage未动。[证据](./evidence/v036-round203-t01-t02-coordinated-ledger-provenance-gate.md)。
**R202 Root T01/T02（来源裁框原生像素与注册表互证，非认证）：** 复现R201接受伪造legacy:J:4观察坐标+真实像素SHA的证据链缺陷；R202新增失败关闭守卫，直接复核冻结JPEG 170观察+161裁框原生RGB与161组成员关系，M/V/K/E/B/J/R/X高风险单列。父R201 2535/2535逐SHA继承；旧199+新41=240/240选定QA，累计2547文件ZIP SHA `b02c6b499e4f29ae557880f22970a016bcd978286df7b8ce428b0baab72d02d2`，Python/unzip双独立恢复各2547 SHA与240 QA，QA后SHA不变。真实Chromium旧套件超时not-run，真同源/真机/读屏/历史全量not-run；T01 0/25、正式ID0、缺根未知、T00–T11 0/12 Accepted；生产入口/用户Storage未动。[证据](./evidence/v036-round202-t01-t02-native-crop-ledger-integrity.md)。

**R201 Root T01/T02（来源身份审阅冲突图，非认证）：** 实际读取R200累计ZIP2520/2520逐SHA继承，跨R156/R157/R174/R196/R4账本建立170来源观察、161裁框、151旧别名、36旧未匹配、12无旧别名、2共享裁框冲突、6低清原生矩形交叠与41历史高清审阅边的类型化图谱。审阅图133组、其中28组多观察；V五观察簇、K:2/K:3及E:1/E:8冲突、M四未绑定仍阻断，禁止自动合并或签发永久ID。实跑选定旧229+新71=300/300；R200递归1037套件超时不计pass。R201累计2535文件ZIP SHA `4f190390fd8cacb37e845e8e6de71e913a03a6c8f5b1d05294954e8a9ce63418`，Python/unzip两套独立恢复各2535 SHA和300 QA。高分辨率原始字节/许可/逐笔认证、真同源、真机、读屏、历史全量not-run；T00–T11仍0/12 Accepted、T01 0/25、正式ID0、缺根未知，R11/R12/R35及R12 20SVG缺；冻结入口和用户Storage未动。[证据](./evidence/v036-round201-t01-t02-source-identity-conflict-components.md)。

**R200 原始T03（真实Chromium含描边inkBBox隔离模块，非验收）：** 真读R199父ZIP2508/2508 SHA继承；真实浏览器 `about:blank` 对151草案实例×三视图×编辑前后共906组/918 Path按圆头stroke计算保守inkBBox，修正H:7 `getBBox()`忽略描边的0.90434345差异，最大解析式/真实DOM差0.000003706074；6种非法paint/CSS改动拒绝。实跑旧1001+新Chromium18+静态18=1037/1037；累计2520文件ZIP SHA `2940c4c28686599858acffb5c19fda47ce25605a8175fdfc7b4ed0c63beaba9d`，Python/unzip双独立恢复各2520 SHA与1037 QA。完整历史全量、真同源Storage、真机、真实读屏not-run；T00–T11 0/12 Accepted、T01 0/25、永久ID0、T03未生产集成、缺根未知，R11/R12/R35及R12 20SVG缺。冻结入口/用户Storage未动。 [证据](./evidence/v036-round200-t03-real-stroke-inclusive-dom.md)。


**R199 Root T03（真实Chromium SVG DOM几何预验，非验收）：** 真读R198父ZIP2495/2495 SHA继承；直接渲染R198签发的三视图×编辑前后150 SVG/906实例组/918 Path，about:blank Chromium getBBox/getScreenCTM 83/83；M/V两矩阵变化、149不变，H:7 stroke-inclusive与浏览器geometry-only差异0.90434345已解释。旧901+新浏览器83+静态17=1001/1001；R199累计2508文件ZIP SHA `8b0987baef9181773b01a3189e24effbc1842b7eb570bbd48e20e569bb584ff7`，Python/unzip双独立恢复各2508 SHA及1001 QA。T00–T11仍0/12 Accepted，T01 0/25、永久ID0、T03未生产集成、缺根未知；真同源Storage/真机/读屏/历史全量not-run，R11/R12/R35及R12 20SVG缺；冻结入口和用户Storage未动。[证据](./evidence/v036-round199-t03-real-chromium-svg-geometry.md)。


**R198 Root T03（来源绑定光学校正接入25键三视图隔离组合器，非验收）：** 真读R197父ZIP2482/2482逐SHA继承；R197→R175的隔离桥接仅更新SVG组transform，25键/151实例/153旧Path在full/mini/focus共享100×100坐标，M/V两矩阵变化、其他149不变且Path属性完全一致。实跑旧844+新Node41+静态16=901/901；R198累计2495文件ZIP SHA `6e2c7460154f08c347d7e0835d5f06aa6ad4fc04e669e76f066a006391f5ebe0`，Python/unzip双独立恢复各2495 SHA和901 QA（禁用pyc缓存后无变动）。正式T03未生产集成、T01 0/25、永久ID0、缺根未知、T00–T11 0/12 Accepted；真同源/真机/读屏/历史全量not-run，R11/R12/R35及R12 20SVG仍缺，冻结入口和用户Storage未动。[证据](./evidence/v036-round198-t03-source-bound-optical-three-view.md)。

**R197 Root T03（来源绑定151旧Path光学校正桥接，隔离非验收）：** R196父ZIP2469/2469逐SHA继承，R125/R160真实冻结矢量inkBBox绑定100×100光学编辑、M/V独立示例、来源/基线双SHA及非规范/越界/ID冲突拒绝；选定旧791+新Node35+静态18=844/844，累计R197 2482文件ZIP SHA `ce2c14605f9febdecff64243692db962b9c43247ac1c3dad23eedb2cb09b3769`，Python/unzip双独立恢复各2482 SHA和844 QA，QA后SHA不变。正式T03未生产集成，T01 0/25、永久ID0、缺根未知、T00–T11 0/12 Accepted；真同源/真机/读屏/完整历史not-run，R11/R12/R35和20SVG仍缺，冻结入口/用户Storage未动。[证据](./evidence/v036-round197-t03-source-bound-optical-preview.md)。


**R196 Root T01/T02（原生来源证据交叉审阅，非验收）：** 真实复验R195父ZIP2457/2457逐SHA继承；冻结2008 JPEG上170/170原生RGB证据、14/14审阅卡PNG/上下文SHA、41/41高分辨率审阅边的低清端点复核；36旧槽未匹配、12未绑定来源裁框、2旧槽共享裁框和6原生矩形交叠独立分账。M/V/K/E优先，不把几何交叠当笔画归属；新34+静态18+实跑旧739=791/791，R196累计2469文件ZIP SHA `ac99a7e7f36a9af57b3bc0ca2c120d7e6dc6ccb460913eaaf1efc9e85dc7a024`，Python/unzip双独立恢复各2469 SHA和791 QA。高清原始字节/许可/逐笔认证、真机/读屏/完整历史QA not-run，T01 0/25、永久ID0、真实缺根未知、T00–T11仍0/12 Accepted；缺R11/R12/R35及R12 20SVG；冻结入口和用户Storage未动。[证据](./evidence/v036-round196-t01-t02-exact-source-review-frontier.md)。

**R195 Root T04（25键/156旧槽全量v16来源隔离预演，非验收）：** 实际复验R194父ZIP2447/2447逐文件SHA，使用原R148/R152/R178/R179与R192事务核心，对冻结V0.35 25键156坐标槽全部作合规1单位编辑，签发156别名/156编辑；另测M键局部覆盖、来源不变、幂等、崩溃恢复、克隆/过期/非法来源拒绝。Node私有Map+模拟锁46/46、静态22/22、实跑选定旧671/671，共739/739；R195累计2457文件ZIP SHA `6ba77588da4a7e19b2622d9da722474e3b4be910cbd2b727ee6ac663fbe2895c`，Python/unzip双独立恢复各2457/2457 SHA和739/739 QA。真实浏览器本地管理员阻断，本轮真实浏览器not-run；正式迁移/真机/读屏/历史全量not-run，T00–T11仍0/12 Accepted，T01 0/25，永久ID0，缺根未知；R11/R12/R35与R12 20SVG缺，冻结入口/用户Storage未动。[证据](./evidence/v036-round195-t04-full25-v16-source-rehearsal.md)。

**R194 Root T04：首次在授权真实Chromium执行完整R148/R152/R178/R179来源签发链+R192隔离事务核心，双标签30/30，run 40712389404、artifact SHA256 56fb43276363bcd023fcf9f128f7b6e0650ac77ab7633b58b54c741eec3de42f；R193父2417/2417 SHA继承，R194累计2447文件ZIP SHA256 35eeaf4d0f9bf6b350dc915269ad46f1428d829594cfe8c3bf1894cd51734839，Python/unzip双独立恢复各2447/2447 SHA和671/671选定新旧QA。本地Chromium管理员阻断；远端使用合成v16来源与隔离profile，正式迁移/永久ID/真机/读屏/历史全量not-run。T00–T11仍0/12 Accepted，T01 0/25，缺根未知，R11/R12/R35和R12 20SVG仍缺，冻结生产入口及用户Storage未动。** [证据](./evidence/v036-round194-t04-real-issuer-r192-chromium.md)。

**R193 Root T04（真实Chromium幂等快路径竞态，隔离非验收）：** 独立核实此前R190真实浏览器15/15与R192 Node13/13的原始CI artifact；新增同一R192 ESM在127.0.0.1双标签Web Locks/localStorage/WebCrypto的异步来源变化回归，远端真实Chromium 15/15 success（run 40703055405，artifact SHA `0c8dc9e0a5cba157a4365aa34c153d9d624704b07ceb462a2343620792fe6592`）。R192父ZIP2402/2402逐SHA继承，R193累计2417文件ZIP SHA `88d7258d80cc83aed15b17fa8c97482202dd6d113b49454c610b15896003e6d7`，Python/unzip双独立恢复各2417 SHA、600/600选定新旧QA且QA后SHA不变。本地真实Chromium管理员阻断；浏览器仅合成签发，不是完整R148/R152/R178/R179或正式迁移。T00–T11仍0/12 Accepted，T01 0/25，永久ID0，缺根未知，R11/R12/R35与20SVG缺失；生产入口及用户Storage未动。[证据](./evidence/v036-round193-t04-real-chromium-stale-idempotent.md)。

**R192 Root T04（幂等快路径来源过期拒绝，隔离非验收）：** 实际R189旧ESM复现buildPayload异步期间来源变化后仍返回idempotent；R192候选核心二次来源SHA+原始字节读回并检查shadow/journal。R191父ZIP2390/2390逐SHA继承；新Node36/36+CI等价烟测13/13+静态18/18、选定旧521/521，总计588/588；累计2402文件ZIP SHA `7e844d4126ed6b830088e9346f288509d317646d3d5eaa729cf91e0dfdb014c9`，Python/unzip双独立恢复各2402/2402 SHA及588/588 QA，QA后SHA不变。本地真实Chromium ERR_BLOCKED_BY_ADMINISTRATOR=blocked，远端R190/R192 CI未独立核实；正式T00–T11仍0/12 Accepted、T01 0/25、正式ID0、缺根未知，R11/R12/R35与R12 20SVG缺，冻结生产入口及用户Storage未动。[证据](./evidence/v036-round192-t04-stale-idempotent-source.md)。


**R191 Root T04（Storage同步异常回滚，隔离非验收）：** 父R190 ZIP2379/2379 SHA继承；Node私有Map写入故障29/29、静态18/18、选定旧474/474，共521/521；累计2390文件ZIP SHA `d2d8b2b400daa5ba83011b9df007348927fa2a55c612af6fc69f616dc325453b`，Python/unzip双独立恢复各2390/2390 SHA与521/521 QA，QA后SHA不变。真实Chromium临时127.0.0.1仍ERR_BLOCKED_BY_ADMINISTRATOR=blocked/not-run，R190远端CI unverified。正式T00–T11 0/12 Accepted、T01 0/25、永久ID0、缺根未知；R11/R12/R35与R12 20SVG缺，冻结入口及用户Storage未动。[证据](./evidence/v036-round191-t04-storage-quota-fault-matrix.md)


**R190 Root T04（真实同源SHA异步竞态CI基础设施，隔离非验收）：** R189父ZIP2360/2360成员SHA继承，新增19成员，累计2379文件ZIP SHA `ee13e558617a268763fd6a5869532bf13ad851e6a6b15091b50fdb110babe1c0`；Python/unzip双独立恢复各2379/2379 SHA及474/474选定新旧QA（旧456+新静态18），QA后SHA一致。新增同一R189 ESM真实Chromium双标签Web Locks/localStorage/WebCrypto第三次来源SHA延迟竞态测试与CI工作流；**本地Chromium管理员阻断、远端CI结果未独立核实，浏览器0项计pass**；完整真实R148/R152/R178/R179签发链浏览器测试not-run。正式T00–T11仍0/12 Accepted，T01 0/25、永久ID0、缺根未知；R11/R12/R35及20SVG仍缺，冻结入口与用户Storage未动。[证据](./evidence/v036-round190-t04-real-browser-async-readback-infrastructure.md)。


**R189 Root T04（异步来源SHA读回竞态修复，隔离非验收）：** Node复现R187在第三次来源摘要计算期间外部修改旧v16来源后仍提交过期影子；R189 SHA后读回原始来源字节，变化则拒绝并回滚。R188父ZIP2342/2342 SHA继承；新Node竞态14/14+真实签发Map47/47+静态17/17，选定旧378/378，总计456/456；累计2360文件ZIP SHA `6daddf37eb4c8df9990ee750650d4e9b934f1cbe309d240538fa6a29b1d71946`，Python/unzip双独立恢复各2360 SHA及456 QA。真实同源本地blocked、远端not-run；正式0/12 Accepted、T01 0/25、永久ID0、缺根未知；R11/R12/R35及20SVG缺，冻结入口与用户Storage未动。[证据](./evidence/v036-round189-t04-async-source-digest-readback.md)。


**R188 Root T04（真实签发链接入R187 typed-slot v3，隔离非验收）：** 真实读取R187父ZIP2325/2325 SHA继承；实际R148/R152/R178/R179签发与R187核心连接，Node47/47+静态26/26+实跑旧305/305=378/378；累计2342文件ZIP SHA `b2c13aad18a87e0da0b43ece78d5ad0541f3a96c7557694209c5a24316b07471`，Python/unzip双独立恢复各2342 SHA、378 QA，QA后SHA一致。本地真实Chromium ERR_BLOCKED_BY_ADMINISTRATOR=blocked/not-run，远端R188真实CI not-run；生产迁移/历史全量/真机/读屏not-run。T00–T11仍0/12 Accepted、T01 0/25、永久ID0、缺根未知；R11/R12/R35及20SVG仍缺，冻结入口/用户Storage未动。[证据](./evidence/v036-round188-t04-actual-issuer-typed-slot-bridge.md)。


**R187 Root T04（typed-slot v3隔离恢复，非验收）：复现R186 `before??''`将不存在的shadow与空字符串视为同一SHA，导致非协作空字符串被回滚覆盖；新v3 typed-slot SHA拒绝该冲突，旧v2日志失败关闭。R186父ZIP2310/2310 SHA继承；R187累计2325文件SHA `6f35d9e783986ab16245fcdca7e567808bcab3411cc299aa4252c99361b22ae3`，Python/unzip双独立恢复各2325 SHA、305/305选定新旧QA、QA后SHA一致；本地旧270+新Node18+静态17=305/305。远端真实Chromium同一ESM双标签17/17（CI 40654063434，artifact SHA `cebf673d75c26e179860574bf6bf80e99f0c39efe31558ff962e6d6efa091ff3`），但使用合成来源计划，非R148真实签发浏览器验证；本地浏览器管理员阻断。完整历史、真机、读屏、生产迁移not-run；T00–T11仍0/12 Accepted，T01 0/25、正式ID0、缺根未知；R11/R12/R35和20SVG仍缺，冻结入口及用户Storage未动。** [证据](./evidence/v036-round187-t04-typed-storage-slot-recovery.md)。

**R186 Root T04（非协作影子写入冲突防护，隔离非验收）：** R185父ZIP2289/2289 SHA继承；新增v2 before/next双SHA日志与回滚/恢复冲突拒绝，外部写入不被静默覆盖。Node真实签发65/65+异步竞态16/16+静态20/20+选定旧169/169=270/270；累计2310文件ZIP SHA `0897ac244652dd7fa93038c5717967e8d8a47b61599abf11015ef85ba289b456`，Python/unzip双独立恢复各2310 SHA、270 QA，QA后SHA一致。本地真实Chromium管理员阻断，远端CI/历史全量/真机/读屏not-run；T00–T11仍0/12 Accepted、T01 0/25、永久ID0、缺根未知；R11/R12/R35及20SVG缺，冻结入口与用户存储未动。[证据](./evidence/v036-round186-t04-noncooperative-shadow-conflict.md)。


**R185 Root T04（真实来源签发隔离事务桥接，非验收）：** 实际读取R184父ZIP2271文件并逐项2271/2271 SHA继承；连接原样R148/R152/R178/R179签发与R183共享ESM事务核心，旧v16源只读、隔离影子日志可回滚、127.0.0.1原点先于Storage校验。新增Node40/40+静态21/21+选定旧215/215=276/276；R185累计2289文件SHA `18450dde7b141cb58888f1f2608c76cd0d3dcd71ce97e32aa088a09872fb8b38`，Python/unzip双独立恢复各2289 SHA及276 QA、QA后SHA不变。本地真实Chromium ERR_BLOCKED_BY_ADMINISTRATOR=blocked，远端真实CI not-run；正式T00–T11仍0/12 Accepted、T01 0/25、正式ID0、缺根未知，R11/R12/R35及20SVG缺；生产入口/用户Storage未动。[证据](./evidence/v036-round185-t04-actual-source-issued-disposable-bridge.md)。

**R184 Root T04（真实浏览器故障分支QA修复，非验收）：** R183真实同源CI 40630751605失败：测试复用相同payload走幂等分支，未触发故障；修复后CI 40635880938成功，实际Chromium同一ESM双标签25/25，原始artifact 12793257183 SHA独立核验。R183父ZIP2257/2257 SHA继承，R184累计2271文件ZIP SHA `1404f851ae798a32c5e5698448755c4ddc838421c4920fee85b11f13b3ad23fa`，本地选定旧170+新21+静态24=215/215，Python/unzip双独立恢复各2271 SHA与215 QA。真实迁移/来源认证/真机/读屏/历史全量仍未验收，T00–T11保持0/12 Accepted、T01 0/25、永久ID0、缺根未知；冻结生产入口及用户存储未动。[证据](./evidence/v036-round184-t04-real-browser-fault-branch-fix.md)。

**R183 Root T04（跨Node/浏览器同一ESM隔离事务核心，非验收）：** 新增可注入存储/锁/SHA/签发验证的纯ESM隔离核心及真实R148/R152/R178签发桥接；Node新44/44+真实旧签发17/17，实际重跑选定旧109/109=170/170。R182父ZIP2247/2247逐文件SHA继承，R183累计2257文件ZIP SHA `65526b6e12e03f8fd6a83f9a458e5a492180fe6fd23e4134575c561395ccd185`，Python/unzip双独立恢复各2257/2257 SHA、170/170 QA，QA后SHA不变。本地真实127.0.0.1 Chromium管理员阻断，真实浏览器not-run；远端同一ESM CI工作流已提交，结果尚未核实。历史全量/真机/读屏not-run；正式T00–T11仍0/12 Accepted、T01 0/25、正式ID0、缺根未知；R11/R12/R35和R12 20SVG仍缺，生产入口/用户存储未动。[证据](./evidence/v036-round183-t04-shared-disposable-transaction-core.md)。

**R182 Root T04（真实同源隔离暂存与回滚，非验收）：** 重新核实R181远端真实浏览器原语CI 16/16（run 40619051747），新增R182远端真实127.0.0.1 Chromium独立隔离暂存/回滚/崩溃重载/过期来源/损坏journal QA 24/24（run 40624848783），两份CI原始artifact ZIP SHA与内部JSON均独立校验；R181父ZIP2234/2234 SHA继承，R182累计2247文件SHA `0d44faa8e833f67eea49cc314c92559e4224055780dc9b9f25b6e729ae1e5b23`，Python/unzip双独立恢复各2247/2247 SHA及109/109本地选定QA。R180递归1181旧QA超时不计通过，完整历史全量not-run。本地真实浏览器仍管理员阻断，R182额外26项本地浏览器草案未运行。**远端fixture不是R180生产迁移代码的直接执行**；无正式永久ID、无用户存储写入，T00–T11仍0/12 Accepted，T01 0/25，缺根未知，R11/R12/R35及R12 20SVG仍缺。[证据](./evidence/v036-round182-t04-real-same-origin-disposable-quarantine.md)。


**R181 Root T04（真实同源浏览器QA基础设施，非验收）：** 实际读取R180父ZIP2224文件，2224/2224逐文件SHA继承；新增独立Chromium双标签临时127.0.0.1同源Web Locks/storage事件/WebCrypto源摘要/隔离context QA及GitHub Actions工作流。本地真实Chromium访问被`ERR_BLOCKED_BY_ADMINISTRATOR`阻断（0浏览器检查通过），远端CI结果尚未核实，不能计真实同源通过。新增静态12/12+实跑R180选定旧1181/1181；R181累计2234文件SHA `060e219c8874f4164e7e5683159d85db446fc23dbfc7acccf07a5871e4ce319f`，Python/unzip双独立恢复各2234/2234 SHA、1193/1193 QA，QA后SHA一致。R10嵌入R164，R11/R12/R35及20SVG缺失；真实迁移/历史全量/真机/读屏not-run；原始T00–T11仍0/12 Accepted、T01 0/25、正式ID0、缺根未知，冻结入口与用户存储未动。[R181证据](./evidence/v036-round181-t04-real-same-origin-browser-infrastructure.md)。

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


**R156 Root T02（隔离、非验收）：** 冻结2008 JPEG 170/170原生RGB裁框复核；170来源观察仅对应161个不同原生裁框，8组精确同框证据别名、9条额外观察别名（E1/K3/M4组）。新增内容寻址sourceCropId与独立evidenceObservationId，不把同框等价当成字形/永久ID等价；151旧UID仍草案，15未绑定仍隔离。新42/42、旧1859/1859选定QA；父R155 1942/1942 SHA继承，新ZIP1951文件SHA `082e9c5f03400337205c60fec98323bf66b4fa0559776da38271ac5a19696ac0`；Python/unzip双恢复各1951/1951 SHA、1901/1901 QA且QA后SHA不变。完整历史全量QA not-run，正式0/25键、永久ID0、T00–T11 0/12 Accepted。缺R10–12/R35与20SVG，高清许可/逐笔/真机/读屏未完成，冻结入口及用户存储不变。[证据](./evidence/v036-round156-t02-content-addressed-source-evidence-identity.md)。


**R155 Root T01/T02（隔离、非验收）：** 冻结2008 JPEG原生170/170裁框RGB SHA独立复验；25键建立18条同键ROI重叠边（2旧槽重复：E:1/E:8、K:2/K:3；8同框别名：K4/M4；6旧槽局部重叠；2未绑定物理观察互相重叠：V57像素/X32像素），跨键0。像素相交不等于笔画归属或字根认证；正式0/25键、永久ID0、缺根数未知。父R154 1931/1931 SHA继承，新累计ZIP1942文件SHA `99f0c1315800dccceec75331cf01eba86989be01abf788e602e660a0a8c69125`，Python/unzip双独立恢复各1942/1942 SHA及1859/1859选定QA（旧1730+新129），QA后SHA不变；完整历史全量QA not-run。R10–12/R35及20SVG仍缺，合法高清许可/逐笔/真机/读屏未完成；冻结入口/用户存储不变，T00–T11 0/12 Accepted。 [证据](./evidence/v036-round155-t01-t02-native-pixel-ownership-graph.md)。


**R154 Root T03（隔离、非验收）：** 实际复现R48普通对象注册表遇`__proto__`实例ID时自有键丢失、原型被覆盖；新增零原型不可变安全注册表，151草案实例几何与旧R48逐项一致，增删/重排稳定。新Node 24/24、继承定向1706/1706；父R153 1918/1918 SHA继承，新累计1931文件ZIP SHA `ea6340b4207aa8e9b223140bbdc47436bfa9092814579fea102ca2bc0457b051`，Python/unzip两套独立恢复各1931/1931 SHA、1730/1730 QA且QA后SHA不变。R153授权Chromium CI 40418102420最终success、R153 22/22；R154真实同源not-run，完整历史全量QA not-run。正式T00–T11仍0/12 Accepted，T01 0/25、正式ID0、T03未集成；缺R10–12/R35及20SVG、高清许可/逐笔/真机/读屏未完成，冻结入口/用户存储不变。[证据](./evidence/v036-round154-t03-null-prototype-instance-registry.md)。

**R153 Root T04（隔离、非验收）：** 将R152独立raw来源绑定接入授权临时127.0.0.1双标签Chromium测试；本地ERR_BLOCKED_BY_ADMINISTRATOR=blocked，远端首跑40417492203因引用错误失败，已修复并启动40417922284（最终结果待复核）；继承定向1715/1715，父R152 1910/1910 SHA，新累计ZIP1918文件SHA `106319af615d7a5afb4c122306d649435137d7c502e1a084c7de45137c5b378d`，Python/unzip两套恢复各1918/1918 SHA、1715/1715 QA。完整历史全量QA not-run，T00–T11 0/12 Accepted，T01 0/25、正式ID0、正式迁移未完成；缺R10–12/R35及20SVG，许可/逐笔/真机/读屏未完成。 [证据](./evidence/v036-round153-t04-real-origin-raw-source-binding.md)。

## 第152轮 · Root T04 独立raw来源绑定（隔离、非验收）
R152原始T04（隔离、非验收）：R151 WeakMap只能验证当前realm计划签发，不能验证注入reader与原始存储raw相符。R152实际复现R151接受伪SHA、伪编辑、漏键和转义重复JSON键，新增独立raw SHA/坐标/键/编辑校验及只读reader facade。Node新27/27、继承1688/1688；R151父1902/1902 SHA，R152累计1910文件ZIP SHA `2ed630217d3b85a20d18eba07d636d31fe93885212d50eb0a2861ea8a19b62e4`，Python/unzip两次独立恢复各1910/1910 SHA及1715/1715定向QA。R152真实同源not-run，完整历史QA not-run；原始T00–T11仍0/12 Accepted，T01 0/25、正式ID0、T04正式迁移未完成；缺R10–12/R35和R12 20SVG，高清许可/逐笔/真机/读屏未完成。 [证据](./evidence/v036-round152-t04-independent-raw-source-binding.md)。


R151 累计 ZIP：**1902 文件**，SHA256 `f7770b71a7f0aa52eaff20c4afee5481624e6ac7796c4eabf9b5a139d82a78aa`；父 R150 **1892/1892 SHA** 继承；Python zipfile 与系统 unzip 双独立解压，各 **1902/1902 SHA**、**1688/1688 定向 QA**，QA 后 SHA 均不变。完整历史全量 QA 仍 not-run。

## 第151轮 · Root T04 已签发对象校验（隔离、非正式验收）
R150 的 verifyPlan 仅校验调用者自算的 SHA 与顶层冻结状态；实际复现修改 sourceSlots=999、重新计算摘要并冻结后仍被接受。R151 新增私有 WeakMap 签发登记，verifyPlan 只接受本 JS realm 的 planReadOnly 原样返回对象；克隆、重序列化、外部自签计划一律拒绝。**这不是跨进程数字签名，不能代替可信来源/正式永久 ID 或生产迁移。**冻结 V0.35 与 2008 JPEG、176 编码、正式 SVG、用户存储均未修改。Node WebCrypto+FakeStore 新 35/35、继承 R142–R150 定向 1653/1653；本地 Chromium file:// 与 localhost 被策略阻断。R150 真实授权 Chromium CI run 40393427271 已成功（33/33、27/27、16/16），R151 远端真实同源 CI run 40402103656 已完成 success：新增签发门禁 22/22，继承 33/33、27/27、16/16；独立下载并复验 artifact SHA256 `dba4bf50741c95633b055f4028cce883682479cb8c2eba3358b68033c5826d11`。仅为隔离合成数据预检，不是生产迁移或正式验收。R10–12/R35 ZIP 和 R12 20SVG 仍缺，高清许可/逐笔/真机/读屏/完整历史 QA 均未通过；T00–T11 **0/12 Accepted**，T01 0/25，正式永久 ID 0，T04 生产迁移未完成。证据见 [R151](./evidence/v036-round151-t04-issuer-bound-alias-plan.md)。


## 第150轮 · Root T04 来源别名只读影子计划（隔离、非验收）

R149真实同源CI run 40384582893 已从独立artifact确认：33/33旧同源、27/27严格v16 pass；R150新增SHA绑定且深冻结的旧槽别名影子计划，25/25 Node FakeStore QA，明确拒绝未经批准永久ID及任何生产写入。R149父1881/1881 SHA继承，R150累计1892文件ZIP SHA `51396c322a4a4ac7bd47b3aefb3b8bdcf8c7797b72dc353c1b9763f4a0d31d09`；Python/unzip双独立恢复各1892/1892 SHA及1653/1653定向QA，完整历史全量QA not-run。R150本地真实同源blocked，R150远端CI待确认；T00–T11仍0/12 Accepted，T01 0/25、正式ID0、T04生产迁移未完成；R10–12/R35及R12 20SVG仍缺，高清许可/逐笔/真机/读屏未完成。冻结入口、176编码、用户存储未动。[证据](./evidence/v036-round150-t04-immutable-legacy-alias-shadow-plan.md)


## 第149轮 · Root T04 严格v16来源真实同源预检（隔离，非验收）

R149把**原始R148 5944字节、SHA256 93095d5ef4ef85d8238b90b51f6fbc2e8968e6c5a51498e7503dccfe26b27fed**的只读严格JSON重复键门禁接入GitHub Actions授权Chromium双标签真实127.0.0.1原点QA（WebCrypto/Web Locks/localStorage/跨标签storage/独占锁竞争/拒绝非法来源）；运行 [40384582893](https://github.com/tims-SP/glyphspace/actions/runs/40384582893)在取得最终结果前记**pending**，不计通过。本地真实同源仍ERR_BLOCKED_BY_ADMINISTRATOR=blocked；R142–R148定向1628/1628通过。父R148 ZIP1875/1875 SHA继承，新R149累计1881文件ZIP SHA `a8f88dfbf54380e848c6610525d3272e9aeda69745f07247c707fe5635256259`，Python/unzip两套独立恢复各1881/1881 SHA、1628/1628定向QA，QA后SHA不变；完整历史全量QA not-run。原始T00–T11 0/12 Accepted、T01 0/25、正式永久ID0、T04生产迁移未完成；缺R10–12/R35 ZIP及R12 20SVG、合法高清许可/逐笔/真机/读屏。冻结HTML/JPEG/176编码/正式SVG/用户存储未改。[证据](./evidence/v036-round149-t04-strict-real-origin-shadow-preflight.md)

## 第148轮 · Root T04 旧v16重复来源键失败关闭（隔离、非验收）

R148 Root T04（关联T00/T02）实际复现R147旧v16来源JSON重复G键被JSON.parse静默覆盖、即使raw SHA匹配仍被接纳；隔离增加重复对象键（含转义等价键）失败关闭扫描、冻结25键156槽默认值SHA、部分键/原始raw/来源签名门禁。父R147 ZIP1865/1865逐文件SHA继承；新R148累计1875文件，ZIP SHA `9b9c58ecd97cc1f68960ff4c70086148f197d1ec30704b9d4c8d0d6e490d35fa`，Python zipfile/unzip两套独立恢复各1875/1875 SHA及1628/1628定向QA（旧1590、新Node29、Chromium about:blank仅解析9）。本地真实同源仍管理员blocked；R148远端真实同源not-run、真机/读屏0、完整历史QA not-run。缺R10–12/R35和R12 20SVG、高清许可/逐笔；T00–T11 0/12 Accepted，T01 0/25、正式永久ID0、T04生产迁移未完成，冻结入口/176编码/用户存储未改。 [证据](./evidence/v036-round148-t04-strict-legacy-v16-source-duplicate-key-gate.md)


## 第147轮 · Root T04 合成旧v16部分存储真实同源影子预检（非验收）

R147 Root T04（关联T00/T02）新增冻结V0.35 v16局部坐标来源只读影子测试：从SHA锁定HTML提取25键156旧坐标，在GitHub Actions授权临时127.0.0.1原点双标签读取G/K/X三键、22缺席键与3条模拟编辑，保留原始raw及无关sentinel，来源SHA变化拒绝；真实Chromium 33/33（run 40365890296）通过。容器本地真实同源仍ERR_BLOCKED_BY_ADMINISTRATOR；新Node WebCrypto/FakeStore 14/14、R142–R146继承1576/1576；父R146 ZIP 1855/1855逐文件SHA继承，新R147累计1865文件，Python/unzip双独立恢复各1590/1590本地定向QA与1865/1865 SHA前后不变。ZIP SHA bebcacaafadb23734dc11bb76ac095af21c744fa7b2c2e6fbec65c54c8153f70。真实用户存储未触碰；该CI仅合成数据预检，生产V0.35→V0.36迁移、正式永久ID、T03集成均未验收；历史R10–12/R35 ZIP和R12 20SVG仍缺，高清合法许可/逐笔/真机/读屏/完整历史QA未完成；T00–T11 0/12 Accepted、T01 0/25。 [证据](./evidence/v036-round147-t04-real-origin-v16-partial-shadow.md)

## 第146轮 · Root T02 来源—候选UID交叉核验（隔离、非验收）

R146 Root T02（关联T01/T04/T05）只读交叉核验R73/R75的151个草案UID与R145的170条原生物理来源观察：151旧可视槽各一草案UID；M同框别名4、M未绑定影子4、K4及B/J/R/V/X微形7，共15条未绑定物理观察（不是已确认缺根）；36旧未匹配属于151旧槽子集；5条related关联不生成独立UID。重算170/170原生RGB SHA；新201/201，继承R142–R145共1375/1375，每套1576/1576；父R145 1847/1847 SHA继承，新ZIP 1855文件，Python zipfile与unzip两套独立恢复各1855/1855 SHA且QA后不变。ZIP SHA e01168b3a786903568a8d6173d544f967affd2beb4f71304275d2790764287eb。R10–12/R35及R12 20SVG仍缺，合法同源高清许可/逐笔/真实同源/真机/读屏/历史全量QA未通过；T00–T11仍0/12 Accepted、T01 0/25、正式永久ID0；冻结入口/2008 JPEG/176编码/正式SVG/用户存储未动。 [证据](./evidence/v036-round146-t02-170-source-151-draft-uid-crosswalk.md)

## 第145轮 · Root T01/T02 170来源观察审阅覆盖门禁（关联T05；隔离、非验收）

R145复核R144父ZIP 1839/1839逐文件SHA，170条来源观察中58条关联特定案件、112条无特定案件但仍待审（均非字根/缺根数）；新增逐观察来源审阅失败关闭门禁与379/379新QA，继承R142/R143/R144共996/996定向QA；Python zipfile与unzip双独立恢复各1847/1847 SHA、1375/1375 QA及QA后SHA一致。累计ZIP SHA `4eec6b3b80561532dc79a4915d392a4cfc7506e50cd92d6d01e8b62ec40d68a3`。正式T01 0/25、永久ID0、T05未完成、T00–T11 0/12 Accepted；R10–12/R35及20SVG缺失，高清许可/原字节/逐笔/真同源/真机/读屏/历史全量QA未通过；冻结HTML/JPEG/176编码/正式SVG/用户存储未动。 [证据](./evidence/v036-round145-t01-t02-observation-review-coverage.md)

## 第144轮 · Root T01/T02 全25键逐键来源审查队列（隔离、非验收）

- R144从R143父ZIP继承1830/1830文件SHA，建立25键逐键来源审查登记：170条物理来源记录（R81 159含151旧槽+8 M候选，R95 K 4，R96微形7）；R69 36旧未匹配只作别名。12相交分量+36旧未匹配+4 M影子=52个`review-only`案件，**不是52个缺根**；M重复来源不重复计入151。新676/676+旧957/957定向QA，Python/unzip双恢复各1839/1839文件SHA、1633/1633 QA及QA后SHA一致。R144 ZIP SHA `fc2a2257e9d17d031e7a012e7712987deeffc0110eea6e8ac301333fe635bba0`。高清候选许可未核、原字节不在ZIP，R10–12/R35及R12 20 SVG仍缺，真实同源R108回放管理员阻断，真机/读屏/历史全量QA未完成。T01 0/25、正式ID0、T05未完成、T00–T11仍0/12 Accepted；冻结HTML/JPEG/176编码/正式SVG/用户存储未改。[证据](./evidence/v036-round144-t01-t02-keywise-source-review-queue.md)


## 第143轮 · Root T01/T02/T05 M来源裁框版本谱系（隔离、非验收）

- R143聚焦M键8个来源观察的**原生裁框版本谱系**：4条旧槽完全同框别名+4条不可渲染影子观察；M-vis-02旧M:1框21×23与R86未批准的26×23证据候选框分离，新增115原生像素且RGB SHA不同，禁止将旧别名自动升级为候选框；M-vis-04左侧2像素归属仍未定。新87/87、继承R142/R141/R140/R81/R86/R87定向953/953，Python/unzip双独立恢复各1830/1830文件SHA、各1040/1040 QA且QA后SHA一致；父R142 1821/1821逐文件SHA继承，R143累计ZIP SHA `5b50c4141fdcebbbf42dda3c3e140426788f9cbcdd16f4449522d26ea55e833b`。正式T00–T11仍0/12 Accepted、T01 0/25、正式永久ID0、T05未完成，真实缺根数未知；历史R10–12/R35 ZIP及R12 20SVG未恢复，合法同源高清/逐笔/真同源迁移/真机/读屏/完整历史全量QA仍未通过。冻结HTML、2008 JPEG、176编码、正式SVG、用户存储未修改。 [证据](./evidence/v036-round143-t01-t02-t05-m-crop-evidence-lineage.md)

## 第142轮 · Root T01/T02 全25键物理来源集合（关联T05，隔离、非验收）

- R142将R81 159、R95 K物理观察4、R96微形7合并为25键**170/170原生RGB SHA复核**；R69 36旧未匹配仅作别名交叉核验。全源同键采框相交**18边**（10完全同框、8部分相交），12待审分量涉及28观察，其余142观察在本轮集合内无相交；B1/E1/J1/K5/M4/V4/X2。此为物理来源几何，不证明同一/独立字根、笔画归属或永久ID。父R141 1813/1813 SHA继承，R142累计1821文件ZIP SHA `7c7cf8f7d1036f32fe7e6a89f4d65455a38db4c30ac3d2bbd08b8f0d3876be37`；Python/unzip双独立恢复各1821/1821 SHA、各新233+旧733=966/966定向QA。正式T00–T11仍0/12 Accepted、T01 0/25、正式ID0、T05未完成；历史R10–12/R35和20SVG缺失、高清许可/逐笔/真同源/真机/读屏/历史全量QA未通过。冻结入口、176编码、正式SVG、用户存储未动。[证据](./evidence/v036-round142-t01-t02-full-25key-physical-source-universe.md)


## 第141轮 · Root T01/T02 来源相交连通分量（隔离、非验收）

- R141 Root T01/T02（关联T05）：冻结2008 JPEG、R81 159、R96 7及R69 36条原生裁框**202/202 SHA复核**；7候选与旧槽来源相交图为12节点/8边/5分量。新发现V:4与V-vis-06、V-vis-07三方共有原生矩形[644,662,3,11]共33像素；V:4仍blocked_namespace。X-vis-03经X-vis-02连通旧X:0但**不能传递为身份相同**。父R140 1803/1803逐文件继承，R141累计1813文件ZIP SHA `bbef7887976f9c932439ce803ce7aee0e39bffc5b1b13d3a1804ef30862a9493`，Python/unzip双独立恢复各1813/1813 SHA、各新237+旧484=721/721定向QA。正式T00–T11仍0/12 Accepted、T01 0/25、永久ID0、T05未完成；缺R10–12/R35及20SVG、高清许可未明、真同源/真机/读屏/完整历史QA未验收；冻结入口、176编码、正式SVG和用户存储未动。 [证据](./evidence/v036-round141-t01-t02-source-overlap-component-graph.md)

## 第140轮 · Root T01/T02 微形候选对原生ROI交叠（隔离、非验收）

- R140 Root T01/T02（关联T05）发现R96七个来源微形候选之间的两组**此前未单列**ROI交叠：V-vis-06/07原生57像素（灰度≤160/192/224分别2/3/6暗像素），X-vis-02/03原生32像素（0/0/0）。此为来源审阅候选对，不证明笔画归属或独立字根。R139父1793/1793逐文件SHA继承，R140累计1803文件ZIP SHA `3128d7d725071ef7904bd88bf0d56f73998c3e993a08c1739177b725ecb4c204`；Python zipfile/unzip双独立恢复各1803/1803 SHA、各新25+旧489=514/514定向QA；QA产生2个__pycache__文件均清理后SHA一致。T00–T11仍0/12 Accepted、T01 0/25、正式永久ID0、T05未完成；R10–12/R35及20SVG仍缺、许可未核、真实同源/真机/读屏/完整历史QA未验收；冻结入口、176编码及用户存储不变。 [证据](./evidence/v036-round140-t01-microform-pair-native-overlap.md)


## 第139轮 · Root T03 挂载后DOM失效守卫（隔离、非验收）

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


## 第131轮 · T03自包含SVG符号引用诊断（隔离，非验收）

- 第131轮 Root T03（关联T07）隔离修复浏览器诊断的跨SVG `<use>`→`<symbol>`悬空依赖：新增本地`<defs>`克隆与唯一href绑定，独立Chromium 2 contexts×11对×2尺寸×4模式=176次渲染，396/396历史字段一致；两套恢复分别复测新守卫50/50与精选旧QA282/282，最终ZIP 1722/1722双解压SHA一致、最终各104/104 QA。父R130 1712/1712 SHA继承；第131轮ZIP SHA `f67fed7b5d62d01cf1d50336c66451aefcdfa46c429bcbeec6cbdfc3ce077549`。R129完整953与候选恢复R130完整505曾尝试但超时，**不计pass**。不能证明渲染波动唯一根因或跨设备稳定；T03未集成，T00–T11 0/12 Accepted，T01 0/25、正式ID0、T05未完成；历史R10–12/R35 ZIP和20SVG缺失，真实同源迁移/真机/读屏/许可仍未解，冻结入口及用户存储未动。[证据](./evidence/v036-round131-t03-self-contained-symbol-replay.md)。


## 第130轮 · J:4原图复合区域与区位徽记角色交叉核验（隔离，非验收）

- 第130轮 Root T01/T02/T03：2008 JPEG J:4原生裁框[1005,397,24,32]是包含圈和双竖笔的复合来源区域；R81 J:4来源账本仍为`blocked_invalidated`及`round69Unbound=true`。冻结V0.35源码明确H/J/K区位竖笔是说明性徽记，独立Chromium验证H/J/K分别为1/2/3笔且每键有1圈；R129 J:4/marker1的648/648墨迹重叠不能当作新增独立字根、碰撞已批准或源图认证。新增30/30来源语义QA，精选继承475/475 QA；Python/unzip两套独立恢复最终各505/505，候选1710/1710文件SHA一致，最终1712/1712文件双恢复SHA及新增30/30通过。R129完整953项定向QA未重跑、历史全量QA not-run；Chromium首次重放出现L:1和J:4短暂像素差异，失败已记录，重试才通过。R129父1698/1698继承，R130累计1712文件ZIP SHA `e7d0d0fda95ca938cba1e49359ce3507356e6c65a9cb25d383c0a3cede7c0bb3`。正式T01 0/25、正式永久ID0、T03未生产集成、T05未完成、T00–T11仍0/12 Accepted；历史缺包/20SVG、高清许可、真实同源迁移、真机读屏仍未解，冻结入口及用户存储未动。 [证据](./evidence/v036-round130-t01-j4-zone-badge-source-role-conflict.md)。


## 第129轮 · Root T03区位徽记绘制顺序与J:4根墨迹全包含（隔离，非验收）

- 冻结V0.35真实Chromium DOM 9组BBox候选+2阴性对照，400/800px分别渲染字根、徽记、原始及反向绘制顺序：5组真实像素交叠且绘制顺序敏感，4组所测分辨率无交叠；**J:4/marker1在800px下648/648字根墨迹像素落入区位徽记墨迹区域，反向顺序648像素变化**。此为必须复核的视觉归属风险，不是错误字根或已认证根；新增失败关闭碰撞复核门禁，不自动白名单。父R128 1679/1679 SHA继承，R129累计**1698文件** ZIP SHA `a7facaeaa26667d36dd0584d443b2e8b63abfbed8f24ec0c4a5c1a591286e732`，Python/unzip双独立恢复各新61+旧892=**953/953定向QA**、QA后1698/1698 SHA一致；完整历史全量QA not-run。T01 0/25、正式ID0、T03未集成、T05未完成、T00–T11 **0/12 Accepted**；历史缺包、许可、真同源迁移、真机读屏仍未解决；冻结入口/176编码/正式SVG/用户存储未动。[证据](./evidence/v036-round129-t03-zone-badge-paint-order-and-root-containment.md)。

## 第128轮 · Root T03真实绘制像素遮罩核验（隔离，非验收）

- 从第127轮9组SVG标注BBox候选推进到真实Chromium绘制遮罩：冻结V0.35原生字根/标注DOM独立栅格化，400/800px与两阈值复核；**5/9真实像素交叠、4/9仅BBox假阳性**，2个阴性对照无交叠。重叠不等于错误或来源认证。新增73/73+继承819/819，两套独立恢复各892/892；父R127 1663/1663继承，R128累计1679文件，ZIP SHA `0606855e57ec7e83c8240cc25148802d1aef654833e36933eab6a98605e940b0`，双恢复QA后1679/1679 SHA一致。**T00–T11仍0/12 Accepted**，T01 0/25、正式ID0、T03未集成、T05未完成；历史缺口、许可、真同源/真机/读屏/完整历史QA未解，冻结入口与用户存储未动。[证据](./evidence/v036-round128-t03-frozen-dom-paint-mask-intersection.md)。

## 第127轮 · Root T03 SVG圈注/徽记保留区实测（隔离，非验收）

- 第127轮 Root T03隔离新增冻结V0.35真实SVG圈注/区位徽记包络：Chromium about:blank从原页面DOM实测25键39个标注（7根圈/补码框、32区位徽记），对R125解析式墨迹240对及R126文字标签78对比较；6键H/J/L/N/Q/Y存在9组**保守BBox交叠候选**（非真实涂色碰撞），7组预期根圈叠加单列，标签交叠0/78，越界0/39。新Chromium39/39+Node30/30+继承750/750，两套Python/unzip独立恢复各819/819、1663/1663后验SHA一致；R126父1652/1652继承，R127 ZIP SHA `f2692f705f93b26b3e722c86b61725dcc22b506d2c1eda95b29f32347eb6eb6e`。**仍非正式验收**：T01 0/25、正式ID0、T03未集成、T05未完成、原始T00–T11 0/12 Accepted；历史R10–12/R35和20SVG缺失、许可/真机/读屏/正式迁移/全量历史QA未完成，冻结入口及用户存储未动。 [证据](./evidence/v036-round127-t03-frozen-svg-annotation-paint-envelopes.md)。


## 第126轮 · Root T03 SVG标签保留区真实浏览器测量（隔离，非验收）

- **第126轮 Root T03隔离新增字母/区号保留区实测**：从SHA冻结V0.35源码取25键区号与P/Q特殊字母坐标，在独立Chromium about:blank实测50个SVG文字BBox，与151旧实例解析式墨迹进行302对几何比较；直接交叠0/302，但R:5距字母仅0.782472/100，按1/100安全间距有1/302预警。新浏览器50/50+Node19/19+继承681/681，两套各750/750；R125父1641/1641 SHA继承，R126累计ZIP1652文件SHA `d8707b50a0249052fb74d208d2f6b135e3be6c7727255862badba7c20661e3d2`，Python/unzip两套各1652/1652 SHA一致。**仍仅隔离**：T01 0/25、正式ID0、T03未集成、T05未完成、T00–T11 0/12 Accepted；历史缺包、许可、真同源/真机/读屏/完整历史QA未解；冻结入口/176编码/用户存储未动。[证据](./evidence/v036-round126-t03-chromium-label-reservation-clearance.md)。


## 第125轮 · Root T03 SHA绑定解析式矢量墨迹与光学校正守卫（隔离，非验收）

- **第125轮 Root T03隔离实质修复**：将R54解析式矢量墨迹BBox（151旧形态/153真实Path）SHA绑定R50 Path与R53几何，再接入R48/R124光学校正越界判定；151中145条与R50近似BBox存在非零差异（最大0.4841016564源单位、0.105布局单位）。新Node24/24+独立Python157/157+继承500/500，每套681/681；R124父1629/1629继承、R125 ZIP1641文件SHA `b64d144b0c4f79ce113330e4399db4a2fae3916e277e595e402d9a45893955cb`，Python/unzip两套各1641/1641后验SHA一致。**仍仅隔离实现**：正式T03未集成、T01 0/25、正式ID0、T05未完成、原始T00–T11 0/12 Accepted；历史R10–12/R35及20SVG缺失，真同源/真机/读屏/历史全量QA未运行。冻结入口/176编码/用户存储未动。[证据](./evidence/v036-round125-t03-sha-bound-analytic-vector-optical-guard.md)。


## 第124轮 · Root T03 光学校正后墨迹越界守卫（隔离实现，非正式验收）

- 发现R48 SVG坐标解析器只限制目标geometry，未限制光学校正ox/oy之后的真实inkBBox；冻结151条Path草案逐项注入ox=200均可在旧解析器中越出100×100。新增隔离守卫拒绝越界、验证锚点重构、保留未认证来源标记；**151/151**原始几何与旧矩阵一致、**151/151**恶意偏移拒绝、**151/151**小偏移往返。新增22/22 + 继承478/478，两套Python/unzip独立恢复各500/500 QA与1629/1629 SHA一致；父R123 1620/1620继承，新ZIP SHA256 `1b2ece4a2a2486aaf078b0fc27136c7a02f3c24b30a959832a03c9deb509aec9`。
- 本轮未生产集成；R50 Canvas inkBBox并非精确矢量边界，不能宣称T03 Accepted。T01 0/25、正式ID0、T05未完成、T00–T11 **0/12 Accepted**；历史R10–12/R35与20SVG缺失，真实同源仍被管理员策略阻断，真机/读屏/正式迁移未运行。冻结HTML/176编码/正式SVG/用户存储未动。[证据](./evidence/v036-round124-t03-optical-envelope-guard.md)。


## 第123轮 · Root T01/T02 M相邻候选墨迹最小割与脆弱桥接（关联T05，非认证）

- 冻结2008 JPEG/R81清单SHA绑定；M03/04五阈值4/8邻接最小割均0；M05/06仅阈值176连通（4邻接割4、8邻接割8）；M07/08在144/160/176的4邻接割1/1/2、8邻接割2/2/3，8邻接割像素位于原图x=1039、y=658–660。新28/28+旧450/450，两套Python/unzip恢复各478/478 QA及1620/1620后验SHA；R122父1610/1610继承，R123 ZIP SHA256 `20d5aa05ff4b26e0b5d7e46b4d2818df73b66983f184bebeb646db3f8be86812`。只是阈值脆弱桥接，不是逐笔归属或字根拆分证据。T01 0/25、正式永久ID0、T05未完成、T00–T11 0/12 Accepted；缺历史第10–12/35轮与20SVG，高清许可/真机/读屏/正式迁移未解，冻结入口/176编码/用户存储未动。 [证据](./evidence/v036-round123-t01-m-pair-min-cut-bottleneck.md)。


> **核对日期：2026-10-26**。仓库正式网页仍是V0.35冻结版本；GitHub保留第46轮基线，并登记已独立复验的第123轮隔离累计ZIP（ZIP本体不在GitHub）。这不是已发布的V0.36版本。

## 第122轮 · Root T01/T02 M-vis-04/08阈值隔离与邻根拓扑（关联T05，非认证）

- 冻结2008 JPEG/R81来源SHA绑定：M04原框[1017,623,14,13]在阈值96分裂、128–176可隔离且左伸2原生像素；M08原框[1040,653,12,15]在96分裂、128可隔离且底伸2像素，144–176因邻近墨迹连通触及隔离ROI边界而阻断。低清M07/08共享连通分量3/5档、M05/06仅1/5档、M03/04为0/5；R117高清5/5与本轮低清3/5是不同分辨率测量。**无笔画归属、裁框、身份或正式SVG认证。**
- R121父ZIP SHA `c3be0c550f467c94aaf38e38a0f855752eca44e0d6b9dac0ad29931270df4711`，1595/1595逐文件继承；R122累计**1610文件** SHA256 `e1b878d2c23ea2db07db1c27959911d9208a6e505ad5dad842af762f31f210bc`。新增30/30、继承420/420，两套Python/unzip恢复各450/450定向QA，QA后各1610/1610 SHA一致；完整历史QA not-run。
- T01正式0/25、T02正式永久ID0、T05未完成、原始T00–T11 **0/12 Accepted**。第10–12/35轮与20SVG仍缺；高清许可、真实迁移、真机/读屏未解；冻结入口/176编码/正式SVG/用户存储未动。[证据](./evidence/v036-round122-t01-m04-m08-source-topology.md)。

## 第121轮 · Root T01/T02 M-vis-02原生墨迹包络诊断（关联T05，非认证）

- 冻结2008 JPEG与R81原生清单SHA绑定，M-vis-02旧框`[1045,585,21,23]`在五档8邻接连通分量中均截断右侧4–5原生像素；联合**未批准**墨迹包络`[1053,587,18,21]`，不与其他M来源框重叠。该结论仅为低清像素几何诊断，非笔画归属/补图/永久ID批准。
- 父R120 **1582/1582**逐文件SHA继承；R121累计**1595文件** ZIP SHA256 `c3be0c550f467c94aaf38e38a0f855752eca44e0d6b9dac0ad29931270df4711`；Python zipfile与系统unzip两套各**420/420定向QA**、QA前后**1595/1595** SHA一致。完整历史全量QA not-run。
- T01 **0/25**、正式永久ID **0**、T05未完成、T00–T11 **0/12 Accepted**。历史第10–12/35轮ZIP及20SVG仍缺；高清许可、真实迁移、真机和读屏未解；冻结入口/176编码/正式SVG/用户存储未动。[证据](./evidence/v036-round121-t01-m02-component-envelope.md)。

## 第120轮 · Root T01/T02 全25键旧裁框原生边缘审计（非正式认证）

- 第120轮读取冻结2008 JPEG及R81来源清单，**151/151旧可视+8/8 M暂存**逐框原生RGB SHA核验，25键旧来源均有记录；五阈值四侧边界审计标记**81/151**旧框为墨迹延续待复核（不是确认错误/缺根），M-vis-02右侧、M-vis-04左侧、M-vis-08底侧优先；K/E/B/V身份阻断未解。新46/46、继承354/354；父R119 1572/1572继承，新累计**1582文件** ZIP SHA256 `81fd92d03b6b5f92dd827a10ea2bf5a12116e6ea0c91524475d088aa0cbffd84`；Python/unzip两套各400/400定向QA、QA后各1582/1582 SHA一致。完整历史全量QA not-run；T01 **0/25**、正式ID **0**、T00–T11 **0/12 Accepted**。历史10–12/35与20SVG仍缺，许可/真机/读屏/正式迁移未解；冻结入口和用户存储未动。[证据](./evidence/v036-round120-t01-all-key-native-crop-edge-census.md)。

## 第119轮 · Root T01/T02真实高低清ORB跨来源配准（非正式认证）

- 独立[GitHub Actions 40196733036](https://github.com/tims-SP/glyphspace/actions/runs/40196733036) **success**：固定SHA真实3508×2480高清JPEG与冻结2008图的133个不可逆ORB数值特征配准，101比值匹配、**99 RANSAC内点**、22/25空间格，中位误差**0.0636低清像素**、95分位0.9552。五组M/K/E风险框实际投影相对纯尺寸比例最大角点差0.126高清像素。两次前置CI因数值特征转录错误被SHA拒绝，未计pass。**这是几何配准，不是逐笔、笔画归属或许可认证**。
- 父R118 **1560/1560**逐文件SHA继承，R119累计 **1572文件** ZIP SHA256 `d2a160a86764c2b903241d3b9efdb49b756544411f13d55a03a0f46f21efa898`；Python/unzip两次独立解压、QA前后各1572/1572 SHA一致，每套新增7+继承347=**354/354**定向QA。完整历史全量QA not-run；本地高清原字节不可得，真实跨图配准仅CI完成。
- T01 **0/25**、正式永久ID **0**、T05未完成、T00–T11 **0/12 Accepted**。高清许可未确认，缺第10–12/35轮与20SVG；真实迁移/真机/读屏not-run；冻结入口/176编码/正式SVG/用户存储不动。[证据](./evidence/v036-round119-t01-real-cross-source-orb-registration.md)。

## 第118轮 · Root T01/T02高低清特征配准前置（非正式认证）

- 本轮新增SIFT/RANSAC来源坐标仿射配准器，冻结2008 JPEG来源SHA通过，**仅源图派生合成仿射7/7 QA**；904内点、中位误差0.1171为合成测试，不是3508×2480高清跨图实测。真实高清原始字节本地不可得，**真实跨来源配准not-run**，不批准裁框/字根/永久ID。
- 父R117 **1551/1551**逐文件SHA继承，R118累计**1560文件** SHA256 `287e93524cd698319bb502d5517c4c806f84c04f5fbc440185f7a6a89bbee993`；Python/unzip双独立恢复及QA后各1560/1560一致，每套新7+旧340=**347/347**定向QA；完整历史全量QA not-run。
- T01 **0/25**、正式永久ID **0**、T05未完成、T00–T11 **0/12 Accepted**。高清许可未确认，缺第10–12/35轮与第12轮20SVG；真实迁移/真机/读屏not-run；冻结入口/176编码/正式SVG/用户存储不动。[证据](./evidence/v036-round118-t01-affine-registration-preflight.md)。

## 第117轮 · Root T01/T02 M键严格边界来源核验（非正式认证）

- [独立高清GitHub Actions 40187583179](https://github.com/tims-SP/glyphspace/actions/runs/40187583179) **success**：SHA固定3508×2480 JPEG，M-vis-02五阈值直接跨旧框边界的暗像素对 **30/34/34/37/37**，严格框内连通扩框像素 **166/177/180/186/190**；M03/04严格交集连通0/5档，M05/06仅最高阈值连通，M07/08五档连通。修正R116“上下文连通可能绕行框外”的证据歧义；**不批准裁框/笔画归属/永久ID**。
- 父R116 **1540/1540**逐文件SHA继承，R117累计 **1551文件** SHA256 `a7aa36bcf6e994da9a93430881202649310bb48ebf5b5e8714bc357c7f1b0cca`；Python/unzip两次独立恢复与QA后均1551/1551 SHA一致。新增9/9、继承331/331，两份恢复各 **340/340** 定向QA；完整历史全量QA not-run。
- 高清版权许可、精确特征配准、逐笔归属未解决；历史第10–12/35轮及第12轮20SVG仍缺；T01 **0/25**、正式永久ID **0**、T05未完成、原始T00–T11 **0/12 Accepted**。真机/读屏/真实用户迁移not-run，冻结正式入口及用户存储未动。[证据](./evidence/v036-round117-t01-m-strict-seam-topology.md)。

## 第116轮 · Root T01/T02 M键高清连通性（非正式认证）

- [独立GitHub Actions 40183270210](https://github.com/tims-SP/glyphspace/actions/runs/40183270210) **success**：真实3508×2480高清JPEG固定SHA，M-vis-02右扩高清11×52像素在五阈值下166/177/180/186/190个暗像素**全部连接旧框内同一墨迹分量**；M03/04五阈值无跨框连通，M05/06仅最高阈值连通，M07/08五阈值均连通。只是裁框截断风险与候选归属冲突证据，**不批准扩框、字根或永久ID**。
- 冻结2008 JPEG本地同算法20/20新增QA；继承R115/R114/R113/R112/R96/R95/R84共311项，每套331/331。父R115 **1529/1529** SHA继承，R116累计**1540文件** SHA256 `a2823ee6844c6fb86b3802a2b1053c6c3abff9345b1f9b7d304da5e1071eff08`；Python/unzip两次独立恢复及QA后1540/1540 SHA一致。
- 高清版权/精确特征配准/逐笔归属仍未解决；T01 **0/25**、正式永久ID**0**、T05未补图、原始T00–T11 **0/12 Accepted**；缺第10–12/35轮ZIP及第12轮20SVG；真机/读屏/真实用户迁移not-run。冻结生产入口与用户存储未动。[证据](./evidence/v036-round116-t01-m-highres-ink-connectivity.md)。

## 第115轮 · Root T01/T02 高清原始像素21 ROI核验与来源导入安全门禁（非正式验收）

- [独立CI](https://github.com/tims-SP/glyphspace/actions/runs/40178902354) success，实际读取3508×2480高清原始JPEG字节，按R81旧图坐标尺寸比例核验M/K/E **21个**风险ROI并输出不可逆RGB SHA；M vis-02未批准右扩框11×52高清像素中灰度<160有186个，不能认定归属。E:1/E:8、K:2/K:3高清采框各自RGB完全同源，旧阻断继续。**版权未确认、逐笔认证仍0/25**。
- R114 ZIP导入函数存在可由匹配伪造元数据绕过的`../`成员路径门禁；R115合成复现并拒绝。新15/15、继承R114/R113/R112/R96/R95/R84 **296/296**，合计每份311/311。R114父1519/1519继承；R115累计1529文件SHA256 `8f77cc07500544e1f28a6b29c7aea2aa078051f63bb17b9f0fef6b4c8d5927d8`，Python/unzip两次独立恢复及QA后1529/1529一致。
- T01正式0/25、永久ID0、原始T00–T11 **0/12 Accepted**；历史第10–12/35轮及20SVG仍缺、许可未解、真机/读屏/正式迁移not-run；冻结生产入口/用户存储未动。[证据](./evidence/v036-round115-t01-highres-roi-pixel-triage.md)。

## 第114轮 · Root T01/T02 高清同版式参考图来源候选（非正式验收）

- 发现06wb社区镜像标为官方的高清简体图ZIP（996823字节、JPEG **3508×2480**，ZIP SHA256 `fb7a9984a84be12a71d71dc86088b8859762ca97cb9a3db173b4a8adaf0b9707`）；[独立GitHub Actions](https://github.com/tims-SP/glyphspace/actions/runs/40175565336) **success**，真实下载/解压两份ZIP，核对JPEG SHA256及尺寸。与冻结1536×1086参考图五区dHash仅**4/320位**差异，是高度相似排版候选，**非逐笔认证/版权授权**。
- 本地只读来源门禁新31/31，继承R113/R112/R96/R95/R84共265项；R113父1509/1509 SHA继承，R114累计**1519文件** SHA256 `a24303d1e53c4643f7c8a7bbf3c68925c1225a4f76b4918dc1ba6f0aeb5af50c`；Python/unzip独立恢复各1519/1519，恢复后**296/296**及QA后SHA均一致。
- 上游无明确可再分发许可，**高清原始图片不入GitHub/累计ZIP**，原图逐笔认证仍0/25，永久ID0，T00–T11 **0/12 Accepted**；第10–12/35轮与20SVG缺失，真机/读屏/正式迁移not-run。冻结生产入口/176编码/用户存储不动。[证据](./evidence/v036-round114-t01-highres-source-candidate.md)。

## 第113轮 · Root T02/T04 候选UID来源绑定与默认坐标防投毒（非正式验收）

- 真实复现R111影子映射可在151/5计数不变时互换Q:0/K:2 UID，及伪造默认坐标导致真实用户编辑被误判未修改。R113在独立隔离脚本中以冻结HTML、2008 JPEG、R46/R73/R75及V0.35 Chromium实取25键156槽默认坐标的SHA绑定阻断，旧版两个漏洞复现且新版拒绝。
- 新34/34，继承6组310项，共7组**344/344**；父R112 **1498/1498**逐文件SHA继承，新累计ZIP **1509成员**，SHA256 `acdd2f820af7e7b2dc45b371edb9856a1e02d9dd26acff56f93ab0ece43dc8e2`，Python/unzip两次独立恢复各1509/1509及QA后SHA一致。首次恢复QA改写历史pyc导致后验SHA失败，已记录为失败并使用禁写字节码环境从头重跑，不计第一次通过。
- **仅候选影子映射，不是永久ID或用户迁移**。T01 0/25、正式永久ID0、T00–T11 0/12 Accepted；缺历史第10–12/35轮和第12轮20SVG、合法同源高清原图、真机/读屏/正式迁移均未解决。冻结正式入口/176编码/用户存储不变。[证据](./evidence/v036-round113-t02-source-bound-uid-shadow.md)。

## 第112轮 · Root T01/T02 原生坐标系与身份交叉门禁（非正式验收）

- R46的旧采框为键位局部坐标，R81为JPEG原生坐标；R112用25键各自referenceRect转换，**25/25键、151/151旧可视、36/36旧未匹配、M 8/8、七微形7/7、K物理4/4**来源与候选身份一致。各键Y原点不宜按整行统一；K/E同框、B/V命名空间与M四未绑定仍阻断。
- 新增36/36、继承R84 124、R96 35、R95 36、R69 19、R111 Chromium60；两份独立恢复各**310项定向QA**通过。父R111 **1488/1488** SHA继承；R112累计ZIP **1498成员**，SHA256 `3ff5b88ee12fc2cc849bee8c01955feac90f3cefee38e75e1c763903a435fb7f`，Python/unzip双恢复与QA后各1498/1498 SHA一致。首次组合验证超时，后续分项完成，不计超时为pass。
- **只是坐标系与历史证据一致性，不是字形认证**：T01 0/25、T02正式永久ID0、T05正式补图0、原始T00–T11 **0/12 Accepted**。同源高清原图/许可、历史10–12/35轮与20SVG、真机/读屏、正式用户迁移缺口未解；冻结入口/176编码/用户存储未动。[证据](./evidence/v036-round112-t01-t02-native-coordinate-frame-identity.md)。

## 第111轮 · Root T04/T02 旧版局部v16快照只读无损准入（非正式验收）

- 发现R110仅接受25键完整旧快照会拒绝V0.35实际合法的局部v16用户调位；R111在隔离代码中保留出现键与缺失键来源位图，只映射显式编辑，不把缺失键伪装为完整用户覆盖。冻结V0.35真实Chromium about:blank + 内存localStorage四组局部案例，新增**60/60**；旧R110 30、R109 16、R108 10、R77 179、R105 170定向QA通过。
- R110父ZIP1477/1477逐文件SHA继承；R111累计**1488文件**，SHA256 `163fc6c599817b2d28e2fd8d6ac64b457630b55b5ac045196f7676151f16f924`；Python/unzip两套独立恢复各1488/1488，QA后逐项SHA一致。ZIP仅外部交付，不在GitHub。
- **仍非正式迁移**：真实V0.35同源用户迁移not-run；T01 0/25、正式永久ID0、原始T00–T11 **0/12 Accepted**。历史第10–12/35轮及20SVG、高清原图许可、真机/读屏缺口不变。冻结正式入口/176编码/用户存储未动。[第111轮证据](./evidence/v036-round111-t04-partial-v16-readonly-preservation.md)。

## 第110轮 · Root T04/T02 冻结旧页浏览器快照准入（非正式验收）

- 真实Chromium `about:blank` 运行未修改的V0.35 HTML，**仅内存替身localStorage**，发现旧版接受部分v16坐标快照、损坏v16阻断有效v15回退两个兼容风险；新增完整25键/156槽只读准入门禁、旧槽→候选UID影子桥接，30/30 QA通过。三处合成用户调位3/3保留，M:4关联隔离，K:2来源阻断不解除；**不是正式迁移**。
- R109父ZIP1468/1468逐文件SHA继承；R110累计1477文件、ZIP SHA256 `8b83bd4abf3807bcf862e748bf1b0928bd759d88d66a24e2d90e94b12186d561`。Python/unzip独立恢复各1477/1477，恢复后R110新30+旧16+10+179+170项定向QA通过，QA后两套成员SHA各1477/1477。完整历史全量QA/R106本轮not-run。
- 本地真实同源迁移、真机、读屏not-run；T01 0/25、正式永久ID0、T00–T11 **0/12 Accepted**，冻结入口/原图/176编码/用户存储未动。详见[第110轮证据](./evidence/v036-round110-t04-v035-browser-storage-shadow.md)。

## 第109轮 · Root T04 真实隔离原点三阶段崩溃恢复（非正式验收）

- 独立核验GitHub Actions [R108先行真实原点运行](https://github.com/tims-SP/glyphspace/actions/runs/40153502403)：Ubuntu Chromium临时127.0.0.1双标签、真实Web Locks/localStorage，**11/11**通过。此前本地管理员阻断的事实仍然成立，不能把CI结果冒称本地通过。
- 修改`scripts/qa_v036_t04_disposable_origin.py`新增三阶段pending/record/head崩溃恢复、pending写入及回滚阻断、恢复后回滚。 [R109真实原点运行](https://github.com/tims-SP/glyphspace/actions/runs/40156644345)（提交`053bb786`）实际日志 **23/23 PASS**，工件ID12584890814、ZIP SHA256 `f8673646e124dbf9b17420696865cd977e8d75cb1d3b6355c30ff0a576f5ae18`。**仅隔离协议真实浏览器预检，非旧用户迁移。**
- R108父ZIP SHA256 `51ee682e0df8ee4cde134b9a2b085be96959e6ed3435bd7c7e094bd02bfcbec5`，**1459/1459**父成员继承；R109累计ZIP **1468文件**，SHA256 `d07f18b0d49bba080a896de22041a90077b8a22dbd4bd61a90c28fbe8f7ef3dc`；Python/unzip独立恢复各1468/1468，恢复后新16+旧10+26+179+170项QA分别通过，QA后SHA仍1468/1468。
- 新发现R108 ZIP内双恢复QA JSON是**1458文件的临时快照**，与外部最终1459文件复验记录不同；本轮保留旧文件原字节并明确差异，绝不把中间日志作为最终ZIP证明。正式T01 0/25、永久ID0、T04真实V0.35迁移not-run、T00–T11 **0/12 Accepted**；同源高清图、历史缺口、真机及读屏未解决。见[第109轮证据](./evidence/v036-round109-t04-real-origin-crash-recovery.md)。

## 第108轮 · Root T04 隔离回滚原子性修复（非正式验收）

- 发现R107回滚在验证前驱记录前就修改head的原子性缺陷；R108改为先核验前驱SHA/schema再写head。Node VM合成存储/锁复现旧缺陷并验证修复 **10/10**；继承R107静态26/26、R77 Node179/179、R105 Chromium about:blank170/170。R106完整浏览器QA尝试超时未计pass。
- 父R107 ZIP **1449/1449**逐文件SHA继承；R108 ZIP **1459文件** SHA256 `51ee682e0df8ee4cde134b9a2b085be96959e6ed3435bd7c7e094bd02bfcbec5`；Python/unzip双独立恢复各1459/1459，定向QA重跑、QA后SHA均一致。ZIP仍仅外部交付。
- 临时127.0.0.1真实浏览器仍`ERR_BLOCKED_BY_ADMINISTRATOR`，T04真实同源事务**blocked/not-run**；新增仓库独立CI回归脚本与工作流，**远端结果待独立确认**。未触碰正式入口/用户存储；T01 0/25、T02正式ID0、T00–T11 **0/12 Accepted**。见[第108轮证据](./evidence/v036-round108-t04-rollback-atomicity.md)。

## 第107轮 · Root T04 独立真实原点预检路径（非正式验收）

- 新增一次性loopback原点、独立Chromium profile双标签的Web Locks/localStorage事务测试脚本（随外部R107 ZIP交付）及[GitHub Actions真实原点烟测](../.github/workflows/v036-t04-disposable-origin.yml)。本地临时127.0.0.1仍被`ERR_BLOCKED_BY_ADMINISTRATOR`阻断，真实事务**blocked/not-run**；远端运行结果尚未独立确认。
- R107静态安全QA **26/26**，旧R77 Node **179/179**、R105 Chromium about:blank **170/170**；R106完整浏览器QA本轮尝试超时，未计pass。父R106 **1439/1439**成员SHA继承；新R107 ZIP **1449文件** SHA256 `3b5c30e922a9f58de189aa817f9369e768e4fed81dc9fedbe34b93a8ad43df5b`；Python/unzip两次独立恢复各1449/1449，QA后SHA一致。
- 仅是T04真实原点测试路径和隔离协议前置，不是旧用户迁移、正式集成或Accepted。T01 0/25、T02正式永久ID0、T00–T11 **0/12 Accepted**；冻结入口/176编码/用户存储未动。详见[第107轮证据](./evidence/v036-round107-t04-disposable-origin-preflight.md)。

## 第106轮 · Root T00 冻结176编码的Chromium行为回归（非正式验收）

- 真实Chromium `about:blank`加载冻结V0.35 HTML，**仅在内存插入测试钩子**；176条旧训练数据逐字交叉比对，引导/进阶/盲打三模式528个实际浏览器案例，错误输入、Backspace、正确编码、短码空格确认、四码自动跳转及盲打遮蔽，新增 **3143/3143** QA通过。
- 父R105 **1433/1433**成员SHA继承；R106累计ZIP **1439文件** SHA256 `55e96b14b2a969e33b7e6b9e39fa132d0836062bbbb4d3fe9104d044d2de26c0`。Python与unzip两次独立解压各1439/1439，恢复后各执行新R106 3143、旧R77 179、旧R105 170项并在QA后各1439/1439 SHA一致；R103/R104/R99继承定向QA亦在工作区执行通过。
- 仅为旧行为**回归基准**，不是新V0.36三视图正式集成或T00/T09验收；T01 0/25、T02正式永久ID0、T03生产未集成、T05未补图、原始T00–T11 **0/12 Accepted**。同源存储blocked/not-run、真机/读屏not-run、完整历史QA not-run；历史ZIP及高清原图许可缺口不变。冻结生产入口/176编码/用户存储未动。见[第106轮证据](./evidence/v036-round106-t00-176-browser-oracle.md)。

## 第105轮 · Root T03/T07 隔离事务性碰撞门禁（非正式验收）

- 实际Chromium复现R104允许同键草案`inkBBox`碰撞仍`attest=true`；R105在提交前检查25键/151候选UID/409对，151个主动撞入测试均被拒绝，批量编辑及签名导入原子回滚。新增 **170/170** Chromium QA。
- 父R104 **1425/1425**成员SHA继承；R105累计ZIP **1433文件** SHA256 `2ffa0ecc3b72bee3ef7d2a24d76431f3619c29b5734ed7dbf513388b0b7d876a`；Python/unzip两次独立解压、QA前后各 **1433/1433** SHA一致，两套恢复环境各5组定向新旧QA（702项）通过。完整历史全量QA not-run。
- 仅隔离候选矩形门禁，不是实际墨迹/描边/圈注/标签全验收；T03/T07未正式集成，T01 0/25、T02正式ID0、原始T00–T11 **0/12 Accepted**。历史缺口、高清原图、真实同源存储/真机/读屏阻断不变。见[证据](./evidence/v036-round105-t03-t07-transactional-collision.md)。

## 第104轮 · Root T03 祖先伪元素遮挡门禁（非正式验收）

- 真实Chromium五类CSS `::before`/`::after`遮挡使R103错误放行、真实截图像素变化而SVG `getBBox()`不变；R104隔离HTML新增祖先伪元素绘制/层叠签名并拒绝，新增Chromium **25/25**。
- 父R103 **1410/1410**逐文件SHA继承；R104累计ZIP **1425文件** SHA256 `3840ac7eaeea34c66d3c251dd8906117d92de2f5536b34256d26b6afad275289`。9组新旧定向QA **637项**；Python/unzip各分两段独立恢复，共四次QA前后**1425/1425** SHA一致。首次整批执行超时未计通过；完整历史QA not-run。
- 独立临时profile访问127.0.0.1仍`ERR_BLOCKED_BY_ADMINISTRATOR`，真实Web Locks/localStorage blocked/not-run；真机/读屏not-run。T03未生产集成、T01 **0/25**、T02正式永久ID **0**、原始T00–T11 **0/12 Accepted**；历史第10–12/35轮ZIP和第12轮20SVG仍缺，冻结入口/2008 JPEG/176编码/用户存储未动。见[证据](./evidence/v036-round104-t03-pseudo-element-occlusion.md)。

## 第103轮 · Root T03 SVG祖先绘制完整性（非正式验收）

- 真实Chromium复现R94祖先CSS可隐藏字根而attest误放行：父级opacity=0使截图10522像素改变，SVG getBBox不变；九类祖先opacity/filter/clip/mask/transform攻击R94均误放行，R103隔离门禁全部拒绝。新增Chromium 26/26。
- 父R102 **1397/1397**成员SHA继承；R103累计ZIP **1410成员** SHA256 `bdd1f42c847c01bc98b278294b7a6074550e293c9e4b977f601dc4fe75ef8874`，Python/unzip双恢复各1410/1410、QA后SHA再一致。每份8组定向新旧QA共612项通过；合并执行曾超时，unzip恢复环境分项重跑通过，完整历史QA仍not-run。
- T03仍**未生产集成**；T01正式认证0/25、正式永久ID0、T00–T11 **0/12 Accepted**。同源存储blocked/not-run，真机/读屏not-run，历史ZIP/高清原图缺口未补；冻结正式入口与用户存储未动。见[第103轮证据](./evidence/v036-round103-t03-ancestor-paint-integrity.md)。

## 第102轮 · T01/T02/T05 M键原生像素交叠拓扑（非正式验收）

- R101三组未批准扩框交叠，经原始JPEG原生像素五阈值复核：**M03/04的2×13区域五阈值暗像素均0（框交叠）；M05/06的4×18区域有8/9/11/13/23暗像素；M07/08的2×17区域有1/2/4/5/7暗像素且连通性随阈值变化**。三组均不解除来源归属阻断，不产生正式字根/永久ID/SVG。
- 父R101 1385/1385逐文件SHA继承；R102累计ZIP **1397文件**，SHA256 `1e5972251f3386e91d709e1869a36009f8aead732eaa4e22bfb93d9f21b094a5`；Python/unzip两次独立解压与QA后各1397/1397 SHA一致。新增52/52、继承R101 58/58、R84 124/124、R86 20/20、R100局部、R99 Chromium302/302通过。
- 缺R90 ZIP无法重跑R100十包链；第10–12/35轮ZIP、第12轮20SVG仍缺；同源合法高清原图未取得；同源存储blocked/not-run，真机/读屏not-run，完整历史QA not-run。**T01 0/25，T00–T11 0/12 Accepted**，冻结正式入口未动。见[第102轮证据](./evidence/v036-round102-m-native-overlap-topology.md)。

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

## 第91轮 Root T03 · 候选UID几何驱动真实三视图SVG DOM（2026-10-24；非验收）

- R64/66来源绑定三视图与R77/78候选UID几何在隔离Chromium SVG DOM贯通：151 UID/25键、100×100、inkBBox、五锚点/光学位移，full/mini/single transform同步、非法编辑原子回滚。5关联及4个M影子观察不渲染。
- 新Chromium about:blank真实DOM **27/27**，继承R77/R78/R83–R90 **10组**QA；父1270/1270 SHA继承，累计ZIP **1283文件** SHA256 `b15be0b2c893ae448b7a80b59939098029c7c89ae3e149744690f1a6669367c3`，Python zipfile与系统unzip双独立解压及恢复后QA/逐文件SHA一致。ZIP不在GitHub，见 [R91证据](./evidence/v036-round91-t03-live-uid-three-view-dom.md)。
- **原始T03生产内核仍未正式集成/Accepted**；T01 0/25、T02正式永久ID0、T00–T11 0/12 Accepted。真实同源存储blocked/not-run，真机/读屏not-run，历史第10–12/35轮ZIP及第12轮20SVG缺失；冻结入口/176编码/用户存储未动。

## 第92轮 Root T03 SVG DOM来源完整性门禁（2026-10-24；非验收）

真实Chromium复现R91可接受伪造`<use href>`、跨键替换UID及篡改`<defs>` Path的问题；R92独立隔离模块改为全25键成员/资产/变换/Path逐项核验，并修复导入/撤销预检提交及真实click/Enter/Space键帽事件绕过包装层的问题。新29/29、旧R91 Chromium27/27、旧10组QA通过；父1283/1283继承，累计ZIP1296成员，SHA256 `cc737571ca35ee6f9b8adda7172954021868a8f3ee6019540fac70b1dad80953`，两次独立解压及QA后SHA均1296/1296。仅about:blank，不是生产内核验收。证据：[R92](./evidence/v036-round92-t03-dom-provenance-attestation.md)。T01 0/25、正式永久ID 0、原始T00–T11 0/12 Accepted；真实同源/真机/读屏仍blocked/not-run。

## 第93轮 Root T03 · SVG片段ID全局来源门禁（2026-10-24；非验收）

- Chromium实际复现R92漏洞：在可信defs之前注入同名fragment ID，`<use>.getBBox()`绘制几何被替换，但R92 attest仍通过。R93在整个document检查149规范ID唯一性、`getElementById`指向规范defs节点，并拒绝额外base[href]；非法DOM修改在编辑/切键前失败关闭。
- 新Chromium12/12、R92回归29/29、R91回归27/27、继承10组定向QA通过。第92轮1296/1296逐文件继承，第93轮累计1308文件，SHA256 `ea618a9dffc1e03f5aad5affa63de7a13f1e5d0da75e4059ef5a7b31b8e57480`；Python zipfile/system unzip双独立恢复各1308/1308，恢复后QA/文件SHA一致。ZIP本体不在GitHub，见 [R93证据](./evidence/v036-round93-t03-document-fragment-identity.md)。
- 仍非正式T03生产集成；T01 0/25、T02正式ID 0、T00–T11 0/12 Accepted；真同源/真机/读屏not-run，冻结入口/用户存储未动。

## 第94轮 Root T03 SVG computed-paint 完整性修复（2026-10-24；隔离，非验收）

- 第93轮可信defs中的g可被外部加transform使真实Chromium getBBox宽度82→164而attest仍通过；CSS将Path opacity置0也未被发现。第94轮隔离模块新增SVG节点属性/身份、computed paint属性和computed transform门禁，阻断两类真实绘制漂移。
- 新Chromium about:blank 18/18、R91 27/27、R92 29/29、R93 12/12、继承10组定向QA通过。父第93轮1308/1308 SHA继承；累计第94轮ZIP **1319文件**，SHA256 `2dcbc8880ab8adde82a8693c5c05f163d81c1476763a10d57d925d4a296df4fc`；Python zipfile/system unzip双恢复各1319/1319且QA后SHA一致。首次组合验证超时，第二恢复环境后续单独重跑成功。
- 初始样式可信只是隔离原型假设，未实现生产T03/正式字根认证。T01正式0/25、T02永久ID 0、T00–T11仍0/12 Accepted。缺历史第10–12、35轮与第12轮20SVG；同源高清许可、真实同源存储、真机和读屏未验收。见 [第94轮证据](./evidence/v036-round94-t03-computed-svg-paint-integrity.md)。

## 第95轮 Root T01/T02 · K键物理来源身份仲裁（2026-10-24；隔离非验收）

- 基于原始2008 JPEG/R46/R88/R89固定SHA，K键4个不同原生像素**物理观察位置**与5条旧槽分开建账；K:1仅关联，K:2/K:3仍共享左下历史框双阻断，K:3**未发现独立来源ROI**，K:4冻结「〢」与右下来源形态仍待逐笔复核；右上圈注未分类。4个位置**不是4个认证字根**。
- 新增隔离来源身份仲裁，拒绝K:3借用K:2框、圈注自动升级、伪造来源/许可/永久ID。Pillow/OpenCV原生RGB交叉核验，新QA **36/36**，R81/R86–R94十组旧QA均通过；父R94 **1319/1319** SHA继承，累计ZIP **1331文件** SHA256 `7deea5a9de203a1cefee6f52ca988f7d26c5588b6b0316a68fab42c2b1dd6db0`，Python zipfile/system unzip双独立恢复、两环境各11组QA及QA后1331/1331 SHA通过。完整历史全量QA未运行；ZIP本体不在GitHub。详见 [R95证据](./evidence/v036-round95-k-physical-source-identity-arbitration.md)。
- 真实临时127.0.0.1 Chromium原点仍被 `ERR_BLOCKED_BY_ADMINISTRATOR` 阻断，Web Locks/localStorage事务blocked/not-run；真机/读屏not-run。缺第10–12/35轮ZIP及第12轮20 SVG，同源高清原图和许可仍缺。**T01 0/25、正式永久ID 0、T00–T11 0/12 Accepted**；冻结入口/176编码/用户存储未动。

## 第96轮七微形原生来源观察（2026-10-24，非验收）

- 原始T01/T02前置、关联T05：以第41轮七项未映射清单、第46轮阻断账本和2008原始JPEG，建立B/J/R/X/V五键**7个独立物理来源观察ID**，逐项原生RGB与历史ROI一致；B vis-02↔B:7、V vis-06/07↔V:4存在来源框交叠但原命名空间阻断不解除，R vis-02与X vis-03不与旧槽框相交但不能据此宣称新增字根。正式ID 0、T01 0/25、缺根数未知。
- 父第95轮1331/1331 SHA继承；第96轮隔离累计ZIP **1340文件** SHA256 `d1e609c29a3852e724a6192ef2795c993a85cdc21a2cddfb9a11163a05a7be0c`；两种独立解压各1340/1340并各跑12组新旧QA、QA后SHA一致。新增35/35，旧11组；完整历史全量QA未执行。GitHub不包含ZIP字节。
- 原始T00–T11仍**0/12 Accepted**，真实同源存储、真机、读屏本轮not-run；冻结入口/176编码/正式SVG/用户存储未动。缺第10–12、35轮ZIP及第12轮20SVG；高清同源合法原图和许可未获得。证据：`docs/evidence/v036-round96-seven-microform-source-crosswalk.md`。

## 第97轮 Root T07 · SVG变换后矩形碰撞预检（2026-10-24；非正式验收）

- 发现Chromium `<use>.getBBox()`未应用use自身transform：直接以其做碰撞会让完整/mini各409/409对误报。新增独立CTM四角映射到100×100键内坐标的几何对照；1440×900与390×844两个about:blank视口，各306/306实例几何、824/824配对，转换后0矩形相交；H:7 stroke使用既有inkBBox保守预检，不等于真实墨迹碰撞认证。
- 父第96轮1340/1340逐项SHA继承；第97轮累计ZIP**1348文件** SHA256 `bb744069860dd24c51e5fe08a6c81e63ff7b94768c3fae822533a7e8cb08d0d5`，Python zipfile与系统unzip双独立解压各1348/1348，两套恢复环境各13/13组新旧QA通过，QA后SHA一致。ZIP不在GitHub。见[第97轮证据](./evidence/v036-round97-t07-transformed-svg-bbox-preflight.md)。
- T07仍未正式验收；T03未生产集成；T01正式0/25、永久ID0、原始T00–T11仍**0/12 Accepted**。真实同源存储导航管理员阻断，真机/读屏not-run；缺历史第10–12/35轮ZIP及第12轮20SVG、合法同源高清原图。冻结入口/176编码/正式SVG/用户存储未动。

## 第98轮 Root T07 · 屏幕空间stroke/键头/跨键碰撞预检（2026-10-25；非验收）

第97轮1348/1348逐文件SHA继承；R98使用Chromium `getScreenCTM()`把草案inkBBox投影至CSS像素坐标，扩展检查跨键、键头、SVG裁切、键格外溢与H:7描边包络。8视口×DPR1/2/3=24个模拟上下文，7344实例、19776同键及523968跨键配对，隔离草案矩形重叠/越界0；3类主动DOM篡改均被检测。320px完整/mini键格约24.7 CSS px，触控目标风险待真实UI/设备审查。14组新旧QA在两份独立解压环境均通过；累计ZIP1359文件，SHA256 `1e1aeeac3c0dd321f5e2f22d26eb00e133ef6f6ecc7087c46dc3e231155da7ed`，ZIP不在GitHub。见[R98证据](./evidence/v036-round98-t07-screen-space-stroke-header-crosskey.md)。**T07尚未正式集成/认证，T01 0/25、T00–T11 0/12 Accepted**；真同源/真机/读屏未验收，历史缺口未补。

## 第99轮 Root T03/T07 · Chromium真实alpha像素绘制包络（2026-10-25；非验收）

- 从R98累计ZIP **1359/1359** SHA逐项继承；对151候选UID在Chromium about:blank中独立构造SVG并读取Canvas alpha像素，在400×400及800×800两档各151个实际绘制实例，合计**302/302**非空且草案inkBBox包络误差不超过1栅格像素；H:7描边包含在内。3个主动篡改（描边加粗、路径消失、几何位移）均检出。R98继承14组定向QA重跑通过。
- R99累计ZIP **1366文件** SHA256 `7fe43e62975b1e1b339f46674d452c519a3ad6b6d130e448e8c2f670d12f4fea`，Python zipfile/system unzip各1366/1366、恢复后新旧QA及逐文件SHA一致；外部ZIP不在GitHub。证据：[R99](./evidence/v036-round99-t03-t07-raster-alpha-ink-envelope.md)。
- **仅草案SVG渲染证据**，不等于原图逐笔、正式墨迹/圈注/标签碰撞或生产集成。T01 0/25、正式永久ID0、T00–T11 **0/12 Accepted**；真同源存储/真机/读屏未验收，缺历史第10–12/35轮与第12轮20SVG，同源高清合法原图/许可未获得。冻结入口、176编码、正式SVG及用户存储未动。

## 第100轮独立归档链与M键来源复验（2026-10-25；非验收）

- T00：工作区真实存在的第90–99轮十份累计ZIP逐包SHA/文件数/成员SHA复验；第90→99轮9次相邻继承完整一致。**不证明第90轮以前的历史连续完整**。
- T01/T05：M键8个来源ROI独立从2008 JPEG重算RGB SHA、原始PNG SHA和解码像素均8/8一致；其中4个无旧槽，只是审阅候选，**正式新增字根0、T01 0/25、真实缺根数未知**。
- 第10–12、35轮目录及第12轮20SVG在R99累计包中仍缺。第100轮父R99 1366/1366继承；累计ZIP **1373文件** SHA256 `f90595913cb0469809897a0dab9c20a84628fff2b61e032d2506b5e691cc559c`，Python/unzip两套独立恢复各1373/1373及新旧定向QA、QA后SHA通过。ZIP不在GitHub。证据见[第100轮](./evidence/v036-round100-archive-chain-m-provenance.md)。
- 真实独立profile本轮127.0.0.1/localhost/file://导航均管理员阻断；Web Locks/localStorage事务blocked/not-run。完整历史QA、真机、读屏not-run；**原始T00–T11仍0/12 Accepted**，生产入口/176编码/用户存储未动。

## 第101轮 T01/T02/T05 M来源归属冲突（2026-10-25；非验收）

- 父R100累计ZIP 1373/1373逐文件SHA继承；R101隔离包**1385文件**，SHA256 `e40cae7e5932df6c2784bd977d1c511a5d7a4609e7002b509f10b72ef3795cd2`，Python/unzip双独立解压各1385/1385及恢复后新旧定向QA通过，ZIP本体不在GitHub。
- 8个M原生ROI、6px上下文halo与4旧别名+4未绑定候选重新绑定，6个未批准复框发现**3组像素归属交叠**：M03/04、M05/06、M07/08。新增58/58失败关闭QA；旧124/124、20/20、R99 Chromium 302/302双恢复复跑。**无正式新增字根或Path**。
- 当前运行环境缺R90 ZIP，R100外部十包链**本轮复跑blocked**；不能将此前R100链记录冒充本轮新通过。缺第10–12、35轮及第12轮20SVG，同源高清合法原图未取得。
- **T01正式0/25、正式永久ID0、T00–T11 0/12 Accepted**；真同源事务blocked/not-run，真机/真实读屏not-run；生产入口、176编码、正式SVG及用户存储不变。[证据](./evidence/v036-round101-m-native-source-ownership.md)。
