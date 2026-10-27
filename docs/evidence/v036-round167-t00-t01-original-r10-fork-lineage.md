# R167 · Root T00/T01/T02 · 原始R10历史快照分歧门禁（非验收）

本轮实际读取R166累计ZIP，SHA256 `a0bd753dd2d2be8b95c3cfdb8bf05bb98bde02998b9ef7c94ea63bee6f1a0832`，2066/2066父成员逐文件SHA继承。原始R10嵌套ZIP SHA256 `6a1552b45cfa3512d9fea2ab06df740a6adbb4b598369cd3ea8e214fee1c0ed0`，184成员。

## 新发现

原始R10与当前累计根路径：137同名同字节、6同名不同字节、41原始成员在累计根路径缺失。6项冲突包括R8进度JSON、执行报告、build_round8.py、verify_round8.py，以及R9执行报告、验收JSON。**原始R10实际使用的R9 evidence.json与R8 151旧SVG草案在当前累计根路径缺失，但在原始R10 ZIP内存在。** 从原始R10快照独立核验15条来源候选与对照记录一一对应，其中8条旧SVG Path SHA与原始R8 151资产一致，另7条无旧资产映射。R10原始ZIP保持完整，不覆盖6个同名冲突；不能把当前累计根路径的R8/R9文件替换为R10的原始输入，也不能据此推断历史时间顺序、字根身份或正式认证。

## 实测QA及独立恢复

新增来源分歧/Path来源/损坏ZIP失败关闭QA **39/39**；实际重跑旧定向R164 45、R165 62、R166 108、R162 T03 14、R163 T03 20，合计选定旧249/249、新39/39、总288/288。**此前2358项递归选定全套及完整历史全量QA本轮not-run**，不计通过。R10原始verify_round10.py依赖硬编码路径及原始R9 ZIP，未原样执行；本轮使用独立只读审计。

新累计ZIP **2075文件**，SHA256 `f0ebd556f75e48cb09aef569054aa6b0c8f5dff62bed74a8647bf268c5504286`。Python zipfile与系统unzip分别独立解压，各2075/2075 SHA、2066/2066父继承、288/288选定QA、QA后2075/2075 SHA不变。源码、完整审计和可执行QA保存在隔离累计ZIP。

## 验收边界

原始T00–T11仍**0/12 Accepted**；T01 0/25正式认证，T02永久ID0，T03未生产集成，T05缺根数量未知。R11/R12/R35原始ZIP及R12 20SVG仍缺。合法同源高清原图逐笔认证、真实同源Web Locks/localStorage、Android/iOS真机、真实屏幕阅读器本轮not-run；完整历史全量QA not-run。冻结V0.35 HTML SHA `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`、2008 JPEG SHA `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`、176旧编码、历史正式SVG及用户原有存储均未修改。

下一步：恢复R11/R12/R35原始ZIP及R12 20SVG；以隔离原始来源逐笔核验M/K/E/B/J/R/V/X，勿用旧SVG或阈值代替正式认证。
