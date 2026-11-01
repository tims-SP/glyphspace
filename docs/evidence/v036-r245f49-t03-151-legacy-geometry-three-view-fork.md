# V0.36 R245F49 — Root T03 151个历史SVG几何与三视图隔离候选（非验收）

- 父ZIP R245F48 SHA256 `438d378eeef36699c143425871288ca22c89d94b0e750e50f45286f90451c3c4`，3534/3534成员逐文件SHA256一致。
- 从冻结V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc` 在真实Chromium about:blank提取25键151个旧可视实例：100×100 viewBox、旧实例ID、旧槽、SVG getBBox几何、锚点/光学偏移候选；2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`未变。
- 新增隔离单HTML：真实旧SVG的完整键盘、单键焦点、迷你键盘，三视图同步光学偏移及复位，拒绝无效实例ID、越界/非有限偏移，不使用localStorage。未修改生产入口。
- 新增真实Chromium 672/672 QA：151原SVG独立几何重测、151规范化/有限边界、151未认证门禁、25键三视图检查、M三视图同步与其余150实例不变、无效编辑拒绝/复位。继承选定507/507，总计1179/1179。
- 累计ZIP：3544成员，SHA256 `53693fcdd1941a8fb0c6f03508ddf506ba52a73d9aa8de571fc3e3af53ce235b`。Python/unzip两次独立解压各3544/3544 SHA、1179/1179选定QA，QA后0漂移；首个合并编排超时后将unzip QA单独重跑并通过。
- **边界**：getBBox仅为浏览器几何边界，不等于经过stroke/paint验证的真实inkBBox。151旧实例不是正式字根总数；T01正式认证0/25，T02批准ID0，T05缺根未知，T03未生产集成，T00–T11 0/12 Accepted。
- R10原始ZIP在R164内嵌，184成员及SHA独立复核；R11/R12/R35 ZIP、第12轮20SVG、R246主线累计原始ZIP仍缺。高清合法同源/许可/逐笔、真实同源生产迁移、真实读屏、Android/iOS真机、历史全量QA均未验收。
- 独立累计ZIP包含`v036_r245f49/`下的151条候选JSON、单HTML、可重建脚本、Chromium QA、旧新QA、父成员SHA及审计报告。冻结HTML、176旧编码、正式SVG、用户Storage均未动。
