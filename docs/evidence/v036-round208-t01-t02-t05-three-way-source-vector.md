# V0.36 R208 · Root T01/T02, T05依赖：冻结JPEG—旧SVG—参考匹配三向证据核对

**状态：隔离审阅，非来源认证、非T05正式补图、非永久ID批准。**

实际读取R207累计ZIP（2613成员，SHA256 `1b69983adafb0d4b972a9411ef2b3f849add4279fa1626505daae9ec5ce76e2a`），并独立从冻结V0.35 HTML重新抽取151个可视旧SVG实例、153条Path、重算151个路径SHA256，与R50/R54矢量账本、R156 JPEG 170观察/161裁框、R207 156旧槽来源账本交叉核对。

**新发现：** 36/36个“参考形态未匹配”旧槽实际上同时存在JPEG来源观察和冻结旧SVG Path。故未匹配既非缺来源，亦非缺旧SVG。151可视槽均有旧SVG；5关联槽不渲染。15条无旧别名来源观察分为12个仅无别名裁框（各1条观察），以及3条与已有旧别名共享K键裁框的观察：K-physical-upper-left与K:0；K-physical-lower-right与K:4；K-physical-lower-left与K:2/K:3。**15观察不可直接推断15新增字根。**

**硬冲突保留：** E:1（舟）与E:8（用）共用一张JPEG裁框，但旧SVG Path SHA不同；K:2（川）与K:3（丨）亦共用裁框但旧SVG Path SHA不同。不能以单一ROI自动合并或签发两个形态；E旧空白框否定不撤销。R208低清JPEG 3×最近邻审阅图并非同源高清原件。

父ZIP 2613/2613逐文件SHA继承；选定旧QA487+新对抗QA50+静态QA17=**554/554**。新累计ZIP **2628成员**，SHA256 `200db5147697b9686bee3fd1073464707105bd060f821c24eda815364a02dc46`；Python zipfile与系统unzip两次独立恢复，均2628/2628 SHA一致且各554/554 QA通过。首次合并执行在第二套解压期间被中断，之后重新独立完成unzip恢复/QA并复核两棵恢复树，未计中断为通过。

冻结HTML SHA256 `fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc`、2008 JPEG SHA256 `df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49`；176编码、正式SVG、生产入口、用户localStorage未修改。缺R11/R12/R35原始ZIP及R12 20SVG；同源高清原始字节与许可未取得。真实同源Storage blocked/not-run；Android/iOS真机、真实读屏、完整历史全量QA not-run。

**正式状态不变：** T00–T11 0/12 Accepted；T01 0/25键认证；永久ID 0；真实缺根数量未知。隔离R208目录可直接删除回滚。原始T05不因本轮三向证据核对被标记Accepted。
