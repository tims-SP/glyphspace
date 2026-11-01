# R245F53 · Root T03 异步墨迹放置事务竞态修复（隔离候选，非验收）

日期：2026-11-02。原始任务编号 **T03**（100×100 SVG坐标内核、墨迹边界、锚点与光学校正）；并非UI-track T03/T05。

## 父版实证与本轮代码

- 已读取主线六份必读文档；main正式生产入口保持不动。
- 父R245F52累计ZIP SHA256 `f3f085c1aff16d7b4cb2d26d19aa3b662343a89e071636cc4cc27934085e6db5`；父成员3575/3575逐SHA继承。
- 真实Chromium在about:blank复现：父版`setPlacement()`等待Image/SVG解码时，`reset()`先执行，异步旧放置仍提交，重置后重新出现几何记录（stale=true、error=null）。
- R245F53使用每实例递增版本与全局reset epoch，后发放置、`reset`、`clearPlacement`、`setOptical`取消在途旧提交；`await`后再次检查SVG来源DOM，拒绝来源变化。
- 正常三视图放置、身份绑定、焦点切换、不同实例互不干扰。所有数据仅为151旧可视SVG和156个T02 planning_only草案；正式批准永久ID仍0。

## 可复验的QA与归档

- 新Chromium（真实SVG Image解码、about:blank）20/20；继承R245F52 217/217、R245F51 175/175、R245F50 348/348；选定合计 **760/760**。
- 累计ZIP SHA256 `ea7bbc4827073952068c26ca7a9f34e9dba74b0eb75830bc9e774f8049587bb0`；**3586成员**，新增11。
- Python zipfile和系统unzip两次独立恢复：各3586/3586逐SHA，父3575/3575继承，各760/760选定QA，QA后漂移0。
- 完整历史全量QA、真实同源Web Locks/localStorage、真实屏幕阅读器、Android/iOS物理设备：**not-run**。
- ZIP及逐成员SHA清单在对话独立附件中；GitHub仅保留可审计摘要，不公开第三方高清图或私有裁片。

## 正式验收边界

T00–T11仍0/12 Accepted；T01正式0/25键、T02批准ID0、T03正式inkBBox及生产集成未完成、T05缺根数未知。缺R11/R12/R35 ZIP、第12轮20SVG和R246主线累计ZIP；高清官方同源与再分发许可未确认。冻结V0.35 HTML、2008 JPEG、176旧编码、正式SVG、生产入口及用户Storage均未修改。

下一步：来源许可与逐笔身份认证（M/K优先），并推进T03正式inkBBox与生产集成；不能用隔离几何测试冒充正式验收。
