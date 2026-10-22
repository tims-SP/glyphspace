# 字间 · GlyphSpace

**新世纪五笔06版交互式学习网页**。设计方向：字根空间位置稳定、动态拆字、逐键聚焦、沉浸式一屏训练、移动端渐进键盘。

> **正式入口仍是V0.35冻结版，不是V0.36整合发布。** V0.36目前存在原图来源审计和隔离UI原型，正式T00–T11还没有全部验收。当前可核对隔离进度：**第46轮**（审计层冲突隔离，不是字根认证）。

## 网页

- **[完整正式学习网页](./index.html)**：离线单HTML V0.35冻结原文件。其页面内部标题可能显示V0.34，不能为改标题而修改已冻结字节。
- **[V0.36渐进键盘预览](./preview/v0.36/index.html)**：继承第40轮UI-track实验，含物理键位、字母帽与焦点交互；不具有正式V0.36整合版的完整学习功能。

GitHub Pages若已经在Settings→Pages启用`main/(root)`，首页和预览分别为`/`及`/preview/v0.36/`；是否已上线需检查实际Pages部署状态，不凭URL推断成功。

## 项目方向与设计资料

[阅读**完整文档索引**](./docs/README.md)，重点阅读：

| 问题 | 文档 |
|---|---|
| 为什么做 / 怎样降低认知负担 | [愿景](./docs/00-vision.md) · [原则](./docs/01-design-principles.md) |
| 要实现哪些功能 | [需求](./docs/02-requirements.md) |
| 代码应该怎样拆分 | [技术架构](./docs/03-architecture.md) |
| 字根证据、ID、渲染和存储如何分开 | [数据模型](./docs/04-data-model.md) |
| 桌面/移动体验如何约束 | [UI/UX](./docs/05-ui-ux.md) |
| **原始T00–T11正确职责与依赖** | [路线图](./docs/06-roadmap.md) · [原始规划](./docs/history/V0.36-P0-original.md) |
| 如何判定真正完成 | [验收闸门](./docs/07-acceptance.md) · [具体测试矩阵](./docs/12-test-matrix.md) |
| 25键哪里可能遗漏 | [逐键复核矩阵](./docs/10-key-audit.md) |
| 任务代码与证据进度 | [追踪台账](./docs/11-traceability.md) · [STATUS](./docs/STATUS.md) |
| 为什么UI版本与旧任务编号重叠 | [编号调和](./docs/14-ui-change-control.md) |
| 后续Agent应遵守什么 | [AGENTS.md](./AGENTS.md) |

## 两条开发工作流

**Root track（T00–T11）**：原图清点→身份和ID→SVG坐标内核→存储迁移→独立补图→轮廓、位置、审阅闭环→三视图/编码回归→真机验收→发布。

**UI track（UI-01–UI-05）**：沉浸一屏、移动渐进键帽、焦点字根放大分页、折叠迷你键盘、无障碍与软键盘。第36–40轮曾误把UI原型称作“T03/T05”；历史标签保留，但今后的正式任务编号**不再混用**。

## 目前验收事实（2026-10-22）

- T01正式认证**0/25键**；缺根真实数量未知，历史36未匹配不是36缺根。
- T02的156条只是**草案**。真正T03 SVG内核与真正T05补图均未正式集成。
- 第46轮隔离ZIP共685文件，来源冲突候选K:2/K:3被阻断；静态26/26、Chromium审阅20/20；不等于原图逐笔认证。
- 真正共享原点Web Locks/localStorage、Android/iOS实机读屏尚未验收；T06–T11未正式完成。
- 第10–12和第35轮ZIP及第12轮20个SVG仍缺失，不能假定历史完整。

## 冻结、数据安全和许可证

正式`index.html` SHA256：`fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`。

本次文档/脚本修复**不改V0.35正式HTML、SVG、176编码和用户真实localStorage**。仓库暂未提供LICENSE；公开阅读≠获取第三方参考图、字体和SVG再分发权利。详见[素材来源清单](./docs/13-asset-provenance.md)。

可在仓库根目录执行`python3 scripts/verify_repo.py`做只读静态校验；其通过**不能**声称V0.36完成。
