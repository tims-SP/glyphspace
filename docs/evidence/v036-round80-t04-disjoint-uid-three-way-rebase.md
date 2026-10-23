# V0.36 第80轮 · 原始T04隔离候选UID三方合并证据

- **父档案**：第79轮累计ZIP，1141文件，SHA256 `7da4350b7f2e9fc69500038c8b7e7045450fea31aa60457cc8af77ad94eabddc`；逐文件SHA继承1141/1141。
- **新档案**：第80轮累计ZIP，1151文件，SHA256 `26285567c81a302cd9dcb9b96bb57a39a8a57110bf98d948a1ff7a8412142185`。ZIP原始字节仅在外部交付文件工作区，不在GitHub。
- **实质实现**：`v036_round80/disjoint_uid_rebase.mjs`（隔离ZIP内），SHA256 `05b8e9d24443456079d9feac85c440bc5bf6fb75aab636ff69da3191f4f53ec9`。在R79不可变候选UID几何修订日志之上，以共同祖先执行三方合并：不同UID的过期标签页编辑可安全合并，同UID分歧拒绝，未知祖先、非法几何和来源变更失败关闭；HEAD条件提交防止覆盖并发修订。
- **QA**：Node 22新增24/24通过，继承R79及以前13/13组通过。Python zipfile与系统unzip分别恢复1151/1151文件、复跑新旧QA通过，QA后1151/1151文件SHA一致。系统unzip首次组合编排超时，后续在其独立解压目录单独复跑成功；超时未计入成功。
- **数据边界**：仅FakeStore与SimulatedExclusiveLocks，不触碰真实用户localStorage，不是浏览器Web Locks。151个候选UID、5个关联隔离记录均保持；来源认证0/25键，正式永久ID 0，原始T00–T11 0/12 Accepted。
- **阻塞**：真实共享原点事务 blocked/not-run；Android/iOS真机和真实读屏 not-run；第10–12、35轮完整ZIP与第12轮20SVG未找回；同源高清原图原始字节及合法许可未取得，真实缺根数未知。
- **冻结**：V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`，2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49` 未变。176旧编码、正式SVG、生产入口和用户存储未修改。
