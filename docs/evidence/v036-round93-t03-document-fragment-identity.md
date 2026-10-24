# V0.36 第93轮 · Root T03 SVG片段ID来源完整性（隔离证据）

日期：2026-10-24。任务：原始T03（SVG 100×100坐标内核），非UI-01至UI-05。**非正式验收、非生产集成。**

## 可复现缺陷与修复

R92只校验可信 `svg.isolated-definitions defs > g` 的149个草案Path/属性及三视图 `<use href="#draft-...">` 的文本属性，却未检查整个文档中是否存在同名SVG fragment ID。Chromium实际复现：在可信定义之前插入同ID的伪造SVG `<g>`，`<use>.getBBox()` 从原字形包围盒变化为(0,0,100,100)，**R92 attest()仍错误返回true**。这会令已验证的Path属性与实际绘制的字形脱节。

R93隔离修复：在提交几何、切换键位与显式attest时，扫描 `ownerDocument` 内149个规范fragment ID，禁止任何重复ID，要求 `document.getElementById(id)` 严格等于可信defs中的规范节点；拒绝额外 `base[href]` 修改片段解析基准。未知、无关的文档ID不受影响。R92其他逐键成员、Path、描边、100×100 viewBox与transform门禁保留。

## 真实执行与来源

- 父第92轮ZIP SHA256：`cc737571ca35ee6f9b8adda7172954021868a8f3ee6019540fac70b1dad80953`，**1296/1296成员逐文件SHA继承一致**。
- 第93轮累计ZIP **1308文件**，SHA256 `ea618a9dffc1e03f5aad5affa63de7a13f1e5d0da75e4059ef5a7b31b8e57480`。ZIP原始字节仅在会话交付，不在GitHub。
- 新增Chromium Playwright `page.set_content` / `about:blank` 12/12；R92 29/29、R91 27/27；第77/78/83–90轮定向历史QA 10/10组。Python zipfile和系统unzip两次独立恢复各1308/1308，恢复后新旧QA及文件SHA均通过。
- 冻结V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`，2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`，176旧编码/正式SVG及用户存储未修改。

## 未满足的验收与历史缺口

T01正式0/25、真实缺根数未知；T02正式永久ID 0；T03仅隔离修复，生产未集成；T04真实同源Web Locks/localStorage blocked/not-run；T05正式补图未完成；Android/iOS真机及真实读屏not-run；T00–T11 **0/12 Accepted**。第10–12、35轮完整ZIP及第12轮20SVG仍缺失，不能宣称连续历史归档；同源高清合法原始图仍未取得。完整历史全量QA未执行，不能将定向十组称为全量。

回滚：删除隔离第93轮文件并使用经SHA复验的第92轮父包；冻结生产入口保持不变。
