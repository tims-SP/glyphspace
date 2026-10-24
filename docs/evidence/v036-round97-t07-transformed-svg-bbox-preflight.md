# 第97轮 · Root T07 真实Chromium变换后SVG矩形碰撞预检（非正式验收）

日期：2026-10-24；关联原始T03。**T07仍未Accepted，正式T00–T11仍0/12。**

## 本轮真正发现与技术修正

在第94轮隔离三视图SVG HTML中，Chromium的`<use>.getBBox()`返回未应用use自身transform的字形局部框。若直接使用该框做同键碰撞，完整视图409/409对、迷你409/409对、M单键6/6对都会被**错误报告为重叠**。新独立QA用`svg.getCTM().inverse().multiply(use.getCTM())`把四角映射到100×100键内坐标，再做真实DOM几何对照。该修正针对原始T07位置/碰撞，不是第36–40轮UI轨道。

H:7「皮头」为描边草案，Chromium `getBBox()`不含stroke；该实例以已有来源绑定草案`inkBBox`进行保守几何预检，stroke扩展折合键内宽度0.9016单位。**未宣称像素级真实墨迹轮廓已验收**。

## 实际执行证据

- 真实读取父第96轮累计ZIP：**1340/1340**原成员逐文件SHA256一致；父ZIP SHA256 `d1e609c29a3852e724a6192ef2795c993a85cdc21a2cddfb9a11163a05a7be0c`。
- 第94轮隔离HTML来源SHA256：`a9c913da95de58a8f718186cd8c49d8678c930e7e9ff6c809f3dc04e3aebc592`，不修改来源。
- Chromium about:blank的1440×900、390×844两个独立视口：各完整151、mini151、单键M4个use，共**306/306几何对照**；每视口409+409+6=**824对矩形**，经CTM转换后0对相交；原始getBBox法824/824误报。
- 最大几何差异<0.000004/100；H:7两视图stroke单独标注，非像素级描边认证；每视口1次非法transform被检测，回滚后无异常。
- 重新执行R97新增与R81/R86–R96选定旧QA共**13/13组**；完整历史全部轮次QA**not-run**。
- 累计ZIP **1348文件**，SHA256 `bb744069860dd24c51e5fe08a6c81e63ff7b94768c3fae822533a7e8cb08d0d5`；Python zipfile和系统unzip独立恢复各**1348/1348**，两份恢复环境各13/13组QA通过，QA后逐文件SHA一致。ZIP本体不在GitHub，保留于隔离交付文件。
- 临时独立Chromium访问127.0.0.1仍`ERR_BLOCKED_BY_ADMINISTRATOR`；真实同源Web Locks/localStorage事务**blocked/not-run**，未触碰用户存储。

## 严格边界与后续

**不能据此声称T07正式碰撞0**：原始参考图25键正式认证0/25、真实缺根数未知，正式永久ID0；真实stroke轮廓、圈注、字母/区号、标签、全部三视图生产集成、真机与真实读屏均未验收。第10–12/35轮完整ZIP及第12轮20SVG仍缺，合法同源高清原图尚未取得。

冻结V0.35 `index.html` SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`、2008原图SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`、176旧编码、正式SVG及用户原存储均未修改。正式12任务`accepted=false`。
