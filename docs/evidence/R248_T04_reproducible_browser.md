# R248 T04 可重复真实 Chromium 测试（非正式验收）

- 修复 R239 测试入口：在临时 HTTP 服务器内返回内存 HTML，不再依赖缺失的 scripts/index.html。
- 允许通过 GLYPHSPACE_QA_CHROMIUM 指定授权隔离 Chromium 可执行文件。
- 2026-11-05 实测：22/22 PASS，真实 Chromium 双标签页 Web Locks/localStorage/WebCrypto；仅合成25键156槽位。
- 运行：`GLYPHSPACE_QA_CHROMIUM=/path/to/headless_shell /path/to/venv/bin/python scripts/r239_cross_tab_real_browser.py`。
- 测试写入全新127.0.0.1随机端口浏览器上下文，不使用用户存储。
- 不代表真实生产迁移、合法高清原图、读屏或真机认证。原始T00–T11 Accepted仍0/12。
- 本轮没有可读累计父ZIP，逐SHA继承、新累计ZIP、双解压均BLOCKED/NOT-RUN；R46独立基线不升级。
