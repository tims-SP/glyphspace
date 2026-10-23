# V0.36 第66轮 · T03隔离三视图来源绑定门禁（非正式验收）

日期：2026-10-23。任务编号：原始T03 SVG坐标内核；不属于UI-01～UI-05。

## 发现与修复
第64轮DOM适配器允许在保持旧草案assetId时替换SVG Path，仍会挂载，造成第63轮来源绑定门禁与浏览器渲染之间的断层。第66轮新增SHA256模型摘要预检，覆盖151个旧可视实例的Path、stroke、几何、变换、key membership及旧槽位；挂载前深拷贝并冻结草案模型。单HTML审阅页内联纯JS SHA256，不依赖WebCrypto、网络或外部字体。该摘要仅对父包冻结草案进行完整性检查，不是抗恶意篡改的签名，更不是字根原图认证。

## 已实跑证据
- 第65轮父ZIP：981文件，SHA256 f9a61e9cad2022e48e943bead7766c8645ef9c31b69810728f385ede9d27f6c4；继承981/981逐文件SHA一致。
- 第66轮独立累计ZIP：996文件，SHA256 29735c2ce105e93c0ad843ff3d894c81329f0808810865d35454e055f8fc3690。Python zipfile与系统unzip两次独立解压各996/996 SHA一致，各复跑25组旧QA+1组新QA通过。
- 新Chromium about:blank DOM QA 43/43：含16类篡改拒绝、三视图151实例/25键同源、空/ASCII/Unicode SHA256向量、DPR1/2/3。旧适配器接受改写Path的缺陷已实证复现。
- T04真实同源预检：全新一次性Chromium profile + 临时127.0.0.1服务器，导航ERR_BLOCKED_BY_ADMINISTRATOR，结果blocked；未运行真实Web Locks/localStorage事务。
- 原图正式认证0/25，缺根数未知；真实Android/iOS与屏幕阅读器均not-run；第10–12、35轮ZIP及第12轮20 SVG仍缺。

## 状态边界
原始T00–T11仍0/12 Accepted；T03仅隔离实现，未集成正式入口。冻结V0.35 HTML、正式SVG、176编码和用户真实存储未修改。完整ZIP及源代码在独立交付包，不在此GitHub仓库。CI静态成功不等于来源或设备正式认证。
