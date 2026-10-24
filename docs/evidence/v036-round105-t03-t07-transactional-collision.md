# 第105轮 · Root T03/T07 隔离事务性墨迹包络碰撞门禁（非正式验收）

日期：2026-10-25。**原始任务 T03=SVG 100×100坐标内核，T07=位置与碰撞**。不涉及UI-01～UI-05任务编号。

## 真实缺陷与修复

R104的隔离SVG预览支持 `move/apply/importPreview`，但其`attest()`只校验来源与几何矩阵，未拒绝两个同键草案`inkBBox`重叠。真实Chromium对照中，R104接受了这种移动且`attest()`仍为true。

R105在DOM写入与overlay提交**之前**检查完整未来事务状态：25键、151候选UID、409对同键候选矩形，重叠即fail-closed。签名导入、批量编辑均不会部分提交；无碰撞的光学校正、移动、撤销、导入及三视图仍工作。该检查不将候选`inkBBox`冒充已认证的2008原图笔画。

## 可重算证据

- 父R104累计ZIP：1425成员，SHA256 `3840ac7eaeea34c66d3c251dd8906117d92de2f5536b34256d26b6afad275289`；R105逐成员继承 **1425/1425** SHA一致。
- R105累计ZIP：**1433成员**，SHA256 `2ffa0ecc3b72bee3ef7d2a24d76431f3619c29b5734ed7dbf513388b0b7d876a`。ZIP本体仅在独立交付，不在GitHub仓库；缺失历史轮次不声明连续完整。
- R105真实Chromium about:blank：**170/170**，包括151个候选UID逐个主动碰撞负例，拒绝后DOM与预览SHA不变；R104对照实际错误放行。
- 定向继承：R104 Chromium 25/25、R103 Chromium 26/26、R77 Node 179/179、R99 Chromium真实像素绘制302/302。
- Python zipfile与系统unzip**两次独立解压**：QA前后各 **1433/1433** 成员SHA一致；两份恢复环境均重跑上述5组QA（每份702项）。完整历史全量QA **not-run**。
- 隔离文件：`v036_round105/R105_T03_T07_transactional_collision_guard_isolated.html`、`qa_collision_transactions_r105.py`、`R105_Chromium_collision_transaction_QA.json`、`R105_parent_1425_member_SHA256.json`、`verify_recovery_r105.py`（均位于交付ZIP内，**不在GitHub**）。

## 证据边界与阻断

此处仅为**隔离草案的100×100矩形碰撞预检**；不证明真实墨迹、描边、圈注、标签、视觉位置与真机无冲突，T03/T07均未生产集成。T01正式认证 **0/25**，T02正式永久ID **0**，原始T00–T11仍 **0/12 Accepted**。第10–12/35轮ZIP及第12轮20SVG仍缺；合法同源高清参考图未取得。真实共享原点Web Locks/localStorage此前被管理员阻断，本轮**not-run**；Android/iOS真机、真实屏幕阅读器**not-run**。冻结V0.35 HTML、2008 JPEG、176编码、正式SVG与用户原有存储未修改。
