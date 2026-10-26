# V0.36 第150轮 · Root T04 旧v16来源别名只读影子计划（非验收）

## 来源及已独立确认的远端结果

- 执行前GitHub main HEAD为R149 `afb03cd44b34fdf5de26051264ed3b734a844077`。R149授权临时127.0.0.1真实Chromium [run 40384582893](https://github.com/tims-SP/glyphspace/actions/runs/40384582893)已完成成功；独立下载的artifact 12679858834 ZIP SHA256 `3fc0a1faca5975ee03eaa39d7db77effe023f104377c37259babb359c229f087`；JSON分别显示旧同源33/33、严格v16来源27/27 pass。此为合成数据，不能推断正式迁移。
- R150父R149累计ZIP SHA256 `a8f88dfbf54380e848c6610525d3272e9aeda69745f07247c707fe5635256259`，1881/1881文件SHA继承。R150新累计ZIP 1892文件，SHA256 `51396c322a4a4ac7bd47b3aefb3b8bdcf8c7797b72dc353c1b9763f4a0d31d09`；Python zipfile与系统unzip双独立恢复各1892/1892文件SHA，旧定向1628/1628 + 新Node 25/25 = 1653/1653 QA；QA后1892/1892 SHA不变。完整历史全量QA not-run。
- 冻结V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`、2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49` 均复验一致。

## 实质代码与边界

隔离新增 `scripts/v036_r150_alias_plan.js`（与累计ZIP同字节，SHA256 `e4a07125641bf837d68f03ddebd99feebd1a77aa9b1897cc503166c7c03ef159`），复用R148严格只读v16来源校验，构造SHA绑定、递归冻结、排序稳定的源槽别名影子计划。核对25键156旧默认槽、来源key存在性、逐槽别名完整且无重复、用户显式坐标修改及sourceSHA；拒绝任何未经批准的永久ID绑定；没有apply/commit/write操作。G/K/X三键合成局部数据的22个缺席键不伪装成原始来源，草案槽别名绝不宣称正式instanceId。

- 本地Node 22 + FakeStore/WebCrypto新增25/25；R150本地真实同源仍 `ERR_BLOCKED_BY_ADMINISTRATOR` = blocked。R150远端新真实同源CI待确认，未计通过。
- 原始T00–T11保持0/12 Accepted；T01 0/25正式认证，T02正式永久ID0，T03未生产集成，T04生产V0.35→V0.36迁移未执行，T05未完成。
- 缺第10–12、35轮原始ZIP及第12轮20SVG；合法同源高清原图许可/逐笔归属、真实Android/iOS与屏幕阅读器QA仍未完成。冻结入口、176编码、历史正式SVG和用户存储未修改。

## 回滚

移除R150隔离脚本、CI测试和文档，不需对用户localStorage或冻结生产入口进行任何写入或恢复。正式ID及来源认证前严禁执行生产迁移。
