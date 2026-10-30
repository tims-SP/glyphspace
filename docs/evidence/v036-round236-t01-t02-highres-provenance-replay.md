# V0.36 R236 · 原始T01/T02高清坐标来源证据重算门禁（非认证）

日期：2026-10-30。正确任务：Root T01/T02，关联T05；不是UI-01至UI-05，也不是原始任务正式验收。

## 真实复现的R235漏检

R235 `source_identity_fanin_gate.py` 将R219 crosswalk的SHA钉值留空（`PINNED['crosswalk']=None`），只核对161裁框和170观察的数量及`formalAccepted`标志。实际在隔离内存中分别篡改R219的裁框四角坐标、裁框ID、高清候选JPEG SHA，R235对三种篡改仍返回成功（3/3），说明不能依赖该门禁认定R219坐标证据未漂移。

## 本轮修复

R236新增 `v036_round236/t01_t02_highres_provenance_gate.py`，SHA钉住R119真实ORB配准证据、R156原生观察、R209候选注册表、R218就绪表、R219原始投影构建器、R219索引JSON与CSV、2008冻结JPEG和V0.35 HTML。重新运行独立于R235的R219来源投影生成器，以R119仿射矩阵重算161/161原生裁框的四角、多边形、包络、面积、原图RGB SHA、观察ID与候选UID关联；逐字段核对161条JSON记录与161条CSV行，另核对M四未绑定来源及E/K禁止合并关系。任何来源字节、几何或身份链接漂移都拒绝。上述三种R235错误接受的篡改在R236均被拒绝（3/3）。

新旧选定QA：R235继承758/758 + R236新增51/51 = **809/809**。真实父包R235 SHA256 `1e956e197b709c12e4f3d5eff67180e08cd95a7b9990b97abb99d4ff78b57542`，继承2955/2955成员逐SHA一致。R236累计ZIP **2965文件**，SHA256 `126ed92fff3db578e6726abf41483e40f15ce35062e4b81b1ad7844f1edc6e30`；Python zipfile和系统unzip两次独立解压各2965/2965 SHA一致，各809/809选定QA，QA后文件变化0。

## 验收边界

此项仅修复**来源坐标证据完整性**，不是高清JPEG逐笔审阅，也不是参考图来源许可或同源性证明。T01正式0/25键；T02批准永久ID0；T05缺根数未知；T00–T11仍0/12 Accepted。原始R11/R12/R35 ZIP及R12 20 SVG仍缺失，历史全量QA not-run。真实同源Web Locks/localStorage此前被管理员策略阻断，本轮not-run；真实读屏/Android/iOS真机not-run。冻结V0.35 HTML、2008 JPEG、176旧编码、正式SVG、生产入口及用户原有存储均未修改。

交付包内证据：`v036_round236/R236_highres_provenance_replay_audit.json`、`R236_highres_provenance_adversarial_QA.json`、`R236_new_old_QA.json`、`R236_parent_2955_member_SHA256.json`、`R236_missing_history_audit.json`。外部另有双恢复QA和全文件SHA清单。

**结论：** R235来源几何漏检已真实复现并修复；本轮没有新增任何正式认证字根或永久ID。
