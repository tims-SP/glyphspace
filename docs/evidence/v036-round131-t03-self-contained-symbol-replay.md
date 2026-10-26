# V0.36 第131轮 · T03自包含SVG符号依赖与绘制回放稳定性（隔离，非验收）

- 工作轨道：原始Root T03（100×100 SVG坐标内核），关联T07碰撞；不属于UI-01–05。
- 冻结V0.35 HTML SHA256：`fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`。2008参考JPEG SHA256：`df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`。
- 第130轮父ZIP：1712文件，SHA256 `e7d0d0fda95ca938cba1e49359ce3507356e6c65a9cb25d383c0a3cede7c0bb3`；实际逐文件继承1712/1712一致。
- 问题：第129轮诊断从真实DOM克隆`<use href="#wb17-…">`字根，却未在隔离SVG中携带其原始`<symbol>`定义；第130轮曾记录L:1、J:4首次渲染像素差异。**这是可验证的跨SVG依赖缺口，不是已经证明的唯一根因。**
- 本轮隔离实现：`v036_round131/stable_svg_paint_isolation.py`将原生symbol复制到本地`<defs>`并重映射唯一`href`，禁止悬空引用；不修改冻结HTML、正式SVG或用户存储。
- 实测：独立Chromium about:blank，2个browser context，每个11组字根/徽记（含2阴性对照）、400/800px、4绘制模式，合计176次渲染；396项字段与第129轮冻结审计一致，0差异。两个独立解压环境分别再次执行相同Chromium验证；新静态守卫各50/50、精选旧QA各282/282。
- 父树曾运行第130轮精选旧QA505/505；另尝试第129轮完整953项和候选恢复的第130轮505项，因执行超时**未完成、不计入通过**；历史全量QA not-run。
- 第131轮累计ZIP：1722文件，SHA256 `f67fed7b5d62d01cf1d50336c66451aefcdfa46c429bcbeec6cbdfc3ce077549`。Python/unzip最终双独立解压各1722/1722 SHA一致，各另跑104/104静态/来源QA；详情见ZIP内`v036_round131`及ZIP外`R131_final_ZIP_dual_restore.json`。
- 边界：不能宣称跨平台稳定、真实同源迁移、源图逐笔认证或T03生产集成。T00–T11仍0/12 Accepted；T01 0/25，正式永久ID0，T05未完成。R10–12/R35 ZIP和R12 20SVG仍缺失；高清原图许可、Android/iOS真机、真实读屏与真实Web Locks/localStorage均未完成。
- 回滚：删除隔离`v036_round131`文件及本证据即可；冻结V0.35、2008 JPEG、176编码、正式SVG及用户原有存储未修改。
