# 第103轮 · Root T03 SVG祖先绘制完整性隔离修复（非正式验收）

日期：2026-10-25。**不改变原始T00–T11编号或Accepted状态；正式验收0/12。**

## 真实缺陷与修复

第94轮的隔离SVG门禁只对<svg>/<use>/<defs>的computed style及DOM来源进行证明。真实Chromium复现：在父级`.full .key-cell`上添加`opacity:0`，R94 `attest()`仍返回true，实际截图改变10522个RGB像素，但SVG `getBBox()`保持[82,78.33999633789062]。类似的key-row、view、layout、body父级opacity/filter/clip-path/mask/transform可绕过R94。九种主动攻击均经R94实际错误放行、R103拒绝。

第103轮独立HTML新增key-cell、key-row、view、layout、body、html的computed-paint与祖先结构基线校验，覆盖完整/mini/单键三视图；检测到漂移时在草案编辑前失败关闭。R103新增Chromium about:blank QA **26/26**，并验证正常选键/编辑/撤销/导入、拒绝时草案SHA不变。**这不是生产集成，也不证明所有CSS或真实像素攻击均已覆盖。**

## 父包、恢复与测试

- 父R102 ZIP：1397成员，SHA256 `1e5972251f3386e91d709e1869a36009f8aead732eaa4e22bfb93d9f21b094a5`；逐文件继承**1397/1397**一致。
- R103累计ZIP（ZIP本体不在GitHub）：**1410成员**，SHA256 `bdd1f42c847c01bc98b278294b7a6074550e293c9e4b977f601dc4fe75ef8874`。
- Python zipfile及系统unzip两份最终归档独立解压：各**1410/1410**成员SHA一致，运行QA后再核各**1410/1410**一致。
- 每份恢复环境的8组定向新旧QA：R103 26/26、R102 52/52、R101 58/58、R84 124/124、R86 20/20、R99 Chromium 302/302、R94 Chromium 18/18、R93 Chromium 12/12；共**612项，8/8组通过**。
- 自动合并式双恢复运行在第二恢复阶段超时，**不计成功**；系统unzip恢复环境随后分项独立重跑全部8组并复核SHA通过。完整历史全量QA **not-run**。R91/R92只在预打包工作区单独通过，未计入双恢复8组。
- 本地恢复文件：`v036_round103/`内含独立HTML、QA脚本、父包逐成员SHA账本、预检恢复记录、执行报告、审计及打包/验证脚本。回滚仅删除该隔离目录。

## 仍阻断正式验收

T01 **0/25**键正式来源认证、缺根数未知；T02正式永久ID **0**；T03正式生产内核未集成，T05正式补图未完成；原始T00–T11 **0/12 Accepted**。第10–12/35轮ZIP、第12轮20 SVG、合法同源高清原图字节与许可仍缺失；真实同源Web Locks/localStorage **blocked/not-run**；Android/iOS真机、真实读屏 **not-run**。冻结V0.35 HTML、2008 JPEG、176编码、正式SVG和用户原有存储均未修改。
