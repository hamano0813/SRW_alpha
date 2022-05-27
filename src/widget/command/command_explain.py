#!/usr/bin/env python
# -*- coding: utf-8 -*-

from parameter import EnumData
from widget.command import ParamRCombo, ParamCCombo, ParamVSpin
from widget.command.param_widget import ParamWidget


class CommandExplain:
    def __init__(self, **kwargs):
        self.w = dict()

        self.w['机体'] = ParamRCombo('选择机体', 0, kwargs.get('robots'))
        self.w['机师'] = ParamRCombo('选择机师', 0, kwargs.get('pilots') | {-0x1: ''})
        self.w['文本'] = ParamRCombo('选择文本', 0, kwargs.get('messages'))

        self.w['关卡'] = ParamRCombo('选择关卡', 0, EnumData.STAGE)
        self.w['音乐'] = ParamRCombo('选择音乐', 0, EnumData.MUSIC)
        self.w['事件'] = ParamRCombo('选择事件', 0x10, EnumData.EVENT)
        self.w['芯片'] = ParamRCombo('选择芯片', 0, EnumData.PART)
        self.w['精神'] = ParamRCombo('选择精神', 0, EnumData.SPIRIT)

        self.w['表情'] = ParamRCombo('选择表情', 0, EnumData.COMMAND['表情'])
        self.w['阵营'] = ParamRCombo('选择阵营', 0, EnumData.COMMAND['阵营'])
        self.w['比较'] = ParamRCombo('比较符号', 2, EnumData.COMMAND['比较'])
        self.w['触发'] = ParamRCombo('触发状态', 0, EnumData.COMMAND['触发'])
        self.w['点数'] = ParamRCombo('全局点数', 0, EnumData.COMMAND['点数'])
        self.w['状态'] = ParamRCombo('存在状态', 0, EnumData.COMMAND['状态'])
        self.w['行动'] = ParamRCombo('行动状态', 0, EnumData.COMMAND['行动'])
        self.w['移动'] = ParamRCombo('移动状态', 0, EnumData.COMMAND['移动'])
        self.w['势力'] = ParamCCombo('势力编号', 0, EnumData.COMMAND['势力'], sep='＆')
        self.w['选项'] = ParamCCombo('选项序号', 0, EnumData.COMMAND['选项'], sep='＆')
        self.w['演出'] = ParamCCombo('选择演出', 0, EnumData.COMMAND['演出'], sep='＆')

        self.settings = {
            0x00: ('BLOCK<{0}>',
                   [ParamVSpin('区块序号', 0, 'X')],
                   '[00]流程控制 - BLOCK区块号',
                   '各区块在运行中有时机差异'),
            0x01: ('STOP',
                   [],
                   '[01]流程控制 - BLOCK区块结束符',
                   '每个区块均需要有结束符'),
            0x02: ('ALL ({0})',
                   [ParamVSpin('套欠层级', 0)],
                   '[02]流程控制 - 检查全部表达式是否为真',
                   '只有当后跟的表达式全部为真才会执行THEN，反之执行ELSE'),
            0x03: ('ANY ({0})',
                   [ParamVSpin('套欠层级', 0)],
                   '[03]流程控制 - 检查任一表达式是否为真',
                   '只需要后跟的表达式有一条为真就执行THEN，全部为假则执行ELSE'),
            0x04: ('THEN ({0})',
                   [ParamVSpin('套欠层级', 0)],
                   '[04]流程控制 - 检查结果为真时执行',
                   '检查结果为真时执行'),
            0x05: ('ELSE ({0})',
                   [ParamVSpin('套欠层级', 0)],
                   '[05]流程控制 - 检查结果为假时执行',
                   '检查结果为假时执行'),
            0x06: ('END ({0})',
                   [ParamVSpin('套欠层级', 0)],
                   '[06]流程控制 - 结束判断符',
                   '每个检查语句均需要有结束判断符'),
            0x08: ('GOTO {0}',
                   [ParamVSpin('目标偏移', 0, '04X')],
                   '[08]流程控制 - 跳转定位',
                   '跳至指定定位并顺延逐行执行'),
            0x09: ('RUN {0}',
                   [ParamVSpin('目标偏移', 0, '04X')],
                   '[09]流程控制 - 执行定位',
                   '从指定定位开始执行并在遇到BACK后回调'),
            0x0A: ('BACK',
                   [],
                   '[0A]流程控制 - 回调符号',
                   '从回调符号开始切回原转来的定位'),
            0x0B: ('载入地图设计{0} 敌方设计{0} AI设计{0}',
                   [ParamVSpin('地图设计', 0, '02X'), ParamVSpin('敌方设计', 0, '02X'), ParamVSpin('AI设计', 0, '02X')],
                   '[0B]流程控制 - 载入场景相关信息',
                   '分别载入地图设计、敌方设计、AI设计'),
            0x0C: ('触发全局事件{0}',
                   [self.w['事件']],
                   '[0C]事件控制 - 触发全局事件',
                   '全局事件列表在修改器目录下的event.txt中，可根据需要自定义，适用于跨关卡的隐藏条件'),
            0x0D: ('触发场景事件[{0}]',
                   [ParamVSpin('场景事件', 0, '02X')],
                   '[0D]事件控制 - 触发场景事件',
                   '场景事件每次切换场景刷新，适用于本关内的隐藏条件'),
            0x0E: ('场景点数[{0}]{1}',
                   [ParamVSpin('场景点数', 0, '04X'), ParamVSpin('数值操作', 0, '+d')],
                   '[0E]事件控制 - 场景点数',
                   '场景点数每次切换场景刷新，适用于本关内的计数统计'),
            0x0F: ('全局点数{0}{1}',
                   [self.w['点数'], ParamVSpin('数值操作', 0, '+d')],
                   '[0F]事件控制 - 全局点数',
                   '全局点数包括熟练度、恋爱度等，用于跨关卡的点数操作'),
            0x10: ('全局事件{0}为{1}状态',
                   [self.w['事件'], self.w['触发']],
                   '[10]事件控制 - 判断全局事件触发情况',
                   '当全局事件已触发时返回真，否则为假'),
            0x11: ('场景事件[{0}]为{1}状态',
                   [ParamVSpin('场景事件', 0, '02X'), self.w['触发']],
                   '[11]事件控制 - 判断场景事件触发情况',
                   '当场景事件已触发时返回真， 否则为假'),
            0x12: ('场景点数[{0}]{1}{2}',
                   [self.w['点数'], self.w['比较'], ParamVSpin('点数', 0)],
                   '[12]事件控制 - 比较场景点数数值情况',
                   '当比较表达式为真时返回真，否则为假'),
            0x13: ('全局点数{0}{1}{2}',
                   [self.w['点数'], self.w['比较'], ParamVSpin('点数', 0)],
                   '[13]事件控制 - 比较全局点数',
                   '当比较表达式为真时返回真，否则为假'),
            0x14: ('路线为真实系',
                   [],
                   '[14]事件控制 - 路线为真实系',
                   '当路线选择为真实系时返回真，否则为假'),
            0x15: ('路线为超级系',
                   [],
                   '[15]事件控制 - 路线为超级系',
                   '当路线选择为超级系时返回真，否则为假'),
            0x16: ('返回假',
                   [],
                   '[16]事件控制 - 必定返回假',
                   '无条件返回假'),
            0x17: ('{0} 表情{1}\n{3}',
                   [self.w['机师'], self.w['表情'], ParamVSpin('无效', 0), self.w['文本']],
                   '[17]文本语音 - 机师普通文本会话',
                   '指定机师以指定表情说指定文本内容'),
            0x18: ('{0} 表情{1} 文本编号[{3}]',
                   [self.w['机师'], self.w['表情'], ParamVSpin('无效', 0), ParamVSpin('文本编号', 0, '04X')],
                   '[18]文本语音 - 变量普通文本会话',
                   '主角或恋人以指定表情说文本内容，文本八套一组，按性格变化'),
            0x19: ('{1} 表情{2} 语音[{0}]  文本编号[{4}]',
                   [ParamVSpin('语音', 0, '04X'), self.w['机师'], self.w['表情'], ParamVSpin('无效', 0), ParamVSpin('文本编号', 0, '04X')],
                   '[19]文本语音 - 机师普通语音会话',
                   '指定机师以指定表情说指定文本内容并伴随指定语音'),
            0x1A: ('最终话不同主角对战BOSS',
                   [ParamVSpin('未知', 0, '04X'),
                    ParamVSpin('未知', 0, '04X'),
                    ParamVSpin('未知', 0, '04X'),
                    ParamVSpin('未知', 0, '04X'),
                    ParamVSpin('未知', 0, '04X'),
                    ParamVSpin('未知', 0, '04X'),
                    ParamVSpin('未知', 0, '04X'),
                    ParamVSpin('未知', 0, '04X')],
                   '[1A]文本语音 - 主角特殊文本',
                   '最终话主角对战尤泽斯时所使用的特殊指令'),
            0x1B: ('{0} 表情{1} 文本编号[{3}]',
                   [self.w['机师'], self.w['表情'], ParamVSpin('无效', 0), ParamVSpin('文本编号', 0, '04X')],
                   '[1B]文本语音 - 变量普通语音会话',
                   '主角或恋人以指定表情说文本内容并伴随指定语音，文本八套一组，按性格变化'),
            0x1C: ('{0} 表情{1} 音乐《{4}》 文本编号[{3}]',
                   [self.w['机师'], self.w['表情'], ParamVSpin('无效', 0), ParamVSpin('文本编号', 0, '04X'), self.w['音乐']],
                   '[1C]文本语音 - 机师播放音乐会话',
                   '指定机师以指定表情说指定文本内容并伴随指定音乐'),
            0x1D: ('{0} 表情{1} 停止音乐 文本编号[{3}]',
                   [self.w['机师'], self.w['表情'], ParamVSpin('无效', 0), ParamVSpin('文本编号', 0, '04X')],
                   '[1D]文本语音 - 机师停止音乐会话',
                   '指定机师以指定表情说指定文本内容并停止指定音乐'),
            0x1E: ('胜利条件： 文本编号[{1}]\n失败条件： 文本编号[{3}]',
                   [ParamVSpin('无效', 0), ParamVSpin('文本编号', 0, '04X'),
                    ParamVSpin('无效', 0), ParamVSpin('文本编号', 0, '04X')],
                   '[1E]文本语音 - 显示胜利与失败文本',
                   '更新显示胜利条件与失败条件'),
            0x1F: ('{0}选择：文本编号[{2}]',
                   [self.w['机师'], ParamVSpin('无效', 0), ParamVSpin('文本编号', 0, '04X')],
                   '[1F]文本语音 - 选项会话文本',
                   '指定机师在二选一选项文本中做选择'),
            0x21: ('选择了第一项',
                   [ParamVSpin('无效', 0)],
                   '[21]文本语音 - 选项判断',
                   '指定机师在选项文本中选择了第一项'),
            0x22: ('场景胜利',  # TODO
                   [ParamVSpin('未知', 0)],
                   '[22]场景控制 - 场景胜利',
                   '场景完成过关，参数未知'),
            0x23: ('场景失败',
                   [],
                   '[23]场景控制 - 场景失败',
                   '场景失败 GAME OVER'),
            0x24: ('下一关为{0}',
                   [self.w['关卡']],
                   '[24]场景控制 - 选择下一关',
                   '选择下一关所用的指令'),
            0x25: ('当前回合{1}{0}',
                   [ParamVSpin('当前回合', 0), self.w['比较']],
                   '[25]场景控制 - 判断当前回合数',
                   '根据当前回合数的表达式返回真或假'),
            0x26: ('本方回合音乐为《{0}》\n敌方回合音乐为《{1}》',
                   [self.w['音乐'], self.w['音乐'], ParamVSpin('无效', 0)],
                   '[26]场景控制 - 设定场景音乐',
                   '根据选择分别设置本方回合默认音乐和敌方回合默认音乐'),
            0x27: ('播放音乐《{0}》',
                   [self.w['音乐']],
                   '[27]场景控制 - 播放音乐',
                   '播放指定音乐'),
            0x28: ('音乐复位',
                   [],
                   '[28]场景控制 - 音乐复位',
                   '停止播放指定音乐并复位为关卡默认音乐'),
            0x29: ('播放声音《{0}》',
                   [ParamVSpin('音效', 0, '04X')],
                   '[29]场景控制 - 播放声音',
                   '播放指定声音一次'),
            0x2A: ('播放动画《{0}》',
                   [ParamVSpin('CG动画', 0, '04X')],
                   '[2A]场景控制 - 播放动画',
                   '播放指定CG动画一次'),
            0x2B: ('静止等待{0}秒',  # TODO
                   [ParamVSpin('秒数', 3)],
                   '[2B]场景控制 - 静止等待',
                   '静止等待指定秒数，不确定'),
            0x2C: ('敌方设计第{0}组以{1}势力出击设为{2}阵营到地图绝对坐标',
                   [ParamVSpin('敌方组号', 0), self.w['势力'], self.w['阵营']],
                   '[2C]敌方出击 - 出击到绝对坐标',
                   '将敌方设计指定组的单位，出击到地图绝对坐标，并设定这些单位的势力和阵营'),
            0x2D: ('敌方设计第{0}组以{1}势力出击设为{2}阵营到{3}的相对坐标',
                   [ParamVSpin('敌方组号', 0), self.w['势力'], self.w['阵营'], self.w['机师']],
                   '[2D]敌方出击 - 出击到相对坐标',
                   '将敌方设计指定组的单位，出击到指定机师的相对坐标，并设定这些单位的势力和阵营'),
            0x2F: ('敌方设计第{0}组以{1}势力复活设为{2}阵营',
                   [ParamVSpin('敌方组号', 0), self.w['势力'], self.w['阵营']],
                   '[2F]敌方出击 - 复活出击',
                   '将敌方设计指定组复活并从被击破处原地出击'),
            0x30: ('格纳库开启',
                   [],
                   '[30]机库操作 - 机库开启',
                   '打开格纳库做机体机师的增删改操作'),
            0x31: ('格纳库关闭',
                   [],
                   '[31]机库操作 - 机库关闭',
                   '机体机师操作完毕后必须要关闭格纳库'),
            0x32: ('{0}入库 机体{2}改 武器{1}改',
                   [self.w['机体'], ParamVSpin('武器改造', 0), ParamVSpin('机体改造', 0)],
                   '[32]机库操作 - 增加机体',
                   '增加指定机体并确定机体和武器的默认改造幅度'),
            0x33: ('{0}分流',
                   [self.w['机体']],
                   '[33]机库操作 - 机体分流',
                   '指定机体分流，在机体合流前无法在格纳库中看到，但改造保留'),
            0x34: ('{0}合流',
                   [self.w['机体']],
                   '[34]机库操作 - 机体合流',
                   '指定机体合流，保留分流时的改造，重新进入格纳库'),
            0x35: ('{0}离队',
                   [self.w['机体']],
                   '[35]机库操作 - 机体离队',
                   '指定机体完全离队，不再保留改造'),
            0x36: ('{0}换成{1}',
                   [self.w['机体'], self.w['机体']],
                   '[36]机库操作 - 机体替换',
                   '将指定机体替换为另一台机体，并保留对应的改造'),
            0x37: ('{0}加入 机师{2}级 击坠数{1}',
                   [self.w['机师'], ParamVSpin('击坠数', 0), ParamVSpin('等级', 1)],
                   '[37]机库操作 - 加入机师',
                   '指定机师加入并确定等级和击坠数'),
            0x38: ('{0}分流',
                   [self.w['机师']],
                   '[38]机库操作 - 机师分流',
                   '指定机师分流，在机师合流前无法在格纳库中看到，但等级和击坠数保留'),
            0x39: ('{0}合流',
                   [self.w['机师']],
                   '[39]机库操作 - 机师合流',
                   '指定机师合流，保留分流时的等级和击坠数，重新进入格纳库'),
            0x3A: ('{0}离队',
                   [self.w['机师']],
                   '[3A]机库操作 - 机师离队',
                   '指定机师完全离队，不再保留等级和击坠数'),
            0x3B: ('{0}换成{1}',
                   [self.w['机师'], self.w['机师']],
                   '[3B]机库操作 - 机师替换',
                   '将指定机师替换为另一名机师，并保留等级和击坠数'),
            0x3C: ('未知',  # TODO
                   [ParamVSpin('未知', 0)],
                   '[3C]未知',
                   '未知'),
            0x3D: ('加入或强制换乘 {0} 机师{2}级 击坠数{1} 搭乘{3} 机体{5}改 武器{4}改',
                   [self.w['机师'], ParamVSpin('击坠数', 0), ParamVSpin('等级', 1),
                    self.w['机体'], ParamVSpin('武器改造', 0), ParamVSpin('机体改造', 0)],
                   '[3D]机库操作 - 机师机体同时加入或强制换乘',
                   '未加入的情况下，机师机体同时以指定等级击坠数和改造加入\n已加入的情况下，则机师强制换乘该机体'),
            0x3E: ('{0}与搭乘机体分流',
                   [self.w['机师']],
                   '[3E]机库操作 - 机师与搭乘机体分流',
                   '指定机师与所搭乘的机体一同分流'),
            0x3F: ('{0}与搭乘机师分流',
                   [self.w['机体']],
                   '[3F]机库操作 - 机体与搭乘机师分流',
                   '指定机体与所搭乘的机师一同分流'),
            0x40: ('{0}与搭乘机体合流',
                   [self.w['机师']],
                   '[40]机库操作 - 机师与搭乘机体合流',
                   '指定机师与所搭乘的机体一同合流'),
            0x41: ('{0}与搭乘机师合流',
                   [self.w['机体']],
                   '[41]机库操作 - 机体与搭乘机师合流',
                   '指定机体与所搭乘的机师一同合流'),
            0x42: ('{0}与搭乘机体离队',
                   [self.w['机师']],
                   '[42]机库操作 - 机师与搭乘机体离队',
                   '指定机师与所搭乘的机体一同离队'),
            0x43: ('{0}强制搭乘{1}',
                   [self.w['机师'], self.w['机体']],
                   '[43]机库操作 - 强制换乘',
                   '指定机师强制换乘指定机体'),
            0x44: ('{0}强制搭乘[07D]V2ガンダム',
                   [self.w['机师']],
                   '[44]机库操作 - 强制换乘V2ガンダム',
                   '指定机师强制换乘V2ガンダム'),
            0x45: ('{0}强制取消搭乘',
                   [self.w['机师']],
                   '[45]机库操作 - 机师强制取消搭乘',
                   '指定机师取消搭乘机体'),
            0x46: ('{0}强制取消搭乘',
                   [self.w['机体']],
                   '[46]机库操作 - 机体强制取消搭乘',
                   '指定机体取消搭乘机师'),
            0x47: ('{0}强制出场',
                   [self.w['机师']],
                   '[47]机库操作 - 机师强制出场',
                   '指定机师强制出场并从待出击列表中隐藏'),
            0x48: ('妖精{0}附加给{1}',
                   [self.w['机师'], self.w['机师']],
                   '[48]机库操作 - 妖精配属',
                   '指定妖精附加配属给指定机师'),
            0x49: ('{0}从出击名单中隐藏',
                   [self.w['机师']],
                   '[49]机库操作 - 机师隐藏',
                   '指定机师从待出击列表中隐藏'),
            0x4A: ('{0}从出击名单中隐藏',
                   [self.w['机体']],
                   '[4A]机库操作 - 机体隐藏',
                   '指定机体从待出击列表中隐藏'),
            0x4B: ('{0}强制搭乘空机体',
                   [self.w['机师']],
                   '[4B]机库操作 - 机师强制搭乘空机体',
                   '指定机师找任意空机体搭乘'),
            0x4E: ('{0}以分离状态出击',
                   [self.w['机体']],
                   '[4E]机库操作 - 合体机以分离状态出击',
                   '指定合体机以分离状态出击'),
            0x4F: ('开始出击',
                   [],
                   '[4F]出击操作 - 开始出击',
                   '出击打开'),
            0x50: ('出击完毕',
                   [],
                   '[50]出击操作 - 出击完毕',
                   '出击关闭'),
            0x51: ('{0}出击到地图绝对坐标 X{1} Y{2}',
                   [self.w['机师'], ParamVSpin('X坐标', 0), ParamVSpin('Y坐标', 0)],
                   '[51]出击操作 - 机师出击到绝对坐标',
                   '将指定机师出击到地图绝对坐标'),
            0x52: ('{0}出击到{3}相对坐标 X{1} Y{2}',
                   [self.w['机师'], ParamVSpin('X坐标', 0, '+d'), ParamVSpin('Y坐标', 0, '+d'), self.w['机师']],
                   '[52]出击操作 - 机师出击到相对坐标',
                   '将指定机师出击到另一机师的相对坐标'),
            0x54: ('{0}出击到地图绝对坐标 X{1} Y{2}',
                   [self.w['机体'], ParamVSpin('X坐标', 0), ParamVSpin('Y坐标', 0)],
                   '[54]出击操作 - 机体出击到绝对坐标',
                   '将指定机体出击到地图绝对坐标'),
            0x55: ('{0}出击到{3}相对坐标 X{1} Y{2}',
                   [self.w['机体'], ParamVSpin('X坐标', 0, '+d'), ParamVSpin('Y坐标', 0, '+d'), self.w['机师']],
                   '[55]出击操作 - 机体出击到相对坐标',
                   '将指定机体出击到指定机师的相对坐标'),
            0x57: ('选择{0}台机体出击到地图绝对坐标配置[{1}]',
                   [ParamVSpin('数量', 0), ParamVSpin('坐标配置', 0)],
                   '[57]出击操作 - 选择机体出击到绝对坐标配置',
                   '将指定数量的机体出击到地图设计中划定的绝对坐标配置'),
            0x58: ('选择{0}台机体出击到{2}相对坐标配置[{1}]',
                   [ParamVSpin('数量', 0), ParamVSpin('坐标配置', 0), self.w['机师']],
                   '[58]出击操作 - 选择机体出击到相对坐标配置',
                   '将指定数量的机体出击到指定机师的相对坐标配置'),
            0x5A: ('选择母舰出击到地图绝对坐标 X{1} Y{2}',
                   [ParamVSpin('无效', 1), ParamVSpin('X坐标', 0), ParamVSpin('Y坐标', 0)],
                   '[5A]出击操作 - 选择母舰出击到绝对坐标',
                   '选择一艘母舰出击到地图绝对坐标'),
            0x5B: ('设定{0}等级为{2}{1}',
                   [self.w['机师'], ParamVSpin('设定等级', 0, '+d'), self.w['机师']],
                   '[5B]机库操作 - 设定机师等级',
                   '设定指定机师等级，可选择以另一机师等级为参照'),
            0x5C: ('{0}等级{1}',
                   [self.w['机师'], ParamVSpin('等级变化', 0, '+d')],
                   '[5C]机库操作 - 调整机师等级',
                   '调整指定机师等级'),
            0x5D: ('设定{0}击坠为{1}',
                   [self.w['机师'], ParamVSpin('设定击坠', 0)],
                   '[5D]机库操作 - 设定机师击坠数',
                   '设定指定机师击坠数'),
            0x5E: ('{0}击坠{1}',
                   [self.w['机师'], ParamVSpin('击坠变化', 0, '+d')],
                   '[5E]机库操作 - 调整机师击坠数',
                   '调整指定机师击坠数'),
            0x5F: ('{0}加入本方',
                   [self.w['机师']],
                   '[5F]场景控制 - 机师加入本方',
                   '场景上指定机师加入本方'),
            0x60: ('{0}转为{1}势力',
                   [self.w['机师'], self.w['势力']],
                   '[60]场景控制 - 机师势力转换',
                   '场景上指定机师转为指定势力'),
            0x61: ('增加芯片 {0}',
                   [self.w['芯片']],
                   '[61]资源操作 - 增加芯片',
                   '增加指定芯片'),
            0x62: ('允许换装 V2{0}{1}ガンダム',
                   [ParamRCombo('アサルト', 0, {0: '', 1: 'アサルト'}), ParamRCombo('バスター', 0, {0: '', 1: 'バスター'})],
                   '[62]资源操作 - 增加V2ガンダム换装',
                   '增加V2ガンダム的不同换装'),
            0x63: ('[07D]V2ガンダム换装为{0}',
                   [self.w['机体']],
                   '[63]资源操作 - 指定V2ガンダム换装',
                   '为V2ガンダム更换上指定换装'),
            0x64: ('增加资金 {0}',
                   [ParamVSpin('资金', 0, )],
                   '[64]资源操作 - 增加资金',
                   '增加资金'),
            0x65: ('{0}复活',
                   [self.w['机师']],
                   '[65]场景操作 - 复活机师',
                   '复活指定机师'),
            0x66: ('{0}复活',
                   [self.w['机体']],
                   '[66]场景操作 - 复活机体',
                   '复活指定机体'),
            0x67: ('移动{0}到地图绝对坐标 X{1} Y{2}',
                   [self.w['机师'], ParamVSpin('X坐标', 0), ParamVSpin('Y坐标', 0)],
                   '[67]光标操作 - 移动机师对话光标到绝对坐标',
                   '将机师光标移动到地图绝对坐标以待对话使用'),
            0x68: ('移动{0}到{1}相对坐标 X{2} Y{3}',
                   [self.w['机师'], self.w['机师'], ParamVSpin('X坐标', 0, '+d'), ParamVSpin('Y坐标', 0, '+d')],
                   '[68]光标操作 - 移动机师对话光标到相对坐标',
                   '将机师光标移动到另一机师相对坐标以待对话使用'),
            0x69: ('移动{0}到敌方序号[{2}]相对坐标 X{3} Y{4}',
                   [self.w['机师'],
                    ParamVSpin('无效', -0x80, '2X'),
                    ParamVSpin('序号', 0x0, '02X'),
                    ParamVSpin('X坐标', 0, '+d'),
                    ParamVSpin('Y坐标', 0, '+d')],
                   '[69]光标操作 - 移动机师对话光标到敌方相对坐标',
                   '将机师光标移动到敌方设计指定单位的相对坐标以待对话使用'),
            0x6A: ('移动光标到地图绝对坐标 X{0} Y{1}',
                   [ParamVSpin('X坐标', 0), ParamVSpin('Y坐标', 0)],
                   '[6A]光标操作 - 移动光标焦点到绝对坐标',
                   '将对话光标的焦点移动到地图绝对坐标'),
            0x6B: ('移动光标到{0}相对坐标 X{1} Y{2}',
                   [self.w['机师'], ParamVSpin('X坐标', 0, '+d'), ParamVSpin('Y坐标', 0, '+d')],
                   '[6B]光标操作 - 移动光标焦点到相对坐标',
                   '将对话光标的焦点移动到指定机师的相对坐标'),
            0x6C: ('移动光标到地图绝对坐标 X{0} Y{1} 并停留{2}单位时间',
                   [ParamVSpin('X坐标', 0), ParamVSpin('Y坐标', 0), ParamVSpin('停留时间', 0)],
                   '[6C]光标操作 - 移动光标焦点到绝对坐标并停留',
                   '将对话光标的焦点移动到地图绝对坐标并停留一定时间'),
            0x6E: ('屏幕静止{0}',
                   [ParamVSpin('停留时间', 0)],
                   '[6E]光标操作 - 屏幕静止',
                   '对话光标焦点停留一定时间'),
            0x6F: ('{0}撤退',
                   [self.w['机师']],
                   '[6F]场景控制 - 机师撤退',
                   '指定机师强制撤退'),
            0x70: ('敌方序号[{1}]撤退',
                   [ParamVSpin('无效', -0x80, '2X'), ParamVSpin('序号', 0x0, '02X')],
                   '[70]场景控制 - 敌方撤退',
                   '指定敌方设计单位强制撤退'),
            0x71: ('敌方第{0}组全部撤退',
                   [ParamVSpin('组号', 0x0, '02d')],
                   '[71]场景控制 - 敌方小组撤退',
                   '指定敌方设计小组强制撤退'),
            0x72: ('{0}势力全部撤退',
                   [self.w['势力']],
                   '[72]场景控制 - 势力撤退',
                   '指定势力强制撤退'),
            0x73: ('{0}阵营撤退',
                   [self.w['阵营']],
                   '[73]场景控制 - 阵营撤退',
                   '指定阵营强制撤退'),
            0x74: ('{0}阵营撤退到 X{1}-X{3} Y{2}-Y{4}区域内',
                   [self.w['阵营'], ParamVSpin('X1', 1), ParamVSpin('Y1', 1), ParamVSpin('X2', 1), ParamVSpin('Y2', 1)],
                   '[74]场景控制 - 阵营撤退到区域',
                   '指定阵营撤退到划定的区域'),
            0x75: ('{0}{1}',
                   [self.w['机师'], self.w['状态']],
                   '[75]条件判断 - 判断机师状态',
                   '判断机师是否存在'),
            0x77: ('{0}{1}',
                   [self.w['机体'], self.w['状态']],
                   '[77]条件判断 - 判断机体状态',
                   '判断机体是否存在'),
            0x78: ('{0}处于搭载中',
                   [self.w['机师']],
                   '[78]条件判断 - 判断机师搭载状态',
                   '判断机师是否处于搭载状态中'),
            0x79: ('敌方第{0}组数量{1}{2}台',
                   [ParamVSpin('组号', 0, '02d'), self.w['比较'], ParamVSpin('数量', 0)],
                   '[79]条件判断 - 判断敌方小组数量',
                   '判断敌方小组数量'),
            0x7A: ('{0}势力数量{1}{2}台',
                   [self.w['势力'], self.w['比较'], ParamVSpin('数量', 0)],
                   '[7A]条件判断 - 判断势力数量',
                   '判断势力数量'),
            0x7B: ('{0}阵营数量{1}{2}台',
                   [self.w['阵营'], self.w['比较'], ParamVSpin('数量', 0)],
                   '[7B]条件判断 - 判断阵营数量',
                   '判断阵营数量'),
            0x7C: ('{0}进入 X{1}-X{3} Y{2}-Y{4}区域内',
                   [self.w['机师'], ParamVSpin('X1', 1), ParamVSpin('Y1', 1), ParamVSpin('X2', 1), ParamVSpin('Y2', 1)],
                   '[7C]条件判断 - 判断机师位置',
                   '判断指定机师是否进入划定区域'),
            0x7D: ('敌方序号[{1}]进入 X{2}-X{4} Y{3}-Y{5}区域内',
                   [ParamVSpin('无效', -0x80, '2X'),
                    ParamVSpin('序号', 0, '02X'),
                    ParamVSpin('X1', 1),
                    ParamVSpin('Y1', 1),
                    ParamVSpin('X2', 1),
                    ParamVSpin('Y2', 1)],
                   '[7D]条件判断 - 判断敌方位置',
                   '判断敌方列表单位是否进入划定区域'),
            0x7E: ('{0}进入 X{1}-X{3} Y{2}-Y{4}区域内',
                   [self.w['机体'], ParamVSpin('X1', 1), ParamVSpin('Y1', 1), ParamVSpin('X2', 1), ParamVSpin('Y2', 1)],
                   '[7E]条件判断 - 判断机体位置',
                   '判断指定机体是否进入划定区域'),
            0x80: ('{0}势力进入 X{1}-X{3} Y{2}-Y{4}区域内',
                   [self.w['势力'], ParamVSpin('X1', 1), ParamVSpin('Y1', 1), ParamVSpin('X2', 1), ParamVSpin('Y2', 1)],
                   '[80]条件判断 - 判断势力位置',
                   '判断势力是否进入划定区域'),
            0x81: ('{0}阵营进入 X{1}-X{3} Y{2}-Y{4}区域内',
                   [self.w['阵营'], ParamVSpin('X1', 1), ParamVSpin('Y1', 1), ParamVSpin('X2', 1), ParamVSpin('Y2', 1)],
                   '[81]条件判断 - 判断阵营位置',
                   '判断阵营是否进入划定区域'),
            0x82: ('{0}与{1}相距{2}格',
                   [self.w['机师'], self.w['机师'], ParamVSpin('距离', 1)],
                   '[82]条件判断 - 判断机师间距离',
                   '判断指定机师之间的距离'),
            0x83: ('{0}与敌方序号[{2}]相距{3}格',
                   [self.w['机师'], ParamVSpin('无效', -0x80, '2X'), ParamVSpin('序号', 0, '02X'), ParamVSpin('距离', 1)],
                   '[83]条件判断 - 判断机师与敌方列表单位距离',
                   '判断指定机师与敌方列表单位之间的距离'),
            0x84: ('{0}气力调整为{1}',
                   [self.w['机师'], ParamVSpin('气力', 100)],
                   '[84]场景操作 - 调整机师气力',
                   '调整指定机师气力'),
            0x85: ('{0}阵营气力调整为{1}',
                   [self.w['阵营'], ParamVSpin('气力', 100)],
                   '[85]场景操作 - 调整阵营气力',
                   '调整阵营气力'),
            0x86: ('{0}EN减少{1}',
                   [self.w['机师'], ParamVSpin('EN减少', 100)],
                   '[86]场景操作 - 减少机师EN',
                   '减少指定机师EN'),
            0x87: ('未知',  # TODO
                   [],
                   '[87]未知',
                   '未知'),
            0x88: ('{0}HP调整{1}%',
                   [self.w['机师'], ParamVSpin('HP变化', 100)],
                   '[88]场景操作 - 调整机师HP',
                   '调整指定机师HP'),
            0x89: ('{0}阵营HP调整{1}%',
                   [self.w['阵营'], ParamVSpin('HP变化', 100)],
                   '[89]场景操作 - 调整阵营HP',
                   '调整指定阵营HP'),
            0x8B: ('{0}阵营SP调整{1}%',
                   [self.w['阵营'], ParamVSpin('SP变化', 100)],
                   '[8B]场景操作 - 调整阵营SP',
                   '调整指定阵营SP'),
            0x8C: ('{0}电缆连接到地图绝对坐标 X{1} Y{2}',
                   [self.w['机师'], ParamVSpin('X坐标', 1), ParamVSpin('Y坐标', 1)],
                   '[8C]场景操作 - EVA电缆连接到绝对坐标',
                   '将指定机师的EVA电缆连接到地图绝对坐标'),
            0x8D: ('{0}电缆连接到{1}',
                   [self.w['机师'], self.w['机师']],
                   '[8D]场景操作 - EVA电缆连接到母舰',
                   '将指定机师的EVA电缆连接到指定母舰机师'),
            0x8E: ('{0}电缆就近连接',
                   [self.w['机师']],
                   '[8E]场景操作 - EVA电缆就近连接',
                   '将指定机师的EVA电缆就近连接到插座'),
            0x8F: ('{0}电缆强制断开',
                   [self.w['机师']],
                   '[8F]场景操作 - EVA电缆强制断开',
                   '将指定机师的EVA电缆断开'),
            0x90: ('{0}移动到地图绝对坐标 X{1} Y{2}',
                   [self.w['机师'], ParamVSpin('X坐标', 1), ParamVSpin('Y坐标', 1)],
                   '[90]场景操作 - 移动机师到绝对坐标',
                   '将指定机师移动到地图绝对坐标'),
            0x91: ('敌方序号[{1}]移动到地图绝对坐标 X{2} Y{3}',
                   [ParamVSpin('无效', -0x80, '2X'),
                    ParamVSpin('序号', 0, '02X'),
                    ParamVSpin('X坐标', 1),
                    ParamVSpin('Y坐标', 1)],
                   '[91]场景操作 - 移动敌方列表单位到绝对坐标',
                   '将指定敌方列表单位移动到地图绝对坐标'),
            0x92: ('{0}移动到{1}相对坐标 X{2} Y{3} {4}',
                   [self.w['机师'], self.w['机师'], ParamVSpin('X坐标', 0), ParamVSpin('X坐标', 0), self.w['移动']],
                   '[92]场景操作 - 移动机师到相对坐标',
                   '将指定机师移动到另一机师相对坐标'),
            0x93: ('{0}移动到敌方序号[{2}]相对坐标 X{3} Y{4} {5}',
                   [self.w['机师'],
                    ParamVSpin('无效', -0x80, '2X'),
                    ParamVSpin('序号', 0, '02X'),
                    ParamVSpin('X坐标', 0),
                    ParamVSpin('X坐标', 0),
                    self.w['移动']],
                   '[93]场景操作 - 移动机师到敌方单位相对坐标',
                   '将指定机师移动到指定敌方列表单位相对坐标'),
            0x94: ('敌方序号[{1}]移动到{2}相对坐标 X{3} Y{4} {5}',
                   [ParamVSpin('无效', -0x80, '2X'),
                    ParamVSpin('序号', 0, '02X'),
                    self.w['机师'],
                    ParamVSpin('X坐标', 0),
                    ParamVSpin('X坐标', 0),
                    self.w['移动']],
                   '[94]场景操作 - 移动敌方单位到相对坐标',
                   '将指定敌方列表单位移动到指定机师相对坐标'),
            0x96: ('战斗：{0} 攻击 {1}\n攻方：武器编号[{2}] 命中{4}% 伤害{6}% {8}\n守方：武器编号[{3}] 命中{5}% 伤害{7}% {9}',
                   [self.w['机师'],
                    self.w['机师'],
                    ParamVSpin('攻方武器', 0, 'X'),
                    ParamVSpin('守方武器', 0, 'X'),
                    ParamVSpin('攻方命中', 0),
                    ParamVSpin('守方命中', 0),
                    ParamVSpin('攻方伤害', 0),
                    ParamVSpin('守方伤害', 0),
                    self.w['演出'],
                    self.w['演出']],
                   '[96]战斗演出 - 机师间强制战斗演出',
                   '指定机师攻击另一机师并设定进攻方与反击方效果'),
            0x97: ('战斗：敌方序号[{1}] 攻击 {2}\n攻方：武器编号[{3}] 命中{5}% 伤害{7}% {9}\n守方：武器编号[{4}] 命中{6}% 伤害{8}% {10}',
                   [ParamVSpin('无效', -0x80, '2X'),
                    ParamVSpin('序号', 0, '02X'),
                    self.w['机师'],
                    ParamVSpin('攻方武器', 0, 'X'),
                    ParamVSpin('守方武器', 0, 'X'),
                    ParamVSpin('攻方命中', 0),
                    ParamVSpin('守方命中', 0),
                    ParamVSpin('攻方伤害', 0),
                    ParamVSpin('守方伤害', 0),
                    self.w['演出'],
                    self.w['演出']],
                   '[97]战斗演出 - 敌方列表单位攻击机师强制战斗演出',
                   '指定敌方列表单位攻击指定机师并设定进攻方与反击方效果'),
            0x98: ('战斗：{0} 攻击 敌方序号[{2}]\n攻方：武器编号[{3}] 命中{5}% 伤害{7}% {9}\n守方：武器编号[{4}] 命中{6}% 伤害{8}% {10}',
                   [self.w['机师'],
                    ParamVSpin('无效', -0x80, '2X'),
                    ParamVSpin('序号', 0, '02X'),
                    ParamVSpin('攻方武器', 0, 'X'),
                    ParamVSpin('守方武器', 0, 'X'),
                    ParamVSpin('攻方命中', 0),
                    ParamVSpin('守方命中', 0),
                    ParamVSpin('攻方伤害', 0),
                    ParamVSpin('守方伤害', 0),
                    self.w['演出'],
                    self.w['演出']],
                   '[98]战斗演出 - 机师攻击敌方列表单位强制战斗演出',
                   '指定机师攻击指定敌方列表单位并设定进攻方与反击方效果'),
            0x99: ('战斗关闭',
                   [],
                   '[99]战斗演出 - 关闭战斗演出',
                   '关闭强制战斗演出'),
            0x9A: ('允许{0}势力攻击{1}势力',
                   [self.w['势力'], self.w['势力']],
                   '[9A]规则设置 - 势力攻击许可',
                   '允许指定势力攻击另一势力'),
            0x9B: ('禁止{0}势力攻击{1}势力',
                   [self.w['势力'], self.w['势力']],
                   '[9B]规则设置 - 势力攻击禁止',
                   '禁止指定势力攻击另一势力'),
            0x9C: ('禁用{0}的{1}菜单选项',
                   [self.w['机师'], self.w['选项']],
                   '[9C]规则设置 - 禁用机师菜单选项',
                   '禁用指定机师的部分菜单选项\n菜单根据机体不同顺序有变化\n如变形机体和合体机体的菜单顺序就与普通机体不同'),
            0x9D: ('禁用敌方序号[{1}]的{2}菜单选项',
                   [ParamVSpin('无效', -0x80, '2X'), ParamVSpin('序号', 0, '02X'), self.w['选项']],
                   '[9D]规则设置 - 禁用敌方菜单选项',
                   '禁用指定敌方列表单位的菜单选项'),
            0x9E: ('启用{0}的{1}菜单选项',
                   [self.w['机师'], self.w['选项']],
                   '[9E]规则设置 - 启用机师菜单选项',
                   '启用指定机师的部分菜单选项\n菜单根据机体不同顺序有变化\n如变形机体和合体机体的菜单顺序就与普通机体不同'),
            0x9F: ('{0}强制击破',
                   [self.w['机师']],
                   '[9F]场景操作 - 强制击破机师',
                   '指定机师强制击破'),
            0xA0: ('敌方序号[{1}]强制击破',
                   [ParamVSpin('无效', -0x80, '2X'), ParamVSpin('序号', 0, '02X')],
                   '[A0]场景操作 - 强制击破敌方',
                   '指定敌方列表单位强制击破'),
            0xA1: ('{0}强制搭载',
                   [self.w['机师']],
                   '[A1]场景操作 - 机师强制搭载',
                   '指定机师强制搭载母舰'),
            0xA2: ('{0}取消搭载',
                   [self.w['机师']],
                   '[A2]场景操作 - 机师取消搭载',
                   '指定机师强制从搭载母舰上出击'),
            0xA3: ('{0}强制浮上',
                   [self.w['机师']],
                   '[A3]场景操作 - 机师强制浮上',
                   '指定机师强制浮起'),
            0xA4: ('{0}强制着地',
                   [self.w['机师']],
                   '[A4]场景操作 - 机师强制着地',
                   '指定机师强制着地'),
            0xA5: ('{0}搭乘机体强制变形为{1}',
                   [self.w['机师'], self.w['机体']],
                   '[A5]场景操作 - 强制变形',
                   '指定机师搭乘机体强制变形'),
            0xA6: ('{0}搭乘机体强制合体',
                   [self.w['机师']],
                   '[A6]场景操作 - 强制合体',
                   '指定机师搭乘机体强制合体'),
            0xA7: ('{0}搭乘机体强制分离',
                   [self.w['机师']],
                   '[A7]场景操作 - 强制分离',
                   '指定机师搭乘机体强制分离'),
            0xA8: ('{0}强制使用精神{1} {2}次',
                   [self.w['机师'], self.w['精神'], ParamVSpin('次数', 1), ParamRCombo('未知', 0, {0: '未知', 1: '未知'})],
                   '[A8]场景操作 - 强制使用精神',
                   '指定机师强制使用精神，并设定使用次数'),
            0xA9: ('{0}强制设为{1}',
                   [self.w['机师'], self.w['行动']],
                   '[A9]场景操作 - 强制设定行动状态',
                   '指定机师设定行动状态'),
            0xAA: ('{0}强制切换傀儡系统',
                   [self.w['机师']],
                   '[AA]场景操作 - 强制切换傀儡系统',
                   '指定EVA机师切换傀儡系统'),
            0xAB: ('{0}可以说得{1}',
                   [self.w['机师'], self.w['机师']],
                   '[AB]说得选项 - 增加机师说得机师选项',
                   '指定机师与另一机师间增加说得选项'),
            0xAC: ('{0}可以说得敌方序号[{2}]',
                   [self.w['机师'], ParamVSpin('无效', -0x80, '2X'), ParamVSpin('序号', 0, '02X')],
                   '[AC]说得选项 - 增加机师说得敌方选项',
                   '指定机师与敌方列表单位间增加说得选项'),
            0xAD: ('{0}已经说得{1}',
                   [self.w['机师'], self.w['机师']],
                   '[AD]条件判断 - 判断机师间说得状态',
                   '指定机师已经说得另一机师为真，否则为假'),
            0xAE: ('{0}已经说得敌方序号[{2}]',
                   [self.w['机师'], ParamVSpin('无效', -0x80, '2X'), ParamVSpin('序号', 0, '02X')],
                   '[AE]条件判断 - 判断机师与敌方列表单位说得状态',
                   '指定机师已经说得指定敌方列表单位为真，否则为假'),
            0xAF: ('{0}与{1}交手',
                   [self.w['机师'], self.w['机师']],
                   '[AF]条件判断 - 判断机师间交手',
                   '指定机师与另一机师交手为真，否则为假'),
            0xB0: ('{0}与敌方序号[{2}]交手',
                   [self.w['机师'], ParamVSpin('无效', -0x80, '2X'), ParamVSpin('序号', 0, '02X')],
                   '[B0]条件判断 - 判断机师与敌方交手',
                   '指定机师与指定敌方列表单位交手为真，否则为假'),
            0xB1: ('{0}发起攻击',
                   [self.w['机师']],
                   '[B1]条件判断 - 判断机师交手',
                   '指定机师有交手为真，未交手为假'),
            0xB2: ('敌方序号[{1}]被击破',
                   [ParamVSpin('无效', -0x80, '2X'), ParamVSpin('序号', 0, '02X')],
                   '[B2]条件判断 - 判断敌方被击破',
                   '指定敌方列表单位被击破为真，否则为假'),
            0xB3: ('{0}被击破',
                   [self.w['机师']],
                   '[B3]条件判断 - 判断机师被击破[BLOCK7]',
                   '指定机师被击破为真，否则为假，用于[BLOCK7]'),
            0xB4: ('{0}被击破',
                   [self.w['机体']],
                   '[B4]条件判断 - 判断机体被击破',
                   '指定机体被击破为真，否则为假'),
            0xB5: ('本方被击破{0}机',
                   [ParamVSpin('数量', 1)],
                   '[B5]条件判断 - 判断本方被击破数',
                   '判断本方被击破数量'),
            0xB6: ('{0}HP少于{1}%',
                   [self.w['机师'], ParamVSpin('HP', 0)],
                   '[B6]条件判断 - 判断机师HP量',
                   '判断机师HP量'),
            0xB7: ('{0}被击破',
                   [self.w['机师']],
                   '[B7]条件判断 - 判断机师被击破[BLOCK8]',
                   '指定敌方列表单位被击破为真，否则为假，用于[BLOCK8]'),
            0xB8: ('敌方序号[{1}]未被击破',
                   [ParamVSpin('无效', -0x80, '2X'), ParamVSpin('序号', 0, '02X')],
                   '[B8]条件判断 - 判断敌方未被击破',
                   '指定敌方列表单位未被击破为真，否则为假'),
            0xB9: ('{0} {1} {2} {3}\n{4} {5} {6} {7} ',  # TODO
                   [ParamVSpin('1', 1, '04X'),
                    ParamVSpin('2', 0, '04X'),
                    ParamVSpin('3', 0, '04X'),
                    ParamVSpin('4', 0, '04X'),
                    ParamVSpin('5', 0, '04X'),
                    ParamVSpin('6', 0, '04X'),
                    ParamVSpin('7', 0, '04X'),
                    ParamVSpin('8', 0, '04X'), ],
                   '[B9]地图演出 - 相对坐标特殊地图演出',
                   '在指定机师的相对坐标进行特殊的地图演出'),
            0xBA: ('地图演出[{0}] 地图绝对坐标 X{1} Y{2}',
                   [ParamVSpin('演出特效', 0, '04X'),
                    ParamVSpin('X坐标', 1),
                    ParamVSpin('Y坐标', 1)],
                   '[BA]地图演出 - 绝对坐标地图演出',
                   '在地图绝对坐标进行地图演出'),
            0xBB: ('地图演出[{0}] {1}相对坐标 X{2} Y{3}',
                   [ParamVSpin('演出特效', 0, '04X'),
                    self.w['机师'],
                    ParamVSpin('X坐标', 1),
                    ParamVSpin('Y坐标', 1)],
                   '[BB]地图演出 - 相对坐标地图演出',
                   '在指定机师的相对坐标进行地图演出'),
        }

    def explain(self, command: dict[str, int | list[int] | str]):
        code = command.get('Code')
        param = command.get('Param')
        param_setting: tuple[str, list[ParamWidget], str, str] = self.settings.get(code, (str(code), tuple()))
        param_text, param_widgets, _, _ = param_setting

        if code == 0xB9:
            set_count = param[0]
            param_widgets.extend(param_widgets[4:] * (set_count - 1))
            texts = param_text.splitlines()
            texts.extend(texts[1:] * (set_count - 1))
            param_text = '\n'.join(texts)

        explain_list = list()
        for param_idx, param_widget in enumerate(param_widgets):
            explain_list.append(param_widget.explain(param[param_idx]))
        return param_text.format(*explain_list)
