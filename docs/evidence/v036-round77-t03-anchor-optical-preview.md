# V0.36 第77轮 · Root T03 100×100锚点与光学校正隔离内核（非正式验收）

- 日期：2026-10-24。任务：原始**T03**；**T07仅前置**。第36–40轮UI实验独立为UI-01～UI-05。
- 本轮起始GitHub main记录第76轮。第76轮父ZIP原始字节SHA256：`036d42a90875b30dfc475fbbd4feaccdc2b4a775f6ecf05486f58365db66b76d`，**1111/1111**逐成员SHA继承。父ZIP与本轮ZIP均不在GitHub。
- 第63轮151个草案实例JSON字节SHA256：`a2a9ede90342066a72c6a0d896def7709d0dbe1ca8572b57547492b163afaa1b`。冻结V0.35 HTML SHA256：`fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`；2008参考JPEG SHA256：`df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`。
- 新增隔离`anchor_optical_preview_round77.mjs`：强制来源原始字节SHA门禁、151实例几何与原transform反推一致性、五种ink锚点、独立ox/oy光学校正、移动与撤销、只读内存预览、SHA绑定导出/导入（篡改与部分导入失败关闭）、同键草案墨迹矩形碰撞预检。
- 默认151草案inkBBox矩形无相交配对；合成移动能够被检测为碰撞。**此结果不含标签/圈注、焦点态或逐笔真实墨迹认证**，不能当T07正式验收。
- 新增Node QA **179/179**，历史第76轮及之前QA **10/10组**通过。第77轮累计ZIP **1122文件**，SHA256 `314c5dd3033923f20a959a8df8e555e95460d975284f2df72e59528ecb357e2b`；Python zipfile与系统unzip两次独立解压各**1122/1122**、各自复跑新旧QA并复核QA后文件SHA一致。
- 仍缺第10–12、35轮完整ZIP及第12轮20 SVG；同源高清原图合法字节未取得。K/E/B/V来源阻断与M候选风险不解除；T01 **0/25**、正式永久ID **0**、T00–T11 **0/12 Accepted**。
- 本轮真实同源Web Locks/localStorage **not-run**（此前独立profile导航受管理员策略阻断）；Android/iOS真机、真实读屏均**not-run**。未触碰用户存储、正式SVG、176编码和冻结生产入口。
- 本轮新增代码与全部审计、恢复日志只在外部累计ZIP的`v036_round77/`目录；仓库本文件仅保存可追溯摘要。仓库CI结果需另行核实，不以本地QA代替。
