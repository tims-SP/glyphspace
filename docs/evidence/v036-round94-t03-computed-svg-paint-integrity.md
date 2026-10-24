# V0.36 第94轮 · Root T03 SVG实际绘制完整性隔离修复（非正式验收）

- 日期：2026-10-24。原始任务 **T03=100×100 SVG坐标内核/inkBBox/锚点/光学校正**；非UI-01～05。
- 父ZIP：第93轮，SHA256 `ea618a9dffc1e03f5aad5affa63de7a13f1e5d0da75e4059ef5a7b31b8e57480`；真实读取1308文件，逐文件SHA **1308/1308**。
- **真实缺陷复现**：在第93轮Chromium隔离预览中，对可信 `<defs><g>` 添加 `transform="scale(2)"`，对应 `<use>.getBBox()` 宽度从82变为164，但第93轮 `attest()` 错误返回true；另以CSS将可信Path `opacity:0`，旧门禁也错误通过。
- **本轮修复**：隔离T03模块拒绝额外SVG group/path/use/view属性；绑定原始规范节点身份；校验Computed Style绘制属性和 `<use>` 实际computed transform与100×100几何矩阵一致；保留第93轮文档级fragment ID门禁。冻结正式入口、正式SVG及旧编码不变。
- **测试**：新Chromium `about:blank` 实际DOM/绘制 QA **18/18**；独立重新执行R91 **27/27**、R92 **29/29**、R93 **12/12**；第77/78/83/84/85/86/87/88/89/90轮定向旧QA **10/10组**。两套独立恢复环境均重新执行上述QA，恢复前后各 **1319/1319** 文件SHA一致。
- 第94轮累计ZIP（不在GitHub）：**1319文件**；SHA256 `2dcbc8880ab8adde82a8693c5c05f163d81c1476763a10d57d925d4a296df4fc`。父包1308/1308继承。首次双恢复组合测试超时，随后在系统unzip恢复环境单独重跑全部QA通过；不能把超时记为成功。
- **限制**：初始CSS是隔离预览信任前提，恶意预加载CSS、真实像素逐笔认证、生产集成均未通过；没有真实同源Web Locks/localStorage、真机、真实屏幕阅读器测试。完整仓库 `scripts/verify_repo.py` 未在本轮本地运行。
- 2008原始JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`；冻结V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`；本轮均核验字节不变。
- 第10–12、35轮完整历史包及第12轮20SVG仍缺失；K/E/M/B/J/R/X/V及36旧未匹配、同源高清原图许可均未解决。**T01 0/25，T02正式永久ID 0，T03仍隔离未集成，T00–T11正式Accepted 0/12**。
