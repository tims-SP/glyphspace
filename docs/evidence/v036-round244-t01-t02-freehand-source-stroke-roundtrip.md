# V0.36 R244 · Root T01/T02 来源像素自由描记与JSON自回环修复（非认证）

- GitHub main前置：`baa85bffcc91cb6f7a86f369f19963011159f8e7`；按AGENTS.md读取六份强制文档，原始任务编号不变。
- R243累计父ZIP SHA `eafddc9d9b028a97a55628d7326e771cd2dd63b6237757450b2292a235d24964`；实际解包3024文件、外部SHA清单逐成员3024/3024一致。
- **复现真实故障**：R243隔离Chromium `addPixel`接受130个点，`finish()`成功，但同一页面的 `importData(document())` 拒绝该导出（输入验证最大128点）。R244在采集时封顶128点；自由描记超过上限取消未提交笔画，防止静默截断。
- **实质交互改进**：独立R244 HTML使用真实mouse/pointer按住拖动，连续采样2008 JPEG原生像素坐标，来源观察ID和裁框RGB SHA绑定；pointer capture、pointercancel、失焦及越界失败关闭，松开自动结束；R243点击两点后手动结束仍可用。导出未批准JSON不产生SVG/正式ID。
- R239=852、R240=190、R241=32、R242=153、R243=41旧选定QA全通过（1268）；R244新增真实Chromium about:blank鼠标拖动31/31，总1299/1299。
- R244累计ZIP 3034文件、SHA `33e45a7924f10292e5e0794535e8a240b2cfebd913e55462b010c38844847d82`；Python zipfile与系统unzip两次独立恢复各3034/3034逐SHA、1299/1299 QA、QA后0漂移。完整历史全量QA **not-run**。
- 参考JPEG SHA `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`、冻结V0.35 HTML SHA `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`，未修改。
- R10历史包已恢复；R11/R12/R35 ZIP及R12 20SVG仍缺失。合法同源高清字节及许可、逐笔人工正式认证、真实读屏、真机、真实用户数据迁移均未验收。T01 0/25、T02批准永久ID0、T05缺根未知、Root T00–T11 **0/12 Accepted**。
- 生产入口、176旧编码、正式SVG和用户原有Storage不变。隔离恢复使用本轮ZIP内 `v036_round244/R244_recovery_instructions.md` 与外部逐成员SHA清单。

**本轮界限：** 这是实际审阅工具可用性与数据可逆性修复，不是任何字根来源认证；不能把QA数量提升为T01/T02 Accepted。
