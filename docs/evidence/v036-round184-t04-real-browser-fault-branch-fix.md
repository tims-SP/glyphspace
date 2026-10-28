# R184 · Root T04：真实浏览器故障分支QA修复（非正式验收）

2026-10-28。首先核对 `main`、原始T00–T11账本及R183累计ZIP（SHA256 `65526b6e12e03f8fd6a83f9a458e5a492180fe6fd23e4134575c561395ccd185`）。原始任务编号未改。

## 实际发现

[R183首次真实浏览器CI](https://github.com/tims-SP/glyphspace/actions/runs/40630751605) **failure**，job `122626294628`，`fault-rollback: unexpectedly passed`。原因是脚本对已成功暂存的**相同**payload注入故障，核心按设计返回`idempotent`，未进入故障分支；不是事务核心故障已经被证明。

## 修复与证据

修复 `scripts/r183_shared_core_browser.py`：隔离payload增加revision，成功stage后由0改1，故障路径 `after-journal`、`after-shadow`、`crash-after-shadow` 真正执行，逐字节核对旧shadow回滚和新文档恢复。共享ESM事务核心代码未修改。新增 `scripts/r184_fault_branch_regression.mjs`，Node私有Map独立21/21，证明旧用例误走幂等分支、修复后故障与恢复实际触发。

[修复后真实Chromium CI](https://github.com/tims-SP/glyphspace/actions/runs/40635880938) **success**，job `122642619173`，临时127.0.0.1同源双标签**25/25**；独立下载原始artifact ID `12793257183`，ZIP SHA256 `e3bc3d5d3e146c254e7d57a9b89d48c8162ad11340daf4e21985317caa1719c6`，内部JSON 25/25。完整远端证据随R184隔离累计ZIP存档。

R183父文件逐项SHA继承 **2257/2257**，R184累计 **2271** 文件，ZIP SHA256 `1404f851ae798a32c5e5698448755c4ddc838421c4920fee85b11f13b3ad23fa`。本地选定旧170/170+新增Node21/21+静态合同12/12+远端artifact独立校验12/12=**215/215**；Python zipfile与系统unzip两套独立解压各2271/2271 SHA、215/215 QA，QA后SHA不变。远端25项不重复计入本地215项。

## 不得升级验收

真实浏览器成功仅验证隔离fixture的同一ESM及Web Locks/localStorage，不是正式V0.35用户数据迁移。**原始T00–T11仍0/12 Accepted**，T01正式认证0/25键、T02永久ID批准0、缺根数未知；R11/R12/R35 ZIP及R12 20SVG仍缺，高清许可、逐笔来源、真机、真实读屏、完整历史QA均未完成。本地localhost Chromium仍`ERR_BLOCKED_BY_ADMINISTRATOR`。冻结HTML、2008 JPEG、176旧编码、正式SVG、生产入口和用户原有存储均未改动。
