# V0.36 第96轮：B/J/R/X/V七个微形来源物理观察交叉账本（非正式验收）

日期：2026-10-24。原始任务 **T01**（关联 **T02/T05**），不属于UI-01–05。

从第41轮七项未映射来源清单、第46轮156项来源阻断账本和2008原始JPEG，建立 **7个来源锚定的物理观察ID**，覆盖B/J/R/X/V五键。身份基于原始JPEG SHA、键位、历史候选标签、原生像素坐标与ROI RGB SHA；不复用旧槽作为唯一身份。七项原生RGB与第41轮第9轮提案采框逐项一致；五键原始PNG文件字节SHA及JPEG键位裁框RGB一致。

| 来源观察 | 与旧槽原始采框相交 | 保留的身份限制 |
|---|---|---|
| B vis-02 | B:7 | B:7命名空间阻断；不能自动认作「孑」 |
| J vis-07 | J:1 | J:1「曰」不自动等同微形 |
| R vis-02 | 无 | 无旧裁框交集不代表已认证新字根 |
| V vis-06 | V:3、V:4 | V:4命名空间阻断，不能自动合并/拆分 |
| V vis-07 | V:4 | 同上 |
| X vis-02 | X:0 | 「纟」与微形身份未认证 |
| X vis-03 | 无 | 仍待逐笔认证 |

所有观察：`referenceShapeId=null`、`assetId=null`、正式永久`instanceId=null`，`sourceCertified=false`，`strokeCertified=false`，`legacyBinding=null`。**7个物理ROI不是7个正式字根**，真实缺根数量仍未知。审阅图只是原生像素放大，不生成新笔画。没有更高分辨率同源合法字节与可分发许可。

父第95轮ZIP：1331文件，SHA256 `7deea5a9de203a1cefee6f52ca988f7d26c5588b6b0316a68fab42c2b1dd6db0`，1331/1331逐项SHA继承。第96轮隔离累计ZIP：**1340文件**，SHA256 `d1e609c29a3852e724a6192ef2795c993a85cdc21a2cddfb9a11163a05a7be0c`，ZIP原始字节不在GitHub。Python zipfile和系统unzip各1340/1340恢复、两套环境各12组新旧QA通过且QA后1340/1340 SHA一致。新增35/35 QA，历史第81、86–95轮11组定向QA重新运行通过，完整历史全量QA未执行。第一次组合双恢复脚本超时，随后系统unzip环境单独重新运行12组并通过。

源图SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`；冻结V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`。第41轮清单SHA `c960dac4882ade911399e53a8a3da27bd876b40024988f88070ac3e0956160a9`；第46轮账本SHA `a1fcff7e48794e20275859746ce014318c4c407f51312bc3c58dd5f065436d67`。完整代码、原生像素审阅图、交叉账本、父SHA清单和双恢复证据在本轮用户交付ZIP。

第10–12、35轮完整ZIP及第12轮20SVG仍缺；正式T01 **0/25**、T02正式永久ID **0**、T00–T11 **0/12 Accepted**。真实共享原点Web Locks/localStorage本轮not-run（此前管理员阻断）；Android/iOS真机及真实读屏not-run。冻结生产HTML、正式SVG、176编码和用户存储均未修改。
