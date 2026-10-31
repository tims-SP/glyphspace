# R245F15 · 原始 T03：活体三视图 DOM 预检与校准持久化隔离（非验收）

本轮从独立R245F14累计ZIP **3181/3181成员SHA一致**的真实父字节推进。父ZIP SHA256：`4354ed408d6b4b10ea245504cabef8e58b84cddc93a89e372511440bed1b8be8`。

## 实际复现

Chromium about:blank中，先修改完整键盘SVG Path为`M0 0 L1 1`，再执行M键合法X坐标13→14。R245F14仍写入隔离Storage且保留X=14，随后`GlyphSpaceR245F12.inspect()`报告`candidate contour drift: Q:0`。因此此前的inkBBox预检不能阻止已有活体DOM损坏时错误保存。

R245F15独立单HTML候选新增`commitCalibTransaction`：先检查当前full/focus/mini三视图，再验证投影坐标，更新并重新检查三视图，最后才写Storage；异常时回滚内存坐标且不覆盖已保存值。滑块、JSON导入、单键重置统一走该入口。候选只用独立内存Storage，未触碰用户真实localStorage。

## 独立验证

- 新Chromium真实复现与回归：**37/37**，三模拟视口1280×800 DPR1、390×844 DPR2、844×390 DPR2。
- 继承定向旧QA实际重跑：**771/771**，包含核心592、R245F10 42、R245F11 46、R245F12 51、R245F14 40。
- **本轮选定808/808**，Python zipfile与系统unzip各自独立恢复**3194/3194**成员SHA，恢复后各808/808 QA，QA后0文件漂移。
- R245F13原有151实例穷举浏览器套件本轮超时（>240秒），**不计入通过**；完整历史全量QA not-run。
- 累计ZIP SHA256：`abd45644160fc933bb7a1b83e9a16bb94e5932e6ba8ed012e6302785ab7b1a60`。本轮源代码、脚本、报告、逐成员SHA清单和双恢复QA在独立累计ZIP中。

## 验收边界与下一步

GitHub main仍为R246（`03c29e0fcc4b968224b9fdf37bc6d45b54da6b97`），其3054成员累计ZIP的原始字节未取得，故**没有升级主线基线**。R11/R12/R35原始ZIP及R12的20SVG仍缺；R10原始ZIP SHA `6a1552b45cfa3512d9fea2ab06df740a6adbb4b598369cd3ea8e214fee1c0ed0`已在父包复验。2008参考JPEG SHA `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`；同源高清原图合法原始字节尚未取得。

T01正式来源认证0/25键、T02正式批准ID0、T05真实缺根未知、**原始T00–T11 0/12 Accepted**。T03仍是隔离候选，未替换生产单HTML。真实同源Web Locks/localStorage、真实读屏、Android/iOS物理设备not-run。冻结V0.35 HTML SHA `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`、176旧编码、历史SVG、用户Storage未动。

下一步优先恢复R246原始ZIP、R11/R12/R35历史包及R12 20SVG，并获取合法同源高清参考图逐笔复核K/E/B/J/R/X/V及36旧未匹配；T03候选不得绕过T01/T02/T04依赖直接正式发布。
