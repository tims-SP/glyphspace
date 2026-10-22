# 04 · 新世纪五笔字根身份、来源、渲染与迁移数据模型

> 状态：原始V0.36-P0 Schema/关系的**目标规范**，不是已部署的正式数据表。来源：[历史规划](./history/V0.36-P0-original.md)与[历史问题清单](./history/V0.35-root-audit-original.md)。截止第46轮正式字根认证仍为**0/25键**。

## 不可混淆的六种实体

| 实体 | 必备字段与职责 | 关联 |
|---|---|---|
| **ReferenceShape** | `referenceShapeId`、`key`、`sourceImageSha256`、`bbox`、形态可辨性、候选语义/父子圈注标记 | 原始参考图片中**可辨视觉形态**；不一定是编码根 |
| **GlyphAsset** | `assetId`、`pathData`/`symbolId`、`viewBox`、`inkBBox`、`pathSha256`、`source`、`license`、`modifiedFrom` | 轮廓本身；一个asset可被多实例引用 |
| **GlyphInstance** | 永久`instanceId`、`referenceShapeId`、`assetId`、`semanticRootId`、`key`、`category`、`geometry`、`layer`、`legacySlot` | 字根键位里**可选择、可独立定位**的展示实例；不得从数组下标生成ID |
| **KeyMeta** | `key`、五笔区位编号、QWERTY物理行列、键名字母/区号/标记保留区 | 25正式键；Z学习键与正式根键分类分开 |
| **Review** | `reviewId`、`instanceId`、五维审核结果、来源与资产/几何签名、人员/日期、证据链接、过期原因 | 是审核意见，未满足原图认证门槛不能视为`certified` |
| **UserOverride** | `schemaVersion`、`instanceId`、用户独立几何、历史key及迁移版本、冲突隔离/恢复字段 | **用户设置层**，不得覆盖发布默认几何或原始证据 |

建议`geometry = {x,y,width,height,anchor,ox,oy}`，局部键帽坐标100×100。anchor与inkBBox配合确定光学定位。字根标签、区号、圈注各有独立边界。

## 数量与身份规则

* 旧版`ROOTS` 156条记录 = **151条可视字根实例 + 5条关联记录**（D:镸、K:中、M:骨、U:辛、O:业）；Z学习键不属于正式字根25键。
* 第44轮审计115条原图暂定对应 + 36条未匹配 = 151条可视。**36未匹配不代表36个缺根**。
* 第6轮232原图候选区域 = 222暂定叶 + 9父证据 + 1已否定空白锚点；不是正式字根总数。
* 第46轮阻断账本分类 139仅人工审阅 + 2新阻断 + 8旧否定 + 2旧命名空间冲突 + 5关联 = **156**。各自不等于已认证绑定。
* 路径Hash重复（H:4、J:4、K:3等）可能只是SVG资产复用，不可当作同语义字根判据。

## 分类与复核签名

`category`至少区分：`root`、`variant`、`annotation`、`supplement`、`related`。`variantOf`指向明确的语义根身份，`annotation`和补码**第二键提示**不得误触发普通字根高亮；关联项须逐个判断是口诀关系、构形还是独立视觉实例。

五维独立复核：

1. `existence`：原图是否确有独立可辨形态；
2. `outline`：笔画/走向/拆合/构形是否逐笔对应；
3. `position`：相对于单键参考图的定位；
4. `scale`：尺寸、笔画重量和相邻视觉主次；
5. `classification`：root/variant/annotation/supplement/related的语义分类与编码效应。

复核签名建议覆盖`sourceImageHash+referenceShapeId+bbox+assetPathHash+instanceId+geometry+category+schemaVersion`。任一变更仅使**受影响的Review**进入`stale`并保留历史，禁止沿用旧`match`冒充新版本认证。

## 源字节与可信度

冻结V0.35 HTML SHA256：`fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`。

2008参考图 SHA256：`df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`。当前真实存在的键位PNG是低分辨率裁片，同源高清JPEG真实字节未落盘，不得把最近邻放大当高保真笔画证据。

K:2「川」和K:3「丨」共同引用`2008-K-vis-03`框(10,69,21,24)；第46轮**两条都被隔离为不可作为候选来源**，原证据保留。这不是身份确认。E:1「舟」与E:8「用」的`2008-E-vis-04`为已否定空白误框；B:7/V:4候选仍待身份复核。

## T04迁移流程

旧`ROOTS[key][index]`、`ROOT_COORDS[key][index]`及旧`localStorage`字段是历史槽位与配置来源，**不能直接当永久ID**。未来：

1. 制作只读旧版本key/value/坐标及人审快照，在隔离环境校验来源版本。
2. 对每个旧槽分配固定`instanceId`草案，遇到K/E/B/V冲突写入隔离队列而不是静默套坐标。
3. 以`schemaVersion`记录迁移范围，将**手工改动**与默认坐标严格分离、保留用户覆盖。
4. 多次执行结果幂等；脏数据、部分写入、存储空间不足及多标签并发失败时可回退原始版本。
5. 先FakeStore、再独立真实同源profile；没有真正Web Locks/storage事件测试前不得触碰用户生产profile。

## 验收与版本发布

只有拥有来源证明、逐笔人工认证、全部25键完整覆盖、五维签名、跨视图同实例几何、正确176编码和可逆用户存储迁移的正式候选，才可发布。所有null/unknown必须保留，不可自动标0或false为完成。

完整规则见[原始规划](./history/V0.36-P0-original.md) · [10键位清单](./10-key-audit.md) · [13资产来源](./13-asset-provenance.md)。
