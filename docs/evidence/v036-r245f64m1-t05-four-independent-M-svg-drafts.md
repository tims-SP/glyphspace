# R245F64M1 · Root T05 M键四个独立SVG隔离草案（非验收）

日期：2026-11-02。分支自 R245F64 commit d858bbbe6429c061c4b5f72ea45c474291343e30；**未继承远端R245F65累计ZIP**，其原始ZIP字节在本轮运行容器不可用。

## 实质工作

- 对 M-vis-04、M-vis-06、M-vis-07、M-vis-08 四个独立物理候选建立各自的**仅供审阅SVG Path**和 draftAssetId；每项有独立100×100局部几何、ink-center锚点、可独立设置的光学校正。
- 在继承的151历史可视实例T03隔离候选HTML上，新增四个草案叠层；完整键盘、迷你键盘、单键焦点复用相同符号。没有修改旧151实例Path/坐标、176编码、正式HTML、正式SVG或用户Storage。
- 三尺寸Chromium浏览器验证四草案与旧根、标签及彼此没有BBox碰撞；修正最初M-vis-08与M标签的冲突，将底部三草案统一上移至独立预览坐标。
- 高分辨率3508×2480候选JPEG仅用于私有目视中心线草绘，**来源许可未确认，手绘Path非逐笔认证，不能签发正式assetId/instanceId，也不能宣称新增4个正式字根**。派生Path仅在本轮用户私有累计ZIP中，未上传公开仓库。

## 实际验证

- 父R245F64 ZIP SHA256：`11ba7e812a8a9bcec7e778513bef279b038f3116abf7f97f0b500c379364192f`；3750/3750父成员逐SHA继承。
- 新累计ZIP：**3767文件**，SHA256 `3dc6bd6975739b157ea1ef7979183264bcbea332276ed1e5c648e28982d5452d`；Python zipfile 与系统unzip两套独立解压各3767/3767逐SHA一致，QA后0漂移。
- 两套恢复均实际运行：旧R245F63 279/279 + R245F64契约66/66；新浏览器28/28 + 静态21/21 + 三视图/三尺寸碰撞27/27。**各421/421选定QA**。
- 另在打包前真实运行冻结V0.35的176字、三模式浏览器行为Oracle：3143/3143通过；不计入两套恢复421。
- 本地独立Chromium profile访问127.0.0.1仍`ERR_BLOCKED_BY_ADMINISTRATOR`，真实同源Web Locks/localStorage QA为blocked/not-run。
- 真机Android/iOS、真实读屏、高清逐笔人工认证、合法来源核验、完整历史全量QA均未执行；没有任何Root任务因此Accepted。

## 继承与限制

- 仍缺原始第11、12、35轮ZIP及第12轮20个SVG；R246主线完整累计ZIP未取得。R245F65存在文档证据，但本轮没有其可实际复验的完整ZIP，不将它并入继承链。
- 正式认证25键0/25、批准永久ID0、真实缺根数未知，原始T00–T11 **0/12 Accepted**。
- 冻结V0.35 HTML SHA `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`，2008原图SHA `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`，均未改。

下一步：合法同源与人工逐笔审查这四个候选，再按T01→T02→T03→T04门槛集成T05；不可因候选Path存在就通过T05。
