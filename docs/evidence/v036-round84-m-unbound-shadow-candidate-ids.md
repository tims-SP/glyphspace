# 第84轮 · 原始T01/T02/T05 M键未绑定观察的隔离影子身份（非验收）

日期：2026-10-24。父包：第83轮1193文件，ZIP SHA256 `d28dec3bc9118b334f0ffdcf724ad307c265b08b2756f3a421bb57d7d3366aa6`，1193/1193原始文件SHA继承一致。

## 实际数据工作

第55轮M键8个原图裁框与第81轮159条来源观察、第73轮151个候选UID三方交叉核验。vis-01/02/03/05与M:0/1/2/3的原图裁框完全相同，继续引用旧候选UID，不创建重复身份。vis-04/06/07/08没有旧槽映射，为其创建4个独立、不可变、隔离保存的UUIDv4影子候选UID；这些UID**仅代表待审来源观察**，不是正式字根/永久instanceId/assetId，也不能断言增加了4个独立字根。旧151候选UID及5关联记录不变。

门禁绑定2008 JPEG、第55轮暂存清单、第73轮UID账本、第81轮来源位置清单的原始字节SHA；8/8 M裁框原生RGB SHA复验。拒绝UUID漂移、重复UID、错误旧槽别名、原图裁框/哈希漂移、未审分类伪装、正式永久ID或Accepted冒充、生产绑定和新增未登记字段。

## 可复验证据

新增Python正负例124/124通过，旧第83轮353/353及此前17组QA重新通过。第84轮累计ZIP **1203文件**，SHA256 `9e95931ab39c37261aee085ee66d9e1c9cf763dca3248ce46b7d175736af0956`；Python zipfile与系统unzip分别解压1203/1203，恢复后重跑新旧QA通过、两份QA后1203/1203 SHA一致。ZIP本体**不在GitHub**，需使用另行交付的独立累计包；原始第10–12、35轮ZIP和第12轮20SVG仍缺失，不能声明历史连续归档。

本轮新模块及证据位于累计包的 `v036_round84/`：`m_staging_shadow_gate.py`、`R84_M_shadow_candidate_identity_registry.json`、`qa_round84.py`、`verify_round84.py`、`R84_M_shadow_identity_audit.json`、`R84_new_old_QA.json`、`R84_parent_1193_member_SHA256.json`。

## 未通过/未执行

T01正式认证0/25键、真实缺根数未知；T02正式永久ID 0；原始T00–T11仍0/12 Accepted。2008同源高清图合法原始字节未取得。2017年Wikimedia Commons独立CC BY-SA图仅有许可元数据，二进制下载因网络/DNS失败，不能作为2008同源来源。

新临时Chromium profile访问127.0.0.1报`ERR_BLOCKED_BY_ADMINISTRATOR`，真实Web Locks/localStorage事务**blocked/not-run**；Android/iOS真机及真实屏幕阅读器**not-run**。冻结V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`、2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`未变；176编码、正式SVG及用户真实存储未触碰。
