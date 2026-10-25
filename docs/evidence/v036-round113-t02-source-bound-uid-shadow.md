# V0.36 第113轮 · Root T02/T04 来源绑定影子UID门禁（非正式验收）

日期：2026-10-25。根任务：T02（候选身份来源约束），关联T04（旧版局部v16坐标只读迁移预检）。第36–40轮的UI轨道不计入T03/T05。

## 真实漏洞及修复

R111的`map_candidate_shadow`仅核对151个active、5个related以及`publishAllowed=false`，未将每个旧槽与R73的`candidateUid/sourceGate/sourceBindingSHA256`逐一核对。R113在合成数据中互换Q:0与K:2候选UID，**R111旧函数仍返回错误UID**。R111的`admit_partial_v16`还信任调用者提供的默认坐标；若将Q:0默认值伪造为用户覆盖值，旧函数会把真实修改静默视作未修改。两项均在独立脚本中复现，不是仅推测。

R113新增外部累计包中的`v036_round113/source_bound_shadow.py`：冻结HTML、2008 JPEG、R46门禁账本、R73候选身份、R75旧槽计划及冻结V0.35 Chromium实取的25键156槽默认坐标均以SHA256绑定。151条active逐项检查旧槽、键位、UID、sourceGate和来源绑定哈希；5条related保持隔离。输入的计划、注册表、默认坐标或角色账本被替换即拒绝。Q:0/K:2/M:4合成用户编辑保持，K:2来源阻断、M:4口诀关联隔离均未解除。

## QA与归档

- 父ZIP：R112 1498文件，SHA256 `3ff5b88ee12fc2cc849bee8c01955feac90f3cefee38e75e1c763903a435fb7f`。
- 新增R113 **34/34**；继承R111 Chromium about:blank **60/60**、R112 **36/36**、R84 **124/124**、R95 **36/36**、R69 **19/19**、R96 **35/35**，共**7组344/344**。
- 新累计ZIP **1509文件**，SHA256 `acdd2f820af7e7b2dc45b371edb9856a1e02d9dd26acff56f93ab0ece43dc8e2`；1498/1498父成员逐文件SHA一致；Python zipfile和系统unzip独立解压各1509/1509，QA后再次1509/1509一致。首次恢复QA会改写ZIP内已有`__pycache__/*.pyc`，因此该次后验SHA失败、不计通过；随后使用`PYTHONDONTWRITEBYTECODE=1`从新目录独立重跑，两种恢复均通过。
- ZIP原始字节与完整脚本仅在外部交付，不在GitHub；GitHub文档不是ZIP字节存在证明。

## 边界与阻断

只读候选UID映射，不是正式永久ID，不是生产存储迁移。没有访问用户实际localStorage，也没有修改冻结V0.35 HTML、2008参考JPEG、176编码或正式SVG。T01正式认证**0/25**、正式永久ID**0**、T05正式补图未完成、原始T00–T11 **0/12 Accepted**。第10–12、35轮ZIP与第12轮20 SVG仍缺；同源高清合法原图及许可未取得。完整历史全量QA、真实旧用户迁移、Android/iOS真机及真实屏幕阅读器均`not-run`。R109的临时同源CI通过不等于正式迁移。

回滚：删除外部R113隔离目录并恢复R112累计ZIP；GitHub仅撤销本轮证据/状态提交，不改变生产入口。
