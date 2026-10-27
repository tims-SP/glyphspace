# R170 · Root T01/T05 官方图候选来源与M键隔离掩码预检（非验收）

2026-10-27。已通过GitHub连接读取main的六份强制规范与第169轮父ZIP原始字节，父ZIP SHA256 `a428e4ae95cfc039b052c877b269211a8a226b2a96f4132d9fbf7713676181b5`、2094/2094逐文件继承。

## 新发现：高分辨率候选归档

在 [06wb教程资源](https://06wb.github.io/Tutorials/index.html) 找到标记“第三代五笔字型（新世纪版）简体、繁体字根键位图(官方)”的ZIP；通过GitHub连接读取仓库 `06wb/06wb.github.io` 的 `Tutorials/第三代五笔字型（新世纪版）简体、繁体字根键位图(官方).zip`，实际在内存解析ZIP中央目录：

- Git blob SHA1：`542ee2067965b2d5498ad211dfd763ca0e7f6447`，ZIP原始字节数359250。
- 仅有一个成员 `zgjwt_jf_1479x843.jpg`，DEFLATE压缩359110字节、声明解压416166字节、CRC32 `2e28738d`。
- **尚未把候选ZIP原始字节落地容器**；JPEG成员未解压、未SHA256、未确认图像尺寸/与冻结2008图同源。文件名的1479×843不能代替实际解码。
- 网站“官方”标签不是独立的版权/再分发许可。不得发布候选原图，不得认定25键通过原图认证。

## M键T05隔离研究

以冻结2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49` 和R101来源裁框，复核4项未绑定M观察。M-vis-04因相邻墨迹所有权不明保持**blocked**，不分配SVG；M-vis-06/07/08仅将meanRGB<170的原生像素掩码游程编码为100×100 SVG Path（无bitmap或字体），是**低清像素掩码研究草案**，不是平滑笔画、形态认证、正式根或可用生产SVG。全部 `referenceShapeId/assetId/instanceId=null`，认证和生产绑定标志为false，真实缺根数仍未知。

## 真实复验

- R169父2094/2094 SHA继承；R170累计ZIP **2106文件**，SHA256 `d3fbd466fabee4bcb58c9eaceae4fd1df43b7cb923d02c64250295c247ae8d8d`。
- 新增隔离QA23/23、真实重跑选定继承333/333；Python zipfile与系统unzip两套独立恢复各2106/2106 SHA、356/356 QA、QA后2106/2106 SHA一致。
- 历史全量QA、真实同源Web Locks/localStorage、Android/iOS真机、真实读屏均**not-run**。冻结V0.35、2008 JPEG、176旧编码、正式SVG、生产入口和用户存储均未修改。
- 原始T00–T11仍**0/12 Accepted**，T01正式0/25，T02正式永久ID0，T05正式补图未完成；缺R11/R12/R35 ZIP及R12 20 SVG。

下一步：先获取候选ZIP合法原始JPEG字节并独立解压、核对图像SHA/像素/许可；再进行M/K/E/B/J/R/X/V逐笔审阅。不得将掩码或网站标签作为来源认证。
