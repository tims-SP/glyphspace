# V0.36 第136轮 · Root T03 私有SHA验证渲染入口（隔离，非验收）

日期：2026-10-26。原始任务：**T03 SVG坐标内核**，关联T09三视图；非UI-01～UI-05。冻结V0.35正式入口未修改。

## 发现与实现

R134 `GlyphSpaceR134.mountView`在SHA验证后仍接受原manifest嵌套篡改；R135的`GlyphSpaceR135.mountView`虽要求深冻结，却无法阻止同页面直接调用仍公开的R134入口。本轮不修改R132–R135历史代码，而是将它们的原始脚本封装在词法私有的`privateGlobal`中，只公开`GlyphSpaceR136.mountVerified(raw, sha, view, ids)`。页面若预先存在R132–R136任一公开旧API则失败关闭，防止错误混合加载。SHA原始字节验证、深冻结、三视图挂载全部在不可直接访问的私有闭包内完成。此设计不等于DOM不可被宿主脚本改写，也不等于生产集成。

## 真实测试

- Chromium 144.0.7559.96，独立`about:blank`上下文：151旧可视字根×full/mini/focus = 453 SVG，453/453 symbol ID唯一；151/151实例身份跨三视图一致；所有viewBox为100×100，`sourceCertified=false`、`productionReady=false`。
- SHA错误、原始JSON伪认证篡改、未知/重复instanceId、无SHA、错误视图均拒绝；预置R134公开入口时R136失败关闭，保留原入口不覆盖。
- 新QA **20/20**。本轮实际重跑继承R132 **21/21**、R133 **12/12**、R134 **10/10**、R135 **14/14**，合计每套**77/77**。旧R135用例仍有意复现旧R134入口缺陷，不得将其误称为旧接口修复。
- 父R135 ZIP SHA256 `dbc54639aa409d773aa39316c91bad1fe040b9ae6756d6413fb7ed1c67072c43`，**1760/1760**逐文件SHA继承；新增8文件。R136累计ZIP **1768**文件，SHA256 `a60486ed2af060f774450669d6c81e3ad99edab089a46f62b33d9144470d3806`。Python zipfile和系统unzip两次独立恢复均**1768/1768** SHA一致、各**77/77** QA、QA后SHA仍1768/1768一致。
- 冻结HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`；2008原图 SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`，均实际复核不变。176编码、历史正式SVG及用户localStorage未写入。

## 不得升级的状态

**T00–T11仍0/12 Accepted；T01正式0/25；T02正式永久ID0；T03仅隔离，T05未完成。** 第10–12、35轮原始ZIP与第12轮20 SVG仍缺，历史链不完整。高清同源原始字节及许可、逐笔来源认证、真实同源Web Locks/localStorage迁移、Android/iOS真机、真实读屏均未验收；完整历史全量QA和本轮仓库全量verify_repo均not-run。冻结生产入口保持不动。累计ZIP仅为隔离技术证据，不能替代正式字根认证或发布。

下一步：先消除T01/T02来源身份阻断，确认T03集成前提；如需接入生产，必须明确禁用所有旧公开API、验证宿主DOM和状态机，并完成正式依赖验收。
