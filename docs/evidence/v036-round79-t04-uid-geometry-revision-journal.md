# V0.36 第79轮 · 原始T04：候选UID几何修订隔离事务

> 2026-10-24；Root T04（关联T02/T03），**仅合成存储预演，非正式验收**。原始T00–T11编号与定义保持不变。

## 实际新增

- 将第75轮156条旧坐标记录（151个候选UID + 5个非视觉关联隔离）、第76轮不可变事务思想、第77–78轮100×100/inkBBox/锚点/光学校正预览接入**一个可逆版本日志**。此前第76轮只能提交固定迁移计划，不能持久化连续的候选UID几何编辑。
- 新增隔离模块 `v036_round79/isolated_uid_geometry_journal.mjs`（**代码在外部累计ZIP，不在GitHub仓库**），SHA256 `40dc21f72e1698ee441c7df06467947e30f8cbef084b03689f22f2672b0792da`。
- 每次修订绑定可信迁移计划SHA、候选注册表SHA和草案几何模型SHA，保存候选UID预览及前版本指针；支持两阶段意向日志、模拟HEAD提交、幂等、故障恢复、条件冲突与回滚。未知/重复UID、旧槽位、M:4非视觉关联、篡改、越界和冒充正式认证均拒绝。
- **只能注入Node FakeStore与SimulatedExclusiveLocks**，显式拒绝真实浏览器存储；所有候选仍是未认证身份，5条关联不会升级为字根。摘要SHA只用于完整性，非授权签名。

## 独立复验

- 父第78轮累计ZIP：1131文件，SHA256 `48fe5a2b6cda30d1ef72ce09454a9ddd78ab55dfdf1d0360f6ccd669cc6e55c9`；继承文件 **1131/1131** SHA一致。
- 第79轮累计ZIP：**1141文件**，SHA256 `7da4350b7f2e9fc69500038c8b7e7045450fea31aa60457cc8af77ad94eabddc`；**ZIP本体不在GitHub**，需使用外部交付包验证。
- 新增Node QA **38/38**；继承第78轮及更早QA **12/12组**。Python zipfile与系统unzip各独立解压1141/1141、复跑新旧QA后全部1141/1141 SHA一致。组合复验第二解压阶段曾超时，随后单独复跑system-unzip环境QA通过；不把超时尝试记为通过。
- 冻结V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`；2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`。176旧编码、正式SVG、用户存储未改。

## 验收边界

- 独立Chromium file:// 探针未返回DOM；此前HTTP导航受管理员策略阻断。真实共享原点Web Locks/localStorage事务 **blocked/not-run**，并非QA通过。
- 第10–12轮、第35轮完整ZIP与第12轮20 SVG未找回；同源高清原图及许可未取得。T01 **0/25**，缺根数未知，正式永久ID **0**；Android/iOS真机及真实读屏 **not-run**。
- **原始T00–T11：0/12 Accepted**。T04仍未生产集成，不能替换冻结 `index.html` 或宣称正式发布。
