# R202 · Root T01/T02 冻结来源裁框完整性守卫（非正式认证）

2026-10-29。父R201累计ZIP SHA256 `4f190390fd8cacb37e845e8e6de71e913a03a6c8f5b1d05294954e8a9ce63418`，真实读取2535个成员并逐文件SHA继承。原始T00–T11编号不变。

## 实际发现与复现

R201来源身份审阅图只校验冻结JPEG总SHA，未将R156中每个观察的nativeRect/nativeRGBSHA256与同一账本的161条sourceCrops记录及JPEG原始RGB像素做完整互证。隔离内存篡改 `legacy:J:4` 的nativeRect为 `[1200,500,13,11]`，并计算该位置真实JPEG RGB SHA后，R201仍接受并生成170观察、133分组。R202对同一篡改拒绝：`crop-observation-geometry-disagreement`。**没有修改历史R156或R201文件。**

新增隔离Python守卫 `v036_round202/native_source_crop_integrity.py`，实际从冻结1536×1086 JPEG重新计算170条观察、161条sourceCrops原生RGB SHA，并核对161组成员关系、键位、矩形、像素哈希；异常/伪造认证/永久ID均失败关闭。M/V/K/E/B/J/R/X分别列入高风险摘要。仅为来源账本防伪与一致性校验，不是字根笔画认证、高清原图认证或合法许可证明。

## 真实QA与恢复

R196像素34、R197光学35、R198三视图41、R200静态18、R201图55与静态16：**旧199/199**。R202对抗与正向29、冻结静态12：**新41/41**。本轮实际**240/240**；R199/R200真实Chromium套件尝试超时，not-run，不计pass。完整历史全量QA、真实同源Storage、真机、真实读屏not-run。

R202累计ZIP **2547成员**，SHA256 `b02c6b499e4f29ae557880f22970a016bcd978286df7b8ce428b0baab72d02d2`。Python zipfile与系统unzip独立恢复，各2547/2547逐SHA一致，各240/240 QA通过，QA后原文件SHA未变化。源码、对抗QA、来源审计和逐文件SHA清单位于隔离累计ZIP；未将未认证的原图像素/正式SVG推入生产入口。

## 正式验收边界

T01正式认证0/25键；T02正式永久ID0；真实缺根数未知；原始T00–T11仍**0/12 Accepted**。R11/R12/R35原始ZIP及R12 20SVG缺失。2008同源高清原始字节及许可/逐笔复核未完成。冻结V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`，2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`；176旧编码、生产入口和用户localStorage未修改。
