# V0.36 第147轮 · Root T04：真实浏览器同源局部旧坐标影子预检（非正式验收）

## 证据与任务边界

原始任务 **T04 存储与旧版迁移**（关联T00/T02，依赖T02/T03尚未正式Accepted）。UI-track无新增任务。本轮在仓库的 `scripts/qa_v036_t04_disposable_origin.py` 中新增冻结V0.35的**局部v16旧存储**双标签只读影子预检；不使用用户已有origin/profile，不写生产HTML或真实localStorage。

冻结HTML SHA256：`fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`。测试从该HTML提取25键、156个旧槽默认坐标；只在随机端口127.0.0.1临时HTTP原点生成G/K/X三键合成样本，明确保留22个缺席键、3条人工模拟修改，禁止把缺席键推导成用户编辑或批准永久ID。另验证源SHA变化拒绝、原始raw和旁路sentinel不被只读程序改变。

## 实际测试

- GitHub Actions授权临时原点真实Chromium双标签：**33/33通过**，含此前Web Locks/localStorage/回滚与本轮冻结v16部分来源影子预检。url工作流运行https://github.com/tims-SP/glyphspace/actions/runs/40365890296（commit `0ced66a61e2dfa17363fbf6f0b8e9fa0c42c0068`）。静态仓库完整性run `40365890764` success。
- 初次提交 `cde6fd3ed9ba8ed1b1c02ec62ab784d17029c27a` 的Python正则误转义导致CI失败；后续修复后成功，**不得把首次失败计为通过**。
- 本地真实临时原点：`ERR_BLOCKED_BY_ADMINISTRATOR`，标记**blocked**，不计pass。
- 新Node WebCrypto/FakeStore独立14/14；实际重跑R142–R146来源定向QA 1576/1576，完整历史全量QA not-run。
- R146父ZIP SHA `e01168b3a786903568a8d6173d544f967affd2beb4f71304275d2790764287eb`，1855/1855父文件SHA一致；R147累计1865文件SHA `bebcacaafadb23734dc11bb76ac095af21c744fa7b2c2e6fbec65c54c8153f70`。Python zipfile及系统unzip两套独立解压各1865/1865，执行1576旧+14新=1590/1590定向QA，QA后1865/1865 SHA不变。

## 不能由本轮推断的结论

本轮并非实际用户V0.35→V0.36迁移；没有生产ID/asset绑定，没有迁移旧humanReviews、签名过期与冲突回滚全链，也未批准任何来源字根。旧v16的JSON重复键检测仍须另行失败关闭，不能以当前JS JSON.parse通过代替该项。原始T00–T11 **0/12 Accepted**、T01正式0/25、正式永久ID0；真实缺根数未知。缺第10–12、35轮原始ZIP与第12轮20SVG，合法高清原图许可、逐笔、真机与真实读屏QA仍缺。

## 修改范围与回滚

远端仅改隔离T04 QA脚本、状态/追踪/验收文档、任务账本和SHA清单；正式 `index.html`、2008 JPEG、176旧编码、历史正式SVG、用户存储均未动。回滚本轮隔离代码与文档即可，不需要改用户数据。
