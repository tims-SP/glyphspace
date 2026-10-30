# R240 · Root T01/T02 25键原图人工复核工作台（非正式认证）

- 基线：GitHub main `b211a28c19150400031a0ec04fd266bd1d487f50`；本地实际读取R239累计ZIP，SHA256 `1c00ab27ca12bb13d16b26d53e1cc3d37c1bb2c574756a1349c6d7ac08aa99c0`，2989/2989文件逐SHA继承。
- 实际新增：`v036_round240/R240_source_bound_human_review_workbench.html`（隔离审阅工具，非生产键盘）；复用ZIP中的原始2008 JPEG（SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`）和R144审阅注册表（SHA256 `cafa1c6eae872e1562109830faae5347094b41690c7bb63e5a4ce784a95e77bb`）。
- 工作台覆盖25键、170条物理来源观察、52个待审案件；M键12条观察/8个案件、四个未绑定候选可直接逐框审阅；原始JPEG像素放大、裁框叠加、键位/案件导航、人工备注、待审JSON导入导出；不调用localStorage/IndexedDB、不触碰用户存储、不提供认证/批准ID按钮。导入检查来源SHA、注册表SHA、案件ID及禁止认证字段；源图缺失时明确失败。
- 本轮170/170来源裁框原生RGB SHA独立重算一致；新静态+Chromium about:blank 190/190；继承R239选定旧QA 852/852。真实`file://`导航受到本地`ERR_BLOCKED_BY_ADMINISTRATOR`阻断，Chromium QA改用`about:blank`加载实际HTML并注入相同原始JPEG data URL，不冒充真实文件原点。
- R240累计ZIP：`R240_cumulative_isolated_T01_T02_25key_human_review_workbench.zip`，3000文件，SHA256 `4e6c646f9b48f3e66a7de681fb485bb5de84912498bbe746caf803235120a208`；Python与系统unzip两次独立解压各3000/3000 SHA、852/852旧QA、190/190新QA、QA后0漂移。
- 缺档：R11/R12/R35原始ZIP与R12的20个SVG仍未找回；本轮本地与Library关键词搜索未发现精确匹配，不宣称全Library穷尽。高清同源合法原始字节/许可/逐笔、真机、真实读屏、历史全量QA均not-run。
- 正式结果：T01认证0/25，T02批准永久ID0，T05真实缺根数null；T00–T11均accepted=false（0/12）。冻结V0.35 HTML、2008 JPEG、176旧编码、正式SVG及生产入口未修改；无真实用户存储写入。
- 工作台仅提供人工证据判读与可追溯待审意见，不把170来源观察、52案件或自动化测试数量冒充字根数量、来源认证或Root任务验收。
