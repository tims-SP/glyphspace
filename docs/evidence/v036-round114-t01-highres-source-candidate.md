# 第114轮 · T01/T02 外部高清源候选与原始字节远端核验（非正式验收）

2026-10-25。原始Root T01参考图清点、T02身份来源，关联T05完整性补图；UI-track不占用任务编号。

## 新来源与独立字节核验

上游为公开社区镜像 [06wb/06wb.github.io Tutorials](https://github.com/06wb/06wb.github.io/tree/master/Tutorials)，目录标称“官方”，但**无独立确认的著作权/分发许可**。本仓库新增 [只读源探针](../../.github/workflows/v036-t01-reference-provenance.yml)，[GitHub Actions run 40175565336](https://github.com/tims-SP/glyphspace/actions/runs/40175565336) 已 success，真实读取两份ZIP原始字节、解压JPEG、核对图像尺寸与SHA256；不上传图片。

| 资源 | ZIP SHA256 | JPEG SHA256 | JPEG尺寸 |
|---|---|---|---|
| 高清简体ZIP（996823B，Git blob 92f37f92c7e7ab4eb0ba6fe084112d9a56cd2dc4） | `fb7a9984a84be12a71d71dc86088b8859762ca97cb9a3db173b4a8adaf0b9707` | `47c5d53f6cf57ac67c957c6510a3e2696072c3ce63e73024ed025367f31c600e` | 3508×2480，zgjwt_jt_3508x2480.jpg |
| 简繁ZIP（359250B，Git blob 542ee2067965b2d5498ad211dfd763ca0e7f6447） | `eaad30ee3ee50b54c6631967dcb794ca95503190ae6f3ea3f7ab7f8be16e6179` | `e9593765a1e4d43bdd0d7cb34ea3302ffd566288252245272392081b543667c4` | 1479×843，zgjwt_jf_1479x843.jpg |

冻结2008参考JPEG为1536×1086、SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`。整图与四象限各64位dHash比较高清简体图，Hamming差异为**1、1、0、2、0，共4/320位**。仅证明布局高度相似，**不能证明同一原始字节、每笔形态相同、字根完整或法律许可**。外部JPEG未加入仓库及累计ZIP；本地原始高清字节获取not-run/blocked（容器无法外网直连），远端CI已核验真实字节。

## 可复验的隔离累计档案

第113轮父ZIP `acdd2f820af7e7b2dc45b371edb9856a1e02d9dd26acff56f93ab0ece43dc8e2`，1509/1509逐项SHA继承；第114轮外部累计ZIP1519文件、SHA256 `a24303d1e53c4643f7c8a7bbf3c68925c1225a4f76b4918dc1ba6f0aeb5af50c`。新增31/31只读来源+合成恶意ZIP负例；继承R113 34、R112 36、R96 35、R95 36、R84 124；Python zipfile与系统unzip各独立恢复1519/1519并在恢复环境重跑**296/296**，QA后1519/1519 SHA不变。完整历史全量QA not-run。ZIP仅外部交付，不在仓库。

## 禁止越级

T01正式0/25键，T02永久ID0，T05正式补图0，原始T00–T11 **0/12 Accepted**；M四未绑定、K/E同源冲突、B/V命名空间、36旧未匹配不自动解除。第10–12/35轮ZIP与第12轮20SVG仍缺。原图逐笔/许可/Android/iOS真机/真实读屏/用户同源迁移均未验收。冻结正式index.html、176旧编码、正式SVG、用户localStorage完全未触碰。
