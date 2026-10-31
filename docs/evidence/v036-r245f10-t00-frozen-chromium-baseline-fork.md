# R245F10 · 原始T00冻结V0.35真实Chromium视觉与输入基线（独立分叉，非正式验收）

- 工作轨道：Root T00冻结基线；不涉及UI-01–UI-05，不将本轮视为T10真机验收。
- GitHub main核对：`03c29e0fcc4b968224b9fdf37bc6d45b54da6b97`，R246累计ZIP原始字节仍不可得，不能连续升级；本轮从已独立复验R245F9分叉。
- 父ZIP：`R245F9_isolated_R245F8_fork_T00_pinned_baseline_provenance.zip`，SHA256 `d3d81e594527f24703697f5626bb34f29964142ca8fe297061a5f4edbcfe0f21`，3128/3128逐文件继承SHA一致。
- 冻结V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`；2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`，均未修改。
- 实际Chromium版本144.0.7559.96。独立临时about:blank context，用原始冻结HTML字节通过set_content加载。仅测试上下文固定Math.random种子0x12345678，使随机练习起始状态可复现；未修改生产HTML，不访问真实用户profile、localStorage或生产域名。
- 桌面1280×800 DPR1 PNG SHA256 `5461d0d1999afed4a132d1a440a8f0b794e0a9bf9090d0e9741556c3a8d52168`（123077字节）。
- 手机竖屏390×844 DPR2 PNG SHA256 `12824c88fc47934eb6f0f488fbf7ae4fc4701457c7fd6f83c4a44566e5a479bb`（136572字节）。
- 手机横屏844×390 DPR2 PNG SHA256 `817c35dd84a47e773d17a1b745443c0fa4946b8b945104b3bb0eeacf646344c7`（136332字节）。
- 每个视口由两套独立context重新生成：PNG字节相同、DOM初始状态相同；26键、零文档滚动、无JS异常、1/20初始进度。三视口均实际键盘输入EEEE完成首题「月」，显示正确反馈。新增42/42浏览器断言。
- 父选定QA582/582 + R245F9 T00 SHA钉值10/10 + 新增42/42 = **634/634**选定QA。
- R245F10累计ZIP：3138文件，SHA256 `1953c645c8769afb1401a9fd29fac324a0f32a109d7af6e58c6eaa92f96273e6`。Python zipfile和系统unzip两次独立恢复各3138/3138 SHA、各634/634 QA、QA后0漂移。截图、QA脚本、原始报告和成员SHA清单在独立累计ZIP内或随包报告中，未将PNG提交到公开仓库。
- 首次测试将页面内部词法变量误当公开接口，30/33，已修正为DOM可见1/20进度后通过；补充真实键盘输入测试，最终42/42。失败尝试不计通过。
- **不等于**历史原始设备截图、真机、真实同源localStorage/Web Locks、真实读屏或合法同源高清原图逐笔认证。T00仍缺真实既有存储样本/原始历史设备截图来源及完整发布回归，accepted=false。
- R10原始ZIP已在累计包，R11/R12/R35原始ZIP及R12 20SVG仍缺。T01认证0/25，T02永久ID批准0，T05真实缺根未知，T00–T11仍0/12 Accepted。
- 未修改冻结HTML、2008 JPEG、176旧编码、正式SVG、生产入口或用户现有存储；完整历史全量QA、物理设备、读屏均not-run。

隔离累计ZIP根目录复验命令：

```bash
PYTHONDONTWRITEBYTECODE=1 python v036_r245f8/run_selected_qa.py .
PYTHONDONTWRITEBYTECODE=1 python v036_r245f9/verify_t00_pinned_freeze.py .
PYTHONDONTWRITEBYTECODE=1 python v036_r245f10/qa_t00_chromium_frozen_screenshots.py .
```

截图像素SHA与本次Chromium版本及隔离环境绑定；不同浏览器版本需重新独立审阅，不得静默替换历史证据。
