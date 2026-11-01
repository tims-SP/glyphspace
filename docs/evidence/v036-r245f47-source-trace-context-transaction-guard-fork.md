# R245F47 · Root T01/T02：来源描记上下文切换事务取消（非认证）

- GitHub main复核：03c29e0fcc4b968224b9fdf37bc6d45b54da6b97（R246）。R246原始ZIP仍缺失，本分叉不能称作继承R246。
- 真读R245F46父ZIP SHA256 `a6645a50ed9c0ffdfa99b1b2b7d461e14fb980340d8bf3e7f7d8a5cd31b530a8`，3508/3508逐成员SHA一致。
- 真实Chromium about:blank加载冻结JPEG字节并验证SHA。旧R245F46在指针按下时切换案件或键位，虽清空未提交点，旧pointer事务仍保持active；新案件首次pointerdown被当作多指冲突取消。旧版切换来源观察时，已有未完成草案继续保留，但UI已显示新的观察对象，存在描记上下文误关联风险。
- R245F47独立候选在切换案件、键位、来源观察时取消旧指针事务、释放可用的pointer capture并清空未完成草案；已经完成的笔画记录和规范导入导出保持可用。
- 真实Chromium旧新回归35/35，继承选定386/386，合计421/421。Python zipfile和系统unzip双独立解压各3518/3518逐SHA，恢复后各421/421选定QA，QA后0漂移。第一次合并双恢复执行环境超时，系统unzip QA单独重跑通过；超时不计pass。
- 新累计ZIP 3518文件（父3508+新10），SHA256 `5fbb8fe0b0123e9dfc5548f90f3a8e8e30d20faf6744eef402a58afb0d6ea039`。仅隔离候选与证据，未加入许可未明高清原图。
- 冻结V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`、2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`不变。176旧编码、正式SVG、生产入口及用户Storage未改。
- 正式边界：T01 0/25键认证，T02永久ID批准0，T05缺根数未知，原始T00–T11 0/12 Accepted。真实同源Web Locks/localStorage本轮not-run；真实读屏、真机、合法同源高清逐笔及历史全量QA均not-run/blocked。
- 缺失R11/R12/R35原始ZIP、第12轮20SVG及R246主线ZIP；R10原始ZIP仅在父档案内存在，不代表完整连续历史。
