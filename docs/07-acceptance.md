# 07 · V0.36验收标准：原始T00–T11 + UI-track

**R245F19 Root T01/T02（M四组同物理裁框来源别名人工描记解阻，非认证）：** 真实读取R245F18父ZIP3220/3220 SHA；独立重算25键170/170原生JPEG裁框RGB SHA，发现17条零独占像素来源观察。R245F18将M四对完全同裁框的候选/旧索引别名错误互斥，旧Chromium4/4无法描记；R245F19仅对白名单四对且nativeRect/RGB SHA完全相同的M别名允许人工笔画描记，8条恢复可审阅，E/K余9条仍阻断；不合并/批准任何正式身份。新35/35、继承选定475/475，共510/510；累计3230文件ZIP SHA `b2a15a68826afbaa0f411948a4c02491755f23782df6175185e7489aa2f069ec`，Python/unzip双恢复各3230 SHA与510 QA、QA后0漂移。T01正式0/25、T02批准ID0、T05缺根未知、Root 0/12 Accepted；R246 ZIP、历史R11/R12/R35缺失，高清许可逐笔/真同源/真机/读屏/历史全量not-run；冻结HTML/176编码/用户Storage未动。[R245F19证据](./evidence/v036-r245f19-t01-t02-M-shared-physical-crop-review-fork.md)。


**R245F18 Root T01/T02（来源审阅意见必须先校验原始JPEG，非认证）：** 实际Chromium复现R245F17未校验JPEG时可编辑并导出带原图SHA的意见JSON；R245F18隔离候选禁止未校验编辑/保存/导出，失败撤销输入、恢复合法原图后保留已验证意见。父ZIP3213/3213 SHA继承；新Chromium19/19、旧Chromium14+63、R145 Python379，选定475/475；累计3220文件ZIP SHA `3cfbcfd15c8006a3beb7bfa9f9aacfc67501785eb0e205f356c8252463e9ff2e`，Python/unzip双独立恢复各3220 SHA及475 QA、QA后0漂移。仍是about:blank，非高清逐笔/正式ID；T01 0/25、T02批准ID0、T05缺根未知、Root 0/12 Accepted；R246主线ZIP未取得、历史缺口未补，真同源/真机/读屏/历史全量not-run，冻结入口/用户Storage未动。[R245F18证据](./evidence/v036-r245f18-t01-source-review-note-provenance-fork.md)。


**R246 Root T01/T02（M四项来源像素跨候选污染修复，非认证）：** R245父ZIP3044/3044逐SHA继承；真实Chromium复现M-vis-04/06/07/08四项虽来源ID正确，但±7px上下文可描记其他候选精确裁框像素且导入仍接受。R246在活体描记/结束/导入三处保守隔离跨候选精确框像素，四项R245 4/4错误接受、R246 4/4拒绝，52案件映射不变；旧1387+新106=**1493/1493**选定QA。累计3054文件ZIP SHA `3f2c863af624bee7f9e2c96c3c0262fbb9af777924264612b49da2cc948da6fe`，Python/unzip双恢复各3054/3054 SHA及1493/1493 QA，QA后0漂移。仅隔离about:blank，**非来源逐笔认证**；高清许可、真实同源/真机/读屏/历史全量not-run，T01 0/25、T02批准ID0、T05缺根未知、Root 0/12 Accepted；冻结入口/176编码/用户Storage未动。[R246证据](./evidence/v036-round246-t01-t02-M-cross-crop-pixel-ownership.md)。


**R245 Root T01/T02（M四项来源案件身份绑定修复，非认证）：** 实际读取R244累计ZIP SHA `33e45a7924f10292e5e0794535e8a240b2cfebd913e55462b010c38844847d82`，3034/3034成员继承。真实Chromium复现R244把M shadow-04案件错误关联M-vis-01笔画且导出/导入仍接受；根因是4个shadow案件evidence原始ID与R144来源观察前缀不一致，且描记工具没有验证案件证据成员关系。R245只为M04/06/07/08建立显式别名，所有52案件描记与导入强制证据绑定、错误同键来源拒绝且保留旧草案。旧选定1299+新Chromium88=**1387/1387**；R245累计3044文件ZIP SHA `ae9b2181f8279db4e2fdebadc24f23da828193c0a6d6ebd806c06e44ce24626f`，Python/unzip双独立恢复各3044/3044 SHA及1387/1387 QA、QA后0漂移。仅隔离about:blank、非合法高清逐笔/正式SVG/真实读屏或真机；完整历史not-run，T01 0/25、T02批准ID0、T05缺根未知、Root 0/12 Accepted；冻结入口/176编码/用户Storage未动。[R245证据](./evidence/v036-round245-t01-t02-M-shadow-case-binding.md)。


**R244 Root T01/T02（原图笔画自由描记与自导出修复，非认证）：** 实际读取R243累计ZIP 3024/3024 SHA，真实Chromium复现R243允许130点描记完成但自身JSON导出无法导入（校验上限128点）；新增按住拖动的真实pointer自由描记、原生JPEG坐标连续采样、pointercancel/失焦取消、128点上限，保留点击两点再结束功能。旧选定1268+新Chromium 31=1299/1299；R244累计3034文件ZIP SHA `33e45a7924f10292e5e0794535e8a240b2cfebd913e55462b010c38844847d82`，Python与系统unzip双独立恢复各3034/3034 SHA、1299/1299选定QA，QA后0漂移。仅about:blank注入冻结JPEG，不是合法高清逐笔认证/正式SVG/真实读屏或真机；历史全量not-run，T01 0/25、T02正式ID0、T05缺根未知、Root 0/12 Accepted；冻结入口/176编码/用户Storage未动。[R244证据](./evidence/v036-round244-t01-t02-freehand-source-stroke-roundtrip.md)。


**R243 Root T01/T02（来源像素逐笔描记工具，非认证）：** R242父累计ZIP 3015/3015逐文件SHA一致；在R240 25键/170观察/52案件工作台新增人工笔画中心线描记、原生1536×1086坐标与裁框RGB SHA绑定、完整图/键位视图不变坐标、撤销与未批准JSON导入导出；10类伪造/越界输入拒绝且保留原内存。旧选定1227+新Chromium about:blank真实鼠标41=1268/1268 QA；R243累计3024文件ZIP SHA `eafddc9d9b028a97a55628d7326e771cd2dd63b6237757450b2292a235d24964`，Python/unzip双独立恢复各3024/3024 SHA、1268/1268 QA、QA后0漂移。仅两点M键测试草案，**不代表逐笔认证/正式SVG**；合法同源高清许可、真机/读屏/历史全量not-run；T01 0/25、T02正式ID0、T05缺根未知、Root 0/12 Accepted；冻结入口和用户Storage未动。[R243证据](./evidence/v036-round243-t01-t02-source-pixel-stroke-tracing.md)。


**R242 Root T01/T02（36个旧未匹配槽的原图逐项视觉分流，非认证）：** 真读R241父ZIP 3007/3007 SHA；冻结2008 JPEG与R144来源注册表钉SHA，36/36原裁框RGB及±7px上下文独立核验。人工低清视觉初筛6个右上圈注候选（D:1/E:7/F:2/H:4/J:4/N:7）、2个同框圈注边缘否定（E:1/E:8）、28项笔画归属未决；不自动改分类、Path或ID。旧1074+新153=1227/1227选定QA；R242累计3015文件ZIP SHA `d5020f167bc5d38dc0255678361de192384841d0a061c80c6ac583e0b8241527`，Python/unzip双恢复各3015 SHA与1227 QA，QA后0漂移。高清许可/逐笔、真实读屏/真机/历史全量not-run；T01 0/25、T02正式ID0、T05缺根未知、Root 0/12 Accepted；冻结入口和用户Storage未动。[R242证据](./evidence/v036-round242-t01-t02-36-unmatched-triage.md)。


**R241 Root T01/T02（M四个未绑定微形原图裁框上下文复核，非认证）：** 真读R240父ZIP 3000/3000 SHA；对M-vis-04/06/07/08原始裁框逐RGB SHA复验，实际并排审阅精确框与±7px上下文，发现低清原框边界邻近仍有深色笔画结构，不能把裁框当完整独立字根或直接生成Path。四项保持needs_highres、无替代裁框、无ID签发。旧R239 852+R240 190+新R241 32=1074/1074选定QA；R241累计3007文件SHA `9c720309427a10c86af633e1157c8b993474df14a37bf065b3df44b0bd21d8a4`，Python/unzip双独立恢复各3007/3007 SHA及1074/1074 QA、QA后0漂移。Chromium仅about:blank注入原始JPEG字节；合法同源高清逐笔、真机/读屏/历史全量not-run。T01 0/25、T02 ID0、T05缺根未知、Root 0/12；冻结入口/用户存储未动。[R241证据](./evidence/v036-round241-t01-t02-M-microform-context.md)。


**R240 Root T01/T02（25键原图人工复核工作台，非认证）：** 真实继承R239父ZIP 2989/2989 SHA，复验冻结2008 JPEG及R144注册表，170/170原生RGB裁框SHA；新增独立25键170观察/52待审案件审阅HTML（M12观察/8案件、无存储、仅导出未批准意见）。旧852+新190=1042/1042选定QA，Chromium为about:blank注入原始JPEG字节，file://被管理员阻断；R240累计3000文件SHA `4e6c646f9b48f3e66a7de681fb485bb5de84912498bbe746caf803235120a208`，Python/unzip双恢复各3000 SHA及1042 QA、QA后0漂移。T01认证0/25、T02批准ID0、T05缺根未知、Root 0/12；高清许可/逐笔、真机/读屏/完整历史not-run，冻结入口与用户存储未动。[R240证据](./evidence/v036-round240-t01-t02-source-review-workbench.md)。


**R239 Root T04（真实同源双标签并发恢复，非验收）：** 真实GitHub Actions独立127.0.0.1 Chromium Web Locks/localStorage/WebCrypto 22/22（run 41052963001），将R238 Node FakeStore并发冲突与恢复扩展至真实双标签；25键156旧槽仅合成数据。R238父ZIP 2984/2984逐SHA继承；R239累计2989文件SHA `1c00ab27ca12bb13d16b26d53e1cc3d37c1bb2c574756a1349c6d7ac08aa99c0`，Python/unzip双恢复各2989 SHA、852/852选定旧QA及QA后0漂移。本地真实同源仍管理员阻断；生产用户迁移、高清逐笔、真机/读屏/完整历史not-run。T04未Accepted，Root 0/12，T01 0/25、T02 ID0、T05缺根未知；冻结入口/176编码/用户存储未动。[R239证据](./evidence/v036-round239-t04-real-cross-tab-ci.md)。


**R238 Root T04（并发冲突隔离，非验收）：** 真读R237父ZIP SHA `68f84281940ed43892b71408e95ab3259268f5efdaa13e7f3db42366072a7d6a`，2976/2976逐成员继承；实际25键156槽签发+R192事务内核的Node私有Map双实例并发、崩溃日志、非协作写入冲突及恢复拒绝新增17/17，继承旧835/835，共852/852选定QA。R238累计2984文件SHA `28ea55adeb80a8309bb9d66ee077a4d559f9b7f8c54cfa76d0eb1698bf506580`，Python/unzip双恢复各2984 SHA及852 QA、QA后0漂移。本地真实同源仍blocked，R238真实浏览器not-run；生产迁移、高清逐笔、真机/读屏、历史全量not-run。T04未Accepted，Root 0/12，T01 0/25、T02 ID0、缺根未知；冻结入口及用户Storage未动。[证据](./evidence/v036-round238-t04-concurrent-recovery-conflict.md)。


**R237 Root T04验收边界：** 全25键156旧槽合成来源签发+影子事务的真实授权127.0.0.1 Chromium测试24/24（[run 41037798793](https://github.com/tims-SP/glyphspace/actions/runs/41037798793)）；本地真实同源blocked，生产用户数据迁移/回滚及正式ID映射not-run，T02/T03依赖未Accepted，因此**T04未验收**。Node新增26+旧809=835/835选定QA；R237累计2976成员ZIP两次独立恢复各2976 SHA及835 QA，完整历史QA未运行；Root仍0/12。[证据](./evidence/v036-round237-t04-fullslot-real-origin.md)。


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


**R222验收边界：** B/J/V/X 29个冻结来源裁框的38个精确互斥几何覆盖成员组（741个多框像素，V三重33）只能定位低清来源裁框重叠，不是笔画分割、来源许可、形态分类、永久ID或T05补图认证。R221父2785 SHA继承、R222累计2800双独立SHA与1016选定QA；高清原始字节及许可、真实同源、真机、读屏、完整历史QA仍未完成。T01正式0/25、批准ID0、缺根未知、原始T00–T11 0/12 Accepted。 [证据](./evidence/v036-round222-t01-t02-disjoint-native-crop-membership.md)。

**R221正式验收边界：** 8对冻结JPEG裁框交集的低清RGB暗像素及25键覆盖计数仅是来源审阅风险；不是高清逐笔、形态分类、笔画归属、永久ID或T05补图认证。R220父2773逐SHA、选定685/685 QA、R221累计2785文件双独立SHA/QA恢复。高清原始字节及许可、真同源、真机、真实读屏、完整历史QA仍未完成。T01 0/25、批准ID0、缺根未知、原始T00–T11 0/12 Accepted。 [证据](./evidence/v036-round221-t01-t02-native-overlap-pixel-ownership.md)。

**R220验收边界：** 161个冻结JPEG来源裁框RGB SHA复核、阈值60/100/140边缘风险、8对原生裁框几何重叠及3高清像素经验留白仅供来源风险分流；不是高清原始像素逐笔核验、笔画截断证明、永久ID、T05正式补图或生产集成。父2762逐SHA、累计2773双恢复各628选定QA通过；高清原始字节本地未取得、许可未确认、真同源/真机/读屏/历史全量not-run。T01 0/25、ID0、缺根未知、Root 0/12 Accepted。 [证据](./evidence/v036-round220-t01-t02-native-crop-boundary-risk.md)。

**R219验收边界：** 161个高清候选坐标包络是R119已验证仿射对R156低清裁框的数学投影，不是读取高清像素、来源授权、逐笔认证、正式补图或永久ID。M四来源框独立，E/K同裁框身份不合并；双恢复2762 SHA/588选定QA通过。高清原始字节本地未取得、许可未确认；T01 0/25、T02永久ID0、缺根未知、T00–T11 0/12 Accepted。 [证据](./evidence/v036-round219-t01-t02-25key-highres-coordinate-crosswalk.md)。

**R218验收边界：** 166草案身份的证据就绪门禁及25键来源采集队列是隔离T01/T02准备工作，非原图逐笔认证、非永久ID签发。R217父2740/2740 SHA，选定QA518/518，累计R218 2751文件Python/unzip双恢复各2751 SHA和518 QA；来源高清合法原始字节/许可、真同源/真机/真实读屏/历史全量未验收。T01正式0/25、永久ID0、缺根未知、Root T00–T11仍0/12 Accepted。[证据](./evidence/v036-round218-t01-t02-source-identity-readiness.md)。


**R217验收边界：** Root T03子组几何漂移守卫只在隔离包，真实Chromium旧3例错误接受、新8例拒绝；选定QA2667/2667，2740文件双独立恢复通过。未取得同源高清原始字节或正式来源认证，未集成生产内核，真实同源存储/真机/读屏未运行，递归历史QA超时未计pass。Root T00–T11仍0/12 Accepted、T01正式0/25、T02批准永久ID0、缺根数未知。[证据](./evidence/v036-round217-t03-pointer-group-geometry-drift.md)。

**R216边界：** Root T03仅新增隔离指针→100×100光学校准提案，真实Chromium about:blank 1510个坐标断言及12个异常拒绝、Node42、静态24、继承311，合计选定1899/1899；双独立2727成员SHA/QA通过。未完成生产集成、原图逐笔/永久ID、真同源存储、真实读屏、真机或完整历史QA。**T00–T11仍0/12 Accepted，T01正式0/25，T02正式ID0。** [证据](./evidence/v036-round216-t03-pointer-to-optical-bridge.md)。

**R215验收边界：** 独立CSS rotate/scale/translate裁剪守卫在真实Chromium复现R214漏包40黑像素，R215拒绝未验证变换；旧261+新31+静态19=311/311，2713成员双独立SHA/QA恢复。仅隔离上界修复，不等于T03生产集成、精确墨迹、原图逐笔或永久ID；Root 0/12 Accepted、来源0/25、ID0、缺根未知；同源blocked，真机/读屏/历史全量not-run。[证据](./evidence/v036-round215-t03-css-individual-transform-guard.md)。


**R214正式验收边界：** 根SVG overflow视口的保守裁剪上界已在真实Chromium复核（新增40+静态18、选定旧203，合计261/261），2701成员累计包双独立SHA/QA恢复；但不代表精确墨迹、来源逐笔、永久ID或正式T03生产集成。Root 0/12 Accepted、来源0/25、永久ID0、缺根未知；真同源blocked，真机/读屏/历史全量not-run。[证据](./evidence/v036-round214-t03-svg-viewport-clipping.md)。

**R213 Root T03（缩放祖先overflow上界修复，隔离非验收）：** 真实Chromium发现R212在scale(.5)时屏幕可见500黑像素却报告仅10×15上界，漏掉真实墨迹；R213改用CSS subpixel border-box与屏幕缩放比率，scale(.5)修正为20×25，scale(2)为80×100，906旧SVG几何不变，旋转/透视等失败关闭。父R212 2675/2675 SHA继承，选定旧159+新44=203/203；累计2688文件ZIP SHA `5907af02850e0084528b3082f6524e9fd8750d20a88ecbcf9eeae7fb5aee7089`，Python/unzip双独立恢复各2688 SHA及203 QA、QA后0变化。T03未生产集成、Root 0/12 Accepted、来源0/25、永久ID0、缺根未知；同源blocked、真机/读屏/历史全量not-run；冻结入口/用户Storage未动。[R213证据](./evidence/v036-round213-t03-scaled-overflow-border-fix.md)。

**R212 Root T03（HTML overflow裁剪保守包络，隔离非验收）：** 修复R211一律拒绝合法overflow:hidden/clip/scroll祖先；新增真实Chromium矩形裁剪上界（保留原inkBBox，完全裁剪null），906旧SVG几何不变，截图黑像素10000→2000→0；父R211 2663/2663逐SHA继承，选定旧126+新33=159/159；累计2675文件ZIP SHA `4f4fd0283aa87dba0f95224c5e6afc5a11ca67b048ab8c263be5e79ce9e296ae`，Python/unzip双独立恢复各2675 SHA及159 QA、QA后0变化。R211递归670套件超时不计pass，完整历史全量not-run。T03未生产集成，Root 0/12 Accepted、来源0/25、永久ID0、缺根未知；同源blocked、真机/读屏not-run；冻结入口/用户Storage未动。[R212证据](./evidence/v036-round212-t03-rectangular-overflow-upper-bound.md)。
**R211 Root T03（HTML祖先绘制抑制，隔离非验收）：** 实际Chromium发现R210只检查SVG内祖先，HTML外层opacity=0/全裁剪时仍返回inkBBox，截图黑像素3200→0；新增HTML祖先computed-style失败关闭守卫。906组正常几何一致，11个外层反例拒绝（9个旧R210误接受），选定旧644+新Chromium14+静态12=670/670；父R210 2651/2651 SHA继承，R211累计2663文件SHA `ddc0127fe6317f1c9f336b00069766f5b1ea2ff5178be2e328024d4036a99739`，Python/unzip双独立恢复各2663 SHA及670 QA，QA后0变化。T03未生产集成，T01 0/25、永久ID0、Root 0/12 Accepted；同源blocked、真机/读屏/历史全量not-run；冻结入口及用户Storage未动。[R211证据](./evidence/v036-round211-t03-outer-html-ancestor-paint-gate.md)。

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
