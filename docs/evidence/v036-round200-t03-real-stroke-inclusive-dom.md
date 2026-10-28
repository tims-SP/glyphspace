# R200 · 原始 Root T03：真实 Chromium 含描边 inkBBox 隔离几何模块（非验收）

日期：2026-10-29。原始 T03 为 SVG 坐标内核（100×100、inkBBox、锚点、光学校正），不属于 UI-01–UI-05。

## 实际来源与修正

已真实读取 R199 累计 ZIP（2508 文件），SHA256 `8b0987baef9181773b01a3189e24effbc1842b7eb570bbd48e20e569bb584ff7`；逐成员 SHA 2508/2508 与解压一致。GitHub main 读取强制六文档，起点提交 `4e12d9810f833912ad5c875dddb70b088d50ad0c`。

R199 的 `wb06/H/legacy-07` 浏览器 `getBBox()` 与解析式 `inkBBox` 差 0.90434345 键帽单位，因 Chromium 默认不计描边。R200 新增独立 `v036_round200/stroke_aware_ink_dom.mjs`：基于真实浏览器 path.getBBox 与 getScreenCTM，按圆头/圆角 strokeWidth 计算保守墨迹边界；未知 CSS 覆盖、虚线、miter、非均匀变换等失败关闭。不改变冻结旧 Path。模块源码、测试和完整证据在 R200 累计 ZIP 内，尚未生产集成。

真实 Chromium `about:blank` 检查 151 草案实例×3 视图×2 状态，共 906 实例组、918 Path，含描边墨迹边界与来源绑定解析式的最大差 `0.000003706074` 键帽单位；H:7 六次实例检查涵盖每次三条描边 Path。六种不支持/对抗 paint 改动均被拒绝。新 Chromium 18/18，新增静态 18/18，实跑选定旧 QA 1001/1001，总计 **1037/1037**；完整历史全量 QA not-run。

## 累计与恢复

R200 累计 ZIP `R200_cumulative_isolated_T03_real_stroke_aware_ink_bbox.zip`：**2520 文件**（继承 2508/2508 SHA、新增 12），SHA256 `2940c4c28686599858acffb5c19fda47ce25605a8175fdfc7b4ed0c63beaba9d`。Python zipfile 与系统 unzip 双独立解压各 2520/2520 SHA，通过各自 1037/1037 选定新旧 QA，QA 后逐文件 SHA 不变。完整机器审计见 ZIP 内 `v036_round200/R200_*` 及包外恢复记录。

## 验收边界与安全

**T00–T11 仍 0/12 Accepted。** T01 正式来源 0/25、T02 永久 ID 批准 0、T03 未生产集成、T04 正式迁移未验收、T05 缺根未知。真实共享原点 Web Locks/localStorage、本轮 Android/iOS 真机、真实读屏均 **not-run**；`about:blank` 不冒充同源。保守含 stroke 包围盒不等于原图逐笔/身份认证。

第10轮原始 ZIP 已恢复；第11/12/35轮 ZIP 及第12轮20 SVG仍缺。同源高清 JPEG 合法原始字节本轮未取得。冻结 V0.35 HTML `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc` 与2008 JPEG `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49` 复核一致；176旧编码、正式SVG、生产入口及用户原有存储未修改。

下一步优先 T01/T02 的 M/V/K/E、B/J/R/X、36 旧未匹配来源形态与永久身份；T03 正式集成需等待身份、来源和回滚门槛。
