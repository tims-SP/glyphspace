# R233 · 原始 T03 · 退出校准后残留点击隔离（非正式验收）

GitHub main 起点 R232 `6d91b32dffcf979252caad5ffb3c4718949089ae`；实际父 ZIP SHA256 `b22ec8f6f711dcc651db624bbb8e1ab153babb2923ef39a2ac845cab05c0a1ca`，2926/2926 逐成员 SHA 一致。

**真实缺陷：** R232 的触屏在 V 字根上按下、`disarm()` 后才释放，Chromium 仍生成 click，五笔训练 `inputIndex` 从 0 变 1。390×844 DPR2 与 1280×800 DPR1 两个 CDP 触屏环境均复现。R232 仅在 `armed=true` 时拦截点击。

**隔离修复：** R233 控制器记录在 full/focus/mini 键盘内按下的指针 ID，disarm/dispose 时先安装短生命周期 click 捕获守卫，再取消光学事务；仅阻止已中止指针对应的残留 click，命中或两秒超时后卸载，下一次独立指针正常训练。R232 原文件、冻结 V0.35、176 编码、正式 SVG 和生产入口未修改。

**实际 QA：** 继承旧选定 220/220；新 Chromium 触摸/鼠标 62/62（含 R232 两视口缺陷复现 2/2，disarm/dispose、字根与键帽空白区及后续正常输入）；静态 25/25。合计选定 307/307。R233 独立累计 ZIP 2939 文件，SHA256 `f55de3d71259ea75488b1cf5f3593c420e3e55ae8179b8da07fd7a860059c4f6`；Python zipfile 与系统 unzip 双独立解压，分别 2939/2939 SHA、307/307 QA，QA 后 0 文件变化。首次合并恢复脚本超时，随后分离完成系统 unzip QA，超时未计通过。

**正式边界：** 仅 about:blank/CDP 触屏模拟，非真机。真实同源 Web Locks/localStorage 仍 blocked/not-run；真实读屏、高清原图逐笔、历史全量 QA 均 not-run。R11/R12/R35 原始 ZIP 与 R12 20 SVG 仍缺；T01 来源认证 0/25、T02 批准永久 ID 0、T03 未生产集成、T05 缺根数未知。原始 T00–T11 **0/12 Accepted**。用户原有 Storage 未触碰。回滚删除独立 `v036_round233/` 或恢复 R232 父 ZIP。
