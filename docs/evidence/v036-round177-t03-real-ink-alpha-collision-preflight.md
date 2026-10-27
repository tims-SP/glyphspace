# R177 · Root T03 实际墨迹 alpha 碰撞隔离预检（T07非验收）

日期：2026-10-28。父R176累计ZIP SHA256 `c687d56e8674632735fd03143cc2aa15450c6439224f27e9917cdee41cf15d55`，2181/2181成员逐文件SHA继承。新增R177累计ZIP 2189文件，SHA256 `b44a6720aeb7b27d4303affb4aa681cd93fbaf7030aad17534468da9eb82ecab`，Python zipfile与系统unzip双独立恢复各2189/2189 SHA及1075/1075选定QA，QA后SHA未变化。

## 实际实现

新增隔离 `v036_round177/qa_ink_raster.py`（完整代码与审计数据在R177累计ZIP），用真实Chromium about:blank加载R176来源签发25键SVG宿主，将151个草案实例各自的原始SVG `g`/Path分别绘制到256×256和384×384透明Canvas，读取alpha>=32像素，逐对比较同键实例墨迹；每分辨率检查409对，均0对墨迹像素交叠、0空白实例、0边界裁切像素、0对3px以内近接。与R176仅组BBox测量相比，这是真实Canvas像素交集测量，但**只覆盖现有未认证草案、两种分辨率与固定alpha阈值**，不能据此宣称原图形态正确、全部stroke/滤镜状态安全或正式T07已通过。

## QA范围与缺口

新增Chromium 8/8；本轮实际重跑R176来源13/13、R176 DOM浏览器700/700、R175 Node19/19、R175 Chromium99/99、R174来源+浏览器236/236；选定旧1067/1067，总计1075/1075。尝试R176递归2820项，但超时，不计通过；完整历史全量not-run。真实同源Web Locks/localStorage、Android/iOS真机、真实读屏not-run，file://管理员策略阻断仍未解除。

原始R11/R12/R35 ZIP及R12 20SVG仍缺；3508×2480高清图许可、M/K/E/B/J/R/X/V逐笔来源及正式永久ID未认证。T00–T11全部accepted=false；T01正式0/25、正式ID0、缺根数未知。冻结V0.35 HTML、2008 JPEG、176旧编码、历史正式SVG、生产入口、用户存储未修改。隔离ZIP可直接恢复，不构成正式发布。
