# R245F25 · Root T01/T02 异步导入与本地编辑事务隔离（非正式认证）

- 父ZIP R245F24 SHA256 `3d74464141f2046342366a223aaffae96fdfb2f8c51985e99503de92b79c206b`，3296/3296逐文件继承。
- 真实Chromium复现2项旧数据丢失：冻结JPEG和来源注册表SHA通过后，挂起JSON读取，用户新增备注或M-vis-04笔画，较早导入完成时旧版覆盖本地编辑。
- 隔离候选新增独立的备注/描记editRevision及导入请求序号，异步读取后、提交前校验；新编辑或较新导入出现时拒绝过期导入，正常导入继续可用。
- 新Chromium 17/17；继承27+101+88+20+379=615；合计632/632选定QA。379项包含170条原生RGB裁框。旧错误复现2项不计pass。
- 新累计ZIP **3307文件**，SHA256 `d2da0599d6f72bb128394101f31107f5e94d2bbf38ae09df2a340968b40cbe1e`；Python zipfile和系统unzip双独立恢复各3307/3307 SHA，分别运行632/632选定QA，QA后0漂移。完整历史全量QA未运行。
- 环境仅Chromium about:blank注入原始冻结JPEG。127.0.0.1真实同源Chromium仍被管理员策略阻断；真机、真实读屏、合法同源高清逐笔及生产迁移均not-run。
- GitHub main仍R246(`03c29e0`)，其3054成员原始累计ZIP未获得；R11/R12/R35原始ZIP及R12 20SVG缺失，不能宣称完整历史恢复。
- **T01正式0/25键、T02正式批准ID0、T05真实缺根数未知、原始T00–T11仍0/12 Accepted。** UI-track不冒充原始任务。
- 冻结V0.35 HTML SHA `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`、2008 JPEG SHA `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`、176旧编码、正式SVG、用户Storage均未修改。

本证据对应独立累计ZIP中的`v036_r245f25/`可复验候选与QA脚本，不将其合并至冻结生产入口。
