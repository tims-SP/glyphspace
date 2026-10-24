# V0.36 第82轮 · Root T01 原生像素逐形态证据草案工作台（非验收）

- 日期：2026-10-24。父第81轮累计ZIP SHA256 `211e8e0f3c4d5c5808cfaa87969dfa7cbf9d9dd5872a7a6cfad6c77966f0b6f9`，1164/1164逐文件SHA继承。
- 新增隔离的单HTML原生JPEG审阅工作台：以第81轮159条观察、25键、153个不同原始裁框为只读数据；提供原生像素RGB、25键导航、36条历史未绑定与4条M未绑定候选筛选、ROI原图坐标标注、非正式分类草案JSON导出。**ZIP中的HTML内嵌278538字节原始JPEG，不上传GitHub**，来源SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`。
- 新增独立导出草案校验器：来源JPEG与第81轮清单字节SHA、旧裁框、像素SHA、ROI边界和ID唯一性校验；未知ID、重复条目、篡改来源、越界ROI及伪造Accepted/永久ID全部失败关闭。审阅草案不能自动变成正式认证。
- 新增Chromium **about:blank** UI、标注、下载QA **18/18**；Python静态及负例 **24/24**；第81轮与此前14组历史QA复跑通过。尝试 `file://` 直接导航返回 `ERR_BLOCKED_BY_ADMINISTRATOR`，故真实离线文件导航记 **blocked**，不是通过。
- 累计第82轮ZIP **1181文件**，SHA256 `c1755737b727e6616538a0ade8eaf562fc4c76708aa9331ecf5fcd8a4d369796`；Python zipfile与系统unzip两份独立恢复各 **1181/1181** 文件SHA一致，两份均重新运行新旧QA且QA后SHA不变。ZIP本体在隔离交付工作区，**不在GitHub**。
- 无真实用户存储读写；冻结V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc` 与2008 JPEG原始SHA未改变；176编码和正式SVG未改变。
- 第10–12、35轮完整ZIP及第12轮20SVG仍缺；同源高清原图原始字节与合法分发许可未取得。K/E共享来源、B/V冲突、M四未绑定、36旧未匹配均未认证。
- **原始T01正式0/25键、真实缺根数未知；T02正式永久ID 0；原始T00–T11仍0/12 Accepted。** 真同源Web Locks/localStorage、Android/iOS真机与真实屏幕阅读器仍not-run。

下轮：优先在有合法来源的同源高清原图上对M/K/E/B/J/R/X/V逐笔复核；无原件不得用像素阈值或工作台草案替代认证。
