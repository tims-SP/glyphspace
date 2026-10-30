# R241 · T01/T02（关联T05）M键四个未绑定微形原始裁框上下文复核

- 日期：2026-10-30；基线：R240 `4e6c646f9b48f3e66a7de681fb485bb5de84912498bbe746caf803235120a208`，3000/3000逐文件SHA继承。
- 冻结2008 JPEG SHA256：`df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`；R144注册表SHA256：`cafa1c6eae872e1562109830faae5347094b41690c7bb63e5a4ce784a95e77bb`。
- 真实人工观察：M-vis-04 (1017,623,14,13)、M-vis-06 (1012,652,12,15)、M-vis-07 (1027,653,12,14)、M-vis-08 (1040,653,12,15)。原框只有12–14px宽；独立原始像素上下文显示部分深色结构延伸至原框附近或邻项，无法从孤立小框断定完整笔画归属。
- 交付：R241累计ZIP内 `v036_round241/R241_M_four_unbound_context_evidence.json`（四项原框与上下文RGB SHA、低清初步观察）、`R241_M_four_exact_vs_context.png`、`R241_M_four_context_readonly.html`、`qa_r241.py`。所有上下文框仅为对照，不是正式新裁框，不改变任何正式SVG。
- QA：继承R239 852/852、R240 190/190；R241新增32/32。两次独立解压（Python及系统unzip）各3007/3007 SHA、1074/1074选定QA，QA后0文件变化；历史全量QA not-run。
- ZIP SHA256：`9c720309427a10c86af633e1157c8b993474df14a37bf065b3df44b0bd21d8a4`，3007成员（R240 3000 + R241 7）。
- 浏览器：本地Chromium about:blank注入冻结JPEG原字节；localStorage读取受安全策略限制，不作为真实同源测试；无用户存储写入。
- 正式状态：T00–T11 **0/12 Accepted**；T01 0/25、T02正式ID 0、T05缺根数未知；M四项均needs_highres，未证明是四个独立字根。
- 历史：R10原始ZIP已于R164恢复；R11/R12/R35原ZIP及R12 20 SVG缺失。合法高清同源逐笔、真机、真实读屏仍not-run。
- 下一步：取得合法同源高清原字节，对M四项与邻接笔画进行逐笔复核，再处理K/E/B/J/R/X/V与36旧未匹配；禁止将低清阈值、放大图或裁框SHA冒充来源认证。
