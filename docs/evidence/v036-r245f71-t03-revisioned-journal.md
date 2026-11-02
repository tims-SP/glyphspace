# V0.36 R245F71 · Root T03 隔离事务修订号与确定性日志（非正式验收）

日期：2026-11-03。工作轨道：**原始 T03 SVG坐标内核**，不是UI-03，也不是T01/T02来源认证。

## 真实父版和新累计包

- 父：R245F70 ZIP SHA256 `3f2092029e44545e71d38489f908183ec621ab9220e6f85729e773229c6e1e02`；真实读取并逐成员SHA复验 **3839/3839**。
- 新：R245F71 ZIP SHA256 `b05988d0a4f7102843957968815b257170c347895f0aae63a10607dce7ae8561`，**3854成员**，新增15；父3839/3839 SHA未变化。
- Python zipfile与系统unzip两套独立恢复：各3854/3854 SHA一致；恢复后各运行433/433选定旧新QA，QA后0文件漂移。完整历史全量QA **not-run**。
- 新模块SHA256：`f2e2ab03cc822d1558fc2c1e51ed042442cd5c26a80cc38d28381a5c9b40288f`，对应 `scripts/r245f71_t03_revisioned_journal_registry.js` 与ZIP中的同源JS字节。

## 实质缺陷、修复与测试

真实Chromium 1280×800 DPR1、390×844 DPR2均复现R245F70允许同一旧revision的第二次写入被接受（无并发冲突拒绝）。R245F71独立V2模块强制`expectedRevision`，过期/缺失/未来版本拒绝；支持无副作用`preview`、不可变事务日志、逐条post-state校验与确定性`replayJournal`。还修复四位小数归一化后微小正宽度归零、坐标越界的有效性漏洞；非法paintedBBox被拒绝。

新增真实Chromium about:blank **72/72**，继承F70 56、F69 39、F68 22、F67 63、F56 35、F65 98、T00 48，合计 **433/433选定QA**。本轮未访问用户Storage或正式DOM，未修改176编码或正式SVG。

**限制：** FNV32仅用于偶发漂移检查，不能证明来源真实性或抵御恶意篡改；这仍是151旧可视候选几何与无资产M占位的隔离内核，不是批准的`referenceShapeId`/`assetId`、合法原图逐笔`inkBBox`或生产集成。

## 原始T00–T11验收边界

- T00–T11正式 **0/12 Accepted**；T01 **0/25键**；T02正式批准永久ID **0**；T03未生产集成；T04生产用户迁移未验收；T05真实缺根数量未知；T06–T11未验收。
- R10原始ZIP此前恢复，R11/R12/R35原始ZIP与R12的20SVG仍缺；没有将缺失历史伪称连续全量。
- 高清同源许可/合法原始字节及逐笔人工认证、真实读屏、Android/iOS真机、生产用户迁移、完整历史QA均**not-run/unverified**；真实同源Web Locks/localStorage此前受管理员策略阻断，本轮未运行。
- 冻结V0.35 HTML SHA `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`，2008 JPEG SHA `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`，均已从父ZIP核对且未修改。生产入口保持冻结。

下一阶段优先T01/T02合法来源与K/M逐笔归属，之后才能推进T03正式资产绑定与T05补图。此证据不改变任何Accepted标记。
