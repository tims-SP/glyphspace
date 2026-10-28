# V0.36 第180轮 · Root T04 隔离内存迁移隔离区与崩溃回滚

日期：2026-10-28。**仅原始T04（存储与旧版迁移）的非生产前置实现，不构成Accepted。**

## 真实代码与安全边界

读取 main 分支六份强制规范及R179累计ZIP原始字节。新增 `v036_round180/disposable_quarantine_migration.mjs`（包含于隔离累计ZIP），在**Node 22私有Map**中复用R148严格v16读取、R152签发计划与R178来源新鲜度SHA门禁，将v16槽位别名与显式编辑写入标记为`blocked_pending_T01_T02_formal_identity`的**临时隔离影子**。在写影子前记录恢复日志；支持幂等重放、错误回滚、模拟进程崩溃后的重新实例化恢复、原有影子恢复，以及崩溃后v16来源已更新时仅恢复旧影子而不覆盖新来源。拒绝克隆签发计划、过期源、损坏日志。

**该代码完全没有浏览器localStorage访问、真实存储提交或正式永久ID映射**。使用私有Map、模拟锁和模拟loopback参数，仅测试回滚算法；不代表真实同源Web Locks、多标签竞争、storage事件、持久化崩溃恢复、生产迁移或正式T04验收。原始冻结HTML、2008 JPEG、176旧编码、正式SVG及用户原有存储均未修改。

## 真实执行与复验

| 项目 | 结果 |
|---|---|
| R179父ZIP SHA256 | `87fddbac1512ab8f4b87f4f6fd59291ef88ad5a7c1aac13feaaebb5100be350f` |
| 父文件逐项继承SHA | **2213/2213** |
| R180新增Node QA | **48/48** |
| 实际重跑R179选定旧QA | **1133/1133** |
| 本轮定向QA | **1181/1181** |
| 新累计ZIP | **2224文件** |
| 新累计ZIP SHA256 | `5155e490d3ec295d6f1cf6868ca0dc92397525123262f9058237c41fb44bce5f` |
| Python zipfile独立恢复 | **2224/2224 SHA；1181/1181 QA；QA后SHA一致** |
| 系统unzip独立恢复 | **2224/2224 SHA；1181/1181 QA；QA后SHA一致** |
| 冻结HTML SHA256 | `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc` |
| 冻结JPEG SHA256 | `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49` |

本轮完整历史全量QA、真实同源Web Locks/localStorage、Android/iOS真机、真实屏幕阅读器、正式生产迁移及回滚均为**not-run**。真实loopback浏览器在R179遭管理员策略阻断，本轮未重试，不能计pass。完整仓库`scripts/verify_repo.py`本地未运行（容器无法解析github.com）；后续远端CI需独立确认。

## 任务与历史缺口

原始T00–T11 **0/12 Accepted**；T01原图正式认证0/25键，T02永久ID批准0，真实缺根数未知。第10轮原始ZIP已恢复；仍缺第11、12、35轮原ZIP及第12轮20个SVG。本轮Library标题检索未命中精确历史文件，不证明全库不存在。第三方高清参考图许可和M/K/E/B/J/R/X/V逐笔身份仲裁仍未完成。

下一步：在独立授权profile完成真实同源存储锁/事件/故障恢复验证；在T02身份批准前，不得把本轮隔离影子转换为正式V0.36迁移数据。
