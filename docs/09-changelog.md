# 09 · 历史演化与变更记录

## 第133轮 · Root T03 跨SVG挂载命名空间修复（隔离、非验收）

- R133 Root T03发现并复现R132隔离SVG跨实例默认ID冲突：两个不同符号同挂DOM，原始BBox宽10/80被错误绘制为10/10；新增每次调用唯一命名空间与内部ID/ARIA IDREF安全重映射，修复后10/80。冻结V0.35主键盘25个有根键位、151旧可视字根同时挂载，151/151本地symbol ID唯一、151/151原生BBox一致，5个对抗用例通过。新增12/12+继承定向153/153，两套独立Python/unzip恢复各165/165、1742/1742文件SHA一致；父R132 1734/1734 SHA继承，R133 ZIP SHA `bd866c1e436d8f3d9412fc4e3e47f2543c17f3f8bc806c07a307da8d0a64bbc4`。完整历史QA not-run，T00–T11仍0/12 Accepted、T01正式0/25、正式ID0、T03未生产集成、T05未完成；R10–12/R35 ZIP与R12的20SVG仍缺，许可、真实同源迁移、真机读屏未验收；冻结入口/176编码/用户存储未动。 [证据](./evidence/v036-round133-t03-cross-svg-mount-namespace-collision.md)。


## 第132轮 · Root T03 SVG symbol递归依赖闭包（关联T04，隔离、非验收）

- 本轮新增隔离SVG引用解析器：递归闭包、唯一局部ID、菱形共享依赖、循环/缺失/重复ID/外链及危险节点失败关闭；开发中修复分支汇合局部ID冲突。冻结V0.35真实Chromium `about:blank` 仅计主键盘26物理键（Z旧可视0），其他25键**151/151**自包含引用闭包且**151/151**原生getBBox四分量相同；15个对抗用例，新增21/21，继承R131/R130/R125/R123定向132/132，每套153/153。父R131 **1722/1722**逐文件SHA继承，R132累计**1734文件** ZIP SHA `670c139b1017a793ae6e84155874a633cbd94a602b24dd25f4eb00a1b28d184c`，Python/unzip双独立解压及QA后各1734/1734 SHA一致、各153/153。T04临时独立profile访问127.0.0.1仍被`ERR_BLOCKED_BY_ADMINISTRATOR`阻断，不计通过。完整历史QA not-run；**T00–T11仍0/12 Accepted**，T01 0/25、正式ID0、T03未生产集成、T05未完成，缺历史R10–12/R35及20 SVG、高清许可、真实同源迁移、真机读屏；冻结入口/176编码/用户存储未动。[证据](./evidence/v036-round132-t03-symbol-dependency-closure.md)。


## 第131轮 · SVG本地symbol绑定与稳定性复核（隔离）

- 第131轮 Root T03（关联T07）隔离修复浏览器诊断的跨SVG `<use>`→`<symbol>`悬空依赖：新增本地`<defs>`克隆与唯一href绑定，独立Chromium 2 contexts×11对×2尺寸×4模式=176次渲染，396/396历史字段一致；两套恢复分别复测新守卫50/50与精选旧QA282/282，最终ZIP 1722/1722双解压SHA一致、最终各104/104 QA。父R130 1712/1712 SHA继承；第131轮ZIP SHA `f67fed7b5d62d01cf1d50336c66451aefcdfa46c429bcbeec6cbdfc3ce077549`。R129完整953与候选恢复R130完整505曾尝试但超时，**不计pass**。不能证明渲染波动唯一根因或跨设备稳定；T03未集成，T00–T11 0/12 Accepted，T01 0/25、正式ID0、T05未完成；历史R10–12/R35 ZIP和20SVG缺失，真实同源迁移/真机/读屏/许可仍未解，冻结入口及用户存储未动。[证据](./evidence/v036-round131-t03-self-contained-symbol-replay.md)。


## 第130轮 · J:4复合来源阻断与浏览器回放不稳定性记录（隔离）

- 第130轮 Root T01/T02/T03：2008 JPEG J:4原生裁框[1005,397,24,32]是包含圈和双竖笔的复合来源区域；R81 J:4来源账本仍为`blocked_invalidated`及`round69Unbound=true`。冻结V0.35源码明确H/J/K区位竖笔是说明性徽记，独立Chromium验证H/J/K分别为1/2/3笔且每键有1圈；R129 J:4/marker1的648/648墨迹重叠不能当作新增独立字根、碰撞已批准或源图认证。新增30/30来源语义QA，精选继承475/475 QA；Python/unzip两套独立恢复最终各505/505，候选1710/1710文件SHA一致，最终1712/1712文件双恢复SHA及新增30/30通过。R129完整953项定向QA未重跑、历史全量QA not-run；Chromium首次重放出现L:1和J:4短暂像素差异，失败已记录，重试才通过。R129父1698/1698继承，R130累计1712文件ZIP SHA `e7d0d0fda95ca938cba1e49359ce3507356e6c65a9cb25d383c0a3cede7c0bb3`。正式T01 0/25、正式永久ID0、T03未生产集成、T05未完成、T00–T11仍0/12 Accepted；历史缺包/20SVG、高清许可、真实同源迁移、真机读屏仍未解，冻结入口及用户存储未动。 [证据](./evidence/v036-round130-t01-j4-zone-badge-source-role-conflict.md)。


## 第129轮 · Root T03区位徽记绘制顺序与J:4根墨迹全包含（隔离，非验收）

- 冻结V0.35真实Chromium DOM 9组BBox候选+2阴性对照，400/800px分别渲染字根、徽记、原始及反向绘制顺序：5组真实像素交叠且绘制顺序敏感，4组所测分辨率无交叠；**J:4/marker1在800px下648/648字根墨迹像素落入区位徽记墨迹区域，反向顺序648像素变化**。此为必须复核的视觉归属风险，不是错误字根或已认证根；新增失败关闭碰撞复核门禁，不自动白名单。父R128 1679/1679 SHA继承，R129累计**1698文件** ZIP SHA `a7facaeaa26667d36dd0584d443b2e8b63abfbed8f24ec0c4a5c1a591286e732`，Python/unzip双独立恢复各新61+旧892=**953/953定向QA**、QA后1698/1698 SHA一致；完整历史全量QA not-run。T01 0/25、正式ID0、T03未集成、T05未完成、T00–T11 **0/12 Accepted**；历史缺包、许可、真同源迁移、真机读屏仍未解决；冻结入口/176编码/正式SVG/用户存储未动。[证据](./evidence/v036-round129-t03-zone-badge-paint-order-and-root-containment.md)。

## 第128轮 · Root T03 SVG真实涂色像素遮罩（隔离）

- 将第127轮9组标注BBox交叠候选改用真实冻结DOM原生字根/标注独立绘制遮罩复核，400/800px、两阈值：5组存在像素交集、4组为BBox假阳性；2组阴性对照为0。新增73/73+继承819/819，父R127 1663/1663逐项SHA继承；R128累计1679文件，ZIP SHA `0606855e57ec7e83c8240cc25148802d1aef654833e36933eab6a98605e940b0`，双独立恢复各892/892、QA后1679/1679 SHA一致。仅隔离证据，T00–T11 0/12 Accepted，生产入口/176编码/用户存储未动。[证据](./evidence/v036-round128-t03-frozen-dom-paint-mask-intersection.md)。

## 第127轮 · Root T03真实SVG标注包络与候选交叠（隔离）

- 第127轮 Root T03隔离新增冻结V0.35真实SVG圈注/区位徽记包络：Chromium about:blank从原页面DOM实测25键39个标注（7根圈/补码框、32区位徽记），对R125解析式墨迹240对及R126文字标签78对比较；6键H/J/L/N/Q/Y存在9组**保守BBox交叠候选**（非真实涂色碰撞），7组预期根圈叠加单列，标签交叠0/78，越界0/39。新Chromium39/39+Node30/30+继承750/750，两套Python/unzip独立恢复各819/819、1663/1663后验SHA一致；R126父1652/1652继承，R127 ZIP SHA `f2692f705f93b26b3e722c86b61725dcc22b506d2c1eda95b29f32347eb6eb6e`。**仍非正式验收**：T01 0/25、正式ID0、T03未集成、T05未完成、原始T00–T11 0/12 Accepted；历史R10–12/R35和20SVG缺失、许可/真机/读屏/正式迁移/全量历史QA未完成，冻结入口及用户存储未动。 [证据](./evidence/v036-round127-t03-frozen-svg-annotation-paint-envelopes.md)。


## 第126轮 · Root T03标签独立保留区实测（隔离）

- **第126轮 Root T03隔离新增字母/区号保留区实测**：从SHA冻结V0.35源码取25键区号与P/Q特殊字母坐标，在独立Chromium about:blank实测50个SVG文字BBox，与151旧实例解析式墨迹进行302对几何比较；直接交叠0/302，但R:5距字母仅0.782472/100，按1/100安全间距有1/302预警。新浏览器50/50+Node19/19+继承681/681，两套各750/750；R125父1641/1641 SHA继承，R126累计ZIP1652文件SHA `d8707b50a0249052fb74d208d2f6b135e3be6c7727255862badba7c20661e3d2`，Python/unzip两套各1652/1652 SHA一致。**仍仅隔离**：T01 0/25、正式ID0、T03未集成、T05未完成、T00–T11 0/12 Accepted；历史缺包、许可、真同源/真机/读屏/完整历史QA未解；冻结入口/176编码/用户存储未动。[证据](./evidence/v036-round126-t03-chromium-label-reservation-clearance.md)。


## 第125轮 · Root T03解析式矢量边界门禁（隔离，非正式验收）

- **第125轮 Root T03隔离实质修复**：将R54解析式矢量墨迹BBox（151旧形态/153真实Path）SHA绑定R50 Path与R53几何，再接入R48/R124光学校正越界判定；151中145条与R50近似BBox存在非零差异（最大0.4841016564源单位、0.105布局单位）。新Node24/24+独立Python157/157+继承500/500，每套681/681；R124父1629/1629继承、R125 ZIP1641文件SHA `b64d144b0c4f79ce113330e4399db4a2fae3916e277e595e402d9a45893955cb`，Python/unzip两套各1641/1641后验SHA一致。**仍仅隔离实现**：正式T03未集成、T01 0/25、正式ID0、T05未完成、原始T00–T11 0/12 Accepted；历史R10–12/R35及20SVG缺失，真同源/真机/读屏/历史全量QA未运行。冻结入口/176编码/用户存储未动。[证据](./evidence/v036-round125-t03-sha-bound-analytic-vector-optical-guard.md)。


## 第124轮 · Root T03 光学校正后墨迹越界守卫（隔离实现，非正式验收）

- 发现R48 SVG坐标解析器只限制目标geometry，未限制光学校正ox/oy之后的真实inkBBox；冻结151条Path草案逐项注入ox=200均可在旧解析器中越出100×100。新增隔离守卫拒绝越界、验证锚点重构、保留未认证来源标记；**151/151**原始几何与旧矩阵一致、**151/151**恶意偏移拒绝、**151/151**小偏移往返。新增22/22 + 继承478/478，两套Python/unzip独立恢复各500/500 QA与1629/1629 SHA一致；父R123 1620/1620继承，新ZIP SHA256 `1b2ece4a2a2486aaf078b0fc27136c7a02f3c24b30a959832a03c9deb509aec9`。
- 本轮未生产集成；R50 Canvas inkBBox并非精确矢量边界，不能宣称T03 Accepted。T01 0/25、正式ID0、T05未完成、T00–T11 **0/12 Accepted**；历史R10–12/R35与20SVG缺失，真实同源仍被管理员策略阻断，真机/读屏/正式迁移未运行。冻结HTML/176编码/正式SVG/用户存储未动。[证据](./evidence/v036-round124-t03-optical-envelope-guard.md)。


## 2026-10-26 · 第123轮 Root T01/T02 M邻根连接瓶颈复核（非认证）

- 冻结2008 JPEG/R81清单SHA绑定；M03/04五阈值4/8邻接最小割均0；M05/06仅阈值176连通（4邻接割4、8邻接割8）；M07/08在144/160/176的4邻接割1/1/2、8邻接割2/2/3，8邻接割像素位于原图x=1039、y=658–660。新28/28+旧450/450，两套Python/unzip恢复各478/478 QA及1620/1620后验SHA；R122父1610/1610继承，R123 ZIP SHA256 `20d5aa05ff4b26e0b5d7e46b4d2818df73b66983f184bebeb646db3f8be86812`。只是阈值脆弱桥接，不是逐笔归属或字根拆分证据。T01 0/25、正式永久ID0、T05未完成、T00–T11 0/12 Accepted；缺历史第10–12/35轮与20SVG，高清许可/真机/读屏/正式迁移未解，冻结入口/176编码/用户存储未动。 [证据](./evidence/v036-round123-t01-m-pair-min-cut-bottleneck.md)。


## 2026-10-26 · 第122轮 Root T01/T02 M04/M08阈值隔离与邻根拓扑（非认证）

- 冻结2008 JPEG/R81来源SHA绑定：M04原框[1017,623,14,13]在阈值96分裂、128–176可隔离且左伸2原生像素；M08原框[1040,653,12,15]在96分裂、128可隔离且底伸2像素，144–176因邻近墨迹连通触及隔离ROI边界而阻断。低清M07/08共享连通分量3/5档、M05/06仅1/5档、M03/04为0/5；R117高清5/5与本轮低清3/5是不同分辨率测量。**无笔画归属、裁框、身份或正式SVG认证。**
- R121父ZIP SHA `c3be0c550f467c94aaf38e38a0f855752eca44e0d6b9dac0ad29931270df4711`，1595/1595逐文件继承；R122累计**1610文件** SHA256 `e1b878d2c23ea2db07db1c27959911d9208a6e505ad5dad842af762f31f210bc`。新增30/30、继承420/420，两套Python/unzip恢复各450/450定向QA，QA后各1610/1610 SHA一致；完整历史QA not-run。
- T01正式0/25、T02正式永久ID0、T05未完成、原始T00–T11 **0/12 Accepted**。第10–12/35轮与20SVG仍缺；高清许可、真实迁移、真机/读屏未解；冻结入口/176编码/正式SVG/用户存储未动。[证据](./evidence/v036-round122-t01-m04-m08-source-topology.md)。

## 2026-10-25 · 第121轮 Root T01/T02 M-vis-02墨迹包络来源诊断（非认证）

冻结2008 JPEG与R81清单SHA绑定，M-vis-02旧裁框右侧截断连通墨迹4–5原生像素，生成未批准包络[1053,587,18,21]与只读叠框图。父R120 1582/1582 SHA继承，R121累计1595文件SHA256 `c3be0c550f467c94aaf38e38a0f855752eca44e0d6b9dac0ad29931270df4711`，Python/unzip双独立恢复各420/420定向QA与QA后1595/1595 SHA一致。原图逐笔/许可/正式永久ID/补图/迁移/真机/读屏均未验收，T00–T11 0/12 Accepted。[证据](./evidence/v036-round121-t01-m02-component-envelope.md)。

## 2026-10-25 · 第120轮 Root T01/T02 全25键原生边界来源普查（非认证）

- 第120轮读取冻结2008 JPEG及R81来源清单，**151/151旧可视+8/8 M暂存**逐框原生RGB SHA核验，25键旧来源均有记录；五阈值四侧边界审计标记**81/151**旧框为墨迹延续待复核（不是确认错误/缺根），M-vis-02右侧、M-vis-04左侧、M-vis-08底侧优先；K/E/B/V身份阻断未解。新46/46、继承354/354；父R119 1572/1572继承，新累计**1582文件** ZIP SHA256 `81fd92d03b6b5f92dd827a10ea2bf5a12116e6ea0c91524475d088aa0cbffd84`；Python/unzip两套各400/400定向QA、QA后各1582/1582 SHA一致。完整历史全量QA not-run；T01 **0/25**、正式ID **0**、T00–T11 **0/12 Accepted**。历史10–12/35与20SVG仍缺，许可/真机/读屏/正式迁移未解；冻结入口和用户存储未动。[证据](./evidence/v036-round120-t01-all-key-native-crop-edge-census.md)。

## 2026-10-25 · 第119轮 Root T01/T02真实高低清跨来源配准（非认证）

首次在独立GitHub Actions实际取得固定SHA的3508×2480高清JPEG，并与冻结2008 JPEG的133个非图像ORB特征进行跨来源RANSAC配准：101比值匹配、99内点、22空间格，中位0.0636低清像素；五组M/K/E风险框对比纯尺寸比例最大角点差0.126高清像素。父R118 1560/1560继承，R119累计1572文件SHA256 `d2a160a86764c2b903241d3b9efdb49b756544411f13d55a03a0f46f21efa898`，双独立解压/QA后1572/1572一致，各354/354定向QA。许可/逐笔/永久ID/历史缺包/真机/读屏/迁移未完成，原始0/12 Accepted。[证据](./evidence/v036-round119-t01-real-cross-source-orb-registration.md)。

## 2026-10-25 · 第118轮 Root T01/T02来源仿射配准前置（非认证）

冻结2008 JPEG真实SHA核验、SIFT+RANSAC仿射配准器与25键来源区域残差诊断在外部隔离ZIP中实现；**仅合成仿射7/7**，904内点/中位误差0.1171为合成指标，外部高清真实跨图配准not-run。父R117 1551/1551继承，R118 1560文件SHA256 `287e93524cd698319bb502d5517c4c806f84c04f5fbc440185f7a6a89bbee993`，双恢复各347项定向QA、QA后SHA均一致。许可、历史缺包、正式身份、真机/读屏/迁移仍阻断，T00–T11 0/12 Accepted。[证据](./evidence/v036-round118-t01-affine-registration-preflight.md)。

## 2026-10-25 · 第117轮 Root T01/T02 M来源严格边界（非认证）

新增直接跨旧裁框边界暗像素对与严格纵向交集连通性核验，排除第116轮外围上下文绕行的解释歧义。真实高清CI 40187583179 success：M-vis-02直接跨界30/34/34/37/37，严格扩框连通166/177/180/186/190；M03/04全档不连、M05/06阈值敏感、M07/08全档连通。父R116 1540/1540 SHA继承，R117累计1551文件ZIP SHA256 `a7aa36bcf6e994da9a93430881202649310bb48ebf5b5e8714bc357c7f1b0cca`，双独立恢复与QA后1551/1551，各340项定向QA通过。无正式裁框、SVG、永久ID或来源认证；历史缺口、版权/配准、真机/读屏/迁移阻断不变，原始0/12 Accepted。[证据](./evidence/v036-round117-t01-m-strict-seam-topology.md)。


## 2026-10-25 · 第116轮（Root T01/T02，关联T05；非认证）

GitHub Actions 40183270210实际读取固定SHA高清JPEG并开展五阈值8邻接墨迹连通性核验：M-vis-02旧框右扩像素均与旧框相连，M07/08持续跨框连通，M05/06阈值敏感；未批准任何形态或裁框。新增20/20+继承311/311，父R115 1529/1529逐文件继承，R116累计1540文件ZIP SHA256 `a2823ee6844c6fb86b3802a2b1053c6c3abff9345b1f9b7d304da5e1071eff08`，双独立恢复及QA后SHA一致。版权、精确配准、逐笔认证、永久ID、真机/读屏/正式迁移仍未完成，0/12 Accepted。[证据](./evidence/v036-round116-t01-m-highres-ink-connectivity.md)。

## 2026-10-25 · 第115轮（Root T01/T02，关联T05；非验收）

独立GitHub Actions 40178902354对已核验SHA的3508×2480高清JPEG实际读取21个M/K/E来源ROI，记录不可逆RGB SHA及暗像素；M-vis-02右侧未批准扩框存在186个灰度<160像素，K:2/K:3与E:1/E:8共框仍阻断。修复R114通用ZIP导入函数对伪造元数据配合`../`路径的合成绕过；新15+旧296项定向QA通过，R114父1519/1519继承，R115累计1529文件ZIP SHA256 `8f77cc07500544e1f28a6b29c7aea2aa078051f63bb17b9f0fef6b4c8d5927d8`，双独立恢复各311/311及后验SHA一致。版权/逐笔/永久ID未认证，0/12 Accepted。[证据](./evidence/v036-round115-t01-highres-roi-pixel-triage.md)。

## 2026-10-25 · 第114轮（Root T01/T02；非正式验收）

R114从06wb社区镜像发现标称官方的3508×2480高清简体字根图ZIP；GitHub Actions 40175565336实际下载、解压并核验原始ZIP/JPEG SHA256。与冻结1536×1086参考图整图+四象限dHash仅4/320位差异，属于高度相似排版候选，**不是逐笔/同源原始字节/版权认证**。新31/31、继承R113 34+R112 36+R96 35+R95 36+R84 124，两套Python/unzip独立恢复各296/296；R113父1509/1509逐文件继承，R114累计1519文件，ZIP SHA256 `a24303d1e53c4643f7c8a7bbf3c68925c1225a4f76b4918dc1ba6f0aeb5af50c`。原始T00–T11 0/12 Accepted、T01 0/25、正式永久ID0，历史10–12/35轮与20SVG仍缺，未获合法再分发许可，高分辨率原图不入仓/ZIP。 [证据](./evidence/v036-round114-t01-highres-source-candidate.md)。

## 2026-10-25 · 第113轮（Root T02/T04；非正式验收）

修复R111隔离旧槽影子UID映射未核对来源账本、默认坐标信任调用者的两处真实风险；Q:0/K:2 UID错绑与Q:0编辑丢失在旧函数复现，新SHA绑定门禁均拒绝。新增34/34，继承R111/R112/R84/R95/R69/R96共310项，两套独立恢复各344/344。R112父1498/1498继承，R113累计1509文件SHA256 `acdd2f820af7e7b2dc45b371edb9856a1e02d9dd26acff56f93ab0ece43dc8e2`，Python/unzip双恢复及QA后SHA一致。首次QA改写历史pyc后验SHA失败，重新从ZIP恢复并禁写pyc后通过；正式身份/迁移/真机/读屏仍未验收，原始0/12 Accepted。[证据](./evidence/v036-round113-t02-source-bound-uid-shadow.md)。

## 2026-10-25 · 第112轮（Root T01/T02，关联T05；非正式验收）

新增键位局部坐标→2008 JPEG原生坐标的25键显式来源门禁，修正R46/R81直接比框会误报151条冲突的坐标系差异；151旧可视、36旧未匹配、M8、七微形7、K物理4逐项对齐。新36+旧274=310项定向QA在Python/unzip双独立恢复通过；父1488/1488继承，新累计1498文件SHA256 `3ff5b88ee12fc2cc849bee8c01955feac90f3cefee38e75e1c763903a435fb7f`，QA后SHA一致。只是来源账本一致性，不是原图逐笔认证，T01 0/25、正式永久ID0、T00–T11 0/12 Accepted。[证据](./evidence/v036-round112-t01-t02-native-coordinate-frame-identity.md)。

## 2026-10-25 · 第111轮（Root T04/T02，非正式验收）

修正R110只接受完整25键快照而可能拒绝合法局部v16用户调位的问题；隔离只读门禁保留来源键存在位图，仅映射实际编辑，不自动补齐来源或正式ID。冻结V0.35真实Chromium about:blank内存存储新增60/60 QA，旧30+16+10+179+170定向QA通过。父1477/1477 SHA继承，新ZIP1488文件SHA256 `163fc6c599817b2d28e2fd8d6ac64b457630b55b5ac045196f7676151f16f924`，Python/unzip双独立恢复及QA后1488/1488一致。真实用户迁移/真机/读屏not-run，0/12 Accepted。[证据](./evidence/v036-round111-t04-partial-v16-readonly-preservation.md)。

## 2026-10-25 · 第110轮（Root T04/T02，非正式验收）

在真实Chromium about:blank中执行冻结V0.35 HTML及内存存储合成快照，发现并复现旧页局部v16 JSON被接受、损坏v16阻断有效v15回退的兼容风险；新增25键/156槽严格只读准入、3处合成调位→候选UID影子映射（M:4关联隔离）。新30/30与旧16+10+179+170项定向QA在双独立恢复均通过。R109父1468/1468 SHA继承，R110 ZIP1477文件，SHA256 `8b83bd4abf3807bcf862e748bf1b0928bd759d88d66a24e2d90e94b12186d561`；QA后两套1477/1477一致。非真实同源迁移，冻结入口/用户存储不变，T00–T11仍0/12 Accepted。[证据](./evidence/v036-round110-t04-v035-browser-storage-shadow.md)。

## 2026-10-25 · 第109轮（Root T04，非正式验收）

独立核验R108 GitHub Actions真实临时原点11/11，R109扩展Web Locks/localStorage的pending/record/head三阶段崩溃恢复并在Ubuntu Chromium双标签真实原点23/23通过（run 40156644345）。R108父1459/1459继承，R109 ZIP1468文件双独立恢复，恢复后新16+旧385项定向QA各通过；R108 ZIP内1458成员中间QA记录与外部最终1459记录的差异单列审计。**不是旧用户V0.35迁移或正式T04验收**，T00–T11仍0/12；冻结入口、原图、176编码及用户存储未动。[证据](./evidence/v036-round109-t04-real-origin-crash-recovery.md)。

## 2026-10-25 · 第108轮（Root T04，非正式验收）

R107隔离存储rollback在验证前驱前修改head，前驱损坏时会污染最后可读修订。R108先核验前驱SHA/schema再更新head，Node VM旧缺陷复现与修复10/10；继承R107静态26/26、R77 Node179/179、R105 Chromium170/170。父1449/1449 SHA继承，新累计ZIP1459文件，双独立解压及定向QA后1459/1459一致；真实同源依然管理员阻断、远端CI待核验。冻结入口未动，T00–T11 0/12 Accepted。见[证据](./evidence/v036-round108-t04-rollback-atomicity.md)。

## 2026-10-25 · 第107轮（Root T04，非正式验收）

新增隔离临时原点双标签Web Locks/localStorage QA脚本与GitHub Actions烟测；本地原点被管理员策略阻断，远端CI尚未确认。静态26/26、旧179/179与170/170，R106完整回归本轮超时未计通过。R106父1439/1439继承，R107累计1449文件双独立恢复。冻结生产入口不动，原始T00–T11 0/12 Accepted。见[证据](./evidence/v036-round107-t04-disposable-origin-preflight.md)。

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


## 2026-10-25 · V0.36 第99轮（隔离证据，未发布）

- Root T03/T07：新增Chromium独立SVG Path→Canvas alpha像素读取，对151候选UID在4×/8×两档栅格化核对草案inkBBox（302/302），H:7 stroke与3个主动篡改负例通过；不作来源认证。
- 父R98 1359/1359继承；R99累计ZIP1366文件 SHA256 `7fe43e62975b1e1b339f46674d452c519a3ad6b6d130e448e8c2f670d12f4fea`；双恢复/新旧定向QA通过。正式0/12 Accepted，冻结入口未动。

## 2026-10-25 · 第100轮 T00/T01/T05 归档链与M来源复验（非验收）

- 独立核验第90–99轮10份实际ZIP的SHA、成员和9次相邻继承；M键8个原生JPEG来源ROI与8个PNG字节及RGB复算一致，4个无旧槽仍不认证。
- R99父1366/1366继承，R100累计1373文件ZIP SHA256 `f90595913cb0469809897a0dab9c20a84628fff2b61e032d2506b5e691cc559c`；Python/unzip双恢复各执行R100、R99新增2组及R98继承14组定向QA通过，QA后成员SHA1373/1373。完整历史QA未执行。
- 历史缺口未补、同源真实事务blocked、真机/读屏not-run；T00–T11 0/12 Accepted。见[证据](./evidence/v036-round100-archive-chain-m-provenance.md)。

## 2026-10-25 · 第101轮 T01/T02/T05 M键原生像素归属（非验收）

- 8个M原生ROI、6px上下文SHA及R84旧/影子UID交叉绑定；6个未批准复框定位3组来源交叠，全部保持blocked审阅，不产生正式根/Path/ID。新增58/58，继承124/124、20/20、R99 Chromium302/302。
- R100父1373/1373 SHA继承，R101 ZIP1385文件 SHA256 `e40cae7e5932df6c2784bd977d1c511a5d7a4609e7002b509f10b72ef3795cd2`，Python/unzip双恢复及新旧QA通过；当前R90 ZIP缺失，R100十包外部链本轮复跑blocked。原始任务0/12 Accepted，正式入口与用户存储未动。[证据](./evidence/v036-round101-m-native-source-ownership.md)。

## 2026-10-25 · 第102轮 T01/T02/T05 M键原生交叠拓扑（非验收）

- 三组未批准扩框交叠经原生JPEG五阈值审计：M03/04 26像素交叠无暗像素；M05/06 72像素交叠有暗像素候选；M07/08 34像素交叠暗连通性对阈值敏感。均未认证字根/笔画归属/永久ID。
- 新增52/52及继承5组定向QA通过；父R101 1385/1385继承，R102累计1397文件SHA256 `1e5972251f3386e91d709e1869a36009f8aead732eaa4e22bfb93d9f21b094a5`，Python/unzip双恢复各1397/1397 SHA一致，QA后再次全一致。R90缺失阻断十包链复跑；T00–T11仍0/12 Accepted。见[证据](./evidence/v036-round102-m-native-overlap-topology.md)。

## 2026-10-25 · 第103轮 Root T03 祖先绘制完整性（非验收）

- 真实Chromium证明R94 SVG自身computed style门禁忽略父级opacity/filter/clip-path/mask/transform，导致实际墨迹可消失/位移而attest误通过。R103隔离HTML新增父节点绘制与结构基线校验；九种攻击负例全部由R94错误放行、R103拒绝，新26/26。
- 父R102 1397/1397逐成员SHA继承，R103累计1410成员ZIP SHA256 `bdd1f42c847c01bc98b278294b7a6074550e293c9e4b977f601dc4fe75ef8874`；Python/unzip双恢复及各8组定向QA（612项）通过，QA后各1410/1410 SHA一致。合并式双恢复运行第二阶段超时，改分项执行并留痕；完整历史全量QA未执行。
- 正式T03仍未生产集成，来源/永久ID/真同源存储/真机/读屏未验收，T00–T11 0/12 Accepted。冻结V0.35 HTML、2008原图、176编码、正式SVG和用户存储未动。[证据](./evidence/v036-round103-t03-ancestor-paint-integrity.md)。

## 2026-10-25 · 第104轮 Root T03 伪元素遮挡隔离修复（非验收）

- 真实Chromium五类CSS伪元素遮挡让R103祖先样式门禁误放行；R104增加`::before`/`::after`绘制签名，五类均拒绝，新增25/25 QA。
- 父R103 1410/1410 SHA继承，R104累计1425文件SHA256 `3840ac7eaeea34c66d3c251dd8906117d92de2f5536b34256d26b6afad275289`；9组637项定向QA通过，Python/unzip四次分段独立恢复及QA后SHA各1425/1425一致；完整历史QA not-run。
- 独立profile同源导航仍被管理员阻断，Web Locks/localStorage blocked/not-run，真机/读屏not-run。T00–T11 0/12 Accepted；冻结HTML、2008 JPEG、176编码和用户存储未动。[证据](./evidence/v036-round104-t03-pseudo-element-occlusion.md)。

## 2026-10-25 · 第105轮 Root T03/T07 隔离事务性碰撞门禁（非验收）

- R104真实Chromium允许同键候选inkBBox重叠且attest仍放行；R105新增提交前全键草案矩形碰撞检查，151个候选UID逐一主动负例拒绝，批量编辑/签名导入无部分写入。新增Chromium 170/170，继承R104 25、R103 26、R77 179、R99 302定向QA。
- 父R104 1425/1425 SHA继承，R105累计1433文件SHA256 `2ffa0ecc3b72bee3ef7d2a24d76431f3619c29b5734ed7dbf513388b0b7d876a`，Python/unzip双恢复与QA前后1433/1433 SHA一致；完整历史QA not-run。T03/T07均未正式集成，T00–T11仍0/12 Accepted。冻结生产入口及用户存储不变。[证据](./evidence/v036-round105-t03-t07-transactional-collision.md)。

## 2026-10-25 · 第106轮 Root T00旧学习行为基准（非验收）

- 冻结V0.35真实Chromium about:blank测试（仅测试内存插桩）逐字核验176编码、三模式528行为案例及错误输入/重试/短码确认/四码跳转/盲打遮蔽，新增3143/3143 QA通过；继承R105/R104/R103/R77/R99定向QA通过。
- R105父1433/1433继承，R106累计1439文件SHA256 `55e96b14b2a969e33b7e6b9e39fa132d0836062bbbb4d3fe9104d044d2de26c0`；Python/unzip双独立恢复各执行新3143+旧179+170项QA并在QA后1439/1439 SHA一致。完整历史QA not-run。
- 不改冻结正式入口/176编码/用户存储；T00/T09仍未正式Accepted，原始T00–T11仍0/12 Accepted；真同源存储blocked/not-run、真机/读屏not-run、同源高清原图许可及缺档未解决。[证据](./evidence/v036-round106-t00-176-browser-oracle.md)。
