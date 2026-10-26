# 第133轮 · Root T03 跨SVG挂载命名空间冲突复现与修复（隔离、非验收）

日期：2026-10-26。父ZIP SHA256 `670c139b1017a793ae6e84155874a633cbd94a602b24dd25f4eb00a1b28d184c`，1734文件；新累计ZIP SHA256 `bd866c1e436d8f3d9412fc4e3e47f2543c17f3f8bc806c07a307da8d0a64bbc4`，1742文件。完整历史连续性仍缺第10–12、35轮ZIP及第12轮20SVG。

## 可复现的实际缺陷

R132的独立`isolate()`默认使用固定前缀`gs132`，在单独SVG内闭包成立，但把两个隔离SVG挂入**同一个DOM**时，会产生重复`<symbol id="gs132-def-1">`。独立Chromium`about:blank`中构造两个源SVG（相同源symbol ID、不同矩形Path）：原始几何宽分别10与80，R132并列挂载后实际`getBBox().width`分别为10与10；第二个字根错误引用了第一个symbol。这是渲染正确性缺陷，不是源图身份判断。

## 修复及实测

新增隔离文件`v036_round133/svg_mount_namespace_guard.js`，在R132递归闭包上加入每次调用独立的单调命名空间、已占用DOM ID检测、非symbol内部ID重映射、ARIA IDREF重写与重复/未解析引用失败关闭。修复后同一测试宽为10与80，两个symbol ID不同。

从SHA冻结V0.35 HTML中提取主键盘25个有根键位的151个旧可视实例，将每键的多个字根隔离后**同时挂载到同一Chromium DOM**：151个本地symbol ID互不重复，151/151原生`getBBox`四分量与原始根一致，最大差0；5个对抗场景（嵌套内部ID、重复内部ID、有效/无效ARIA、外链）符合预期。新QA 12/12；继承R132/R131/R130/R125/R123定向QA 153/153；Python zipfile与系统unzip两次独立恢复各1742/1742 SHA一致、各165/165定向QA通过。源HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`，2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`。

## 边界与阻断

R133代码仍只在累计ZIP隔离分支，未集成仓库生产入口；`about:blank`几何验证不是正式原图逐笔、真实设备像素或屏幕阅读器QA。T01正式认证0/25键、正式永久ID0、原始T00–T11 0/12 Accepted；真实共享原点Web Locks/localStorage此前管理员阻断，本轮未重试，记blocked；Android/iOS与真实读屏not-run，完整历史全量QA not-run。没有改动冻结HTML、正式SVG、176编码或用户存储。回滚仅移除R133隔离目录并恢复R132 ZIP。
