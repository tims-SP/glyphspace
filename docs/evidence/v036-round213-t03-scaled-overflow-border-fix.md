# V0.36 R213 · Root T03 · 缩放祖先裁剪边界修复（隔离、非正式验收）

## 真实缺陷
R212 将 CSS computed border-width（布局坐标）直接从 getBoundingClientRect（屏幕坐标）扣除。真实 Chromium about:blank：overflow:hidden、CSS 40×50、10px border、scale(.5) 时截图实际黑色像素 500 个，真实屏幕范围 x=105..125、y=105..130；R212 错误报告 x=110..120、y=110..125，**遗漏真实可见像素，违反上界语义**。scale(2) 时旧报告 90×110，新报告 80×100（截图8000像素）。scale(.25) 旧结果可能为 null，但实际截图108个黑像素。

## 隔离修复
新增累计包 `v036_round213/scaled_overflow_ink_envelope.mjs`：用 CSS subpixel used width/height 与 border/padding/box-sizing 还原未缩放 border-box，并以 getBoundingClientRect 比值将 border 转成屏幕坐标；拒绝旋转/倾斜/负缩放、透视、未经验证的 CSS zoom 与不可测盒子。嵌套抵消旋转时仍失败关闭。原 `inkBBox` 保持不变，单独输出 `visibleInkUpperBoundBBox`，仍只表示**保守矩形上界**，不是精确像素墨迹边界。

## 实际验证与档案
- 父 R212 ZIP SHA256：`4f4fd0283aa87dba0f95224c5e6afc5a11ca67b048ab8c263be5e79ce9e296ae`；实际 2675/2675 文件 SHA 与父清单及解压一致。
- R213 新 Chromium 28/28，静态16/16；实际重跑旧 R197/R198/R210/R211/R212 选定159/159；合计 **203/203**。旧151个实例×三视图×编辑前后共906组正常几何一致。
- R213 累计ZIP **2688文件**，SHA256 `5907af02850e0084528b3082f6524e9fd8750d20a88ecbcf9eeae7fb5aee7089`；Python zipfile 与系统 unzip 双独立恢复各2688/2688 SHA及203/203 QA，QA后文件SHA变化0。
- 冻结 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`、2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49` 均核对；176旧编码、正式SVG、生产入口及用户Storage未动。
- 原始 R11/R12/R35 ZIP 与 R12 20SVG 在本轮检索范围未恢复；R10有R164历史证据，不宣称完整历史链。合法同源高清原始字节及许可未取得。

## 验收边界
**原始 T00–T11 仍0/12 Accepted**，T03未集成；T01正式来源认证0/25，T02批准永久ID0，T05缺根数未知。真实同源Web Locks/localStorage仍blocked/not-run，Android/iOS真机、真实屏幕阅读器、完整历史全量QA及逐笔来源认证not-run。R211递归670测试历史超时，不计本轮通过。圆角/遮挡/SVG内部裁剪未获精确像素保证，禁止据此发布。

本轮只在独立累计ZIP中新增 R213 文件，父成员逐SHA原样继承，删除 R213 目录即可回滚。原始任务编号不变，UI-01..UI-05不计入Root验收。
