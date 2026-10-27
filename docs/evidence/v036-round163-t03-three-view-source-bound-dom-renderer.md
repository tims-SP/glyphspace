# V0.36 R163 · Root T03 三视图来源绑定DOM绘制预集成（隔离、非验收）

日期：2026-10-27。原始工作包 **T03 SVG坐标内核**，关联T09三视图回归；不属于第36–40轮UI-track的UI-01至UI-05正式验收。

## 实际实现
- 基于R162从真实冻结SVG Path字节SHA绑定的151实例绘制计划，新增 `v036_round163/draft_three_view_dom_adapter.mjs`；`full/mini/focus`外部尺寸分别100/48/160 CSS px，内部保持同一 `viewBox="0 0 100 100"`、instanceId、Path、变换矩阵及解析式inkBBox。
- 适配器仅返回 detached DocumentFragment，使用 `createElementNS` 和 `setAttribute`，不使用 `innerHTML`，不读写localStorage，不触碰冻结入口。
- 对151个实例一次性自有数据属性快照，拒绝动态getter、重复ID、非法几何与绘制参数、伪造认证状态。**适配器自身不验证任意JSON的来源**；调用者须先通过R162的源SHA绑定计划，不能将此视为生产信任边界。
- 实际Chromium about:blank（DPR1、DPR2）三视图6组，每组151 SVG/153 Path、150项填充DOM解析式BBox比较及26项真实alpha栅格采样；合计900 DOM比较、156栅格采样，6/6通过。最大边缘误差：DPR1 full 1.06158、mini 0.984、focus 0.92576 CSS px；DPR2 full 0.46、mini 0.50956、focus 0.48 CSS px。此为SVG内部一致性，不是与2008参考图逐笔比对。

## 继承与独立复验
- 父R162 ZIP：2028文件，SHA256 `bb5a007aed51cba3ff5b9391eca3d9bd9c21b7f3d64cf91db3f06a5bcecbcd96`；**2028/2028逐文件SHA继承**。
- R163累计ZIP：**2039文件**，SHA256 `4a20d2335cb9f0fd557dd86d3a7b533d15a284467f3c42dd54fe97b0be56efc0`。
- 新增Node 20/20，新增真实Chromium 6/6组，继承选定QA 2117/2117，合计**2143/2143定向QA**。
- Python zipfile独立解压2039/2039 SHA、2143/2143 QA、QA后2039/2039 SHA；系统unzip独立解压2039/2039 SHA、2143/2143 QA、QA后2039/2039 SHA。
- 完整历史全量QA **not-run**。真实共享原点Web Locks/localStorage本轮 **not-run**；Android/iOS真机及真实屏幕阅读器 **not-run**。
- R10–12/R35原始ZIP、R12 20 SVG仍缺失，不能声明连续历史恢复。合法同源高清原图、逐笔/来源授权仍未完成。

## 验收与不变量
T00–T11仍**0/12 Accepted**；T01正式0/25键、T02正式永久ID0、T03未生产集成、T04真实用户迁移未验收、T05真实缺根数未知。冻结V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`、2008参考JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`均复验一致；176旧编码、正式SVG、用户原有存储未修改。公开仓库仅上传文字证据，私有来源JPEG和累计ZIP保留在隔离交付包中。

回滚：删除R163隔离新增目录并使用SHA锁定R162父ZIP恢复；不修改生产入口。
