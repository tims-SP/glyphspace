# R245F61 · Root T01/T02 高清来源裁框重叠像素归属隔离（非正式认证）

## 基线与执行
- 主线main: `03c29e0fcc4b968224b9fdf37bc6d45b54da6b97`；隔离分支从R245F60提交 `5f34fe58a13d20d1e5b9d034ffd53406f7d0556d` 继承，**未合并生产**。
- 父ZIP R245F60 SHA256 `2ef2058f68b3b51332028c64b66b95b9b1f7e8126829209e11778b7c24bfa8f6`，3691/3691成员逐SHA一致。
- R245F57来源注册表：161个物理裁框、25键；R245F59 53张审阅案件；草案候选166（其中156旧实例），批准永久ID0。
- 对全部161裁框成对比较，B/E/J/V/X共10对**同键不同物理裁框**具有正面积重叠；20个有向裁框入口均在R245F60真实Chromium about:blank中错误接受交叉来源描记JSON。
- R245F61新增保守重叠区域禁入：真实pointerdown/pointermove/结束提交、JSON导入/导出均拒绝共享区域或穿越该区域的线段，保留正常M草案描记；没有更改源裁框或正式SVG。

## 可复验交付
- 完整累计ZIP：`R245F61_isolated_R245F60_fork_T02_overlap_ownership_guard.zip`，**3704成员**，SHA256 `93bfa399703ec9df57aba54c1fc38a429a700b49f3542d0f44aa48fb136e2e48`。
- 新Chromium QA 53/53，继承选定QA直接运行新版HTML 117/117，共170/170。
- Python zipfile与系统unzip在两个独立目录恢复：各3704/3704 SHA、3691/3691父成员SHA、170/170 QA，QA后0漂移。
- ZIP内 `v036_r245f61/R245F61_overlap_ownership_audit.json`、`R245F61_browser_QA.json`、`R245F61_parent_3691_member_SHA256.json`、HTML、Python QA、恢复说明可复验。
- 这里GitHub同步**文档证据**；完整隔离HTML/QA/ZIP未提交到公开仓库。

## 不可替代的正式验收
- 交叉裁框阻断仅消除工具级错误，不证明笔画属于哪个形态。K:2/K:3共享同一裁框的身份冲突仍未裁定；M四个独立形态仍待合法同源逐笔认证。
- 高分辨率原图的许可、官方同源、逐笔归属，真实用户Storage迁移、屏幕阅读器、Android/iOS真机及完整历史全量QA均**not-run / not-certified**。
- 第11–12、35轮原始ZIP与第12轮20SVG未恢复；R246主线累计ZIP原始字节本轮未获得，不能声明连续全量。
- 冻结V0.35 HTML SHA `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`、2008参考JPEG SHA `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`、176编码、正式SVG、用户Storage及生产入口均未修改。
- T01正式认证0/25键，T02永久ID0，T05缺根数未知，T00–T11仍**0/12 Accepted**。
