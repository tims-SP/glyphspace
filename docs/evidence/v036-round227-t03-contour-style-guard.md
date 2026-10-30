# V0.36 R227 · Root T03 SVG轮廓计算样式漂移守卫（隔离非验收）

## 来源、父版与不可变边界

- 已读取main六份强制文档与V0.35问题矩阵；R226 GitHub提交 `d25e92f5d5f0f52f0d17fc0973e7609810282c28`。
- R226父累计ZIP SHA256 `473f99c16734dff9948a526ab44894caa2132057143315eff8c12ecbcbf50799`，真实读取、解压并逐文件复验2849/2849 SHA一致。
- R227新隔离累计ZIP 2863文件，SHA256 `2a86a5fcedcc29fcb93859f54611ca91589ea042fc1407327a50a4513fb11f1d`；继承父版2849/2849成员SHA一致；Python和系统unzip独立恢复各2863/2863 SHA一致，恢复后各3848/3848选定QA通过，QA后0文件变化。
- 冻结V0.35 HTML、2008 JPEG、176旧编码、正式SVG、生产入口和用户原有Storage均未改动。

## 实质修复

R226的computed-style快照遗漏部分SVG笔画轮廓和绘制属性。真实Chromium about:blank对抗测试通过外部样式表单独修改stroke-linecap、stroke-linejoin、stroke-dasharray、stroke-dashoffset、stroke-miterlimit、fill-rule、clip-rule、shape-rendering、image-rendering、isolation、color-interpolation和marker-start，R226错误接受12/12。R227在旧快照上增加16个轮廓/栅格化相关计算样式属性，异步提交前重新验证，12/12均拒绝，原有DOM/路径/事务回滚逻辑保持。

真实Chromium对旧草案SVG施加仅stroke-dasharray变化，前后截图有3802个RGB像素差异；R226接受、R227拒绝。这证明外部CSS会改变实际绘制，不是官方2008参考图逐笔认证。

## QA

选定旧QA：R226三视图3718、R226样式对抗30、静态16，共3764/3764。新增：12类轮廓对抗61、真实截图像素5、静态18，共84/84。合计3848/3848。Python/unzip两套全新独立恢复均逐SHA且复跑3848/3848；完整历史全量QA未运行，递归R226套件尝试超时不计通过。

浏览器是独立Chromium `about:blank`，SHA256使用Python桥接，不是安全同源。另以独立临时profile访问127.0.0.1返回 `ERR_BLOCKED_BY_ADMINISTRATOR`，真实同源Web Locks/localStorage blocked/not-run。真实读屏、Android/iOS真机、高清原图许可与原始字节、逐笔复核均未完成。

## Root验收边界

原始T00–T11仍0/12 Accepted；T01正式认证0/25键，T02批准永久ID0，T03未生产集成，T05真实缺根数未知。第10轮原始ZIP此前R164恢复；第11、12、35轮原始ZIP和第12轮20SVG仍缺失。R227是T03隔离内核修复，不是UI-01~05，不改变原始任务编号。下一轮优先真实授权同源与合法高清来源，而不是继续把CSS防护视为字根认证。
