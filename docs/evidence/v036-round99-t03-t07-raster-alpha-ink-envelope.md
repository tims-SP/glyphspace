# V0.36 R99 · Root T03/T07 Chromium 独立alpha像素绘制包络（隔离证据，非验收）

2026-10-25。父版R98累计ZIP：1359文件，SHA256 `1e1aeeac3c0dd321f5e2f22d26eb00e133ef6f6ecc7087c46dc3e231155da7ed`；已逐文件复验1359/1359并继承。R99累计ZIP：**1366文件**，SHA256 `7fe43e62975b1e1b339f46674d452c519a3ad6b6d130e448e8c2f670d12f4fea`，ZIP本体不在GitHub。

## 实际新工作

以R94 SHA `a9c913da95de58a8f718186cd8c49d8678c930e7e9ff6c809f3dc04e3aebc592` 的隔离SVG数据为固定输入，在真实Chromium `about:blank` 中，逐个将151候选UID的原始草案Path、局部变换和stroke重新构造为独立SVG，通过Image→Canvas读取alpha像素，计算实际绘制边界，与100×100坐标中的草案inkBBox比较。分别使用400×400和800×800两个栅格分辨率，**302/302实例非空且边界超出预测不超过1个栅格像素**；最大单侧超出0.244/100和0.120/100。H:7「皮头」真实stroke也在核验范围。

三个主动负例：H:7描边加粗、M:0清空路径、M:0平移几何，均导致绘制指纹变化并被空白/包络门禁检出，**3/3通过**。绘制指纹为非密码学FNV32，不可代替文件SHA256或安全认证。R98原有14组定向QA两套独立恢复环境均重新执行通过；完整历史全量QA未运行。

## 独立恢复与限制

Python zipfile及系统unzip各解压**1366/1366**，解压前后逐文件SHA256均一致；两份恢复环境各执行R99新Chromium QA及14组R98继承定向QA。首次组合验证超时后，将套件拆分重跑，超时未计pass。

本轮是**草案Path的实际像素渲染一致性**，不是2008原图逐笔认证、正式SVG资产许可、生产T03/T07集成或真实标签/圈注碰撞验收。冻结V0.35 HTML SHA `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`、2008 JPEG SHA `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`，正式SVG、176编码、用户存储未修改。

**T01正式0/25、T02正式永久ID 0、原始T00–T11仍0/12 Accepted。** 第10–12/35轮ZIP及第12轮20 SVG缺失；合法同源高清图与许可未取得；真实同源Web Locks/localStorage本轮not-run（此前blocked），真机/真实读屏not-run。源脚本、逐UID栅格化审计及双恢复日志在外部R99累计ZIP中，不伪称已上传GitHub。
