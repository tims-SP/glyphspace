# V0.36 第139轮 · Root T03 挂载后DOM完整性失效守卫（隔离）

- 日期：2026-10-26；工作轨道：Root T03，关联T07；正式验收：**false**。
- 父ZIP：R138，1784成员，SHA256 `e2df22e36096a664a9fa592f15a9b0f3e2b8c1fa6f7679279e898afc498dc3ee`；真实逐文件继承1784/1784。
- 新ZIP：R139，1793成员，SHA256 `344f5adfbb307de298a27e19d8dcfb890fe0bd839800f22ee507c1904c24db72`；Python zipfile与系统unzip两套独立恢复，QA前后1793/1793文件SHA一致。
- 隔离实现：`v036_round139/postcommit_integrity_watcher.js`（位于累计ZIP中，不在正式HTML），只公开`GlyphSpaceR139.mountWatched`。把R138原子挂载私有化，MutationObserver检测提交后的外部同名ID、Path/属性篡改、短暂插入碰撞和节点移动；同步`assertIntact`检查子树快照及宿主ID唯一性；`dispose`只卸载自身。
- 实测：Chromium 144.0.7559.96 `about:blank`新24/24、R132–R138旧120/120；三个视图共453个SVG/453唯一symbol ID；无冲突宿主DOM更新保持有效；已失效句柄不会自动恢复。每份独立恢复均重新执行144/144。
- 真实失败与修正：首次QA静态检查将源码注释中的`localStorage`一词误当存储调用而失败，修正为检查实际API调用标识后通过；该失败不计pass。
- 历史来源：枚举父ZIP全部1784条路径，未找到R10–12/R35原始ZIP或R12的20 SVG；R114高分辨率候选来源有历史报告，但其可授权原始字节未保存在父ZIP，不得当作逐笔认证。
- 边界：观察器并非对恶意宿主脚本/原型污染的安全沙箱；渲染前须主动`assertIntact`，宿主可在检查后继续修改DOM；没有真实同源Web Locks/localStorage、Android/iOS真机、真实屏幕阅读器或完整历史全量QA。未获得2008高清原图许可、T02正式永久ID、T03生产集成。
- 冻结HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`，2008参考JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`，均在父恢复目录实测一致；176旧编码/历史正式SVG/用户存储未修改。
- 回滚：删除隔离`v036_round139`，使用R138原ZIP；Root T00–T11保持0/12 Accepted，正式T01 0/25。
