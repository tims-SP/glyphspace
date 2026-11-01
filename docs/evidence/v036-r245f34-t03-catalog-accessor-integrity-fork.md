# R245F34 · Root T03 派生目录访问器一致性修复（隔离分叉，非正式验收）

日期：2026-11-01。原始任务：T03（100×100 SVG坐标内核），不是历史UI-01–05。

## 来源与父版
父包 R245F33 3389文件，ZIP SHA256 `dcbf5d1d22937e3c7e8eedba19e8f337d700b1f4090ecaa0deb4927c45885ce3`。本轮真实读取并逐文件SHA复核3389/3389一致。冻结V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`，2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`，均未修改。

## 真实缺陷与代码
R245F31只验证source/vector为纯JSON，不验证派生catalog。测试向catalog.byId[id].paths[0].d注入访问器，首次读取返回冻结Path，后续读取返回M999 999 L1000 1000；旧审计错误通过151实例（复现1/1，不计入通过数）。新增 `v036_r245f34/t03_strict_catalog_gate.mjs` 和 `qa_t03_strict_catalog.mjs`：严格拒绝派生目录及补丁参数中的getter、隐藏toJSON、原型与数组属性注入；补丁引擎合法的geometry共享引用以描述符受控复制去别名并深冻结。隔离导出器 `t03_strict_export.mjs` 接入新门禁；输出HTML SHA256 `efc75fdaa607168f0c40e1d03bb1613df0e9b35328eba24fdb0045e09779b762` 与R245F33字节一致，151 SVG实例、25键、旧Path与变换不变，无UI新功能。

## 实际QA与恢复
父版R245F24–F33选定QA逐套重跑492/492，新QA17/17，合计509/509。累计ZIP 3400文件，SHA256 `cf2ae5731ebc322464a7b648309e9f0dd70b4c7497492442c75d1f8c918eb674`。Python与系统unzip两套独立恢复各3400/3400逐文件SHA一致；恢复后分别运行R245F31 23、R245F32 78、R245F33 107、新R245F34 17，均225/225通过；QA后各3400/3400不漂移。完整历史全量QA not-run。ZIP、QA和成员SHA清单保存在本轮隔离工件中，GitHub仅同步技术证据与状态。

## 严格边界
GitHub main R246累计ZIP原始字节未取得，不能宣称本分叉继承R246；原始R11/R12/R35 ZIP及R12 20SVG缺失。合法同源高清逐笔与许可未完成，T01认证0/25、T02正式永久ID0、T05缺根数未知，原始T00–T11 0/12 Accepted。真实同源Web Locks/localStorage、真实读屏、Android/iOS物理设备本轮not-run；此前本地同源被管理员策略阻断。冻结生产入口、176旧编码、正式SVG及用户存储均未触碰。
