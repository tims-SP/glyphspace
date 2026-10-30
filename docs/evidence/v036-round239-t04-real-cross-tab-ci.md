# R239 · 原始T04 · 真实跨标签并发恢复验收前证据（非Accepted）

日期：2026-10-30。原始Root T04，不属于UI-01–UI-05。

## 来源、执行和实际结果

- GitHub main基线R238：`c00ae6425a4722ae98175497683ae6bf5c32520c`；本地R238父ZIP SHA256 `28ea55adeb80a8309bb9d66ee077a4d559f9b7f8c54cfa76d0eb1698bf506580`。
- 本轮新增仓库 `scripts/r239_cross_tab_real_browser.py` 和 `.github/workflows/r239-t04-real-cross-tab.yml`，将R238仅在Node FakeStore验证的跨标签并发恢复用例提升为GitHub Actions隔离Chromium真实原点测试。
- [GitHub Actions run 41052963001](https://github.com/tims-SP/glyphspace/actions/runs/41052963001)，job 124053302957，实际日志 `{"passed": 22, "expected": 22, "allPassed": true, "error": null}`。测试环境：ubuntu-latest、Chromium、临时127.0.0.1、两个真实标签、Web Locks/localStorage/WebCrypto，25键156旧槽**合成数据**。
- 验证独占锁/幂等、跨标签共享日志、注入崩溃、非协作写入冲突拒绝与恢复、伪造日志拒绝、旧来源失效、独立profile和清理。
- 本地浏览器实际尝试返回 `ERR_BLOCKED_BY_ADMINISTRATOR`，本地真实同源仍blocked/not-run。
- 本地R238选定继承QA 852/852；父ZIP 2984/2984成员逐SHA继承；R239累计ZIP 2989文件SHA `1c00ab27ca12bb13d16b26d53e1cc3d37c1bb2c574756a1349c6d7ac08aa99c0`；Python和unzip独立恢复各2989/2989 SHA、852/852选定QA、QA后0漂移。

## 验收边界

未对用户原有存储执行迁移；正式T02 ID0、T03生产未集成，故T04仍未Accepted。T01正式0/25、T05真实缺根未知、原始T00–T11 0/12 Accepted。高清许可与逐笔认证、R11/R12/R35原始ZIP及R12 20 SVG、真机、读屏、完整历史QA未完成。冻结V0.35 HTML、2008 JPEG、176旧编码、正式SVG和用户存储未修改。

记录中CI的22/22为独立真实浏览器验证，ZIP中的852/852为本地选定继承QA，**两者不相加冒充同一环境通过数量**。
