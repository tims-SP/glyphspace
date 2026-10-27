# R169 · Root T03 · SHA来源签发三视图适配器（隔离、非验收）

- 父档案：R168累计ZIP 2083成员，SHA256 `3ca7a8f727bd28790816a96f6ecd342a946891203a40ddbdd55c4d4087625f0f`；2083/2083逐成员SHA继承。
- 新隔离源码：`v036_round169/source_issued_three_view_adapter.mjs`（保存在R169累计恢复包，不覆盖GitHub生产入口）。调用方只能提供R125固定SHA的R50 Path、R54 inkBBox、R53几何三份原始字节，不接受自造plan/registry；在第一个await前同步复制三份Uint8Array，避免调用方在异步SHA验证与JSON解析之间修改输入。通过R160/R162/R163连接151草案实例、25键和full/mini/focus三个100×100视图。输出detached DOM，非正式字根认证。
- 新增Node QA **17/17**；实际重跑选定旧QA **316/316**，合计**333/333**；完整历史全量QA **not-run**。
- R169累计ZIP **2094文件**，SHA256 `a428e4ae95cfc039b052c877b269211a8a226b2a96f4132d9fbf7713676181b5`；Python zipfile与系统unzip独立恢复各2094/2094 SHA、333/333 QA、QA后2094/2094 SHA一致。
- 真实Chromium独立临时profile访问localhost遭`net::ERR_BLOCKED_BY_ADMINISTRATOR`，真实共享原点Web Locks/localStorage迁移 **blocked/not-run**；真机与真实读屏 **not-run**。未触碰用户存储。
- 第10轮原始ZIP已恢复；第11、12、35轮原始ZIP及第12轮20个SVG仍缺；合法同源高清原图与逐笔认证未取得。T01正式0/25键、正式永久ID0、真实缺根数未知。
- 冻结V0.35 HTML、2008 JPEG、176旧编码、正式SVG及生产入口未修改。原始T00–T11仍**0/12 Accepted**，T03尚未生产集成。
