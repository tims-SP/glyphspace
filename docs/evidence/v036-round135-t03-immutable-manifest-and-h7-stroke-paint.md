# 第135轮 · Root T03 SHA绑定不可变入口与H:7描边paint边界

**2026-10-26，隔离技术证据，非来源认证、非正式验收。**

## 实际缺陷

R134 `verifyManifestBytes`只将验证后的对象引用登记在WeakSet中，嵌套paths仍可变。Chromium独立复现：SHA校验后将H:7首Path的strokeWidth由7改成0，旧R134 mountView仍挂载修改后字形。R135新增`immutable_paint_gate.js`，经SHA验证后递归Object.freeze，受控入口只接收已冻结manifest。路径strokeWidth与光学校正ox后置修改均被拒。**旧R134公开API仍可绕过新入口，尚未完成生产整合。**

## 真实stroke墨迹测量

H:7是151个旧可视实例中唯一使用stroke的字形（3条round-cap Path，strokeWidth=7）。Chromium 144.0.7559.96独立about:blank上下文挂载full/mini/focus三视图，将自包含SVG在800/1600/3200像素下分别栅格化，alpha>16提取paint边界；9/9与解析式stroke-inclusive inkBBox在量化+0.08/100容差内一致，最大差0.155/100（800px），同分辨率三视图结果一致。9/9将预期宽度缩小1/100的错误对照被拒。浏览器DOM BBox不包含完整stroke，不能直接当作墨迹边界。

## 复验与边界

- 父R134 ZIP SHA256 `3c9e9fc821afbed248fe45d20018e41c5fe1818be12a928bae0a1cf5f2fbd274`，1753/1753逐文件SHA继承。
- R135累计1760文件，ZIP SHA256 `dbc54639aa409d773aa39316c91bad1fe040b9ae6756d6413fb7ed1c67072c43`。新14/14+继承175/175，Python zipfile与系统unzip两套独立恢复各189/189 QA。QA重写4个历史审计/pyc文件并产生2个临时文件，均已记录副作用，按ZIP恢复原字节并清理临时文件后各1760/1760 SHA一致；不声称测试执行期间零写入。
- 完整历史QA not-run；真实共享原点此前blocked、本轮not-run；真机、真实读屏not-run；来源许可及逐笔认证未解决。原始T00–T11仍0/12 Accepted，T01 0/25、正式永久ID0、T03未生产集成、T05未完成；R10–12/R35原始ZIP与R12的20SVG仍缺失。
- V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`，2008原图SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`；176旧编码、历史正式SVG、用户存储未改。

隔离代码与机器审计在R135累计ZIP的`v036_round135/`内，ZIP本体不在GitHub。回滚删除R135隔离目录；不得替换冻结入口。
