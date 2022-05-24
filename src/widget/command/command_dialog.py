#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog

from parameter import EnumData
from widget.command import ParamValueSpin, ParamRadioCombo, ParamCheckCombo
from widget.command.param_widget import ParamWidget


class CommandDialog(QDialog):
    def __init__(self, parent, command: dict = None, **kwargs):
        super(CommandDialog, self).__init__(parent, f=Qt.Dialog)
        self.command = command if command else {'Pos': 0x0, 'Code': 0x0, 'Count': 0x1, 'Param': list(), 'Data': ''}

        self.widgets = dict()
        self.widgets['机体'] = ParamRadioCombo('选择机体', 0x0, kwargs.get('robots'))
        self.widgets['机师'] = ParamRadioCombo('选择机师', 0x0, kwargs.get('pilots'))
        self.widgets['文本'] = ParamRadioCombo('选择文本', 0x0, kwargs.get('messages'))

        self.widgets['关卡'] = ParamRadioCombo('选择关卡', 0, EnumData.STAGE)
        self.widgets['音乐'] = ParamRadioCombo('选择音乐', 0x0, EnumData.MUSIC)
        self.widgets['事件'] = ParamRadioCombo('选择事件', 0x0, EnumData.EVENT)

        self.widgets['表情'] = ParamRadioCombo('选择表情', 0x0, EnumData.COMMAND['表情'])
        self.widgets['势力'] = ParamCheckCombo('选择势力', 0x0, EnumData.COMMAND['势力'])
        self.widgets['阵营'] = ParamRadioCombo('选择阵营', 0, EnumData.COMMAND['阵营'])
        self.widgets['比较'] = ParamRadioCombo('比较符号', 0x2, EnumData.COMMAND['比较'])
        self.widgets['触发'] = ParamRadioCombo('触发状态', 0x2, EnumData.COMMAND['触发'])
        self.widgets['点数'] = ParamRadioCombo('全局点数', 0x2, EnumData.COMMAND['点数'])
        self.widgets['状态'] = ParamRadioCombo('存在状态', 0x2, EnumData.COMMAND['状态'])

        self.COMMAND_SETTING = {
            0x00: ('BLOCK<{0}>', [ParamValueSpin('区块序号', 0, 'X'), ]),
            0x01: ('STOP', []),
            0x02: ('ALL ({0})', [ParamValueSpin('套欠层级', 0), ]),
            0x03: ('ANY ({0})', [ParamValueSpin('套欠层级', 0), ]),
            0x04: ('THEN ({0})', [ParamValueSpin('套欠层级', 0), ]),
            0x05: ('ELSE ({0})', [ParamValueSpin('套欠层级', 0), ]),
            0x06: ('ENDIF ({0})', [ParamValueSpin('套欠层级', 0), ]),
            0x08: ('GOTO {0}', [ParamValueSpin('目标偏移', 0), ]),
            0x09: ('RUN {0}', [ParamValueSpin('目标偏移', 0), ]),
            0x0A: ('BACK', []),
            0x0B: ('载入地图设计{0} 敌方设计{0} AI设计{0}', [
                ParamValueSpin('地图设计', 0, '02X'),
                ParamValueSpin('敌方设计', 0, '02X'),
                ParamValueSpin('AI设计', 0, '02X'),
            ]),
            0x0C: ('触发全局事件{0}', [self.widgets['事件'], ]),
            0x0D: ('触发场景事件[{0}]', [ParamValueSpin('场景事件', 0, '02X')]),
            0x0E: ('场景点数[{0}]{1}', [ParamValueSpin('场景点数', 0, '04X'), ParamValueSpin('数值操作', 0, '+d'), ]),
            0x0F: ('全局点数{0}{1}', [self.widgets['点数'], ParamValueSpin('数值操作', 0, '+d'), ]),
            0x10: ('全局事件{0}为{1}状态', [self.widgets['事件'], self.widgets['触发'], ]),
            0x11: ('场景事件[{0}]为{1}状态', [ParamValueSpin('场景事件', 0, '02X'), self.widgets['触发'], ]),
            0x12: ('场景点数[{0}]{1}{2}', [self.widgets['点数'], self.widgets['比较'], ParamValueSpin('点数', 0), ]),
            0x13: ('全局点数{0}{1}{2}', [self.widgets['点数'], self.widgets['比较'], ParamValueSpin('点数', 0), ]),
            0x14: ('路线为真实系', []),
            0x15: ('路线为超级系', []),
            0x16: ('返回假', []),
            0x17: ('{0}{2}的说 -- {3}', [
                self.widgets['机师'],
                ParamValueSpin('无效', 0),
                self.widgets['表情'],
                self.widgets['文本'],
            ]),
            0x18: ('{0}{2}的说 -- {3}', [
                self.widgets['机师'],
                ParamValueSpin('无效', 0),
                self.widgets['表情'],
                self.widgets['文本'],
            ]),
            0x19: ('{1}{3}的用语音[{0}]说 -- {4}', [
                ParamValueSpin('语音', 0, '04X'),
                self.widgets['机师'],
                ParamValueSpin('无效', 0),
                self.widgets['表情'],
                self.widgets['文本'],
            ]),
            0x1A: ('文本 - 最终话不同主角对战BOSS切换', []),
            0x1B: ('文本 - 最终话主角对战BOSS会话', []),
            0x1C: ('文本 - 播放音乐会话', []),
            0x1D: ('文本 - 停止音乐会话', []),
            0x1E: ('显示胜利条件：{1}  失败条件：{3}', [
                ParamValueSpin('无效', 0),
                self.widgets['文本'],
                ParamValueSpin('无效', 0),
                self.widgets['文本'],
            ]),
            0x1F: ('{0}选择 -- {2}', [
                self.widgets['机师'],
                ParamValueSpin('无效', 0),
                self.widgets['文本'],
            ]),
            0x21: ('选择了第一项', [ParamValueSpin('无效', 0), ]),
            0x22: ('场景胜利', [ParamValueSpin('未知', 0), ]),
            0x23: ('场景失败', []),
            0x24: ('下一关为{0}', [self.widgets['关卡'], ]),
            0x25: ('当前回合{1}{0}', [ParamValueSpin('当前回合', 0), self.widgets['比较'], ]),
            0x26: ('设定本方回合音乐为《{0}》  敌方回合音乐为《{1}》', [
                self.widgets['音乐'],
                self.widgets['音乐'],
                ParamValueSpin('无效', 0),
            ]),
            0x27: ('播放音乐《{0}》', [self.widgets['音乐'], ]),
            0x28: ('音乐复位', []),
            0x29: ('播放《0x{0}》音效', [ParamValueSpin('音效', 0, '04X'), ]),
            0x2A: ('剧情 - 播放动画', []),
            0x2B: ('剧情 - 静止等待', []),
            0x2C: ('敌方设计第{0}组以[{1}]势力出击设为{2}阵营', [
                ParamValueSpin('敌方组号', 0),
                self.widgets['势力'],
                self.widgets['阵营'],
            ]),
            0x2D: ('出击 - 敌方列表组出击到机师相对坐标', []),
            0x2F: ('出击 - 敌方列表组再次出击', []),
            0x30: ('格纳库开启', []),
            0x31: ('格纳库关闭', []),
            0x32: ('机库 - 增加机体', []),
            0x33: ('机库 - 机体离队', []),
            0x34: ('机库 - 机体归队', []),
            0x35: ('刪除{0}', [self.widgets['机体'], ]),
            0x36: ('机库 - 替换机体', []),
            0x37: ('机库 - 增加机师', []),
            0x38: ('机库 - 机师离队', []),
            0x39: ('机库 - 机师归队', []),
            0x3A: ('删除{0}', [self.widgets['机师'], ]),
            0x3B: ('机库 - 替换机师', []),
            0x3C: ('未知', []),
            0x3D: ('加入{0} {1}级 击坠数{2} 搭乘{3} 机体{4}改 武器{5}改', [
                self.widgets['机师'],
                ParamValueSpin('等级', 1),
                ParamValueSpin('击坠数', 0),
                self.widgets['机体'],
                ParamValueSpin('机体改造', 0),
                ParamValueSpin('武器改造', 0),
            ]),
            0x3E: ('机库 - 机师分流', []),
            0x3F: ('机库 - 机体合流', []),
            0x40: ('机库 - 机师合流', []),
            0x41: ('机库 - 机体归队', []),
            0x42: ('机库 - 机师离队', []),
            0x43: ('机库 - 强制换乘', []),
            0x44: ('机库 - 换乘空机体', []),
            0x45: ('{0}取消搭乘', [self.widgets['机师'], ]),
            0x46: ('机库 - 增加机体', []),
            0x47: ('机库 - 机师强制出场', []),
            0x48: ('机库 - 指定妖精搭配', []),
            0x49: ('机库 - 隐藏机师', []),
            0x4A: ('机库 - 隐藏机体', []),
            0x4B: ('机库 - 换乘空机体', []),
            0x4E: ('机库 - 合体允许分离', []),
            0x4F: ('开始出击', []),
            0x50: ('出击完毕', []),
            0x51: ('{0}出击到地图绝对坐标 X{1} Y{2}', [
                self.widgets['机师'],
                ParamValueSpin('X坐标', 0),
                ParamValueSpin('Y坐标', 0),
            ]),
            0x52: ('出击 - 机师出击到相对坐标', []),
            0x54: ('{0}出击到地图绝对坐标 X{1} Y{2}', [
                self.widgets['机体'],
                ParamValueSpin('X坐标', 0),
                ParamValueSpin('Y坐标', 0),
            ]),
            0x55: ('出击 - 机体出击到相对坐标', []),
            0x57: ('出击 - 本方部队出击到绝对坐标', []),
            0x58: ('出击 - 本方部队出击到相对坐标', []),
            0x5A: ('出击 - 本方母舰出击到绝对坐标', []),
            0x5B: ('机师 - 设定机师等级', []),
            0x5C: ('机师 - 增加机师等级', []),
            0x5D: ('机师 - 设定机师击坠', []),
            0x5E: ('机师 - 增加机师击坠', []),
            0x5F: ('阵营 - 敌方机师加入', []),
            0x60: ('阵营 - 设定机师阵营', []),
            0x61: ('资源 - 增加芯片', []),
            0x62: ('未知', []),
            0x63: ('未知', []),
            0x64: ('资源 - 增加资金', []),
            0x65: ('复活 - 复活机师', []),
            0x66: ('复活 - 复活机体', []),
            0x67: ('{0}移动到地图绝对坐标 X{1} Y{2}', [
                self.widgets['机师'],
                ParamValueSpin('X坐标', 0),
                ParamValueSpin('Y坐标', 0),
            ]),
            0x68: ('移动 - 移动机师到相对坐标', []),
            0x69: ('移动 - 移动机师到敌方坐标', []),
            0x6A: ('移动 - 移动光标到绝对坐标', []),
            0x6B: ('移动 - 移动光标到相对坐标', []),
            0x6C: ('移动 - 移动光标到绝对坐标后闪烁', []),
            0x6E: ('移动 - 屏幕静止', []),
            0x6F: ('撤退 - 指定机师撤退', []),
            0x70: ('撤退 - 敌方单位撤退', []),
            0x71: ('撤退 - 敌方小组撤退', []),
            0x72: ('撤退 - 指定势力撤退', []),
            0x73: ('撤退 - 指定阵营撤退', []),
            0x74: ('撤退 - 指定阵营撤退到坐标区域', []),
            0x75: ('{0}{1}', [self.widgets['机师'], self.widgets['状态'], ]),
            0x77: ('{0}{1}', [self.widgets['机体'], self.widgets['状态'], ]),
            0x78: ('判断 - 机师是否搭载', []),
            0x79: ('判断 - 敌方小组剩余数量', []),
            0x7A: ('判断 - 指定势力剩余数量', []),
            0x7B: ('阵营{0}数量{1}{2}', [
                self.widgets['阵营'],
                self.widgets['比较'],
                ParamValueSpin('数量', 0),
            ]),
            0x7C: ('判断 - 指定机师位于坐标区域', []),
            0x7D: ('判断 - 敌方单位位于坐标区域', []),
            0x7E: ('判断 - 指定机体位于坐标区域', []),
            0x80: ('判断 - 指定势力位于坐标区域', []),
            0x81: ('判断 - 指定阵营位于坐标区域', []),
            0x82: ('判断 - 指定机师坐标间的距离', []),
            0x83: ('判断 - 指定机师与敌方单位距离', []),
            0x84: ('调整 - 调整机师气力', []),
            0x85: ('调整 - 调整阵营气力', []),
            0x86: ('调整 - 调整机师EN', []),
            0x87: ('未知', []),
            0x88: ('调整 - 调整人物HP', []),
            0x89: ('调整 - 调整阵营HP', []),
            0x8B: ('调整 - 调整阵营SP', []),
            0x8C: ('连接 - EVA机师电缆连接到坐标', []),
            0x8D: ('连接 - EVA机师电缆连接到机师', []),
            0x8E: ('连接 - EVA机师电缆就近连接', []),
            0x8F: ('连接 - EVA机师电缆强制断开', []),
            0x90: ('移动 - 移动机师到绝对坐标', []),
            0x91: ('移动 - 移动敌方单位到绝对坐标', []),
            0x92: ('移动 - 移动机师到相对坐标', []),
            0x93: ('移动 - 移动机师到敌方坐标', []),
            0x94: ('移动 - 移动敌方单位到相对坐标', []),
            0x96: ('演出 - 指定机师强制攻击指定机师', []),
            0x97: ('演出 - 敌方单位强制攻击指定机师', []),
            0x98: ('演出 - 指定机师强制攻击敌方单位', []),
            0x99: ('演出 - 演出关闭', []),
            0x9A: ('规则 - 允许指定势力攻击指定势力', []),
            0x9B: ('规则 - 禁止指定势力攻击指定势力', []),
            0x9C: ('规则 - 禁用指定机师菜单选项', []),
            0x9D: ('规则 - 禁用敌方单位菜单选项', []),
            0x9E: ('规则 - 启用指定机师菜单选项', []),
            0x9F: ('规则 - 指定机师强制击破', []),
            0xA0: ('规则 - 指定敌方单位强制击破', []),
            0xA1: ('规则 - 指定机师为搭载状态', []),
            0xA2: ('规则 - 指定机师为未搭载状态', []),
            0xA3: ('操作 - 指定机师浮上', []),
            0xA4: ('操作 - 指定机师着地', []),
            0xA5: ('操作 - 指定机师强制变形', []),
            0xA6: ('操作 - 指定机师强制合体', []),
            0xA7: ('操作 - 指定机师强制分离', []),
            0xA8: ('操作 - 指定机师使用精神', []),
            0xA9: ('操作 - 指定机师调整行动状态', []),
            0xAA: ('操作 - EVA机师切换傀儡系统', []),
            0xAB: ('操作 - 指定机师增加说得指定机师菜单选项', []),
            0xAC: ('操作 - 指定机师增加说得敌方单位菜单选项', []),
            0xAD: ('判断 - 指定机师说得指定机师', []),
            0xAE: ('判断 - 指定机师说得敌方单位', []),
            0xAF: ('{0}与{1}交手', [self.widgets['机师'], self.widgets['机师'], ]),
            0xB0: ('判断 - 指定机师交战敌方单位', []),
            0xB1: ('判断 - 指定机师攻击', []),
            0xB2: ('判断 - 敌方单位被击破', []),
            0xB3: ('{0}被击破', [self.widgets['机师'], ]),
            0xB4: ('{0}被击破', [self.widgets['机体'], ]),
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
                explain_list.append(param_widget.explain(param[param_idx]))
            return param_text.format(*explain_list)

        for param_idx, param_widget in enumerate(param_widgets):
            if param_idx < 8:
                explain_list.append(param_widget.explain(param[param_idx]))
            else:
                explain_list.append(param_widgets[param_idx % 4 + 4].explain(param[param_idx]))
        return param_text.format(*explain_list)
