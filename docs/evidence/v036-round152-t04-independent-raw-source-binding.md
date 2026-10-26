# R152 · 原始T04 · 旧v16来源原始字节独立绑定（隔离，非验收）

- 执行前main `6fafdc13989c440e1f6df90038bc0207d0304c3c`；父R151 ZIP SHA256 `f7770b71a7f0aa52eaff20c4afee5481624e6ac7796c4eabf9b5a139d82a78aa`，1902/1902逐文件SHA继承。
- **实际漏洞复现：**R151 WeakMap仅保证同realm签发，仍会为伪造strictReader结果签发可通过verifyPlan的计划。复现四类：全零来源SHA、伪G:0编辑、漏K/X键、转义等价重复JSON键。
- **修复：**`scripts/v036_r152_source_bound_plan.js` 在调用reader前独立读取raw，拒绝重复JSON键，校验键/槽位/坐标/编辑及SHA256；reader仅获得只读getItem facade，读后检查来源未变；限制127.0.0.1临时原点。schema v2，同realm WeakMap；没有apply/commit/正式ID接口。
- **QA：**Node22 WebCrypto+FakeStore新27/27，继承R142–R151定向1688/1688，总1715/1715。仓库Node回归脚本纳入Repository integrity CI，CI最终结果须独立确认。
- **恢复：**累计ZIP1910文件，SHA256 `2ed630217d3b85a20d18eba07d636d31fe93885212d50eb0a2861ea8a19b62e4`；Python zipfile和系统unzip双独立解压，各1910/1910 SHA、1902/1902父SHA继承、1715/1715定向QA，QA后SHA不变。
- **边界：**R152真实同源Web Locks/localStorage not-run（R151授权远端CI [40402103656](https://github.com/tims-SP/glyphspace/actions/runs/40402103656)22/22仅为旧证据）；Android/iOS真机、真实读屏、完整历史QA均not-run。不能证明调用者提供的store/crypto/locks/代码真实性，无法排除瞬时ABA；不触碰用户存储，生产迁移not-run。
- **历史：**缺R10–12/R35 ZIP和R12 20SVG；高清同源原始字节及许可未解决，正式25键认证0/25、正式永久ID0、真实缺根数未知。
- **冻结：**V0.35 HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`，2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`；176编码、正式SVG、生产入口和用户存储不变。T00–T11 **0/12 Accepted**。
