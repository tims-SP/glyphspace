# V0.36 第76轮：Root T04 隔离候选UID事务预演（非正式验收）

- 日期：2026-10-24；Root **T04 存储与旧版迁移**。第75轮151个候选UID+5个仅关联记录，保留3条合成调位。
- 父第75轮累计ZIP：1101文件，SHA256 `f809b54708efa819a1b9e0092a9e48b3458eefb596be0b86e53af24c88228607`，逐文件1101/1101 SHA继承一致。
- 第76轮累计ZIP：**1111文件**，SHA256 `036d42a90875b30dfc475fbbd4feaccdc2b4a775f6ecf05486f58365db66b76d`；Python zipfile和系统unzip两次独立解压均1111/1111 SHA一致，解压后新旧QA均通过，QA后1111/1111 SHA一致。**ZIP本体不在GitHub**。
- 新增隔离事务模块SHA256 `f7aec5579c3a41e09b5eed9810c9bb9c088d959d32ba48da75b91b9c126ad37a`，新增QA脚本SHA256 `a66b4cb6e44be0aec4ebe70058d94561355bab3ebccca0e1a0d4c12d5cc8695f`（均位于累计ZIP的`v036_round76/`）。
- 事务协议：强制注入合成store和单进程模拟独占锁；校验可信第75轮预检摘要；意向日志→不可变完整版本→校验→切换HEAD→校验→清理日志；支持崩溃恢复、旧HEAD冲突拒绝、幂等重入、显式回滚、记录/日志篡改拒绝。
- 新增Node测试**70/70**通过；第75轮及R74–R67历史回归**9/9组**通过。测试涵盖3个写入故障时点、发布后清理故障、双模拟tab竞争及用户旧键不变。
- **真实性边界**：模拟锁不是浏览器Web Locks。新临时Chromium profile+127.0.0.1页面导航18秒超时，未取得DOM；真实Web Locks/localStorage事务为**blocked/not-run**。Android/iOS真机与真实读屏均**not-run**。没有读取/修改用户真实存储。
- T01正式认证**0/25**，真实缺根数未知；T02正式永久ID **0**；T03正式内核未集成；T04仍未Accepted；全部T00–T11 **0/12 Accepted**。历史第10–12、35轮ZIP和第12轮20SVG缺失；同源高清原图与许可未解决。
- 冻结V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`、2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`，正式SVG/176编码/生产入口未改。
