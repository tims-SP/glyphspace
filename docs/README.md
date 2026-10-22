# GlyphSpace 项目文档索引

> 2026-10-22对照历史原始规划恢复：原始 **T03=SVG坐标内核，T05=完整性补图**；第36–40轮移动键盘原型属于独立**UI-track**。本目录区分产品设计、历史规划、当前事实及未来提案，不可将计划误作已验收。

## 设计与实现文档

| 文档 | 目的 |
|---|---|
| [00 愿景](./00-vision.md) | 目标用户、产品边界与成功条件 |
| [01 设计原则](./01-design-principles.md) | 空间记忆、聚焦、减法、离线与无障碍 |
| [02 功能需求](./02-requirements.md) | Root track与UI track具体行为 |
| [03 技术架构](./03-architecture.md) | 冻结单HTML、六实体与T03真正坐标内核 |
| [04 数据模型](./04-data-model.md) | ReferenceShape/GlyphAsset/GlyphInstance/KeyMeta/Review/UserOverride |
| [05 UI/UX](./05-ui-ux.md) | 一屏/渐进键盘/折叠/真机交互 |
| [06 路线图](./06-roadmap.md) | **原始T00–T11**、依赖及Gate A–D |
| [07 验收规范](./07-acceptance.md) | 正式发布准入、逐项验收状态 |
| [08 决策记录](./08-decisions.md) | ADR与范围演化 |
| [09 变更历史](./09-changelog.md) | V0.35至第46轮事实与缺失 |
| [10 25键审计](./10-key-audit.md) | 全部25键具体风险和旧实例数 |
| [11 任务追踪](./11-traceability.md) | 任务→源文件→审计证据→未完成项 |
| [12 测试矩阵](./12-test-matrix.md) | GEO/DATA/REF/INPUT/UI/DIST、视口、DPR、真机 |
| [13 资产许可证](./13-asset-provenance.md) | 字体、复合SVG、参考图来源与许可审计 |
| [14 UI编号调和](./14-ui-change-control.md) | 后来UI需求与原始字根任务独立 |
| [STATUS](./STATUS.md) | **最新经可用隔离包核实：第46轮** |
| [SHA256SUMS](./SHA256SUMS.txt) | 仓库文件完整性（不含自身） |

## 原始历史与机器账本

- [**V0.36-P0原始任务规划全文**](./history/V0.36-P0-original.md)：原始T00–T11工作包/依赖/完整测试场景。
- [**V0.35字根问题总清单全文**](./history/V0.35-root-audit-original.md)：25键原始问题、各项高风险、历史尚未核验说明。
- [历史来源说明](./history/README.md)。
- [T00–T11机器可读JSON](./tasks/t00-t11.json) · [25键CSV](./tasks/25-key-audit.csv) · [账本说明](./tasks/README.md)。

## 工程工作流

- [AGENTS.md](../AGENTS.md)：代理执行与安全约束，**必须先读原始任务定义**。
- [只读静态校验脚本](../scripts/verify_repo.py)：检查历史任务映射、25键旧计数、冻结HTML、SHA和文档链接；**不能代替真机/原图验收**。

## 事实与权威排序

1. 当前可验证原始HTML、原图字节SHA、历史原文任务编号/定义、完整Git变更；
2. 第46轮独立ZIP/报告/QA日志（ZIP在独立工作区，**未上传本GitHub仓库**）；
3. 本目录维护的规划和当前受控状态；
4. 尚未认证的UI实验、候选字形、阈值/IoU、单次人工意见。

有冲突应追加审计与ADR，不得无声改写原始文档或把候选晋升为认证。
