# R234 · Root T01/T02：第三方高清候选原始字节独立复验（非认证）

日期：2026-10-30。起点：R233，GitHub main `2cda589395abe5e5c95f3678bffe02df7bb85b9c`。读取了原始规划、STATUS、机器任务账本、追踪表、验收规范、AGENTS及V0.35原问题矩阵。原始任务编号未变。

## 本轮新取得的原始字节证据

通过已授权GitHub连接器对 `06wb/06wb.github.io` 的 `master` 执行 `fetch_file(encoding=base64)`，真实读取路径 `Tutorials/第三代五笔字型（新世纪版）简体字根键位图高清版(官方).zip` 的996823个原始ZIP字节；不是复述R114日志。独立JavaScript解码并计算ZIP SHA256：`fb7a9984a84be12a71d71dc86088b8859762ca97cb9a3db173b4a8adaf0b9707`，与R114相同；Git blob SHA1 `92f37f92c7e7ab4eb0ba6fe084112d9a56cd2dc4`。解析中央目录，DEFLATE实际解压唯一成员 `zgjwt_jt_3508x2480.jpg`，得到1348865个JPEG原始字节，独立SHA256 `47c5d53f6cf57ac67c957c6510a3e2696072c3ce63e73024ed025367f31c600e`、CRC32 `e90cbe82`，JPEG SOF尺寸3508×2480。全部与R114远端记录一致。

新发现上游 `Tutorials/index.html` 的高清ZIP超链接使用全角括号 `（官方）.zip`，但仓库真实文件名为半角括号 `(官方).zip`；前者通过GitHub内容API返回404，后者成功。文件名中“官方”只是第三方声称，不能据此认证官方来源或权利。

上游 `LICENSE`、`LICENSE.md`、`COPYING`、`Tutorials/LICENSE` 均未取得明确许可文件。**原图再分发许可未确认，不能将该图片纳入公开仓库或累计ZIP。** 原始ZIP/JPEG仅在连接器内存中解码校验，没有持久化到本地、没有向用户发布原始图像，也没有进行逐笔图像复核。真实同源关系仍是先前ORB支持的同布局候选，非已证实逐笔同源。

## 可执行本地校验与恢复

新隔离目录 `v036_round234/` 含 `highres_quarantine_gate.py`，为在未来有授权、可读取原始ZIP的环境准备了ZIP SHA、JPEG SHA、CRC、尺寸、成员路径/压缩方法、大小上限及异常失败关闭校验。18/18合成ZIP/JPEG正负例通过，不可当真实高清逐笔QA。

R233父累计ZIP `f55de3d71259ea75488b1cf5f3593c420e3e55ae8179b8da07fd7a860059c4f6`：2939/2939文件SHA继承一致。R234累计ZIP 2947文件，SHA256 `dce2085e82a92c3b75830d710d681f39e49e3df25366680244de3d537b6a5b22`；Python zipfile和系统unzip独立恢复均2947/2947 SHA，分别运行R114旧来源QA31、R223旧25键原生审计QA668、R234新QA18，共717/717，QA后0字节变化。额外R233 Chromium选定套件307/307在父目录和Python恢复通过；系统unzip恢复中该递归浏览器套件超时，未计入双恢复717。完整历史全量QA未运行。

## 正式验收边界

T01正式25键来源认证0/25，T02批准永久ID0，T05真实缺根数未知，原始T00–T11 **0/12 Accepted**。T03仍未生产集成。真实同源Web Locks/localStorage blocked/not-run，真实Android/iOS、真实读屏、高清逐笔认证及历史全量QA not-run。第10轮原始ZIP此前已恢复；第11/12/35轮原始ZIP及第12轮20SVG仍缺。冻结V0.35 HTML SHA `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`、2008 JPEG SHA `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`、176旧编码、正式SVG、生产入口及用户原有Storage均未修改。

下一步：争取权属/使用许可与在隔离授权环境中持久化高清原始字节，逐笔复核M/K/E/B/J/R/X/V及36旧未匹配；不得因本轮字节校验升级来源认证或永久ID。
