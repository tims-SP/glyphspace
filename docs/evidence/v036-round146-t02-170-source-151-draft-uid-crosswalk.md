# V0.36 第146轮 · T02来源—候选身份交叉核验（隔离、非验收）

R146 Root T02（关联T01/T04/T05）只读交叉核验R73/R75的151个草案UID与R145的170条原生物理来源观察：151旧可视槽各一草案UID；M同框别名4、M未绑定影子4、K4及B/J/R/V/X微形7，共15条未绑定物理观察（不是已确认缺根）；36旧未匹配属于151旧槽子集；5条related关联不生成独立UID。重算170/170原生RGB SHA；新201/201，继承R142–R145共1375/1375，每套1576/1576；父R145 1847/1847 SHA继承，新ZIP 1855文件，Python zipfile与unzip两套独立恢复各1855/1855 SHA且QA后不变。ZIP SHA e01168b3a786903568a8d6173d544f967affd2beb4f71304275d2790764287eb。R10–12/R35及R12 20SVG仍缺，合法同源高清许可/逐笔/真实同源/真机/读屏/历史全量QA未通过；T00–T11仍0/12 Accepted、T01 0/25、正式永久ID0；冻结入口/2008 JPEG/176编码/正式SVG/用户存储未动。

## 复验数据

- 父包：R145，SHA256 `4eec6b3b80561532dc79a4915d392a4cfc7506e50cd92d6d01e8b62ec40d68a3`，1847/1847继承文件SHA相同。
- 本轮独立累计包：SHA256 `e01168b3a786903568a8d6173d544f967affd2beb4f71304275d2790764287eb`，1855个文件，8个新增文件；Python zipfile与系统unzip两次独立恢复，均1855/1855 SHA；每套新增201、继承R145 379+R144 676+R143 87+R142 233，合计1576/1576 QA；运行QA后1855/1855 SHA不变。
- 源码：累计ZIP内 `v036_round146/identity_source_crosswalk.py` 与 `qa_identity_source_crosswalk.py`；JSON证据 `R146_identity_source_crosswalk.json`、`R146_identity_source_crosswalk_QA.json`、`R146_execution_report.json`、`R146_parent_1847_member_SHA256.json`、`R146_missing_history_audit.json`。
- 负对照：拒绝候选UID交换、M错误别名、未认证来源晋级、伪造几何SHA、篡改分类和缺失观察。
- 真实同源测试：隔离Chromium profile访问127.0.0.1时超时，HTTP服务端无请求；`blocked`，不计入QA。真机/读屏 `not-run`；完整历史全量QA `not-run`。
- GitHub Releases列表为空；R114已知Actions运行artifact=0。均不证明缺失历史在所有外部存储中不存在。
- 不能将170物理来源、151草案UID、15未绑定观察、36旧未匹配、5关联解释为正式字根数量；没有新的referenceShapeId/assetId/instanceId批准。

## 正式状态与回滚

原始T00–T11编号不变，12项全部`accepted=false`；正式T01 0/25，T02永久ID 0，T03未生产集成，T05未补齐。删除R146隔离目录及本轮文档即可回滚；冻结生产入口、用户存储不受影响。
