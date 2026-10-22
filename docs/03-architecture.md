# 03 · 架构：冻结实现、字根系统目标、并行UI实验

> **规范来源**：[V0.36-P0原始规划](./history/V0.36-P0-original.md)。现有GitHub仅有V0.35冻结网页和V0.36第40轮隔离键盘页；下述模块、Schema不是已经集成的源目录。

## 当前正式事实

`index.html` 是完整离线单文件HTML，含 HTML/CSS/原生JS、五笔06编码练习、旧`ROOTS[key]`与`ROOT_COORDS[key][index]`平行数组、SVG路径渲染、三视图及localStorage设置/校准/人审。旧`KEY-root-index`依赖数组次序，不是跨增删的永久身份。

`preview/v0.36/index.html`来自隔离UI实验；目前尚未承接完整的训练状态机，不能代替正式入口。基础HTML在一次文档提交中**始终不可修改**，完整SHA见[STATUS](./STATUS.md)。

## 正确的工作流与依赖

```text
Root track:
T00 冻结V0.35 → T01 参考图清点 → T02 语义/永久ID
                                               ↓
                   T03 SVG坐标内核（100×100）→ T04 迁移
                                               ↓
                   T05 补图 → T06 轮廓 → T07 碰撞
                                               ↓
                   T08 校准闭环 → T09 输入/三视图
                                               ↓
                         T10 设备 → T11 发布冻结

UI track:
UI-01 一屏减法 → UI-02 字母帽渐进键盘
                      ↓
          UI-03 焦点放大分页 + UI-04 mini键盘
                      ↓
          UI-05 无障碍与软键盘
                      ↓
          依赖T02/T03/T09/T10最终合并，不挤占T03/T05编号
```

依赖以[机器可读原始账本](./tasks/t00-t11.json)为准；上图为示意，并非流水线已经完成。

## 拟议的实体层

```text
[2008参考原图 + 不可变来源] → ReferenceShape / KeyMeta
                                     ↓
                              GlyphInstance
                       (永久instanceId / category)
                       ↙          ↓            ↘
               semanticRootId  GlyphAsset     local geometry
                       ↓          ↓            ↓
                   编码规则      SVG路径       100×100坐标
                       \          |            /
                  练习/完整键帽/单键放大/迷你键盘
                                 ↓
                         Review + UserOverride
                                 ↓
                       版本化持久化与回滚
```

实体详细字段及关系见[04数据模型](./04-data-model.md)。

## T03：真正的SVG坐标内核（原始定义）

1. 单键帽固定`viewBox="0 0 100 100"`，这是**局部虚拟坐标**，非屏幕像素、非原图绝对坐标。
2. `GlyphAsset`包含路径、视框、真实墨迹`inkBBox`、来源/许可和资产内容SHA；`GlyphInstance`持有独立位置/层级/语义根身份。
3. 几何至少含`x,y,width,height,anchor,ox,oy`，后两个为光学校正；键帽字母、区号、圈注留独立区域。
4. SVG的`<symbol>/<path>/<use>`可复用轮廓，但不同视觉实例的ID/坐标不能因此合并。
5. 新增、删除、重排M等微形不得移动其他实例；完整、放大与迷你三视图必须读取**同一份**identity + geometry数据。
6. 焦点放大属于外层辅助视图，不应把持久化基础几何重排。以上**仍需正式实现与验收**。

## T05：补图而非移动键盘布局

在T01已确认参考形态、T02已分配ID、T03几何可用、T04迁移可逆之后，先以M键微型下框/贝旁独立实例试点，再覆盖Q、I、K、L、O、N、B、V及其他键。**原图每个可辨形态必须有独立视觉实例和可选择/复核的SVG路径**；但正式根/变体/圈注/补码/关联身份应审阅后判定，不能“新增候选=新增正式字根”。

## T04持久化迁移

由老数组索引和localStorage迁往`schemaVersion`+`instanceId`键控；保留已有用户手调覆盖和人工审阅记录。强制：只在独立浏览器profile或内存FakeStore做实验；坏数据整批隔离、双标签并发安全、重入幂等、备份及回滚。第46轮独立同源浏览器尝试遭`ERR_BLOCKED_BY_ADMINISTRATOR`，不能宣布真实多标签页验收。

## 其余责任边界

* T06：字形轮廓、偏旁方向、笔画重量/圆圈/补码与异源SVG细校。
* T07：使用真实inkBBox+stroke检测字根/字母/区号/圈注碰撞与越界，必要白名单。
* T08：原图新增形态→分类→五维审阅→版本签名过期→导出与重验。
* T09：引导/进阶/盲打三模式、完整/迷你/单键同源，以及176条取码回归。
* T10：真机Android/iOS、横竖屏、DPR、系统输入与读屏。
* T11：按准入闸门发行可离线单HTML并保留回滚，不能直接覆盖V0.35冻结文件。

## 原生HTML与未来工程化

当前保留原生HTML/CSS/JS的无构建与离线优势；是否引入React/Vue/Svelte是**待评估**。文档/测试可独立模块化，但不能伪称已有`src/`编译架构。新增CI只检验仓库**静态完整性**，不是整个V0.36运行时验收。

关联：[11追踪台账](./11-traceability.md) · [12验收矩阵](./12-test-matrix.md) · [14 UI编号调和](./14-ui-change-control.md)。
