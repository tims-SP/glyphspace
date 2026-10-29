# 07 · V0.36验收标准：原始T00–T11 + UI-track

**R210 Root T03（有效绘制墨迹边界守卫，隔离非验收）：** 真实Chromium复现R200祖先opacity=0/全裁剪仍报告非空inkBBox，截图黑像素正常3200→不可见0；新增computed-style祖先/Path失败关闭守卫，906旧SVG组新旧正常几何一致、14/14对抗拒绝。父R209 2640/2640逐SHA继承；选定旧620+新Chromium12+静态12=644/644，R210累计2651文件ZIP SHA `12e329603696bd85991666c222e14f68124c920a8fb9effa2331661923433449`，Python/unzip双独立恢复各2651 SHA与644 QA、QA后不变。T03未生产集成，原始0/12 Accepted，来源0/25、永久ID0、缺根未知；同源blocked、真机/读屏/历史全量not-run；冻结入口/用户存储未动。[R210证据](./evidence/v036-round210-t03-effective-ancestor-paint-guard.md)。


**R209验收边界：** 166个`draft-only/`候选与50票据的52条类型化链接只证明历史审阅身份可独立追踪，不能作为referenceShapeId、assetId、永久instanceId或已认证字根；E/K同裁框异SVG仍阻断。旧554+新66=620/620选定QA，2640累计成员双独立SHA/QA恢复。来源0/25、永久ID0、缺根未知、T00–T11 0/12 Accepted；合法高清原图/许可/逐笔、真实同源、真机、读屏、历史全量仍blocked/not-run。[证据](./evidence/v036-round209-t01-t02-typed-draft-identity-bridge.md)。


**R208验收边界：** 151旧SVG实例/153 Path、36个未匹配旧槽同时有JPEG观察+旧SVG、K三条无别名混合裁框观察、E/K两组同裁框异SVG Path SHA仅属来源完整性与冲突定位；不证明高清原图逐笔、形态、正式缺根、永久ID、T05补图或生产集成。选定旧487+新50+静态17=554/554，累计2628双恢复SHA/QA；历史全量、真同源、真机、真实读屏not-run/blocked。T01 0/25、永久ID0、Root 0/12 Accepted。[证据](./evidence/v036-round208-t01-t02-t05-three-way-source-vector.md)。


**R207验收边界：** 36/36旧未匹配槽在R156已有原生JPEG观察/裁框，但未获正式referenceShape匹配、逐笔或语义认证；R206顶层sourceCropId=null不能解释为没有原图来源。新增156槽证据映射与36条来源交叉表，旧424+新63=487/487，父2600 SHA继承、累计2613双独立恢复。正式来源0/25、永久ID0、缺根数未知、T00–T11仍0/12 Accepted；真同源blocked，真机/读屏/历史全量not-run。[证据](./evidence/v036-round207-t01-t02-legacy-source-reconciliation.md)。


**R206验收边界：** 50条review-*只是证据工作票据（12未绑定、36旧未匹配、2同裁框冲突），不是referenceShapeId/assetId/instanceId，也没有完成五维审阅。旧359+新49+静态16=424/424、累计2600双独立SHA/QA恢复。没有合法同源高清原始字节/许可、逐笔认证、生产集成、真同源、真机/读屏或历史全量QA；T01 0/25、永久ID0、Root 0/12 Accepted。[R206证据](./evidence/v036-round206-t01-t02-semantic-arbitration-tickets.md)。


**R205验收边界：** 冻结原生JPEG 12未绑定裁框的逐像素矩形覆盖审计，3626逐框像素中2908在同键旧矩形之外；这不代表独立笔画、缺根数量或字根身份。旧306+新53=359/359，累计2586成员双独立SHA与QA恢复。T01 0/25、T02批准ID0、全部Root T00–T11 0/12 Accepted；同源Chromium管理员阻断、真机/读屏/历史全量not-run，未取得同源高清/许可。[证据](./evidence/v036-round205-t01-t02-native-pixel-coverage.md)。

**R204验收边界：** 五类执行代码/审计字节篡改实际绕过R203，R204隔离守卫五类均拒绝；父2558/2558继承、旧268+新38=306/306，累计2569双独立SHA/QA恢复。未获高清原始字节/许可/逐笔/永久ID/生产集成；真同源/真机/读屏/历史全量not-run；T00–T11仍0/12 Accepted。[证据](./evidence/v036-round204-t01-t02-execution-and-audit-byte-anchor.md)。

**R203验收边界：** R202可被观察表与裁框表协同替换为另一真实JPEG ROI绕过，R203以八个冻结输入SHA及父成员清单失败关闭，旧240+新28=268/268、累计2558成员双独立恢复。此项不构成原图逐笔、来源许可、永久ID、生产集成或T01/T02正式验收；真同源/真机/读屏/完整历史not-run，T00–T11仍0/12 Accepted。[证据](./evidence/v036-round203-t01-t02-coordinated-ledger-provenance-gate.md)。
**R202正式验收边界：** 低清冻结JPEG 170观察与161裁框、161组成员关系互证及R201伪造坐标误接受修复；旧199+新41=240/240，累计2547成员双独立SHA/QA通过。**不代表**高分辨率逐笔来源、正式永久ID、缺根认证、生产集成、真同源、真机、真实读屏或历史全量验收。T01 0/25、正式ID0、T00–T11 0/12 Accepted。[证据](./evidence/v036-round202-t01-t02-native-crop-ledger-integrity.md)。

**R201 Root T01/T02验收边界：** R156/R157/R174/R196/R4来源证据被连接成只读、类型化审阅关系图，170观察、133审阅组件（28多观察），未将同裁框/矩形交叠/高清审阅包络当作字根身份或笔画认证；旧229+新71=300/300选定QA，R200递归1037套件超时不得计pass；双独立2535成员SHA与300 QA通过。正式来源0/25键、永久ID0、缺根未知、T00–T11仍0/12 Accepted；高清原始字节许可/逐笔、真同源、真机、读屏、历史全量not-run。[证据](./evidence/v036-round201-t01-t02-source-identity-conflict-components.md)。

**R200验收边界：** 真实Chromium `about:blank` 906组含描边保守inkBBox与解析式最大差0.000003706074；选定旧1001+新浏览器18+静态18=1037/1037，累计2520双独立恢复。仍非来源逐笔认证、永久ID、正式T03生产集成、同源Storage/真机/读屏/历史全量；原始T00–T11仍0/12 Accepted。[证据](./evidence/v036-round200-t03-real-stroke-inclusive-dom.md)。


**R199验收边界：** R198来源签发的三视图SVG在真实Chromium about:blank进行83/83几何检查，证明151草案实例的Path与矩阵局部性及stroke-inclusive/geometry-only差异，不证明原图逐笔来源、正式永久ID或生产集成。选定旧901+新83+静态17=1001/1001、累计2508双独立恢复；真实同源Storage/真机/读屏/历史全量not-run，正式T00–T11仍0/12 Accepted。[证据](./evidence/v036-round199-t03-real-chromium-svg-geometry.md)。


**R198验收边界：** R197 SHA绑定的151历史草案Path光学校正已在隔离R175三视图SVG组合器验证，Node mock DOM各视图25键/151实例/153 Path，M/V独立光学偏移且149其他实例不变；旧844+新57=901/901、累计2495双独立恢复。但没有正式永久ID、原图逐笔认证、生产集成、真实浏览器同源、真机、读屏或完整历史全量QA；不能判T03 Accepted，Root T00–T11仍0/12。[证据](./evidence/v036-round198-t03-source-bound-optical-three-view.md)。

**R197验收边界：** R125/R160真实冻结151旧Path解析式inkBBox上的T03光学校正候选（非生产集成），Node35/35、静态18/18、选定旧791/791，累计2482双独立恢复。正式T01 0/25、T02永久ID0、T03未集成、全部T00–T11 0/12 Accepted；真实同源/真机/读屏/历史全量not-run。[证据](./evidence/v036-round197-t03-source-bound-optical-preview.md)。


**R196验收边界：** Root T01/T02独立来源账本核对：170/170冻结JPEG原生RGB ROI、14/14审阅卡PNG和原生上下文、41/41既存高清审阅边的低清原生端点；36旧槽未匹配、12未绑定来源裁框、2共享裁框及6矩形交叠不构成缺根或笔画认证。R195父2457 SHA继承、R196累计2469双独立恢复，各选定旧739+新52=791/791。高清原始字节本轮未取得/读取，原图许可/逐笔/正式ID未批准，真实同源/真机/读屏/完整历史not-run；T00–T11仍0/12 Accepted。[证据](./evidence/v036-round196-t01-t02-exact-source-review-frontier.md)。

**R195验收边界：** 原始T04冻结25键156旧坐标槽全量v16来源隔离预演，真实R148/R152/R178/R179签发+R192候选核心在Node私有Map 46/46、静态22/22、选定旧671/671，共739/739；父2447 SHA继承、累计2457双独立恢复。**R195真实同源浏览器blocked/not-run**，R194真实Chromium30/30只覆盖G/K/X合成来源，不能外推全25键正式迁移。原始T00–T11仍0/12 Accepted，真机/读屏/历史全量not-run。[证据](./evidence/v036-round195-t04-full25-v16-source-rehearsal.md)。

**R194验收边界：** 真实授权Chromium双标签30/30执行完整R148/R152/R178/R179+R192候选链，但仅合成v16三键覆盖/隔离shadow，不是正式用户迁移；双独立2447文件SHA及671/671选定QA；原始T00–T11仍0/12 Accepted，真实读屏/真机/历史全量not-run。[证据](./evidence/v036-round194-t04-real-issuer-r192-chromium.md)。

**R193验收边界：** 真实Chromium 15/15仅为R192候选核心的合成签发幂等来源竞态；本地600/600选定QA、累计2417双独立恢复；正式T04迁移/真实签发链/读屏/真机/历史全量not-run，全部T00–T11仍0/12 Accepted。[证据](./evidence/v036-round193-t04-real-chromium-stale-idempotent.md)。

**R192验收边界：** R189旧核心幂等来源过期误报已复现，R192隔离候选修复；本地588/588选定QA、2402/2402双独立恢复；真实同源blocked、远端CI unverified、正式迁移/来源认证/真机/读屏/历史全量not-run；原始T00–T11仍0/12 Accepted。[证据](./evidence/v036-round192-t04-stale-idempotent-source.md)。


**R191验收边界：** Node私有Map写入异常29/29+静态18/18+选定旧474/474=521/521，父2379 SHA继承，累计2390双独立恢复；真实浏览器blocked、远端R190 unverified、正式迁移not-run，全部T00–T11 0/12 Accepted。[证据](./evidence/v036-round191-t04-storage-quota-fault-matrix.md)


**R190验收边界：** R189同一ESM真实同源浏览器竞态测试与GitHub Actions工作流已提交，远端结果unverified、本地ERR_BLOCKED_BY_ADMINISTRATOR blocked；474/474为选定旧456与新静态18，不含真实浏览器通过项。R189父2360/2360继承、累计2379双独立恢复；真实签发链浏览器/正式迁移/真机/读屏/完整历史not-run，T00–T11仍0/12 Accepted。[证据](./evidence/v036-round190-t04-real-browser-async-readback-infrastructure.md)。


**R189验收边界：** 新Node14+47+静态17+选定旧378=456/456，双独立2360 SHA恢复；真实同源blocked/not-run，T04及全部T00–T11未验收。[证据](./evidence/v036-round189-t04-async-source-digest-readback.md)。


**R188验收边界：** 实际来源签发与R187 typed-slot v3在Node私有Map 47/47、静态26/26及选定旧305/305通过，双独立2342 SHA与378 QA；R188真实同源联合验证本地blocked、远端not-run，正式T04未验收，T00–T11仍0/12。[证据](./evidence/v036-round188-t04-actual-issuer-typed-slot-bridge.md)。


**R187验收边界：** R186 null/empty影子冲突已由R187 typed-slot v3修复，Node18/18+静态17/17+选定旧270/270、双独立2325 SHA恢复；远端真实Chromium同一ESM 17/17但合成签发fixture，真实R148签发与正式迁移未验证。历史全量/真机/读屏not-run；T00–T11仍0/12 Accepted。[证据](./evidence/v036-round187-t04-typed-storage-slot-recovery.md)。

**R186验收边界：** v2日志before/next SHA与非协作shadow冲突检测通过Node新81/81+静态20/20及选定旧169/169，双独立2310 SHA恢复；真实浏览器管理员阻断、远端CI未运行，正式迁移/生产集成未完成。全部T00–T11仍0/12 Accepted。[证据](./evidence/v036-round186-t04-noncooperative-shadow-conflict.md)。

**R185验收边界：** 实际R148/R152/R178/R179签发模块+R183事务核心在Node私有Map 40/40，通过隔离原点、来源过期、真实故障分支和回滚；本地Chromium管理员阻断、远端CI未运行，**不能视为真实同源通过或正式V0.35迁移**。T00–T11仍0/12 Accepted。[证据](./evidence/v036-round185-t04-actual-source-issued-disposable-bridge.md)。

**R184 Root T04验收边界：** 同一ESM真实Chromium故障分支修复后25/25，artifact SHA独立复核；只证明隔离fixture的rollback和跨文档恢复，不证明正式V0.35迁移、永久ID或生产集成。T00–T11仍0/12 Accepted。[证据](./evidence/v036-round184-t04-real-browser-fault-branch-fix.md)。

**R183 T04验收边界：** 同一隔离ESM事务核心已通过Node私有Map44/44、实际R148/R152/R178签发桥接17/17及选定旧109/109；本地真实浏览器管理员阻断，远端新工作流尚未核实。即使远端真实浏览器成功，也仅证明临时profile的隔离事务，不是正式迁移或T04 Accepted。完整历史、真机、读屏not-run；T00–T11仍0/12。[证据](./evidence/v036-round183-t04-shared-disposable-transaction-core.md)。

**R182 T04验收边界：** 远端真实同源浏览器原语R181 16/16与隔离事务fixture R182 24/24经GitHub Actions成功及原始artifact SHA复验；仅证明独立临时profile的存储/锁/回滚/模拟崩溃恢复行为，**不证明R180代码直接浏览器运行或正式迁移**。本地localhost管理员阻断、真机/真实读屏/完整历史全量QA not-run；原始T00–T11仍0/12 Accepted。[证据](./evidence/v036-round182-t04-real-same-origin-disposable-quarantine.md)。


**R181验收边界（原始T04）：** 临时loopback新浏览器context的16项真实浏览器检查已编码，但本地Chromium导航被管理员阻断，实际0项浏览器通过；远端GitHub Actions CI待核实。静态合同12/12与选定旧1181/1181、双独立2234 SHA仅验证代码/档案稳定性，不构成真同源或正式迁移验收。T00–T11仍0/12 Accepted。[证据](./evidence/v036-round181-t04-real-same-origin-browser-infrastructure.md)。

**R180验收边界（Root T04）：** Node私有Map模拟v16隔离影子事务、失败回滚与重启恢复，48项新增及1133项选定旧QA通过；不是真实同源Web Locks/localStorage、持久化恢复、正式ID或生产迁移。原始T00–T11保持0/12 Accepted。[证据](./evidence/v036-round180-t04-disposable-quarantine-rollback.md)。

**R179 Root T04（浏览器realm真实原点绑定，隔离只读非验收）：** Node VM复现R178接受调用方伪造loopback原点/存储并给出正面来源见证；新增R179浏览器realm绑定入口，在读取localStorage前拒绝非127.0.0.1安全原点，只从当前realm取得单键只读存储/Web Locks/WebCrypto。新35/35+真实Chromium about:blank拒绝1/1+实跑R178选定旧1097/1097=1133/1133；R178父2201/2201 SHA继承，R179累计2213文件SHA `87fddbac1512ab8f4b87f4f6fd59291ef88ad5a7c1aac13feaaebb5100be350f`，Python/unzip双独立恢复各2213/2213 SHA、1133/1133 QA，QA后SHA一致。真实loopback仍ERR_BLOCKED_BY_ADMINISTRATOR=blocked/not-run，历史全量/真机/读屏/正式迁移not-run；T00–T11仍0/12 Accepted，T01 0/25、正式ID0、缺根未知，R11/R12/R35与20SVG仍缺，冻结入口/用户存储未动。[R179证据](./evidence/v036-round179-t04-browser-realm-origin-binding.md)。


**R178验收边界：** 只读v16来源过期门禁通过Node22 22项及1075项选定旧QA，真实loopback Chromium管理员阻断；不代表真实用户迁移、正式ID、生产集成或T04 Accepted。全部仍0/12。[证据](./evidence/v036-round178-t04-legacy-source-freshness-gate.md)。


**R177验收边界：** 256/384px实际Canvas alpha交集检查409对/分辨率均无重叠，只证明R176未认证草案在当前条件下无墨迹交集；T06→T07依赖未满足，T03未生产集成，正式T00–T11仍0/12 Accepted。递归旧QA超时不计pass。[证据](./evidence/v036-round177-t03-real-ink-alpha-collision-preflight.md)。

**R176验收边界（Root T03，T07仅预检）：** 独立键帽宿主50组Chromium DOM检查700/700、来源13/13与选定旧2107/2107通过，证明标签带与SVG组几何矩形在隔离页面不交叠；不证明逐像素墨迹/stroke无碰撞，不满足T06→T07正式依赖，亦不证明生产集成、file://、真同源、真机或读屏。T00–T11保持0/12 Accepted。[证据](./evidence/v036-round176-t03-keycap-host-real-dom-preflight.md)。


> R175隔离T03补充证据：25键单SVG/151组/153 Path在Node19/19、Chromium about:blank DPR1/2/3×三视图99/99通过，选定继承1989/1989；**仍非正式T03 Accepted**。源图逐笔、正式ID、生产集成、真同源、真机/读屏及历史全量QA均未满足。见[证据](./evidence/v036-round175-t03-key-local-source-issued-compositor.md)。


**R174审阅工具不构成验收：** 41对/16键来源双框工作台允许在隔离环境记录笔画疑点，不提供批准接口；冻结低清ROI 82次SHA重算和1989项选定QA通过仅证明证据工具/继承稳定性。正式逐笔来源、第三方许可、25键认证、T02永久ID、T05补图、真实同源迁移、真机/读屏均未验收；T00–T11保持0/12 Accepted。[证据](./evidence/v036-round174-t01-t02-frozen-native-41-pair-review-workbench.md)。


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
