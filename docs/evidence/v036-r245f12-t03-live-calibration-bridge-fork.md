# R245F12 · Root T03 解析式SVG与旧校准桥接（隔离，非验收）

日期：2026-10-31。原始T03，不是UI-03。父R245F11累计ZIP 3151/3151 SHA继承，SHA256 `9dc745ba3d8a057af4e9dc7a98f83afec421c6afbc2e6fc52e5202536b7797fc`。主线R246累计ZIP原始字节仍不可用，不能宣称连续R247。

**真实复现：** R245F11已将151冻结SVG路径和R54 inkBBox/R62 100×100坐标接入V0.35三视图，但原校准X/Y/尺寸控件继续写旧式translate/scale，Chromium中移动E键字根后`inspect()`报告`candidate geometry drift`。原校准工作流失效。

**修复：** 仅在独立候选单HTML的原`synchronizeCoords`中加入坐标快照事件，适配器验证151条输入范围及解析式inkBBox后统一更新full/focus/mini的SVG matrix。键重置、旧训练输入继续工作，Path与未经提交坐标篡改拒绝。事件不等于来源签名。候选用私有内存Storage，不触碰用户原有存储、冻结V0.35 HTML、2008图、176编码、正式SVG和生产入口。

**实际QA：** Chromium about:blank 1280×800 DPR1、390×844 DPR2、844×390 DPR2，父缺陷复现及修复、XYZ/尺寸、三视图、重置、输入和负例新增51/51；继承选定680/680，总731/731。累计ZIP 3160文件，SHA256 `46092b27bcc671aa72b0276d633a83354c382a2aeb2845215ee44e1934b8973c`。Python zipfile及系统unzip双独立恢复各3160/3160 SHA、731/731 QA、QA后0漂移。ZIP和逐文件清单作为会话附件，不上传GitHub。

**验收边界：** 真实同源迁移、真机、读屏、合法同源高清逐笔认证及完整历史全量QA not-run。T01正式0/25键，T02批准永久ID0，T05缺根数未知，T03尚未生产集成，原始T00–T11全部accepted=false（0/12）。R11/R12/R35原始ZIP和R12 20SVG仍缺。
