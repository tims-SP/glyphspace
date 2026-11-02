# R245F52 · Root T03 旧SVG几何与T02草案身份只读绑定（2026-11-02）

**隔离候选，非来源认证、非正式永久ID签发、非生产集成。**

## 真实输入与变更

- 重新读取并验证R245F51父累计ZIP：SHA256 `3b2355a5781c6214560cc40630b4cf323529440538952d9f6e1937388d47e004`，3563/3563成员逐文件SHA一致。
- 将R3 `V0.36_T02_stable_identity_draft.json`的156条`planning_only`草案（151个旧可视、5个仅关联）与R245F49真实Chromium 151旧SVG几何清单按原始键位、槽位、字形、旧DOM实例ID逐项匹配；0条永久ID获得批准。
- 新隔离HTML运行时`GlyphSpaceT03Binding`实现156草案不可变绑定、151可视实例跨完整/焦点/mini三视图映射，5关联不渲染；拒绝草案重复、错误键位/字形/槽位、伪造批准、缺失/重复DOM及错误100×100 viewBox。重排、光学校正、焦点切换保持绑定稳定，失败先验证再写DOM。
- `referenceShapeId`、`assetId`均保留null；旧`paintedBBox`仍是浏览器候选，不是经2008原图逐笔认证的正式`inkBBox`。不得将候选`wb06/.../legacy-xx`当正式已签发ID。

## 可重复验收证据

| 项目 | 结果 |
|---|---:|
| 新Chromium about:blank绑定/伪造/漂移QA | 217/217 |
| 旧R245F51 Chromium回归（在新HTML上） | 175/175 |
| 旧R245F50 Chromium回归（在新HTML上） | 348/348 |
| **每套选定QA** | **740/740** |
| Python zipfile独立解压 | 3575/3575 SHA；父3563/3563 |
| 系统unzip独立解压 | 3575/3575 SHA；父3563/3563 |
| 两套解压后QA | 各740/740，文件零漂移 |

累计R245F52 ZIP SHA256：`f3f085c1aff16d7b4cb2d26d19aa3b662343a89e071636cc4cc27934085e6db5`，3575成员（3563父继承+12新增）。完整累计ZIP及HTML/manifest/测试代码在独立交付物中，未提交到公开GitHub生产目录。

## 仍未满足的正式验收

T01 0/25键正式认证、T02批准永久ID 0、T03正式inkBBox与生产内核未集成、T05缺根数未知、T00–T11 **0/12 Accepted**。R246主线累计原始ZIP及R11/R12/R35历史ZIP、第12轮20SVG仍缺失。高清官方同源与再分发许可未认证；真实同源生产迁移、真实读屏、Android/iOS物理设备及完整历史全量QA均**not-run**。

冻结V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`，2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`，176旧编码、正式SVG、生产入口及用户Storage未修改。

下一步需以真实来源逐笔证据批准`referenceShapeId`/`assetId`和稳定ID后，才可进入T03正式内核集成与T04生产迁移验收。
