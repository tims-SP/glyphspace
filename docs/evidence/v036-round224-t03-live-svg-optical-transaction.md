# R224 · Root T03：151旧Path三视图实时SVG光学校准事务（隔离，非验收）

执行日期：2026-10-30。轨道：**原始Root T03**（100×100 / inkBBox / anchor / optical），不是UI-01–UI-05。

## 真实实现
基于R198 SHA绑定的R125/R160 151项冻结旧Path草案，新增隔离模块 `v036_round224/live_svg_optical_transaction.mjs`。真实Chromium about:blank挂载25键×full/mini/focus=75个SVG，453个g节点和459个path节点；对M、V两个旧草案身份原位更新光学偏移，共6个g transform改变，保留453/453 DOM节点身份、453/453 Path序列化和当前焦点。失败关闭：在第三视图注入setAttribute失败时撤销前两视图写入，453/453变换恢复；Path被篡改和超出100×100的光学几何被拒绝。

浏览器运行在不安全的about:blank隔离上下文，`crypto.subtle`不可用，SHA-256验证委托Python hashlib；因此**不能冒充真实安全同源WebCrypto/Web Locks/localStorage**。尝试https://glyphspace.test及127.0.0.1真实导航仍被管理员策略阻断。

## 可复核累计证据
- 父R223累计ZIP SHA256 `066942bc8b32f55f9c4f76d8445ff8527b2c8ce1297597b7defacabdb98f767b`，**2812/2812**逐文件SHA继承一致。
- 旧QA选定**1701/1701**；Chromium **7个场景组、3718/3718细粒度断言**；新增静态**14/14**；总选定**5433/5433断言**。场景组数与断言数不能混用为独立测试数。
- R224累计独立ZIP：**2821成员**，SHA256 `a325e9beed8ea8e678f4057589168e8ece0596134845ff0f60201328ac353e72`。Python与系统unzip两套独立恢复均2821/2821 SHA一致、各5433/5433选定QA、QA后文件变化0。首次合并双恢复任务超时，第二套QA独立重跑后通过。
- 历史完整全量QA：**not-run**。真实同源：**blocked**。Android/iOS真机、真实读屏：**not-run**。
- 参考图正式认证0/25；批准永久ID0；真实缺根数未知；原始T00–T11 **0/12 Accepted**。
- 第10轮原始ZIP先前已恢复；第11、12、35轮原始ZIP及第12轮20SVG未恢复。3508×2480同源高清原始字节及许可未获。

## 不变项
冻结V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`，2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`，176旧编码、正式SVG、生产入口、用户存储均未修改。新增仅是隔离DOM事务预集成，不等于生产T03正式集成，更不是来源逐笔认证。

下一步：独立授权profile内真实同源存储/锁回滚验证，继续M四微框与E/K、B/J/R/X/V来源认证。全部12项原始任务逐项独立Accepted前持续推进。
