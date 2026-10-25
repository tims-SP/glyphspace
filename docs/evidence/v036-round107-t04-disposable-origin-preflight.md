# V0.36 第107轮 · Root T04 独立真实原点执行路径（非正式验收）

- 日期：2026-10-25；工作轨道：Root T04（旧版存储与迁移），不替代T01/T02/T03前置正式验收。
- 父档案：R106 1439成员，SHA256 `55e96b14b2a969e33b7e6b9e39fa132d0836062bbbb4d3fe9104d044d2de26c0`；R107逐文件继承1439/1439。
- 新累计ZIP：1449成员，SHA256 `3b5c30e922a9f58de189aa817f9369e768e4fed81dc9fedbe34b93a8ad43df5b`。ZIP不在GitHub，不能将本页当作ZIP下载链接；Python zipfile与系统unzip独立解压各1449/1449，QA前后SHA均一致。
- 新增可执行`qa_t04_ephemeral_origin.py`（在外部ZIP内）：随机loopback端口、全新Chromium context、双标签、真实Web Locks/localStorage、跨标签storage事件、expectedHead拒绝、pending→record→head、崩溃恢复、回滚和记录篡改拒绝；仅写独立测试命名空间，不访问GlyphSpace生产站点或用户已有存储。
- 本地执行：访问临时127.0.0.1返回`ERR_BLOCKED_BY_ADMINISTRATOR`；真实事务**blocked/not-run，0 pass**。静态安全检查26/26；继承R77 Node 179/179、R105 Chromium about:blank 170/170在原工作区及双独立恢复目录通过。R106完整旧浏览器回归本轮尝试超时，不计pass。
- 新增[独立GitHub Actions临时原点烟测](../../.github/workflows/v036-t04-disposable-origin.yml)，仅验证托管runner中真实loopback原点、双标签localStorage共享及Web Locks互斥；**本页写入时远端运行结果尚未确认**。该workflow不是V0.35真实用户迁移，不能把其成功视为T04 Accepted。
- 冻结V0.35 HTML `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`，2008参考JPEG `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`；两者未修改。176旧编码、正式SVG、生产入口和用户localStorage未修改。
- 第10–12、35轮ZIP及第12轮20SVG仍缺；2008同源高清原始字节及分发许可未取得。T01 0/25正式认证，T02正式永久ID0，T03未正式集成，T05未正式补图，Android/iOS真机及真实读屏not-run；原始T00–T11仍**0/12 Accepted**。
- 后续：核验远端workflow结果；只有在授权隔离原点运行完整脚本并取得可审计日志后，才能把“真实原点预检”从blocked改为通过。随后仍需来源绑定的V0.35→V0.36真实迁移测试与安全回滚，不能触碰用户生产存储。
