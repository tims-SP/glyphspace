# R218 · Root T01/T02 来源证据→独立身份晋级前置检查（隔离非验收）

## 实际实现与原始任务边界

读取并SHA256校验R217累计父ZIP（2740成员），在隔离R218中新增可执行 `t02_source_identity_promotion_preflight.py`、271项身份/篡改QA、18项静态QA及25键CSV采集队列。基于R209类型化草案166候选（151冻结旧矢量+12无旧别名裁框+3 K混合观察）与R206 50票据/52链接，严格验证UID命名空间、唯一性、旧Path来源、来源裁框、票据和E/K同裁框异Path必须分离。该程序只输出缺失证据和复核准备状态，**从不发行永久ID，也不批准生产绑定**。

- 166/166候选仍缺少同源高清原始字节/合法许可/逐笔比对/语义与第二复核等正式证据，全部 blocked。
- M 8候选中4无旧SVG别名；K 8候选中3为混合来源观察，K:2/K:3仍冲突；E:1/E:8仍冲突；B/J/R/X/V列入下一优先队列。
- 两组E/K同裁框冲突涉及4候选，拒绝自动合并。所有25键正式来源认证仍0/25，永久ID批准0，缺根数null。
- 合成全证据测试只返回 needs-independent-signoff，不产生已批准ID；三份来源文件原始字节篡改均被拒绝。
- 06wb教程页标记“官方”高清字根图（https://06wb.github.io/Tutorials/index.html），**未取得可核实的再分发许可或合法同源高清原始字节**，不可提升为认证。

## 实际校验和恢复

- R217父ZIP SHA256 `6bb1302e283a41a17c6390ce5e9229efc8f4f5008b0a8748784540ba4166728d`；继承2740/2740成员SHA256一致。
- 选定旧QA 229/229；新增候选/对抗271/271、静态18/18；本轮合计**518/518**。
- R218累计ZIP **2751文件**，SHA256 `f4766f9b7760f3bf2df7c3383f4ec24bd3cead0ab4b6b9a008e00a106969b3d0`。
- Python zipfile与系统unzip两套独立恢复各2751/2751 SHA256，且各518/518 QA；QA后文件变化0。
- 新执行模块SHA256 `5e58782886c589c39fa050ef660a29af327d02ca8b3f9c621f9c83338090658e`；逐候选JSON SHA256 `6f530386cb25df6bb0cc2957f43e6b862eebb4a6cb2ac7d563981f826be00b2a`。完整脚本与数据在独立累计ZIP中，未提交生产入口。

## 仍阻断

可访问Library ZIP清单30个文件中未找到R11/R12/R35原始包；R10已于R164恢复，R12的20 SVG仍缺。完整历史QA not-run。真实同源Web Locks/localStorage本轮not-run（历史管理员阻断），真实屏幕阅读器/Android/iOS真机not-run。冻结V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`、2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`、176旧编码、正式SVG、生产入口及用户存储均未修改。

**Root T00–T11 0/12 Accepted；T01 0/25；T02永久ID 0；T03尚未生产集成。** 此轮是独立身份晋级准备，不是源图逐笔认证或T05补图。
