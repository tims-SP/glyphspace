# R245F24 · Root T01/T02：冻结JPEG字节校验与M来源归属集成（隔离、非认证）

- 父包：R245F23 ZIP SHA256 `d31e77245b9d5aa103d53e093820fa44df3a6034c7ed8158aa57de68a9386e44`；3285/3285成员逐SHA继承。
- 本轮包：R245F24 ZIP SHA256 `3d74464141f2046342366a223aaffae96fdfb2f8c51985e99503de92b79c206b`；3296成员，Python和unzip双独立恢复各3296/3296 SHA。
- 真实缺陷复现：R245F23仅校验JPEG尺寸1536×1086，原图追加尾部字节（渲染像素不变但SHA不匹配）仍被接受，并可生成宣称绑定冻结SHA的描记证据。
- 修复：把R245F17便携SHA-256和内嵌注册表哈希校验整合到R245F23 M四组跨候选点/线段归属守卫；只从已验证的同一字节快照构造实际显示的Image。离线使用File API选择原始JPEG；没有来源字节时拒绝描记、审阅意见和笔画导入/导出；替换、失败及过期异步导入均失败关闭。
- 原始2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`；R144注册表原始SHA256 `cafa1c6eae872e1562109830faae5347094b41690c7bb63e5a4ce784a95e77bb`，内嵌注册表文本SHA256 `e5475e64b531d44d357b45af8afea274ebab8f0e86835b50969f08bb7e171d4d`。
- 真实Chromium about:blank新27/27，R245F23兼容101/101，R245兼容88/88，R245F22旧20/20，R145来源379/379（含170裁框RGB），选定615/615；双恢复各615/615；QA后0文件漂移。旧版错误接受作为复现证据，不计为新功能通过。
- 实际交付：隔离累计ZIP内 `v036_r245f24/R245F24_M_verified_source_pixel_ownership_candidate.html`、`build_r245f24.py`、三组Chromium QA、`R245F24_parent_3285_member_SHA256.json`、审计、报告和双恢复证据。ZIP在本轮会话文件中，未进入Git仓库（避免大体积Blob）。
- GitHub main仍`03c29e0fcc4b968224b9fdf37bc6d45b54da6b97`（R246）；无Release，R246 3054成员ZIP原始字节仍不可得。第10轮原始ZIP已恢复，第11/12/35轮ZIP及第12轮20SVG仍缺。
- **正式验收未改变：T00–T11 0/12 Accepted，T01来源认证0/25，T02永久ID批准0，T05缺根数未知。** 真实同源Web Locks/localStorage、合法同源高清逐笔及许可、真读屏、真机、完整历史全量QA未运行。冻结V0.35、176旧编码、正式SVG、用户Storage未修改。
