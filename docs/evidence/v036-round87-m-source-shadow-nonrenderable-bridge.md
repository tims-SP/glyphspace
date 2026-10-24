# V0.36 第87轮 · 原始T01/T02/T05 M键非可渲染来源影子桥接（隔离，未验收）

- 父包：第86轮1223文件，SHA256 `af6260dbda45957892d844d5af1a2f2a3d494547b1b89f82c774971d2cd3a84a`，逐文件1223/1223继承一致。
- 本轮新增 `v036_round87/m_shadow_source_staging.mjs`（位于**外部累计ZIP**，不在GitHub）：以R73的151候选UID、R81的25键来源清单、R84的8条M观察（4旧UID别名+4未绑定影子UID）、R86未批准的vis-02扩框提案为固定SHA输入，提供只读来源/身份桥接及4条纯内存待审笔记的失败关闭导入导出。
- **4个影子候选均无SVG Path、inkBBox、可发布几何、正式assetId/instanceId；不是4个已确认新字根。** vis-02证据框[1045,585,26,23]仍未批准，原[1045,585,21,23]不变；vis-04归属未决。
- 新Node 38/38、Pillow/OpenCV原生RGB交叉检查12/12；第69、70、73–86轮共16组可执行继承QA全部通过。未运行第1–68轮全部历史QA。
- 第87轮累计ZIP **1236文件**，SHA256 `c50653e2bb980a289fb0287d7edb05f99d30f3f671112ec86cb39880e366e89f`；Python zipfile与系统unzip两次独立解压各1236/1236，解压后各18组新旧QA通过，QA后1236/1236文件SHA一致。**ZIP本体不在GitHub**。
- 第10–12、35轮完整ZIP及第12轮20SVG仍缺；合法同源高清2008原图未获。独立Chromium profile访问127.0.0.1返回`ERR_BLOCKED_BY_ADMINISTRATOR`，真实Web Locks/localStorage **blocked/not-run**，Android/iOS真机及真实读屏 **not-run**。
- 冻结V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`、2008原图 SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`；176旧编码、正式SVG及用户真实存储均未修改。
- **正式状态：T01 0/25键、真实缺根数未知；T02正式永久ID 0；T05正式补图未完成；原始T00–T11仍0/12 Accepted。** 这不是T03生产集成、正式来源认证或发布许可。
