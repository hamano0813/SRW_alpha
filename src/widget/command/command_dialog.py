#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog

from parameter import EnumData
from widget.command import ParamVSpin, ParamRCombo, ParamCCombo
from widget.command.param_widget import ParamWidget


class CommandDialog(QDialog):
    def __init__(self, parent, command: dict = None, **kwargs):
        super(CommandDialog, self).__init__(parent, f=Qt.Dialog)
        self.command = command if command else {'Pos': 0x0, 'Code': 0x0, 'Count': 0x1, 'Param': list(), 'Data': ''}

        self.w = dict()
        self.w['机体'] = ParamRCombo('选择机体', 0x0, kwargs.get('robots'))
        self.w['机师'] = ParamRCombo('选择机师', 0x0, kwargs.get('pilots') | {-0x1: ''})
        self.w['文本'] = ParamRCombo('选择文本', 0x0, kwargs.get('messages'))

        self.w['关卡'] = ParamRCombo('选择关卡', 0, EnumData.STAGE)
        self.w['音乐'] = ParamRCombo('选择音乐', 0x0, EnumData.MUSIC)
        self.w['事件'] = ParamRCombo('选择事件', 0x0, EnumData.EVENT)
        self.w['芯片'] = ParamRCombo('选择芯片', 0x0, EnumData.PART)

        self.w['表情'] = ParamRCombo('选择表情', 0x0, EnumData.COMMAND['表情'])
        self.w['演出'] = ParamCCombo('选择演出', 0x0, EnumData.COMMAND['演出'], sep='＆')
        self.w['势力'] = ParamCCombo('势力编号', 0, EnumData.COMMAND['势力'], sep='＆')
        self.w['阵营'] = ParamRCombo('选择阵营', 0, EnumData.COMMAND['阵营'])
        self.w['比较'] = ParamRCombo('比较符号', 0x2, EnumData.COMMAND['比较'])
        self.w['触发'] = ParamRCombo('触发状态', 0x2, EnumData.COMMAND['触发'])
        self.w['点数'] = ParamRCombo('全局点数', 0x2, EnumData.COMMAND['点数'])
        self.w['状态'] = ParamRCombo('存在状态', 0x2, EnumData.COMMAND['状态'])
        self.w['行动'] = ParamRCombo('行动状态', 0x2, EnumData.COMMAND['行动'])
        self.w['移动'] = ParamRCombo('移动状态', 0x2, EnumData.COMMAND['移动'])

        self.COMMAND_SETTING = {
            0x00: ('BLOCK<{0}>',
                   [ParamVSpin('区块序号', 0, 'X')]),
            0x01: ('STOP',
                   []),
            0x02: ('ALL ({0})',
                   [ParamVSpin('套欠层级', 0)]),
            0x03: ('ANY ({0})',
                   [ParamVSpin('套欠层级', 0)]),
            0x04: ('THEN ({0})',
                   [ParamVSpin('套欠层级', 0)]),
            0x05: ('ELSE ({0})',
                   [ParamVSpin('套欠层级', 0)]),
            0x06: ('ENDIF ({0})',
                   [ParamVSpin('套欠层级', 0)]),
            0x08: ('GOTO {0}',
                   [ParamVSpin('目标偏移', 0, '04X')]),
            0x09: ('RUN {0}',
                   [ParamVSpin('目标偏移', 0, '04X')]),
            0x0A: ('BACK',
                   []),

            0x0B: ('载入地图设计{0} 敌方设计{0} AI设计{0}',
                   [ParamVSpin('地图设计', 0, '02X'), ParamVSpin('敌方设计', 0, '02X'), ParamVSpin('AI设计', 0, '02X')]),

            0x0C: ('触发全局事件{0}',
                   [self.w['事件']]),
            0x0D: ('触发场景事件[{0}]',
                   [ParamVSpin('场景事件', 0, '02X')]),
            0x0E: ('场景点数[{0}]{1}',
                   [ParamVSpin('场景点数', 0, '04X'), ParamVSpin('数值操作', 0, '+d')]),
            0x0F: ('全局点数{0}{1}',
                   [self.w['点数'], ParamVSpin('数值操作', 0, '+d')]),
            0x10: ('全局事件{0}为{1}状态',
                   [self.w['事件'], self.w['触发']]),
            0x11: ('场景事件[{0}]为{1}状态',
                   [ParamVSpin('场景事件', 0, '02X'), self.w['触发']]),
            0x12: ('场景点数[{0}]{1}{2}',
                   [self.w['点数'], self.w['比较'], ParamVSpin('点数', 0)]),
            0x13: ('全局点数{0}{1}{2}',
                   [self.w['点数'], self.w['比较'], ParamVSpin('点数', 0)]),

            0x14: ('路线为真实系',
                   []),
            0x15: ('路线为超级系',
                   []),
            0x16: ('返回假',
                   []),

            0x17: ('{0} 表情{2}\n{3}',
                   [self.w['机师'], ParamVSpin('无效', 0), self.w['表情'], self.w['文本']]),
            0x18: ('{0} 表情{2}\n{3}',
                   [self.w['机师'], ParamVSpin('无效', 0), self.w['表情'], self.w['文本']]),
            0x19: ('{1} 表情{3} 语音[{0}]\n{4}',
                   [ParamVSpin('语音', 0, '04X'),
                    self.w['机师'],
                    ParamVSpin('无效', 0),
                    self.w['表情'],
                    self.w['文本']]),
            0x1A: ('最终话不同主角对战BOSS',
                   [ParamVSpin('未知', 0, '04X'),
                    ParamVSpin('未知', 0, '04X'),
                    ParamVSpin('未知', 0, '04X'),
                    ParamVSpin('未知', 0, '04X'),
                    ParamVSpin('未知', 0, '04X'),
                    ParamVSpin('未知', 0, '04X'),
                    ParamVSpin('未知', 0, '04X'),
                    ParamVSpin('未知', 0, '04X')]),
            0x1B: ('{0} 表情{2}\n{3}',
                   [self.w['机师'], ParamVSpin('无效', 0), self.w['表情'], self.w['文本']]),
            0x1C: ('{0} 表情{2} 音乐《{4}》\n{3}',
                   [self.w['机师'],
                    ParamVSpin('无效', 0),
                    self.w['表情'],
                    self.w['文本'],
                    self.w['音乐']]),
            0x1D: ('{0} 表情{2} 停止音乐\n{3}',
                   [self.w['机师'], ParamVSpin('无效', 0), self.w['表情'], self.w['文本']]),
            0x1E: ('胜利条件：\n{1}\n失败条件：\n{3}',
                   [ParamVSpin('无效', 0), self.w['文本'], ParamVSpin('无效', 0), self.w['文本']]),

            0x1F: ('{0}选择 - {2}',
                   [self.w['机师'], ParamVSpin('无效', 0), self.w['文本']]),
            0x21: ('选择了第一项',
                   [ParamVSpin('无效', 0)]),

            0x22: ('场景胜利',  # TODO
                   [ParamVSpin('？未知', 0)]),
            0x23: ('场景失败',
                   []),
            0x24: ('下一关为{0}',
                   [self.w['关卡']]),
            0x25: ('当前回合{1}{0}',
                   [ParamVSpin('当前回合', 0), self.w['比较']]),

            0x26: ('本方回合音乐为《{0}》\n敌方回合音乐为《{1}》',
                   [self.w['音乐'], self.w['音乐'], ParamVSpin('无效', 0)]),
            0x27: ('播放音乐《{0}》',
                   [self.w['音乐']]),
            0x28: ('音乐复位',
                   []),
            0x29: ('播放声音《{0}》',
                   [ParamVSpin('音效', 0, '04X')]),
            0x2A: ('播放动画《{0}》',
                   [ParamVSpin('CG动画', 0, '04X')]),
            0x2B: ('？静止等待{0}秒',  # TODO
                   [ParamVSpin('秒数', 3)]),

            0x2C: ('敌方设计第{0}组以{1}势力出击设为{2}阵营到地图绝对坐标',
                   [ParamVSpin('敌方组号', 0), self.w['势力'], self.w['阵营']]),
            0x2D: ('敌方设计第{0}组以{1}势力出击设为{2}阵营到{3}的相对坐标',
                   [ParamVSpin('敌方组号', 0), self.w['势力'], self.w['阵营'], self.w['机师']]),
            0x2F: ('敌方设计第{0}组以{1}势力复活设为{2}阵营',
                   [ParamVSpin('敌方组号', 0), self.w['势力'], self.w['阵营']]),

            0x30: ('格纳库开启',
                   []),
            0x31: ('格纳库关闭',
                   []),

            0x32: ('{0}入库 机体{1}改 武器{2}改',
                   [self.w['机体'], ParamVSpin('机体改造', 0), ParamVSpin('武器改造', 0)]),
            0x33: ('{0}分流',
                   [self.w['机体']]),
            0x34: ('{0}合流',
                   [self.w['机体']]),
            0x35: ('{0}离队',
                   [self.w['机体']]),
            0x36: ('{0}换成{1}',
                   [self.w['机体'], self.w['机体']]),

            0x37: ('{0}加入 {1}级 击坠数{2}',
                   [self.w['机师'], ParamVSpin('等级', 1), ParamVSpin('击坠数', 0)]),
            0x38: ('{0}分流',
                   [self.w['机师']]),
            0x39: ('{0}合流',
                   [self.w['机师']]),
            0x3A: ('{0}离队',
                   [self.w['机师']]),
            0x3B: ('{0}换成{1}',
                   [self.w['机师'], self.w['机师']]),

            0x3C: ('？',  # TODO
                   [ParamVSpin('？未知', 0)]),
            0x3D: ('加入或强制换乘 {0} {1}级 击坠数{2} 搭乘{3} 机体{4}改 武器{5}改',
                   [self.w['机师'],
                    ParamVSpin('等级', 1),
                    ParamVSpin('击坠数', 0),
                    self.w['机体'],
                    ParamVSpin('机体改造', 0),
                    ParamVSpin('武器改造', 0)]),

            0x3E: ('{0}与搭乘机体分流',
                   [self.w['机师']]),
            0x3F: ('{0}与搭乘机师分流',
                   [self.w['机体']]),
            0x40: ('{0}与搭乘机体合流',
                   [self.w['机师']]),
            0x41: ('{0}与搭乘机师合流',
                   [self.w['机体']]),
            0x42: ('{0}与搭乘机体离队',
                   [self.w['机师']]),

            0x43: ('{0}强制搭乘{1}',
                   [self.w['机师'], self.w['机体']]),
            0x44: ('{0}强制搭乘[07D]V2ガンダム',
                   [self.w['机师']]),
            0x45: ('{0}强制取消搭乘',
                   [self.w['机师']]),
            0x46: ('{0}强制取消搭乘',
                   [self.w['机体']]),

            0x47: ('？{0}',  # TODO
                   [self.w['机师']]),
            0x48: ('妖精{0}附加给{1}',
                   [self.w['机师'], self.w['机师']]),
            0x49: ('{0}从出击名单中隐藏',
                   [self.w['机师']]),
            0x4A: ('{0}从出击名单中隐藏',
                   [self.w['机体']]),
            0x4B: ('{0}强制搭乘空机体',
                   [self.w['机师']]),
            0x4E: ('？{0}允许分离',  # TODO
                   [self.w['机体']]),

            0x4F: ('开始出击',
                   []),
            0x50: ('出击完毕',
                   []),

            0x51: ('{0}出击到地图绝对坐标 X{1} Y{2}',
                   [self.w['机师'], ParamVSpin('X坐标', 0), ParamVSpin('Y坐标', 0)]),
            0x52: ('{0}出击到{3}相对坐标 X{1} Y{2}',
                   [self.w['机师'], ParamVSpin('X坐标', 0, '+d'), ParamVSpin('Y坐标', 0, '+d'), self.w['机师']]),
            0x54: ('{0}出击到地图绝对坐标 X{1} Y{2}',
                   [self.w['机体'], ParamVSpin('X坐标', 0), ParamVSpin('Y坐标', 0)]),
            0x55: ('{0}出击到{3}相对坐标 X{1} Y{2}',
                   [self.w['机体'], ParamVSpin('X坐标', 0, '+d'), ParamVSpin('Y坐标', 0, '+d'), self.w['机师']]),
            0x57: ('选择{0}台机体出击到地图绝对坐标配置[{1}]',
                   [ParamVSpin('数量', 0), ParamVSpin('坐标配置', 0)]),
            0x58: ('选择{0}台机体出击到{2}相对坐标配置[{1}]',
                   [ParamVSpin('数量', 0), ParamVSpin('坐标配置', 0), self.w['机师']]),
            0x5A: ('选择母舰出击到地图绝对坐标 X{1} Y{2}',
                   [ParamVSpin('无效', 1), ParamVSpin('X坐标', 0), ParamVSpin('Y坐标', 0)]),

            0x5B: ('调整{0}等级为{2}{1}',
                   [self.w['机师'], ParamVSpin('设定等级', 0, '+d'), self.w['机师']]),
            0x5C: ('{0}等级{1}',
                   [self.w['机师'], ParamVSpin('等级变化', 0, '+d')]),
            0x5D: ('调整{0}击坠为{1}',
                   [self.w['机师'], ParamVSpin('设定击坠', 0)]),
            0x5E: ('{0}击坠{1}',
                   [self.w['机师'], ParamVSpin('击坠变化', 0, '+d')]),
            0x5F: ('{0}加入本方',
                   [self.w['机师']]),
            0x60: ('{0}转为{1}势力',
                   [self.w['机师'], self.w['势力']]),

            0x61: ('增加芯片 {0}',
                   [self.w['芯片']]),
            0x62: ('未知', []),
            0x63: ('未知', []),
            0x64: ('资源 - 增加资金', []),
            0x65: ('复活 - 复活机师', []),
            0x66: ('复活 - 复活机体', []),

            0x67: ('{0}移动到地图绝对坐标 X{1} Y{2}',
                   [self.w['机师'], ParamVSpin('X坐标', 0), ParamVSpin('Y坐标', 0)]),
            0x68: ('移动{0}到{1}相对坐标 X{2} Y{3}',
                   [self.w['机师'], self.w['机师'], ParamVSpin('X坐标', 0, '+d'), ParamVSpin('Y坐标', 0, '+d')]),
            0x69: ('移动 - 移动机师到敌方坐标', []),
            0x6A: ('移动 - 移动光标到绝对坐标', []),
            0x6B: ('移动 - 移动光标到相对坐标', []),
            0x6C: ('移动 - 移动光标到绝对坐标后闪烁', []),
            0x6E: ('移动 - 屏幕静止', []),
            0x6F: ('{0}撤退',
                   [self.w['机师']]),
            0x70: ('敌方序号[{0}]撤退',
                   [ParamVSpin('序号', 0x0, '02X'), ParamVSpin('无效', -0x80, '2X')]),
            0x71: ('撤退 - 敌方小组撤退', []),
            0x72: ('{0}势力全部撤退',
                   [self.w['势力']]),
            0x73: ('撤退 - 指定阵营撤退', []),
            0x74: ('撤退 - 指定阵营撤退到坐标区域', []),
            0x75: ('{0}{1}',
                   [self.w['机师'], self.w['状态']]),
            0x77: ('{0}{1}',
                   [self.w['机体'], self.w['状态']]),
            0x78: ('{0}处于搭载中',
                   [self.w['机师']]),
            0x79: ('判断 - 敌方小组剩余数量', []),
            0x7A: ('判断 - 指定势力剩余数量', []),
            0x7B: ('阵营{0}数量{1}{2}',
                   [self.w['阵营'], self.w['比较'], ParamVSpin('数量', 0)]),
            0x7C: ('{0}进入 X{1}-X{3} Y{2}-Y{4}区域内',
                   [self.w['机师'], ParamVSpin('X1', 1), ParamVSpin('Y1', 1), ParamVSpin('X2', 1), ParamVSpin('Y2', 1)]),
            0x7D: ('判断 - 敌方单位位于坐标区域', []),
            0x7E: ('判断 - 指定机体位于坐标区域', []),
            0x80: ('判断 - 指定势力位于坐标区域', []),
            0x81: ('{0}进入 X{1}-X{3} Y{2}-Y{4}区域内',
                   [self.w['阵营'], ParamVSpin('X1', 1), ParamVSpin('Y1', 1), ParamVSpin('X2', 1), ParamVSpin('Y2', 1)]),
            0x82: ('{0}与{1}相距{2}格',
                   [self.w['机师'], self.w['机师'], ParamVSpin('距离', 1)]),
            0x83: ('判断 - 指定机师与敌方单位距离', []),

            0x84: ('{0}气力调整为{1}',
                   [self.w['机师'], ParamVSpin('气力', 100)]),
            0x85: ('{0}气力调整为{1}',
                   [self.w['阵营'], ParamVSpin('气力', 100)]),
            0x86: ('调整 - 调整机师EN', []),
            0x87: ('未知', []),
            0x88: ('调整 - 调整人物HP', []),
            0x89: ('调整 - 调整阵营HP', []),
            0x8B: ('调整 - 调整阵营SP', []),

            0x8C: ('{0}电缆连接到地图绝对坐标 X{1} Y{2}',
                   [self.w['机师'], ParamVSpin('X坐标', 1), ParamVSpin('Y坐标', 1)]),
            0x8D: ('{0}电缆连接到{1}',
                   [self.w['机师'], self.w['机师']]),
            0x8E: ('{0}电缆就近连接',
                   [self.w['机师']]),
            0x8F: ('{0}电缆强制断开',
                   [self.w['机师']]),
            0x90: ('{0}移动到地图绝对坐标 X{1} Y{2}',
                   [self.w['机师'], ParamVSpin('X坐标', 1), ParamVSpin('Y坐标', 1)]),
            0x91: ('敌方序号[{0}]移动到地图绝对坐标 X{2} Y{3}',
                   [ParamVSpin('序号', 0x0, '02X'),
                    ParamVSpin('无效', -0x80, '2X'),
                    ParamVSpin('X坐标', 1),
                    ParamVSpin('Y坐标', 1)]),
            0x92: ('移动{0}到{1}相对坐标 X{2} Y{3} {4}',
                   [self.w['机师'], self.w['机师'], ParamVSpin('X坐标', 0), ParamVSpin('X坐标', 0), self.w['移动']]),
            0x93: ('移动{0}到敌方序号[{1}]相对坐标 X{3} Y{4} {5}',
                   [self.w['机师'],
                    ParamVSpin('序号', 0x0, '02X'),
                    ParamVSpin('无效', -0x80, '2X'),
                    ParamVSpin('X坐标', 0),
                    ParamVSpin('X坐标', 0),
                    self.w['移动']]),
            0x94: ('移动 - 移动敌方单位到相对坐标', []),
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
                    self.w['演出']]),
            0x97: ('战斗：敌方序号[{0}] 攻击 {2}\n攻方：武器编号[{3}] 命中{5}% 伤害{7}% {9}\n守方：武器编号[{4}] 命中{6}% 伤害{8}% {10}',
                   [ParamVSpin('序号', 0x0, '02X'),
                    ParamVSpin('无效', -0x80, '2X'),
                    self.w['机师'],
                    ParamVSpin('攻方武器', 0, 'X'),
                    ParamVSpin('守方武器', 0, 'X'),
                    ParamVSpin('攻方命中', 0),
                    ParamVSpin('守方命中', 0),
                    ParamVSpin('攻方伤害', 0),
                    ParamVSpin('守方伤害', 0),
                    self.w['演出'],
                    self.w['演出']]),
            0x98: ('战斗：{0} 攻击 敌方序号[{1}]\n攻方：武器编号[{3}] 命中{5}% 伤害{7}% {9}\n守方：武器编号[{4}] 命中{6}% 伤害{8}% {10}',
                   [self.w['机师'],
                    ParamVSpin('序号', 0x0, '02X'),
                    ParamVSpin('无效', -0x80, '2X'),
                    ParamVSpin('攻方武器', 0, 'X'),
                    ParamVSpin('守方武器', 0, 'X'),
                    ParamVSpin('攻方命中', 0),
                    ParamVSpin('守方命中', 0),
                    ParamVSpin('攻方伤害', 0),
                    ParamVSpin('守方伤害', 0),
                    self.w['演出'],
                    self.w['演出']]),
            0x99: ('演出 - 演出关闭',
                   []),

            0x9A: ('允许{0}势力攻击{1}势力',
                   [self.w['势力'], self.w['势力']]),
            0x9B: ('禁止{0}势力攻击{1}势力',
                   [self.w['势力'], self.w['势力']]),
            0x9C: ('规则 - 禁用指定机师菜单选项', []),
            0x9D: ('规则 - 禁用敌方单位菜单选项', []),
            0x9E: ('规则 - 启用指定机师菜单选项', []),
            0x9F: ('规则 - 指定机师强制击破', []),
            0xA0: ('敌方序号[{0}]强制击破',
                   [ParamVSpin('序号', 0x0, '02X'), ParamVSpin('无效', -0x80, '2X')]),
            0xA1: ('规则 - 指定机师为搭载状态', []),
            0xA2: ('{0}调整为未搭载状态',
                   [self.w['机师']]),
            0xA3: ('操作 - 指定机师浮上', []),
            0xA4: ('操作 - 指定机师着地', []),
            0xA5: ('{0}搭乘机体强制变形为{1}',
                   [self.w['机师'], self.w['机体']]),
            0xA6: ('操作 - 指定机师强制合体', []),
            0xA7: ('操作 - 指定机师强制分离', []),
            0xA8: ('操作 - 指定机师使用精神', []),
            0xA9: ('{0}设为{1}',
                   [self.w['机师'], self.w['行动']]),
            0xAA: ('操作 - EVA机师切换傀儡系统', []),

            0xAB: ('操作 - 指定机师增加说得指定机师菜单选项', []),
            0xAC: ('操作 - 指定机师增加说得敌方单位菜单选项', []),
            0xAD: ('判断 - 指定机师说得指定机师', []),
            0xAE: ('判断 - 指定机师说得敌方单位', []),
            0xAF: ('{0}与{1}交手',
                   [self.w['机师'], self.w['机师']]),
            0xB0: ('判断 - 指定机师交战敌方单位', []),
            0xB1: ('{0}攻击',
                   [self.w['机师']]),
            0xB2: ('敌方序号[{0}]被击破',
                   [ParamVSpin('序号', 0x0, '02X'), ParamVSpin('无效', -0x80, '2X')]),
            0xB3: ('{0}被击破',
                   [self.w['机师']]),
            0xB4: ('{0}被击破',
                   [self.w['机体']]),
            0xB5: ('未知', []),
            0xB6: ('判断 - 指定机师HP量', []),
            0xB7: ('判断 - 指定机师被击破', []),
            0xB8: ('判断 - 敌方单位未击破', []),
            0xB9: ('演出 - 相对坐标特殊演出', []),
            0xBA: ('演出 - 绝对坐标地图演出', []),
            0xBB: ('演出 - 相对坐标地图演出', []),
        }

    def explain(self, command: dict[str, int | list[int] | str]):
        code = command.get('Code')
        param = command.get('Param')
        param_setting: tuple[str, list[ParamWidget]] = self.COMMAND_SETTING.get(code, (str(code), tuple()))
        param_text, param_widgets = param_setting
        explain_list = []

        if code != 0xB9:
            for param_idx, param_widget in enumerate(param_widgets):
                # try:
                explain_list.append(param_widget.explain(param[param_idx]))
                # except:
                #     print(hex(code), param, param_idx)
            return param_text.format(*explain_list)

        for param_idx, param_widget in enumerate(param_widgets):
            if param_idx < 8:
                explain_list.append(param_widget.explain(param[param_idx]))
            else:
                explain_list.append(param_widgets[param_idx % 4 + 4].explain(param[param_idx]))
        return param_text.format(*explain_list)
