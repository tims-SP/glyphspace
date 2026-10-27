# V0.36 R168 · Root T00/T01/T02/T03 — 原始R8到R50的151个冻结Path来源连续性（非验收）

2026-10-27。以R167累计ZIP（2075文件，SHA256 `f0ebd556f75e48cb09aef569054aa6b0c8f5dff62bed74a8647bf268c5504286`）为父版本，实际打开其中原始R10 ZIP（184文件，SHA256 `6a1552b45cfa3512d9fea2ab06df740a6adbb4b598369cd3ea8e214fee1c0ed0`），只从原始ZIP读取R8的151旧SVG草案、156项稳定ID兼容注册表与R9的15项未认证证据，并独立读取R50的151项冻结Path输入。**不得用后期同名根路径文件代替原始R10历史字节。**

本轮对151个可视实例逐一核验instanceId、键位、旧槽别名、显示字符、V0.35坐标、SVG Path数组：**151/151一致**；原始R8的156项注册表中5个related_association未被混入可视资产。149条冻结字体路径的SHA256可直接从原始R8 Path字节重算并与R50记录一致。H:6的Noto Serif部件与H:7的KanjiVG三描边为**2个特殊来源**，其R50 sourcePathSHA并非单个Path d的直接SHA，保留原记录与独立来源类型，不伪造同一哈希算法。

新增28/28来源与变异拒绝QA，实际重跑R167选定继承288/288；本轮316/316选定QA通过。父ZIP **2075/2075** SHA继承，第168轮累计ZIP **2084文件**，SHA256 `1bb96c5dcd658230aee4cfd0836e1c04e74479e6a6d0a3b72ab3b5a1a54a2ef4`；Python/system unzip两次独立恢复均2084/2084 SHA、316/316 QA、QA后2084/2084 SHA不变。完整历史全量QA **not-run**；ZIP及执行代码保存在独立交付包，未提交GitHub。

**边界：** 该证据只确认旧版草案资产在历史R8→R50之间未漂移，**不等于**2008原图逐笔认证、正式永久ID批准或生产T03集成。T01 0/25键正式认证、T02正式永久ID0、真实缺根数未知；原始T00–T11 **0/12 Accepted**。R11/R12/R35原始ZIP与R12 20SVG仍缺。合法同源高清原图、真实共享原点Web Locks/localStorage、Android/iOS真机、真实读屏均未完成。冻结V0.35 HTML、2008 JPEG、176旧编码、正式SVG、生产入口和用户原有存储未修改。

本轮审计产物：`v036_round168/original_r8_to_r50_lineage.py`、`R168_original_R8_to_R50_lineage.json`、`qa_original_r8_to_r50_lineage.py`、`R168_double_independent_restore_QA.json`（后者为包外双恢复记录）。下一步继续寻找R11/R12/R35及20SVG、合法同源高清原图，优先完成M/K/E/B/J/R/X/V逐笔来源仲裁。
