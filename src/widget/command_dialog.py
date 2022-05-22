#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QSpinBox, QComboBox


class ParamWidget:
    def __init__(self, name: str, default: int, **kwargs):
        self.name = name
        self.default = default
        self.kwargs = kwargs

    def install(self, param: int = None):
        pass

    def data(self) -> int:
        pass

    def explain(self, param: int) -> str:
        pass

    def __del__(self):
        # noinspection PyUnresolvedReferences
        self.close()
        del self


class ParamValue(QSpinBox, ParamWidget):
    def __init__(self, name: str, default: int, display: str = 'd', **kwargs):
        QSpinBox.__init__(self, parent=None)
        ParamWidget.__init__(self, name, default, **kwargs)
        self.display = display

    def textFromValue(self, val: int) -> str:
        return f'{val:{self.display}}'

    def valueFromText(self, text: str) -> int:
        fmt = self.display.lower()
        if fmt.endswith('d'):
            return int(text)
        if fmt.endswith('x'):
            return int(text, 16)
        if fmt.endswith('b'):
            return int(text, 2)

    def install(self, param: int = None):
        if param is not None:
            return self.setValue(param)
        return self.setValue(self.default)

    def data(self) -> int:
        return self.value()

    def explain(self, param: int) -> str:
        return self.textFromValue(param)


class ParamCombo(QComboBox, ParamWidget):
    def __init__(self, name: str, default: int, mapping: dict[int, str], **kwargs):
        QComboBox.__init__(self, parent=None)
        ParamWidget.__init__(self, name, default, **kwargs)
        self.mapping = mapping

    def init_mapping(self):
        if self.mapping:
            for data, text in self.mapping.items():
                self.addItem(text, data)

    def install(self, param: int = None):
        if param is not None:
            return self.setCurrentText(self.mapping.get(param))
        return self.setCurrentText(self.mapping.get(self.default, self.currentText()))

    def data(self) -> int:
        return self.currentData()

    def explain(self, param: int) -> str:
        return self.mapping.get(param)


class CommandDialog(QDialog):
    def __init__(self, parent, command: dict = None, **kwargs):
        super(CommandDialog, self).__init__(parent, f=Qt.Dialog)
        self.command = command if command else {'Pos': 0x0, 'Code': 0x0, 'Count': 0x1, 'Param': list(), 'Data': ''}

        self.robots_combo = ParamCombo('选择机体', 0x0, kwargs.get('robots'))
        self.pilots_combo = ParamCombo('选择机师', 0x0, kwargs.get('pilots'))
        self.message_combo = ParamCombo('文本内容', 0x0, kwargs.get('messages'))

        self.COMMAND_SETTING = {
            0x00: ('<BLOCK ({0})>', [
                ParamValue('区块序号', 0, 'X'),
            ]),
            0x01: ('<STOP>', [
            ]),
            0x02: ('<IF ({0})>', [
                ParamValue('套欠层级', 0),
            ]),
            0x03: ('<ANY ({0})>', [
                ParamValue('套欠层级', 0),
            ]),
            0x04: ('<THEN ({0})>', [
                ParamValue('套欠层级', 0),
            ]),
            0x05: ('<ELSE ({0})>', [
                ParamValue('套欠层级', 0),
            ]),
            0x06: ('<ENDIF ({0})>', [
                ParamValue('套欠层级', 0),
            ]),
            0x08: ('<GOTO ({0})>', [
                ParamValue('目标偏移', 0),
            ]),
            0x09: ('<RUN ({0})>', [
                ParamValue('目标偏移', 0),
            ]),
            0x0A: ('<BACK>', []),
            0x0B: ('载入地图配置{0} 敌方配置{0} AI配置{0}', [
                ParamValue('地图配置', 0, '02X'),
                ParamValue('敌方配置', 0, '02X'),
                ParamValue('AI配置', 0, '02X'),
            ]),
            0x0C: ('触发全局事件{0}', [
                ParamValue('全局事件', 0, '04X')
            ]),
            0x0D: ('触发场景事件{0}', [
                ParamValue('场景事件', 0, '02X')
            ]),
            0x0E: ('事件 - 操作场景点数', []),
            0x0F: ('事件 - 操作全局点数', []),
            0x10: ('事件 - 判断全局事件', []),
            0x11: ('事件 - 判断场景事件', []),
            0x12: ('事件 - 场景点数比较', []),
            0x13: ('事件 - 全局点数比较', []),
            0x14: ('判断 - 真实系为真', []),
            0x15: ('判断 - 超级系为真', []),
            0x16: ('判断 - 必定返回假', []),
            0x17: ('{0} {1} 表情{2}\n{3}', [
                self.pilots_combo,
                ParamValue('未知', 0),
                ParamValue('表情', 0),
                self.message_combo,
            ]),
            0x18: ('文本 - 变量会话', []),
            0x19: ('文本 - 语音会话', []),
            0x1A: ('文本 - 最终话不同主角对战BOSS切换', []),
            0x1B: ('文本 - 最终话主角对战BOSS会话', []),
            0x1C: ('文本 - 播放音乐会话', []),
            0x1D: ('文本 - 停止音乐会话', []),
            0x1E: ('文本 - 胜利与失败文本', []),
            0x1F: ('文本 - 选项会话', []),
            0x21: ('文本 - 判断选项', []),
            0x22: ('剧情 - 场景胜利', []),
            0x23: ('剧情 - 场景失败', []),
            0x24: ('剧情 - 选择下一关卡', []),
            0x25: ('剧情 - 判断当前回合数', []),
            0x26: ('剧情 - 设定场景音乐', []),
            0x27: ('剧情 - 播放指定音乐', []),
            0x28: ('剧情 - 场景音乐复位', []),
            0x29: ('剧情 - 播放音效', []),
            0x2A: ('剧情 - 播放动画', []),
            0x2B: ('剧情 - 静止等待', []),
            0x2C: ('出击 - 敌方列表组出击', []),
            0x2D: ('出击 - 敌方列表组出击到机师相对坐标', []),
            0x2F: ('出击 - 敌方列表组再次出击', []),
            0x30: ('机库 - 机库开启', []),
            0x31: ('机库 - 机库关闭', []),
            0x32: ('机库 - 增加机体', []),
            0x33: ('机库 - 机体离队', []),
            0x34: ('机库 - 机体归队', []),
            0x35: ('机库 - 刪除机体', []),
            0x36: ('机库 - 替换机体', []),
            0x37: ('机库 - 增加机师', []),
            0x38: ('机库 - 机师离队', []),
            0x39: ('机库 - 机师归队', []),
            0x3A: ('机库 - 删除机师', []),
            0x3B: ('机库 - 替换机师', []),
            0x3C: ('未知', []),
            0x3D: ('机库 - 增加机体机师或强制换乘', []),
            0x3E: ('机库 - 机师分流', []),
            0x3F: ('机库 - 机体合流', []),
            0x40: ('机库 - 机师合流', []),
            0x41: ('机库 - 机体归队', []),
            0x42: ('机库 - 机师离队', []),
            0x43: ('机库 - 强制换乘', []),
            0x44: ('机库 - 换乘空机体', []),
            0x45: ('机库 - 取消机师乘坐', []),
            0x46: ('机库 - 增加机体', []),
            0x47: ('机库 - 机师强制出场', []),
            0x48: ('机库 - 指定妖精搭配', []),
            0x49: ('机库 - 隐藏机师', []),
            0x4A: ('机库 - 隐藏机体', []),
            0x4B: ('机库 - 换乘空机体', []),
            0x4E: ('机库 - 合体允许分离', []),
            0x4F: ('出击 - 出击开启', []),
            0x50: ('出击 - 出击关闭', []),
            0x51: ('出击 - 机师出击到绝对坐标', []),
            0x52: ('出击 - 机师出击到相对坐标', []),
            0x54: ('出击 - 机体出击到绝对坐标', []),
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
            0x67: ('移动 - 移动机师到绝对坐标', []),
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
            0x75: ('判断 - 机师状态', []),
            0x77: ('判断 - 机体状态', []),
            0x78: ('判断 - 机师是否搭载', []),
            0x79: ('判断 - 敌方小组剩余数量', []),
            0x7A: ('判断 - 指定势力剩余数量', []),
            0x7B: ('判断 - 指定阵营剩余数量', []),
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
            0xAF: ('判断 - 指定机师交战指定机师', []),
            0xB0: ('判断 - 指定机师交战敌方单位', []),
            0xB1: ('判断 - 指定机师攻击', []),
            0xB2: ('判断 - 敌方单位被击破', []),
            0xB3: ('判断 - 指定机师被击破', []),
            0xB4: ('判断 - 指定机体被击破', []),
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
        if code != 0xB9:
            param_setting: tuple[str, list[ParamValue]] = self.COMMAND_SETTING.get(code, (str(code), tuple()))
            param_text, param_widgets = param_setting
            explain_list = []
            for param_idx, param_widget in enumerate(param_widgets):
                explain_list.append(param_widget.explain(param[param_idx]))
            return param_text.format(*explain_list)
        return 0xB9
