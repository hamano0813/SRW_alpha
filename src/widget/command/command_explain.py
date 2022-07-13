#!/usr/bin/env python
# -*- coding: utf-8 -*-

from parameter import EnumData
from widget.command import ParamRCombo, ParamCCombo, ParamVSpin
from widget.command.param_widget import ParamWidget


class CommandExplain:
    def __init__(self, **kwargs):
        self.w: dict[str, ParamWidget] = dict()

        self.w['机体'] = ParamRCombo('选择机体', 0, kwargs.get('robots'))
        self.w['机师'] = ParamRCombo('选择机师', 0, kwargs.get('pilots') | {-0x1: ''})
        self.w['文本'] = ParamVSpin('选择文本', 0, '04X', mapping=kwargs.get('messages'))

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
        self.w['动画'] = ParamRCombo('选择动画', 0, EnumData.COMMAND['动画'])
        self.w['势力'] = ParamCCombo('势力编号', 1, EnumData.COMMAND['势力'], sep='|')
        self.w['选项'] = ParamCCombo('选项序号', 1, EnumData.COMMAND['选项'], sep='＆')
        self.w['演出'] = ParamCCombo('选择演出', 0, EnumData.COMMAND['演出'], sep=' ')

        # self.w['无效'] = ParamVSpin('无效参数', -0x80, '2X')

        self.w['套嵌层级'] = ParamVSpin('套嵌层级', 0, range=(0x0, 0x10))
        self.w['目标偏移'] = ParamVSpin('目标偏移', 0, '04X', range=(0x0, 0x2000))
        self.w['场景事件'] = ParamVSpin('场景事件', 0, '02X', range=(0x0, 0xFF))
        self.w['场景点数'] = ParamVSpin('场景点数', 0, '02X', range=(0x0, 0xFF))
        self.w['敌方组号'] = ParamVSpin('敌方组号', 0, range=(0x0, 0xF))
        self.w['敌方序号'] = ParamVSpin('敌方序号', 0, '02X', range=(0x0, 0x9F))
        self.w['演出代码'] = ParamVSpin('演出代码', 0, '02X', range=(0x0, 0x7F))
        self.w['X绝对坐标'] = ParamVSpin('X坐标', 1, range=(0x1, 0x30))
        self.w['Y绝对坐标'] = ParamVSpin('Y坐标', 1, range=(0x1, 0x30))
        self.w['X相对坐标'] = ParamVSpin('X坐标', 0, '+d', range=(-0x30, 0x30))
        self.w['Y相对坐标'] = ParamVSpin('Y坐标', 0, '+d', range=(-0x30, 0x30))
        self.w['坐标配置'] = ParamVSpin('坐标配置', 0, range=(0x0, 0xF))
        self.w['X1'] = ParamVSpin('X1', 0, range=(0x1, 0x30))
        self.w['X2'] = ParamVSpin('X2', 0, range=(0x1, 0x30))
        self.w['Y1'] = ParamVSpin('Y1', 0, range=(0x1, 0x30))
        self.w['Y2'] = ParamVSpin('Y2', 0, range=(0x1, 0x30))
        self.w['攻方武器'] = ParamVSpin('攻方武器', 0, 'X', range=(-0xF, 0xF))
        self.w['守方武器'] = ParamVSpin('守方武器', 0, 'X', range=(-0xF, 0xF))
        self.w['攻方命中'] = ParamVSpin('攻方命中', 0, range=(-1, 100))
        self.w['守方命中'] = ParamVSpin('守方命中', 0, range=(-1, 100))
        self.w['攻方伤害'] = ParamVSpin('攻方伤害', 0, range=(-1, 200))
        self.w['守方伤害'] = ParamVSpin('守方伤害', 0, range=(-1, 200))
        self.w['特未'] = ParamVSpin('未知参数', 0, '04X', range=(0x0, 0x7FFF))
        self.w['无效参数'] = ParamVSpin('无效参数', 0)
        self.w['声音代码'] = ParamVSpin('声音代码', 0, '04X', range=(0x0, 0x7FFF))
        self.w['等级'] = ParamVSpin('等级', 1, range=(0x0, 0x63))
        self.w['改造'] = ParamVSpin('改造', 0, range=(0x0, 0xA))

        self.settings: dict[int, tuple[str, list[ParamWidget], str, str]] = {
            0x00: ('BLOCK<{0}>',
                   [ParamVSpin('区块序号', 0, 'X', range=(0x0, 0xA))],
                   '[00]流程控制 - BLOCK区块号'),
            0x01: ('STOP',
                   [],
                   '[01]流程控制 - BLOCK区块结束符'),
            0x02: ('ALL ({0})',
                   [self.w['套嵌层级']],
                   '[02]流程控制 - 检查全部表达式是否为真'),
            0x03: ('ANY ({0})',
                   [self.w['套嵌层级']],
                   '[03]流程控制 - 检查任一表达式是否为真'),
            0x04: ('THEN ({0})',
                   [self.w['套嵌层级']],
                   '[04]流程控制 - 检查结果为真时执行'),
            0x05: ('ELSE ({0})',
                   [self.w['套嵌层级']],
                   '[05]流程控制 - 检查结果为假时执行'),
            0x06: ('END ({0})',
                   [self.w['套嵌层级']],
                   '[06]流程控制 - 结束判断符'),
            0x08: ('GOTO {0}',
                   [self.w['目标偏移']],
                   '[08]流程控制 - 跳转定位'),
            0x09: ('RUN {0}',
                   [self.w['目标偏移']],
                   '[09]流程控制 - 执行定位'),
            0x0A: ('BACK',
                   [],
                   '[0A]流程控制 - 回调符号'),
            0x0B: ('載入地圖設計[{0}] 敵方設計[{0}] AI設計[{0}]',
                   [ParamVSpin('地图设计', 0, '02X', range=(0x0, 0x8B)),
                    ParamVSpin('敌方设计', 0, '02X', range=(0x0, 0x8B)),
                    ParamVSpin('AI设计', 0, '02X', range=(0x0, 0x8B))],
                   '[0B]流程控制 - 载入场景相关信息'),
            0x0C: ('触發全局事件{0}',
                   [self.w['事件']],
                   '[0C]事件控制 - 触发全局事件'),
            0x0D: ('触發場景事件[{0}]',
                   [self.w['场景事件']],
                   '[0D]事件控制 - 触发场景事件'),
            0x0E: ('場景点数[{0}]{1}',
                   [self.w['场景点数'], ParamVSpin('数值操作', 0, '+d')],
                   '[0E]事件控制 - 场景点数'),
            0x0F: ('全局点数{0}{1}',
                   [self.w['点数'], ParamVSpin('数值操作', 0, '+d')],
                   '[0F]事件控制 - 全局点数'),
            0x10: ('全局事件{0}為{1}状態',
                   [self.w['事件'], self.w['触发']],
                   '[10]事件控制 - 判断全局事件触发情况'),
            0x11: ('場景事件[{0}]為{1}状態',
                   [self.w['场景事件'], self.w['触发']],
                   '[11]事件控制 - 判断场景事件触发情况'),
            0x12: ('場景点数[{0}]{1}{2}',
                   [self.w['场景点数'], self.w['比较'], ParamVSpin('点数', 0)],
                   '[12]事件控制 - 比较场景点数数值情况'),
            0x13: ('全局点数{0}{1}{2}',
                   [self.w['点数'], self.w['比较'], ParamVSpin('点数', 0)],
                   '[13]事件控制 - 比较全局点数'),
            0x14: ('路綫為真實系',
                   [],
                   '[14]事件控制 - 路线为真实系'),
            0x15: ('路綫為超級系',
                   [],
                   '[15]事件控制 - 路线为超级系'),
            0x16: ('返回假',
                   [],
                   '[16]事件控制 - 必定返回假'),
            0x17: ('{0} 表情{1} \n{2}',
                   [self.w['机师'], self.w['表情'], self.w['文本']],
                   '[17]文本语音 - 机师普通文本会话'),
            0x18: ('{0} 表情{1} \n{2}',
                   [self.w['机师'], self.w['表情'], self.w['文本']],
                   '[18]文本语音 - 变量普通文本会话'),
            0x19: ('{1} 表情{2} 語音[{0}] \n{3}',
                   [self.w['声音代码'], self.w['机师'], self.w['表情'], self.w['文本']],
                   '[19]文本语音 - 机师普通语音会话'),
            0x1A: ('最終話不同主角對戰BOSS',
                   [self.w['特未'], self.w['特未'], self.w['特未'], self.w['特未'],
                    self.w['特未'], self.w['特未'], self.w['特未'], self.w['特未']],
                   '[1A]文本语音 - 主角特殊文本'),
            0x1B: ('{0} 表情{1} \n{2}',
                   [self.w['机师'], self.w['表情'], self.w['文本']],
                   '[1B]文本语音 - 变量普通语音会话'),
            0x1C: ('{0} 表情{1} 音樂「{3}」 \n{2}',
                   [self.w['机师'], self.w['表情'], self.w['文本'], self.w['音乐']],
                   '[1C]文本语音 - 机师播放音乐会话'),
            0x1D: ('{0} 表情{1} 停止音樂 \n{2}',
                   [self.w['机师'], self.w['表情'], self.w['文本']],
                   '[1D]文本语音 - 机师停止音乐会话'),
            0x1E: ('勝利条件：\n{1} \n失敗条件：\n{3}',
                   [self.w['无效参数'], self.w['文本'], self.w['无效参数'], self.w['文本']],
                   '[1E]文本语音 - 显示胜利与失败文本'),
            0x1F: ('{0}選擇：\n{2}',
                   [self.w['机师'], self.w['无效参数'], self.w['文本']],
                   '[1F]文本语音 - 选项会话文本'),
            0x21: ('選擇了第一行',
                   [self.w['无效参数']],
                   '[21]文本语音 - 选项判断'),
            0x22: ('場景勝利',
                   [ParamVSpin('未知参数', 0, range=(0x0, 0x1))],
                   '[22]场景控制 - 场景胜利'),
            0x23: ('場景失敗',
                   [],
                   '[23]场景控制 - 场景失败'),
            0x24: ('下一關為{0}',
                   [self.w['关卡']],
                   '[24]场景控制 - 选择下一关'),
            0x25: ('当前回合{1}{0}',
                   [ParamVSpin('当前回合', 0, range=(0x1, 0x7F)), self.w['比较']],
                   '[25]场景控制 - 判断当前回合数'),
            0x26: ('本方回合音樂為「{0}」 \n敵方回合音樂為「{1}」',
                   [self.w['音乐'], self.w['音乐'], self.w['无效参数']],
                   '[26]场景控制 - 设定场景音乐'),
            0x27: ('播放音樂「{0}」',
                   [self.w['音乐']],
                   '[27]场景控制 - 播放音乐'),
            0x28: ('音樂復位',
                   [],
                   '[28]场景控制 - 音乐复位'),
            0x29: ('播放声音「{0}」',
                   [self.w['声音代码']],
                   '[29]场景控制 - 播放声音'),
            0x2A: ('播放動画「{0}」',
                   [self.w['动画']],
                   '[2A]场景控制 - 播放动画'),
            0x2B: ('静止等待{0}秒',
                   [ParamVSpin('未知参数', 3, range=(0x0, 0x5))],
                   '[2B]场景控制 - 静止等待'),
            0x2C: ('敵方設計第{0}組以第[{1}]勢力出擊設為{2}陣營到地圖絕對坐標',
                   [self.w['敌方组号'], self.w['势力'], self.w['阵营']],
                   '[2C]敌方出击 - 出击到绝对坐标'),
            0x2D: ('敵方設計第{0}組以第[{1}]勢力出擊設為{2}陣營到{3}的相對坐標',
                   [self.w['敌方组号'], self.w['势力'], self.w['阵营'], self.w['机师']],
                   '[2D]敌方出击 - 出击到相对坐标'),
            0x2F: ('敵方設計第{0}組以第[{1}]勢力復活設爲{2}陣營',
                   [self.w['敌方组号'], self.w['势力'], self.w['阵营']],
                   '[2F]敌方出击 - 复活出击'),
            0x30: ('格納庫开启',
                   [],
                   '[30]机库操作 - 机库开启'),
            0x31: ('格納庫關閉',
                   [],
                   '[31]机库操作 - 机库关闭'),
            0x32: ('{0}入庫 机体{1}改',
                   [self.w['机体'], self.w['改造']],
                   '[32]机库操作 - 增加机体'),
            0x33: ('{0}分流',
                   [self.w['机体']],
                   '[33]机库操作 - 机体分流'),
            0x34: ('{0}合流',
                   [self.w['机体']],
                   '[34]机库操作 - 机体合流'),
            0x35: ('{0}离隊',
                   [self.w['机体']],
                   '[35]机库操作 - 机体离队'),
            0x36: ('{0}換成{1}',
                   [self.w['机体'], self.w['机体']],
                   '[36]机库操作 - 机体替换'),
            0x37: ('{0}加入 机師{1}級',
                   [self.w['机师'], self.w['等级']],
                   '[37]机库操作 - 加入机师'),
            0x38: ('{0}分流',
                   [self.w['机师']],
                   '[38]机库操作 - 机师分流'),
            0x39: ('{0}合流',
                   [self.w['机师']],
                   '[39]机库操作 - 机师合流'),
            0x3A: ('{0}离隊',
                   [self.w['机师']],
                   '[3A]机库操作 - 机师离队'),
            0x3B: ('{0}換成{1}',
                   [self.w['机师'], self.w['机师']],
                   '[3B]机库操作 - 机师替换'),
            0x3C: ('出發操作相關未知指令',
                   [ParamVSpin('未知参数', 0, range=(0x0, 0x2))],
                   '[3C]出击操作 - 未知'),
            0x3D: ('加入或强制換乘 \n{0} 机師{1}級 \n{2} 机体{3}改',
                   [self.w['机师'], self.w['等级'], self.w['机体'], self.w['改造']],
                   '[3D]机库操作 - 机师机体同时加入或强制换乘'),
            0x3E: ('{0}与搭乘机体分流',
                   [self.w['机师']],
                   '[3E]机库操作 - 机师与搭乘机体分流'),
            0x3F: ('{0}与搭乘机師分流',
                   [self.w['机体']],
                   '[3F]机库操作 - 机体与搭乘机师分流'),
            0x40: ('{0}与搭乘机体合流',
                   [self.w['机师']],
                   '[40]机库操作 - 机师与搭乘机体合流'),
            0x41: ('{0}与搭乘机師合流',
                   [self.w['机体']],
                   '[41]机库操作 - 机体与搭乘机师合流'),
            0x42: ('{0}与搭乘机体离隊',
                   [self.w['机师']],
                   '[42]机库操作 - 机师与搭乘机体离队'),
            0x43: ('{0}强制搭乘{1}',
                   [self.w['机师'], self.w['机体']],
                   '[43]机库操作 - 强制换乘'),
            0x44: ('{0}强制搭乘[07D]V2ガンダム',
                   [self.w['机师']],
                   '[44]机库操作 - 强制换乘V2ガンダム'),
            0x45: ('{0}强制取消搭乘',
                   [self.w['机师']],
                   '[45]机库操作 - 机师强制取消搭乘'),
            0x46: ('{0}强制取消搭乘',
                   [self.w['机体']],
                   '[46]机库操作 - 机体强制取消搭乘'),
            0x47: ('{0}强制出場',
                   [self.w['机师']],
                   '[47]机库操作 - 机师强制出场'),
            0x48: ('妖精{0}附加給{1}',
                   [self.w['机师'], self.w['机师']],
                   '[48]机库操作 - 妖精配属'),
            0x49: ('{0}从出擊名單中隱藏',
                   [self.w['机师']],
                   '[49]机库操作 - 机师隐藏'),
            0x4A: ('{0}从出擊名單中隱藏',
                   [self.w['机体']],
                   '[4A]机库操作 - 机体隐藏'),
            0x4B: ('{0}强制搭乘空机体',
                   [self.w['机师']],
                   '[4B]机库操作 - 机师强制搭乘空机体'),
            0x4E: ('{0}以分离状態出擊',
                   [self.w['机体']],
                   '[4E]机库操作 - 合体机以分离状态出击'),
            0x4F: ('开始出擊',
                   [],
                   '[4F]出击操作 - 开始出击'),
            0x50: ('出擊完畢',
                   [],
                   '[50]出击操作 - 出击完毕'),
            0x51: ('{0}出擊到地圖絕對坐標 X{1} Y{2}',
                   [self.w['机师'], self.w['X绝对坐标'], self.w['Y绝对坐标']],
                   '[51]出击操作 - 机师出击到绝对坐标'),
            0x52: ('{0}出擊到{3}相對坐標 X{1} Y{2}',
                   [self.w['机师'], self.w['X相对坐标'], self.w['Y相对坐标'], self.w['机师']],
                   '[52]出击操作 - 机师出击到相对坐标'),
            0x54: ('{0}出擊到地圖絕對坐標 X{1} Y{2}',
                   [self.w['机体'], self.w['X绝对坐标'], self.w['Y绝对坐标']],
                   '[54]出击操作 - 机体出击到绝对坐标'),
            0x55: ('{0}出擊到{3}相對坐標 X{1} Y{2}',
                   [self.w['机体'], self.w['X相对坐标'], self.w['Y相对坐标'], self.w['机师']],
                   '[55]出击操作 - 机体出击到相对坐标'),
            0x57: ('選擇{0}台机体出擊到地圖絕對坐標配置[{1}]',
                   [ParamVSpin('数量', 0, range=(0x0, 0x14)), self.w['坐标配置']],
                   '[57]出击操作 - 选择机体出击到绝对坐标配置'),
            0x58: ('選擇{0}台机体出擊到{2}相對坐標配置[{1}]',
                   [ParamVSpin('数量', 0, range=(0x0, 0x14)), self.w['坐标配置'], self.w['机师']],
                   '[58]出击操作 - 选择机体出击到相对坐标配置'),
            0x5A: ('選擇母艦出擊到地圖絕對坐標 X{1} Y{2}',
                   [ParamVSpin('无效参数', 1), self.w['X绝对坐标'], self.w['Y绝对坐标']],
                   '[5A]出击操作 - 选择母舰出击到绝对坐标'),
            0x5B: ('設定{0}等級為{2}{1}',
                   [self.w['机师'], ParamVSpin('设定等级', 1, '+d', range=(0x1, 0x63)), self.w['机师']],
                   '[5B]机库操作 - 设定机师等级'),
            0x5C: ('{0}等級{1}',
                   [self.w['机师'], ParamVSpin('等级变化', 0, '+d', range=(-0x62, 0x62))],
                   '[5C]机库操作 - 调整机师等级'),
            0x5D: ('設定{0}擊墜数為{1}',
                   [self.w['机师'], ParamVSpin('设定击坠', 0, range=(0, 0x7FF))],
                   '[5D]机库操作 - 设定机师击坠数'),
            0x5E: ('{0}擊墜数{1}',
                   [self.w['机师'], ParamVSpin('击坠变化', 0, '+d', range=(-0x7FF, 0x7FF))],
                   '[5E]机库操作 - 调整机师击坠数'),
            0x5F: ('{0}加入本方',
                   [self.w['机师']],
                   '[5F]场景控制 - 机师加入本方'),
            0x60: ('{0}轉爲第[{1}]勢力',
                   [self.w['机师'], self.w['势力']],
                   '[60]场景控制 - 机师势力转换'),
            0x61: ('增加芯片 {0}',
                   [self.w['芯片']],
                   '[61]资源操作 - 增加芯片'),
            0x62: ('增加{0}換装 {1}組件',
                   [ParamRCombo('选择本体', 0, {0: 'V2ガンダム', 1: 'ヒュッケバインMK-Ⅲ'}),
                    ParamRCombo('换装组件', 0, {0: '组件1', 1: '组件2'})],
                   '[62]资源操作 - 增加换装系统组件'),
            0x63: ('[07D]V2ガンダム換装為{0}',
                   [self.w['机体']],
                   '[63]资源操作 - 指定V2ガンダム换装'),
            0x64: ('增加資金 {0}',
                   [ParamVSpin('资金金额', 0, range=(0, 100000000))],
                   '[64]资源操作 - 增加资金'),
            0x65: ('{0}復活',
                   [self.w['机师']],
                   '[65]场景操作 - 复活机师'),
            0x66: ('{0}復活',
                   [self.w['机体']],
                   '[66]场景操作 - 复活机体'),
            0x67: ('移動{0}到地圖絕對坐標 X{1} Y{2}',
                   [self.w['机师'], self.w['X绝对坐标'], self.w['Y绝对坐标']],
                   '[67]光标操作 - 移动机师对话光标到绝对坐标'),
            0x68: ('移動{0}到{1}相對坐標 X{2} Y{3}',
                   [self.w['机师'], self.w['机师'], self.w['X相对坐标'], self.w['Y相对坐标']],
                   '[68]光标操作 - 移动机师对话光标到相对坐标'),
            0x69: ('移動{0}到敵方序号[{1}]相對坐標 X{2} Y{3}',
                   [self.w['机师'], self.w['敌方序号'], self.w['X相对坐标'], self.w['Y相对坐标']],
                   '[69]光标操作 - 移动机师对话光标到敌方相对坐标'),
            0x6A: ('移動光標到地圖絕對坐標 X{0} Y{1}',
                   [self.w['X绝对坐标'], self.w['Y绝对坐标']],
                   '[6A]光标操作 - 移动光标焦点到绝对坐标'),
            0x6B: ('移動光標到{0}相對坐標 X{1} Y{2}',
                   [self.w['机师'], self.w['X相对坐标'], self.w['Y相对坐标']],
                   '[6B]光标操作 - 移动光标焦点到相对坐标'),
            0x6C: ('移動光標到地圖絕對坐標 X{0} Y{1} 并停留{2}單位時間',
                   [self.w['X绝对坐标'], self.w['Y绝对坐标'], ParamVSpin('停留时间', 0, range=(0, 0x7FFF))],
                   '[6C]光标操作 - 移动光标焦点到绝对坐标并停留'),
            0x6E: ('屏幕静止{0}',
                   [ParamVSpin('停留时间', 0, range=(0, 0x7FFF))],
                   '[6E]光标操作 - 屏幕静止'),
            0x6F: ('{0}撤退',
                   [self.w['机师']],
                   '[6F]场景控制 - 机师撤退'),
            0x70: ('敵方序号[{0}]撤退',
                   [self.w['敌方序号']],
                   '[70]场景控制 - 敌方撤退'),
            0x71: ('敵方第{0}組全部撤退',
                   [self.w['敌方组号']],
                   '[71]场景控制 - 敌方小组撤退'),
            0x72: ('第[{0}]勢力全部撤退',
                   [self.w['势力']],
                   '[72]场景控制 - 势力撤退'),
            0x73: ('{0}陣營撤退',
                   [self.w['阵营']],
                   '[73]场景控制 - 阵营撤退'),
            0x74: ('{0}陣營撤退到 X{1}-X{3} Y{2}-Y{4}区域内',
                   [self.w['阵营'], self.w['X1'], self.w['Y1'], self.w['X2'], self.w['Y2']],
                   '[74]场景控制 - 阵营撤退到区域'),
            0x75: ('{0}{1}',
                   [self.w['机师'], self.w['状态']],
                   '[75]条件判断 - 判断机师状态'),
            0x77: ('{0}{1}',
                   [self.w['机体'], self.w['状态']],
                   '[77]条件判断 - 判断机体状态'),
            0x78: ('{0}處于搭載中',
                   [self.w['机师']],
                   '[78]条件判断 - 判断机师搭载状态'),
            0x79: ('敵方第{0}組数量{1}{2}台',
                   [self.w['敌方组号'], self.w['比较'], ParamVSpin('数量', 0, range=(0, 0xA0))],
                   '[79]条件判断 - 判断敌方小组数量'),
            0x7A: ('第[{0}]勢力数量{1}{2}台',
                   [self.w['势力'], self.w['比较'], ParamVSpin('数量', 0, range=(0, 0xA0))],
                   '[7A]条件判断 - 判断势力数量'),
            0x7B: ('{0}陣營数量{1}{2}台',
                   [self.w['阵营'], self.w['比较'], ParamVSpin('数量', 0, range=(0, 0xA0))],
                   '[7B]条件判断 - 判断阵营数量'),
            0x7C: ('{0}進入 X{1}-X{3} Y{2}-Y{4}区域内',
                   [self.w['机师'], self.w['X1'], self.w['Y1'], self.w['X2'], self.w['Y2']],
                   '[7C]条件判断 - 判断机师位置'),
            0x7D: ('敵方序号[{0}]進入 X{1}-X{3} Y{2}-Y{4}区域内',
                   [self.w['敌方序号'], self.w['X1'], self.w['Y1'], self.w['X2'], self.w['Y2']],
                   '[7D]条件判断 - 判断敌方位置'),
            0x7E: ('{0}進 X{1}-X{3} Y{2}-Y{4}区域内',
                   [self.w['机体'], self.w['X1'], self.w['Y1'], self.w['X2'], self.w['Y2']],
                   '[7E]条件判断 - 判断机体位置'),
            0x80: ('第[{0}]勢力進入 X{1}-X{3} Y{2}-Y{4}区域内',
                   [self.w['势力'], self.w['X1'], self.w['Y1'], self.w['X2'], self.w['Y2']],
                   '[80]条件判断 - 判断势力位置'),
            0x81: ('{0}陣營進入 X{1}-X{3} Y{2}-Y{4}区域内',
                   [self.w['阵营'], self.w['X1'], self.w['Y1'], self.w['X2'], self.w['Y2']],
                   '[81]条件判断 - 判断阵营位置'),
            0x82: ('{0}与{1}相距{2}格',
                   [self.w['机师'], self.w['机师'], ParamVSpin('距离', 1, range=(0x1, 0x7F))],
                   '[82]条件判断 - 判断机师间距离'),
            0x83: ('{0}与敵方序号[{1}]相距{2}格',
                   [self.w['机师'], self.w['敌方序号'], ParamVSpin('距离', 1, range=(0x1, 0x7F))],
                   '[83]条件判断 - 判断机师与敌方列表单位距离'),
            0x84: ('{0}气力調整為{1}',
                   [self.w['机师'], ParamVSpin('气力', 100, range=(50, 150))],
                   '[84]场景操作 - 调整机师气力'),
            0x85: ('{0}陣營气力調整為{1}',
                   [self.w['阵营'], ParamVSpin('气力', 100, range=(50, 150))],
                   '[85]场景操作 - 调整阵营气力'),
            0x86: ('{0}EN减少{1}',
                   [self.w['机师'], ParamVSpin('EN减少', 100)],
                   '[86]场景操作 - 减少机师EN'),
            0x87: ('場景操作相關未知指令',
                   [],
                   '[87]场景操作 - 未知'),
            0x88: ('{0}HP調整{1}%',
                   [self.w['机师'], ParamVSpin('HP变化', 100, range=(1, 100))],
                   '[88]场景操作 - 调整机师HP'),
            0x89: ('{0}陣營HP調整{1}%',
                   [self.w['阵营'], ParamVSpin('HP变化', 100, range=(1, 100))],
                   '[89]场景操作 - 调整阵营HP'),
            0x8B: ('{0}陣營SP調整{1}%',
                   [self.w['阵营'], ParamVSpin('SP变化', 100, range=(1, 100))],
                   '[8B]场景操作 - 调整阵营SP'),
            0x8C: ('{0}電纜連接到地圖絕對坐標 X{1} Y{2}',
                   [self.w['机师'], self.w['X绝对坐标'], self.w['Y绝对坐标']],
                   '[8C]场景操作 - EVA电缆连接到绝对坐标'),
            0x8D: ('{0}電纜連接到{1}',
                   [self.w['机师'], self.w['机师']],
                   '[8D]场景操作 - EVA电缆连接到母舰'),
            0x8E: ('{0}電纜就近連接',
                   [self.w['机师']],
                   '[8E]场景操作 - EVA电缆就近连接'),
            0x8F: ('{0}電纜强制断开',
                   [self.w['机师']],
                   '[8F]场景操作 - EVA电缆强制断开'),
            0x90: ('{0}移動到地圖絕對坐標 X{1} Y{2}',
                   [self.w['机师'], self.w['X绝对坐标'], self.w['Y绝对坐标']],
                   '[90]场景操作 - 移动机师到绝对坐标'),
            0x91: ('敵方序号[{0}]移動到地圖絕對坐標 X{1} Y{2}',
                   [self.w['敌方序号'], self.w['X绝对坐标'], self.w['Y绝对坐标']],
                   '[91]场景操作 - 移动敌方列表单位到绝对坐标'),
            0x92: ('{0}移動到{1}相對坐標 X{2} Y{3} {4}',
                   [self.w['机师'], self.w['机师'], self.w['X相对坐标'], self.w['Y相对坐标'], self.w['移动']],
                   '[92]场景操作 - 移动机师到相对坐标'),
            0x93: ('{0}移動到敵方序号[{1}]相對坐標 X{2} Y{3} {4}',
                   [self.w['机师'], self.w['敌方序号'], self.w['X相对坐标'], self.w['Y相对坐标'], self.w['移动']],
                   '[93]场景操作 - 移动机师到敌方单位相对坐标'),
            0x94: ('敵方序号[{0}]移動到{1}相對坐標 X{2} Y{3} {4}',
                   [self.w['敌方序号'], self.w['机师'], self.w['X相对坐标'], self.w['Y相对坐标'], self.w['移动']],
                   '[94]场景操作 - 移动敌方单位到相对坐标'),
            0x96: ('戰斗：{0} 攻擊 {1} \n攻方：武器編号[{2}] 命中{4}% 傷害{6}% {8} \n守方：武器編号[{3}] 命中{5}% 傷害{7}% {9}',
                   [self.w['机师'], self.w['机师'],
                    self.w['攻方武器'], self.w['守方武器'],
                    self.w['攻方命中'], self.w['守方命中'],
                    self.w['攻方伤害'], self.w['守方伤害'],
                    self.w['演出'], self.w['演出']],
                   '[96]战斗演出 - 机师间强制战斗演出'),
            0x97: ('戰斗：敵方序号[{0}] 攻擊 {1} \n攻方：武器編号[{2}] 命中{4}% 傷害{6}% {8} \n守方：武器編号[{3}] 命中{5}% 傷害{7}% {9}',
                   [self.w['敌方序号'], self.w['机师'],
                    self.w['攻方武器'], self.w['守方武器'],
                    self.w['攻方命中'], self.w['守方命中'],
                    self.w['攻方伤害'], self.w['守方伤害'],
                    self.w['演出'], self.w['演出']],
                   '[97]战斗演出 - 敌方列表单位攻击机师强制战斗演出'),
            0x98: ('戰斗：{0} 攻擊 敵方序号[{1}] \n攻方：武器編号[{2}] 命中{4}% 傷害{6}% {8} \n守方：武器編号[{3}] 命中{5}% 傷害{7}% {9}',
                   [self.w['机师'], self.w['敌方序号'],
                    self.w['攻方武器'], self.w['守方武器'],
                    self.w['攻方命中'], self.w['守方命中'],
                    self.w['攻方伤害'], self.w['守方伤害'],
                    self.w['演出'], self.w['演出']],
                   '[98]战斗演出 - 机师攻击敌方列表单位强制战斗演出'),
            0x99: ('戰斗關閉',
                   [],
                   '[99]战斗演出 - 关闭战斗演出'),
            0x9A: ('允許第[{0}]勢力攻擊第[{1}]勢力',
                   [self.w['势力'], self.w['势力']],
                   '[9A]规则设置 - 势力攻击许可'),
            0x9B: ('禁止第[{0}]勢力攻擊第[{1}]勢力',
                   [self.w['势力'], self.w['势力']],
                   '[9B]规则设置 - 势力攻击禁止'),
            0x9C: ('禁用{0}的{1}菜單選項',
                   [self.w['机师'], self.w['选项']],
                   '[9C]规则设置 - 禁用机师菜单选项'),
            0x9D: ('禁用敵方序号[{0}]的{1}菜單選項',
                   [self.w['敌方序号'], self.w['选项']],
                   '[9D]规则设置 - 禁用敌方菜单选项'),
            0x9E: ('启用{0}的{1}菜單選項',
                   [self.w['机师'], self.w['选项']],
                   '[9E]规则设置 - 启用机师菜单选项'),
            0x9F: ('{0}强制擊破',
                   [self.w['机师']],
                   '[9F]场景操作 - 强制击破机师'),
            0xA0: ('敵方序号[{0}]强制擊破',
                   [self.w['敌方序号']],
                   '[A0]场景操作 - 强制击破敌方'),
            0xA1: ('{0}强制搭載',
                   [self.w['机师']],
                   '[A1]场景操作 - 机师强制搭载'),
            0xA2: ('{0}取消搭載',
                   [self.w['机师']],
                   '[A2]场景操作 - 机师取消搭载'),
            0xA3: ('{0}强制浮上',
                   [self.w['机师']],
                   '[A3]场景操作 - 机师强制浮上'),
            0xA4: ('{0}强制着地',
                   [self.w['机师']],
                   '[A4]场景操作 - 机师强制着地'),
            0xA5: ('{0}搭乘机体强制變形為{1}',
                   [self.w['机师'], self.w['机体']],
                   '[A5]场景操作 - 强制变形'),
            0xA6: ('{0}搭乘机体强制合体',
                   [self.w['机师']],
                   '[A6]场景操作 - 强制合体'),
            0xA7: ('{0}搭乘机体强制分离',
                   [self.w['机师']],
                   '[A7]场景操作 - 强制分离'),
            0xA8: ('{0}强制使用精神{1} {2}次',
                   [self.w['机师'], self.w['精神'], ParamVSpin('次数', 1, range=(1, 9)),
                    ParamRCombo('未知参数', 0, {0: '未知选项', 1: '未知选项'})],
                   '[A8]场景操作 - 强制使用精神'),
            0xA9: ('{0}强制設爲{1}',
                   [self.w['机师'], self.w['行动']],
                   '[A9]场景操作 - 强制设定行动状态'),
            0xAA: ('{0}强制切換傀儡系統',
                   [self.w['机师']],
                   '[AA]场景操作 - 强制切换傀儡系统'),
            0xAB: ('{0}可以說得{1}',
                   [self.w['机师'], self.w['机师']],
                   '[AB]说得选项 - 增加机师说得机师选项'),
            0xAC: ('{0}可以說得敵方序号[{1}]',
                   [self.w['机师'], self.w['敌方序号']],
                   '[AC]说得选项 - 增加机师说得敌方选项'),
            0xAD: ('{0}已經說得{1}',
                   [self.w['机师'], self.w['机师']],
                   '[AD]条件判断 - 判断机师间说得状态'),
            0xAE: ('{0}已經說得敵方序号[{1}]',
                   [self.w['机师'], self.w['敌方序号']],
                   '[AE]条件判断 - 判断机师与敌方列表单位说得状态'),
            0xAF: ('{0}与{1}交手',
                   [self.w['机师'], self.w['机师']],
                   '[AF]条件判断 - 判断机师间交手'),
            0xB0: ('{0}与敵方序号[{1}]交手',
                   [self.w['机师'], self.w['敌方序号']],
                   '[B0]条件判断 - 判断机师与敌方交手'),
            0xB1: ('{0}發起攻擊',
                   [self.w['机师']],
                   '[B1]条件判断 - 判断机师交手'),
            0xB2: ('敵方序号[{0}]被擊破',
                   [self.w['敌方序号']],
                   '[B2]条件判断 - 判断敌方被击破'),
            0xB3: ('{0}被擊破',
                   [self.w['机师']],
                   '[B3]条件判断 - 判断机师被击破[BLOCK7]'),
            0xB4: ('{0}被擊破',
                   [self.w['机体']],
                   '[B4]条件判断 - 判断机体被击破'),
            0xB5: ('本方被擊破{0}机',
                   [ParamVSpin('击破数量', 1, range=(0, 30))],
                   '[B5]条件判断 - 判断本方被击破数'),
            0xB6: ('{0}HP少于{1}%',
                   [self.w['机师'], ParamVSpin('HP', 1, range=(1, 100))],
                   '[B6]条件判断 - 判断机师HP量'),
            0xB7: ('{0}被擊破',
                   [self.w['机师']],
                   '[B7]条件判断 - 判断机师被击破[BLOCK8]'),
            0xB8: ('敵方序号[{0}]未被擊破',
                   [self.w['敌方序号']],
                   '[B8]条件判断 - 判断敌方未被击破'),
            0xB9: ('{1}以{3}進行特殊地圖演出 演出代碼[{2}] 子鏡頭数量：{0} \n子鏡頭碼[{}] 方向{} X坐標{} Y坐標{} ',
                   [ParamVSpin('子镜头数', 1, range=(1, 5)), self.w['机师'], self.w['演出代码'],
                    ParamRCombo('坐标定位', 0, {0: '絕對坐標', 1: '相對坐標'}),
                    ParamVSpin('子镜头', 0, range=(0x0, 0x7F)), ParamRCombo('方向', 1, {1: '↖', 4: '↘', 5: ''}),
                    self.w['X相对坐标'], self.w['Y相对坐标']],
                   '[B9]地图演出 - 相对坐标特殊地图演出'),
            0xBA: ('地圖演出[{0}] 地圖絕對坐標 X{1} Y{2}',
                   [self.w['演出代码'], self.w['X绝对坐标'], self.w['Y绝对坐标']],
                   '[BA]地图演出 - 绝对坐标地图演出'),
            0xBB: ('地圖演出[{0}] {1}相對坐標 X{2} Y{3}',
                   [self.w['演出代码'], self.w['机师'], self.w['X相对坐标'], self.w['Y相对坐标']],
                   '[BB]地图演出 - 相对坐标地图演出'),
        }

    def explain(self, command: dict[str, int | list[int] | str]) -> str:
        code = command.get('Code')
        param = command.get('Param')
        param_setting: tuple[str, list[ParamWidget], str, str] = self.settings.get(code, (str(code), tuple()))
        param_text, param_widgets, *_ = param_setting
        if code == 0x62:
            param_widgets[1].init_mapping(EnumData.COMMAND['换装'][param[0]])

        explain_list = list()
        for param_idx, param_data in enumerate(param):
            if code != 0xB9 or param_idx < 8:
                param_widget = param_widgets[param_idx].new()
            else:
                param_widget = param_widgets[param_idx % 4 + 4].new()
            explain_list.append(param_widget.explain(param_data))
        if code == 0xB9:
            main_text, expand_text = param_text.splitlines()
            main_str = main_text.format(*explain_list[:4])
            expand_str = ' \n'.join([expand_text] * param[0]).format(*explain_list[4:])
            return main_str + ' \n' + expand_str
        return param_text.format(*explain_list)
