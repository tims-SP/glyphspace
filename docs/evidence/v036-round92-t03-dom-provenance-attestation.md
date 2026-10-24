# 字间 V0.36 · 第92轮 Root T03 SVG DOM来源完整性门禁

> 2026-10-24；隔离实现与真实Chromium `about:blank`证据。**不是原图逐笔认证、生产集成或正式验收**。

## 发现的真实回归缺陷

第91轮的`apply([])`仅校验SVG `<use>`总数及UID是否在全局候选集合，未核验每键UID成员与顺序、`href`和`<defs>`内实际Path。独立Chromium中已复现：修改`<use href>`为`#forged`、把一键的UID替换成其他键UID、修改SVG Path `d`，第91轮仍返回成功。

第92轮在**新隔离模块**增加全25键full/mini和当前single视图成员及顺序核对、151 UID/149草案资产href绑定、149资产Path与stroke/scale原值比对、100×100 viewBox与外部transform漂移拒绝。撤销与导入使用先预检后提交的内存事务；单键切换先检查旧DOM再恢复overlay。正式`index.html`未改。

## 独立测试与累计档案

- 父第91轮ZIP SHA256 `b15be0b2c893ae448b7a80b59939098029c7c89ae3e149744690f1a6669367c3`；**1283/1283父成员逐文件SHA继承**。
- 新Chromium DOM QA **27/27**（包含3项R91缺陷复现）；第91轮旧Chromium **27/27**；R77/R78/R83–R90旧QA **10/10组**。
- 第92轮累计ZIP **1296成员**，SHA256 `9bc741610e45c740e149110ed2fe208dd5a269e6961a7e810108a16d5c391dfa`；Python zipfile与系统unzip独立解压各1296/1296，两个环境均重跑上述新旧QA，QA后SHA **1296/1296**一致。ZIP本体在外部交付，不在GitHub。
- 首次组合复验程序在第一环境成功后超时，第二环境随后单独完成；超时不计为通过。未执行全部历史轮次QA。

## 不得提升的状态

原始T00–T11仍**0/12 Accepted**；T01 **0/25**正式认证、真实缺根数未知；T02正式永久ID 0；T03正式生产内核未集成；T05补图未完成。第10–12、35轮ZIP和第12轮20SVG缺失，同源高清合法原图未取得。真实Web Locks/localStorage为blocked/not-run；Android/iOS真机及真实读屏not-run。V0.35冻结HTML、2008原图、176旧编码、正式SVG及用户原有存储未修改。

本轮属于原始**T03 SVG坐标内核**，不是第36–40轮UI-track的旧“T03/T05”命名。
