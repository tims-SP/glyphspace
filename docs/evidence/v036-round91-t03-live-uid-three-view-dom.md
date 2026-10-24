# V0.36 第91轮：原始T03候选UID几何→真实SVG三视图DOM隔离闭环（非验收）

> 2026-10-24。Root T03（100×100、inkBBox、五锚点、光学校正），不属于UI-01–05。完整源码/QA/累计ZIP在外部工作区；ZIP原始字节不在GitHub。

## 本轮实质实现

第64/66轮冻结草案三视图SVG渲染与第77/78轮候选UID几何/锚点/光学校正内存编辑首次在**真实Chromium SVG DOM**贯通。R78先校验R63的151条Path、R73候选UID及R67/R70来源门禁；再将同一候选UID的transform同步写入full/mini/single三种SVG `<use>`。25键均使用100×100 viewBox，焦点键切换后恢复编辑。支持内存导入/导出、撤销和整批失败关闭；拒绝未知UID、旧槽别名、重复编辑、越界墨迹及认证/发布字段提升。

固定浏览器模型SHA256 `c82543497f2b21ca625b03c6d67be63f33cc42892cb03c91592ca063e9049603`；隔离HTML SHA256 `2fe153642fcd3eea58eaab73f366e6a3edd84f5c2a2e9efc54eae63dbd335965`。仅151旧可视候选参与渲染；5关联及4个M未绑定影子观察不可渲染。149草案资产不是正式SVG认证资产。

## 实际QA和恢复

Chromium headless Playwright `about:blank/page.set_content` 新真实DOM QA **27/27**；覆盖UID一致性、SVG getBBox非空、三视图transform同步、锚点/光学校正、焦点切换、导入导出、失败回滚与禁止认证升级。R77/R78/R83–R90 **10组**旧定向QA重新执行通过；未执行所有历史轮次完整QA。

父第90轮ZIP SHA256 `7e694c91b8f424390314ea7e92c3c7819536a14551290cc7ad95fba8aa1d52f2`，1270/1270成员SHA继承一致。第91轮累计ZIP **1283文件**，SHA256 `b15be0b2c893ae448b7a80b59939098029c7c89ae3e149744690f1a6669367c3`；Python zipfile及系统unzip两次独立解压各1283/1283，两份恢复环境重跑新27项和十组旧QA，QA前后1283/1283逐文件SHA一致。

## 不得提升的状态

仅隔离真实DOM技术集成，非生产T03正式集成、非原图逐笔认证。真实同源Web Locks/localStorage blocked/not-run；Android/iOS真机与真实读屏not-run。缺第10–12、35轮ZIP及第12轮20SVG，合法同源高清原图未获。T01正式0/25、T02正式永久ID0、T00–T11 **0/12 Accepted**。冻结V0.35 HTML、2008原图、176编码、正式SVG和用户存储未修改。
