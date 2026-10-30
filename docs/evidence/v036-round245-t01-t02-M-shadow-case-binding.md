# R245 · 原始T01/T02：M键来源案件绑定修复（非来源认证）

## 真实缺陷及修复

父版R244独立累计ZIP SHA256 `33e45a7924f10292e5e0794535e8a240b2cfebd913e55462b010c38844847d82`，3034/3034成员继承SHA一致。R144注册表中四个M shadow案件的证据为 `2008-M-vis-04/06/07/08`，但对应来源观察ID为 `M-candidate:2008-M-vis-04/06/07/08`。R244在真实Chromium中复现：`review-only/M/shadow-2008-M-vis-04`默认来源为null；用户选择同键的`M-candidate:2008-M-vis-01`后，可将其笔画错误记录到shadow-04案件并成功导出/重导入。

R245隔离审阅工具只为上述四个M shadow案件添加显式别名映射；对所有52个案件强制要求描记/导入的来源观察属于该案件的evidence。无关来源即使来自同一键、裁框SHA正确，也必须拒绝；导入失败保持原草案不变。未修改冻结R144注册表、正式SVG或V0.35入口。四个M shadow案件现均可绑定其自身正确观察ID并用真实鼠标描记，**不等于确认四个独立字根或完成补图**。

## QA、恢复与交付

- 实际重跑R239–R244选定旧QA：852+190+32+153+41+31 = **1299/1299**。
- 新增R245真实Chromium `about:blank` + 冻结JPEG原始字节：**88/88**，覆盖52案件来源绑定、4个M shadow、错误同键来源导入拒绝、失败原子性、真实鼠标描记。
- R245独立累计ZIP：**3044文件**（继承3034，新增10），SHA256 `ae9b2181f8279db4e2fdebadc24f23da828193c0a6d6ebd806c06e44ce24626f`。
- Python zipfile与系统unzip两次独立解压：各**3044/3044** SHA一致；每套实际重跑选定QA **1387/1387**，QA后各3044/3044 SHA一致。首次恢复曾因截图重复生成导致字节漂移，已修复并重新打包/双独立复验。
- 冻结V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`、2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`及R144注册表SHA钉值通过。176旧编码、正式SVG、用户存储均未修改。
- ZIP内：`v036_round245/R245_source_case_bound_stroke_review_workbench.html`、`qa_r245.py`、`R245_source_case_binding_audit.json`、`R245_execution_report.md`、`R245_M04_case_bound_real_pointer.png`、继承清单与恢复说明。

## 正式验收边界

T01认证仍0/25键、T02正式永久ID仍0、T05真实缺根数未知、T00–T11 **0/12 Accepted**。测试为本地隔离`about:blank` Chromium，不是合法同源高清逐笔认证、真实同源存储、真实读屏或真机；完整历史全量QA not-run。R10已恢复，R11/R12/R35原始ZIP及R12 20 SVG仍缺失，不宣称连续历史全量。持续任务不得停止。
