# V0.36 · 第138轮 Root T03 宿主DOM符号ID碰撞与原子挂载守卫（隔离、非验收）

- **任务轨道**：原始 Root T03 SVG坐标内核；关联T07位置与碰撞。UI-01～UI-05不计入本轮。原始T00–T11仍 **0/12 Accepted**；T01正式认证0/25键、T02正式永久ID0、T03未生产集成、T05未完成。
- **父ZIP**：R137 SHA256 `edfe5508884a5b50a2145f89f9ea47b5651a7333e3eb01cf04bf71df1bb0ecfb`，1776文件，真实逐项继承SHA **1776/1776**。
- **实际缺陷**：R137仅检查源XML临时文档中的ID，未检查将挂载的宿主DOM。Chromium 144预置同名`gs134-1-def-1` symbol（100×100矩形）后，R137生成的`<use href="#gs134-1-def-1">`错误解析为宿主符号；DOM出现两个同名symbol，字根实测BBox为`[0,0,100,100]`。这是实际渲染错误，不是UI阈值或原图认证。
- **隔离修复**：新增`v036_round138/dom_commit_collision_guard.js`，词法私有封装R137，仅公开`GlyphSpaceR138.mountInto(target,raw,view,ids)`。已验证固定SHA的字形在脱离DOM状态构建；提交前对比全宿主文档ID，检测冲突即拒绝；无await地同步append，提交后复核ID唯一性，失败回滚。恶意预置ID被拒，挂载目标仍0子节点；无预置冲突时151个旧可视字根×3视图=**453 SVG、453唯一symbol ID**，151身份稳定。该守卫不能防御挂载后第三方脚本恶意修改DOM。
- **真实QA**：独立Chromium 144 `about:blank`，新22/22；重跑R132–R137旧21+12+10+14+20+21=**98/98**，合计**120/120**。R138 ZIP **1784文件** SHA256 `e2df22e36096a664a9fa592f15a9b0f3e2b8c1fa6f7679279e898afc498dc3ee`，Python zipfile与系统unzip两次独立恢复均1784/1784文件SHA一致，恢复后各120/120 QA通过且QA后1784/1784文件SHA未变化。
- **明确限制**：完整历史全量QA **not-run**；2008高清原图原始字节及许可、逐笔认证 **not-run/blocked**；真实共享原点迁移前序环境`ERR_BLOCKED_BY_ADMINISTRATOR`，本轮 **not-run**；Android/iOS真机、真实读屏 **not-run**。第10–12、35轮ZIP与第12轮20SVG仍缺，历史连续性不成立。
- **冻结**：V0.35 `index.html` SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`、2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`不变；176旧编码、历史正式SVG和用户存储未修改。隔离ZIP不在GitHub，源码/审计/恢复记录保存在ZIP内，仓库仅同步证据与状态。未完成正式T03或V0.36发布。
