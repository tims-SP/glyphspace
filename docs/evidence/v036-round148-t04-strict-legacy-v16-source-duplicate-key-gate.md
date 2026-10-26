# R148 · Root T04 旧v16重复JSON键来源门禁（隔离、非验收）

- 原始任务：T04（关联T00/T02），非UI工作。R147 GitHub main head `78984cfe63c699a02e34e14aa1a9d0984e53ea9b`。
- 父R147累计ZIP：1865文件，SHA256 `bebcacaafadb23734dc11bb76ac095af21c744fa7b2c2e6fbec65c54c8153f70`；实际逐文件继承1865/1865。
- R148累计ZIP：1875文件，SHA256 `9b9c58ecd97cc1f68960ff4c70086148f197d1ec30704b9d4c8d0d6e490d35fa`。Python zipfile与系统unzip独立恢复，各1875/1875前后SHA、1628/1628定向QA（旧R142–R147 1590，新Node 29，Chromium about:blank仅JSON解析9）。
- **真实发现**：直接执行R147的READ读取重复`G` JSON来源，尽管源SHA匹配，`JSON.parse`仍静默覆盖第一个`G`。R148隔离`legacy_v16_strict_shadow.js`新增重复键失败关闭扫描（含转义等价键）、冻结25键156槽默认值SHA固定、部分键存在性/源签名/读取期间源变更检查。有效空白格式仍允许；仅只读，无生产迁移和正式永久ID。
- 新代码SHA：`legacy_v16_strict_shadow.js` = `93095d5ef4ef85d8238b90b51f6fbc2e8968e6c5a51498e7503dccfe26b27fed`。代码仅位于隔离累计ZIP，不接入正式index.html。
- 本地127.0.0.1真实Chromium重试R147协议仍`ERR_BLOCKED_BY_ADMINISTRATOR`：**blocked**。R148独立授权真实同源：**not-run**；Chromium about:blank 9/9不计为真实同源；真机/真实读屏0，历史完整全量QA not-run。
- 冻结V0.35 HTML `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`、2008 JPEG `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`、176编码、历史正式SVG及用户存储未修改。
- 缺R10–12/R35原始ZIP和R12 20 SVG，高清合法许可/逐笔身份认证仍阻断。T01 0/25正式认证、T02永久ID0、T04真实用户迁移未验收、T05正式补图未完成，**T00–T11仍0/12 Accepted**。正式生产入口未修改。
