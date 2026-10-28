# V0.36 R182 · Root T04 真同源隔离暂存、回滚与恢复（非正式验收）

日期：2026-10-28。原始任务T04仅指旧版存储与迁移，不是UI-track。**T00–T11仍0/12 Accepted，T04未验收。**

## 实际远端Chromium证据

- R181真实浏览器原语CI run [40619051747](https://github.com/tims-SP/glyphspace/actions/runs/40619051747) 成功，16/16；原始artifact ID 12786571103，ZIP SHA256 `3402d2e1a87dad42992a58e1f0bd3d4ea63b6c3cfbd545d515814cafc67b2d08`。真实127.0.0.1双标签Web Locks、storage事件、WebCrypto、来源变化与context隔离。
- R182新隔离事务CI run [40624848783](https://github.com/tims-SP/glyphspace/actions/runs/40624848783) 成功，**24/24**；原始artifact ID 12788508330，ZIP SHA256 `8908cf158db5836bd41a54b40800affc70bff54a9a9e0a06cdc6bd82a81eda60`。源代码 `scripts/qa_r182_real_quarantine.py`；临时HTTP服务器、新非持久browser context、真实localStorage与Web Locks；检查隔离影子、journal、普通故障回滚、模拟崩溃后重载恢复、过期来源拒绝、损坏journal拒绝、来源不被恢复覆盖、context隔离。**未访问用户原有存储。**
- R182测试的是独立浏览器fixture事务算法，**不是**R180 Node Map代码在浏览器中直接执行，更不是正式迁移或正式永久ID分配。没有证明真实断电恢复、生产写入、跨设备兼容或完整历史回归。

## 累计档案和本地复验

- R181父ZIP SHA256 `060e219c8874f4164e7e5683159d85db446fc23dbfc7acccf07a5871e4ce319f`，2234/2234成员逐字节SHA继承。
- R182累计ZIP 2247文件，SHA256 `0d44faa8e833f67eea49cc314c92559e4224055780dc9b9f25b6e729ae1e5b23`；Python zipfile与系统unzip独立恢复各2247/2247 SHA、各109/109选定本地QA，QA后SHA一致。实际本地旧95/95+新增静态14/14；旧递归1181 QA曾超时，**不计通过**；完整历史全量QA not-run。
- 本地真实Chromium 127.0.0.1仍 `ERR_BLOCKED_BY_ADMINISTRATOR`，新增26项本地草案浏览器QA未运行，不能混入远端24/24。
- 第10轮原ZIP已嵌入R164；第11、12、35轮原ZIP及第12轮20 SVG仍缺。第三方高清许可、逐笔形态认证、真机和真实读屏均未完成。
- 冻结V0.35 HTML、2008 JPEG、176旧编码、历史正式SVG、生产入口及用户原有存储未修改。

下一步：将真正候选迁移实现抽离为浏览器兼容核心，再对该**同一代码**执行真实同源事务、故障恢复与跨标签冲突测试；T01/T02/T03依赖未满足前不得集成正式入口。
