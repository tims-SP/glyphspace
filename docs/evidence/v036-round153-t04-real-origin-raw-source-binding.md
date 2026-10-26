# V0.36 R153 · Root T04 真实同源raw来源绑定回归（隔离、非验收）

- 执行前 main `f383068dc80195b6d60e0c0748bf11a43ae0583e`，父R152 ZIP SHA256 `2ed630217d3b85a20d18eba07d636d31fe93885212d50eb0a2861ea8a19b62e4`，1910/1910文件逐SHA继承。
- 本轮将R152真实原始JSON来源绑定接入独立授权Chromium双标签临时127.0.0.1原点，测试WebCrypto、Web Locks、localStorage跨标签事件、SHA/旧槽别名/3个编辑、伪来源SHA/伪编辑/重复键拒绝和不写入原始数据；源码 `scripts/qa_v036_t04_r153_source_bound_origin.py`，工作流 `.github/workflows/v036-t04-disposable-origin.yml`。
- 首次CI 40417492203失败：新增脚本引用了不存在的 `v036_r153_issued_plan.js`；已实际下载失败产物，确认2/3前置检查通过、FileNotFoundError，随后修正为R152原文件。新CI运行40417922284最终结论必须独立复核，不得预记pass。
- 本地新真实同源2/3前置检查，浏览器 `ERR_BLOCKED_BY_ADMINISTRATOR`：**blocked**。R142–R152继承定向QA 1715/1715（其中R148 about:blank仅解析9项），R147独立Python命令误传参数不计入分母。完整历史全量QA not-run。
- R153累计ZIP 1918文件，SHA256 `106319af615d7a5afb4c122306d649435137d7c502e1a084c7de45137c5b378d`；Python zipfile和系统unzip两套独立恢复各1918/1918 SHA，实际重跑1715/1715定向QA，QA后逐文件SHA一致。
- 本轮无生产迁移或回滚，未触碰用户原有存储；T00–T11 0/12 Accepted，T01 0/25正式认证，T02正式永久ID 0，T03未生产集成，T05缺根数未知。R10–12/R35原始ZIP与R12 20 SVG未恢复；高清原图合法许可、逐笔、Android/iOS真机、真实读屏未完成。
- 冻结V0.35 HTML、2008 JPEG、176旧编码、历史正式SVG与生产index.html均未修改。
