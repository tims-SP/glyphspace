# R134 · Root T03 SHA绑定解析式SVG三视图挂载（隔离、非正式验收）

日期：2026-10-26。原始T03仍为SVG坐标内核；本轮不属于UI-01至UI-05。源码与QA保存在外部R134累计ZIP，GitHub只同步证据，未改生产入口。

## 实质技术进展

- R125 SHA绑定的R50真实Path、R54解析式inkBBox、R53几何生成151条未认证实例计划；100×100 viewBox、锚点和光学偏移保持同源。
- R132符号闭包、R133跨SVG命名空间隔离与R125几何变换组成新的独立三视图挂载实现。full/mini/focus分别100/48/240px；151条草案×3=453个同时挂载SVG实例，453个symbol ID唯一。
- 450个fill-only实例的浏览器实际BBox与解析式计划一致，最大归一化误差0.000310/100（容差0.25/100）。H:7属于round-stroke特例，浏览器BBox不包含stroke，与stroke-inclusive解析式边界相差约0.9044/100；该3个视图实例没有计入450个fill-only通过分母。
- Chromium about:blank无WebCrypto subtle；增加纯JS SHA-256对manifest原始UTF-8字节验证。篡改拒绝、未验对象拒绝、反序ID与几何不漂移、6个对抗输入拒绝通过。SHA只验证草案字节，不证明原图形态真实。

## 父档案、QA与正式边界

- R133父ZIP SHA256 bd866c1e436d8f3d9412fc4e3e47f2543c17f3f8bc806c07a307da8d0a64bbc4；1742/1742成员SHA继承。
- R134累计ZIP 1753文件，SHA256 3c9e9fc821afbed248fe45d20018e41c5fe1818be12a928bae0a1cf5f2fbd274。Python zipfile与系统unzip双独立解压，QA前后各1753/1753 SHA一致，各新10+继承165=175/175定向QA。
- 完整历史全量QA not-run；真实共享原点本轮not-run（既往独立profile被管理员策略阻断）；真机与真实读屏not-run；逐笔与高清合法许可未认证。
- R10–12/R35原始ZIP与R12的20SVG仍缺。T01正式0/25、T02正式永久ID0、T03仅隔离预集成、T05正式补图未完成，原始T00–T11仍0/12 Accepted。
- 冻结V0.35 HTML SHA256 fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc；2008 JPEG SHA256 df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49；176旧编码、正式SVG及用户存储未修改。

回滚：从累计ZIP删除v036_round134/隔离文件并恢复R133。下一轮优先H:7真实stroke绘制边界、T03集成前提及历史来源缺口。
