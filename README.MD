### 超级机器人大战α静态修改器项目
[![python](https://img.shields.io/badge/Python-≥3.8-darkcyan?logo=python&style=flat&labelColor=013243)](https://www.python.org/)
[![PySide6](https://img.shields.io/badge/PySide6-6.3-darkcyan?logo=qt&style=flat&labelColor=013243)](https://doc.qt.io/qtforpython/)
[![Pillow](https://img.shields.io/badge/Pillow-9.1-darkcyan?logo=nintendogamecube&style=flat&labelColor=013243)](https://python-pillow.org/)
[![pyqtdarktheme](https://img.shields.io/badge/pyqtdarktheme-1.1-darkcyan?style=flat&labelColor=013243)](https://pypi.org/project/pyqtdarktheme/)
[![pyinstaller](https://img.shields.io/badge/pyinstaller-5.1-darkcyan?style=flat&labelColor=013243)](https://pyinstaller.org/en/stable/)
#### 项目说明
用于修改机战α的静态修改器，为了弥补luxiwen版本修改器部分不能改或无法直观修改的数据而写的，所谓自己动手丰衣足食是也。
主要特点是可以修改战场的剧情配置和幕间剧情配置，同时明确熟练度和隐藏的获得条件等。
#### 构建EXE步骤
1. 下载完整代码
2. 安装适合自身操作系统版本的CPython解释器，教程自寻，要求3.8或更高版本。[Python官网下载页面](https://www.python.org/downloads/)
3. 双击所需build.bat等待构建完成
4. 在dist文件夹内找到修改器，程序入口SRWα.exe
#### 主要实现功能
- [x] 机体属性
- [x] 武器属性
- [x] 机师属性
- [ ] 战场剧情配置
- [x] 敌方战场配置
- [x] 敌方AI设计
- [ ] 幕间剧情配置
- [x] 剧情相关文本
- [x] 主角生日技能精神
- [x] 改造金额幅度
- [x] 强化配件属性
- [x] 精神消耗点数
- [ ] 全角字符重绘
#### 所需文件
+ ROBOT.RAF *解压缩为UNCOMPRESS_ROBOT.RAF*
+ PILOT.RAF
+ SNDATA.BIN
+ ENLIST.BIN
+ AIUNP.BIN
+ SCRIPT.BIN
+ SNMSG.BIN
+ PRM_GRP.BIN
+ 12F.DAT
#### 使用方法
将上述所需文件提前准备好，机体文件需要用luxiwen版本修改器解压一下，然后在程序中载入即可开始修改。
修改数据后点击写入会暂存本次修改，退出程序前不要忘记保存ROM。
