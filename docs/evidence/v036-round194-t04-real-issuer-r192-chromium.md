# R194 · Root T04：真实来源签发链与R192核心的Chromium联合测试（隔离候选）

日期：2026-10-28。正确原始任务编号：**T04 存储与旧版迁移**；不是T03/T05，也不是UI-01～UI-05。

## 已实际完成

- 读取R193父累计ZIP，确认SHA256 `88d7258d80cc83aed15b17fa8c97482202dd6d113b49454c610b15896003e6d7`、2417成员，全部2417/2417原始成员逐文件SHA继承。
- 将R148严格v16读取、R152真实计划签发、R178来源新鲜度门禁、R179浏览器realm原点绑定，与**原样R192 typed-slot事务核心**连接；新增独立R194适配器，冻结旧生产入口不变。
- 使用冻结156项ROOT_COORDS及G/K/X三键合成v16覆盖，在**全新127.0.0.1双标签真实Chromium**中验证来源签发、计划不可克隆、暂存、幂等、跨标签崩溃恢复、null与空字符串的非协作写入冲突、来源过期拒绝、无关键保护、隔离context和清理。
- 远端CI **30/30 success**：[R194 GitHub Actions run](https://github.com/tims-SP/glyphspace/actions/runs/40712389404)（head `bb4336364a80932838d96434d9d272a288ac7401`）。原始artifact id `12827280941`，ZIP SHA256 `56fb43276363bcd023fcf9f128f7b6e0650ac77ab7633b58b54c741eec3de42f`，已实际下载、解压并独立核对30项JSON。
- 本地真实Chromium访问临时127.0.0.1仍返回`ERR_BLOCKED_BY_ADMINISTRATOR`，状态**blocked/not-run**，未计入本地通过。
- 本地选定继承QA 600/600（R192 588 + R193 12）；R194真实签发Node 47/47、静态来源检查24/24；合计**671/671**。累计ZIP **2447文件**（继承2417，新增30），ZIP SHA256 `35eeaf4d0f9bf6b350dc915269ad46f1428d829594cfe8c3bf1894cd51734839`；Python zipfile与系统unzip两套独立恢复，各2447/2447 SHA、671/671 QA、QA后SHA未变。
- 原始R148/R152/R178/R179模块与冻结坐标的SHA由独立测试锁定；生产HTML、176条编码、正式SVG、用户原有localStorage均未修改。

## 验收边界与阻断

真实浏览器虽执行完整签发链，仍使用**合成来源数据、临时profile和隔离影子**；不是真实V0.35用户迁移，不签发正式永久ID。Web Storage无原子CAS，非协作写入竞态仍需限制；T02/T03正式依赖未Accepted。完整历史全量QA、Android/iOS真机、真实读屏均not-run。

T00–T11原始任务仍**0/12 Accepted**；T01正式来源认证0/25键，T02正式永久ID批准0，T05真实缺根数未知。R10原始包已恢复；R11/R12/R35原始ZIP和R12 20SVG仍缺。高清参考图合法许可与逐笔来源认证未完成。不能宣称连续全量历史、正式补图或生产迁移通过。

下一步：补齐T01/T02高风险键M/K/E/B/J/R/X/V来源身份，推进正式T03内核与永久ID前置依赖，随后在隔离授权profile用真实迁移样本执行T04；不得触碰用户原有Storage。
