# R211 · Root T03 · HTML祖先绘制抑制守卫（隔离非验收）

日期：2026-10-29。原始任务：**T03 SVG坐标内核**；不是第36–40轮UI-03/UI-05，也不是正式字根认证。

## 真实缺陷与修复

R210的`inspectEffectivePaintInk`只检查SVG组至SVG元素的祖先，未检查SVG外部HTML祖先。实际Chromium about:blank中，外层div的`opacity:0`、`clip-path`、mask等使可见墨迹消失/改变，但R210仍返回非空inkBBox。截图黑色像素正常3200，外层opacity=0为0，外层全裁剪为0。

新增隔离模块`v036_round211/outer_html_paint_gate.mjs`，沿SVG外部HTML祖先到documentElement执行computed-style失败关闭检查：隐藏/透明、clip-path、filter、mask、content-visibility、overflow、paint containment、mix-blend-mode。原R200/R210源代码保持字节不变；不读取或写入用户存储。

## 真实验证与档案

- 父R210累计ZIP：2651/2651逐文件SHA继承，ZIP SHA256 `12e329603696bd85991666c222e14f68124c920a8fb9effa2331661923433449`。
- Chromium正常906组SVG几何完全一致；11组HTML祖先反例全部被新守卫拒绝，其中9组旧R210误接受；stylesheet !important opacity同样拒绝。
- 本轮实际重跑选定旧QA 644/644、新Chromium 14/14、新静态12/12，合计**670/670**；不代表历史全量。
- R211独立累计ZIP：2663文件，SHA256 `ddc0127fe6317f1c9f336b00069766f5b1ea2ff5178be2e328024d4036a99739`；Python zipfile与系统unzip各2663/2663 SHA，各670/670恢复后QA，QA后0字节变化。ZIP交付于会话附件，不存GitHub。
- 只读静态仓库`scripts/verify_repo.py`未在本轮完整克隆上执行；不得声明仓库完整CI已通过。

## 认证边界

T03仍为隔离原型、未生产集成。保守守卫会拒绝部分合法HTML裁剪/滚动布局，后续须做裁剪感知内核后再考虑生产使用。T01正式来源0/25、T02永久ID批准0、真实缺根数未知，原始T00–T11 **0/12 Accepted**。同源高清合法原始字节未取得；R11/R12/R35原始ZIP和R12 20SVG仍缺。真实同源Web Locks/localStorage blocked/not-run，真机、真实读屏、完整历史QA not-run。冻结V0.35 HTML、2008 JPEG、176编码、正式SVG、生产入口、用户Storage均未修改。
