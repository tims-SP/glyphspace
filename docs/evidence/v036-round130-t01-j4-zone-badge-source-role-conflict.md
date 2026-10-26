# V0.36 R130 · J:4原图复合区域与区位徽记来源角色冲突（隔离）

- 日期：2026-10-26。原始任务T01参考图清点，关联T02稳定ID、T03 SVG坐标内核、T07位置碰撞；不是UI-track，不构成正式验收。
- 来源冻结SHA：V0.35 HTML `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`；2008 JPEG `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`。本轮重新核验原始字节。
- **来源角色发现**：R81原生账本的J:4旧槽标记`blocked_invalidated`、`round69Unbound=true`，其`[1005,397,24,32]`原生裁框同时包含圆圈与两条竖笔的复合区域，不能据旧标签`丨`推导独立正式根。冻结HTML源码写明“H/J/K have a live SVG 丨 root already; all badge strokes are just illustrations.”。Chromium原生DOM核验H/J/K区位徽记竖笔数量分别1/2/3，每键另有一圈；J根`J-root-05`的`data-root=丨`，区位徽记`data-annotation-type=zone-badge`、`aria-hidden=true`。DOM节点SHA与R129审计一致。
- R129在800px测得J:4与marker1为648/648根墨迹重叠，**与源码的示意性叠加意图一致，但不能据此自动批准碰撞、证明原图笔画归属或认定J:4是独立根**。决定保留J:4身份阻断、禁止以该复合裁框签发`referenceShapeId`/`instanceId`或正式SVG。正式源图语义仍需合法高清原字节及逐笔复核。
- 父R129累计ZIP：1698文件，SHA256 `a7facaeaa26667d36dd0584d443b2e8b63abfbed8f24ec0c4a5c1a591286e732`，逐文件1698/1698继承；R130累计ZIP：**1712文件**，SHA256 `e7d0d0fda95ca938cba1e49359ce3507356e6c65a9cb25d383c0a3cede7c0bb3`。Python zipfile与系统unzip对候选包各1710/1710 SHA一致并各执行新30+精选旧475=505/505 QA；最终包再经两套独立解压1712/1712 SHA一致、各新增30/30 QA。**不是953项完整继承QA**，完整历史QA not-run。
- **失败记录**：父工作树首次R129浏览器回放L:1 marker2出现0/286差异；独立Python恢复首次J:4出现128/164差异。均未计通过，后续独立重试才505/505；渲染重放存在不稳定性，后续需修复测试同步条件，不能把重试通过称为零缺陷。
- R10–12/R35历史ZIP、R12的20SVG仍缺失；同源高清原始字节及许可、真实共享原点迁移、Android/iOS真机、真实屏幕阅读器均未验收。原始T00–T11 **0/12 Accepted**，T01 0/25、正式ID0、T03未集成、T05未完成；冻结V0.35入口、176编码、正式SVG、用户存储均未修改。

外部ZIP证据：`v036_round130/R130_J_badge_provenance_audit.json`、`R130_J_native_review_only.png`、`j_badge_source_provenance.py`、`qa_j_badge_provenance.py`、`R130_parent_1698_member_SHA256.json`、`R130_double_restore_QA.json`、`R130_final_execution_report.md`。
