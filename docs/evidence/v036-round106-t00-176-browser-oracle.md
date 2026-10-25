# V0.36 第106轮 · Root T00 冻结176编码的真实Chromium行为回归（非正式验收）

- 日期：2026-10-25；工作轨道：**原始T00**（T09仅为未来集成的回归基准，不是T09完成）。
- 父包：第105轮，1433成员，SHA256 `2ffa0ecc3b72bee3ef7d2a24d76431f3619c29b5734ed7dbf513388b0b7d876a`；实际读取后1433/1433成员SHA继承一致。
- 冻结HTML：`fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`；2008 JPEG：`df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`，均未修改。
- **本轮新增**：对冻结V0.35 HTML只在**内存中**插入受限测试钩子，用独立Chromium `about:blank` + `page.set_content`运行原有输入状态机。与R2的176条训练JSON逐字对照char/code/kind/level/steps；176字×引导/进阶/盲打=528实际浏览器行为案例，覆盖错误键不推进、Backspace、正确码序、3键空格确认、4键自动跳转、盲打未来码元遮蔽，新增 **3143/3143断言通过**。
- 原有五组回归重新执行：R105 Chromium170/170、R104 Chromium25/25、R103 Chromium26/26、R77 Node179/179、R99 Chromium raster302/302。独立Python与系统unzip恢复的最终R106包各重新运行R106 3143/3143、R77 179/179、R105 170/170，并于QA后各逐文件核验 **1439/1439** SHA一致。
- R106累计ZIP **1439文件**，SHA256 `55e96b14b2a969e33b7e6b9e39fa132d0836062bbbb4d3fe9104d044d2de26c0`。ZIP真实字节仅保存在本轮隔离交付工作区，**未上传GitHub**；包内含`v036_round106/qa_frozen_176_browser.py`、原始测试JSON、继承成员SHA账本、报告及双恢复脚本。两份恢复日志另行交付。
- **限制**：冻结HTML测试钩子是内存中的测试夹具，不是发布文件变更。about:blank不具备真实同源存储条件；T04真实Web Locks/localStorage仍blocked/not-run；Android/iOS真机、真实读屏、全历史QA仍not-run。缺第10–12轮/35轮ZIP、第12轮20 SVG、合法同源高清原图。T01正式0/25、T02正式永久ID0、T03生产未集成、T05未补图、**原始T00–T11仍0/12 Accepted**。
- 冻结`index.html`、176编码、正式SVG、用户现有localStorage及正式发布入口全部未触碰。T00尚需新发行候选的双版本端到端回归和完整恢复证据，T09尚需正式三视图及设备验收。

复验命令（先解压R106 ZIP到独立目录）：`PYTHONDONTWRITEBYTECODE=1 python v036_round106/qa_frozen_176_browser.py --no-write`。这不会使用真实用户浏览器profile。