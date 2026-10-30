# V0.36 R228 · Root T03 实际冻结V0.35运行时三视图光学校准隔离接入（非验收）

## 来源与父版
- 已读取main六份强制文档、AGENTS.md，确认起始R227提交 `060e73f51ee144a35add3a922c8947297bef1fbc`。
- 真读父R227累计ZIP：2863文件、SHA256 `2a86a5fcedcc29fcb93859f54611ca91589ea042fc1407327a50a4513fb11f1d`，继承2863/2863逐文件SHA一致。
- R228累计独立ZIP：2876文件、SHA256 `d9cd104fa5709a1a281d88bfda986e3088c0cced8e5b0383feee692e7197e1dd`；Python zipfile和系统unzip双独立恢复各2876/2876 SHA、3906/3906选定QA、QA后0文件变化。

## 实质变化
R224–R227使用构造的SVG演示视图；R228首次在**实际冻结V0.35完整应用**的完整键盘、动态焦点预览和折叠迷你键盘中测试隔离T03光学变换。新增不持久化的`live_v035_optical_preview_adapter.mjs`与派生独立单HTML预览；从真实V0.35的151可视根/156旧槽读取旧实例身份，M/V两项预览位移跨三视图一致，动态重绘/折叠后重新应用。真实输入「好」第一键状态前进，176旧编码不变；非法ID、过量位移、重复编辑、原始几何篡改被拒绝，第三视图setter失败可回滚，clear恢复原始transform。Chromium桌面1280×800及手机390×844共34/34断言；旧R227 3848/3848、静态24/24，合计3906/3906。

## 严格边界
- 浏览器是隔离`about:blank`加载完整冻结应用，并非真实安全共享原点；独立127.0.0.1 Chromium再次返回`ERR_BLOCKED_BY_ADMINISTRATOR`，Web Locks/localStorage **blocked/not-run**。
- 仅派生隔离预览，**不是正式T03生产集成**，没有认证参考字形或批准永久ID；冻结V0.35 HTML SHA `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`、2008 JPEG SHA `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`、176旧编码、正式SVG、生产入口及用户Storage均未修改。
- 原始T00–T11 **0/12 Accepted**；T01正式0/25，T02永久ID批准0，T05真实缺根未知；第11/12/35轮原ZIP及第12轮20SVG仍缺，合法高清原始字节/许可未获。真实读屏、Android/iOS真机、完整历史全量QA均**not-run**。

R228累计ZIP及报告由自动化会话附件交付，未将67MB累计包提交GitHub。后续仍须独立同源、正式T03集成与来源认证。
