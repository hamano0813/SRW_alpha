#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QLabel, QLineEdit, QGroupBox, QHBoxLayout, QVBoxLayout, QFormLayout, QGridLayout,
                               QSizePolicy, QPushButton, QSpacerItem)

from parameter.enum_data import EnumData
from structure import RobotRAF
from structure.specific.robot_raf import ROBOT_STRUCTURE, WEAPON_STRUCTURE
from widget import *


# noinspection PyUnresolvedReferences
class RobotFrame(BackgroundFrame):
    def __init__(self, parent=None, **kwargs):
        super(RobotFrame, self).__init__(parent, **kwargs)
        self.rom: Optional[RobotRAF] = None
        self.init_ui()

    def init_ui(self):
        robot_table = self.init_robot_table()
        move_group = self.init_move_group()
        deform_group = self.init_deform_group()
        transfer_group = self.init_transfer_group()
        skill_group = self.init_skill_group()
        bgm_group = self.init_bgm_group()

        robot_sub_layout = QGridLayout()
        robot_sub_layout.addWidget(transfer_group, 0, 0, 1, 1)
        robot_sub_layout.addWidget(skill_group, 0, 1, 1, 1)
        robot_sub_layout.addWidget(bgm_group, 1, 0, 1, 2)
        robot_layout = QHBoxLayout()
        robot_layout.addWidget(move_group)
        robot_layout.addWidget(deform_group)
        robot_layout.addLayout(robot_sub_layout)
        robot_layout.addStretch()

        weapon_table = self.init_weapon_table()
        weapon_group = self.init_weapon_group()
        weapon_map = self.init_weapon_map()
        weapon_adaptation = self.init_weapon_adaptation()

        parse_button = QPushButton('刷新数据')
        build_button = QPushButton('写入数据')
        parse_button.clicked.connect(self.parse)
        build_button.clicked.connect(self.build)
        parse_button.setFixedHeight(40)
        build_button.setFixedHeight(40)

        button_layout = QVBoxLayout()
        button_layout.addWidget(weapon_adaptation)
        button_layout.addStretch()
        button_layout.addWidget(parse_button)
        button_layout.addWidget(build_button)

        weapon_bottom_layout = QHBoxLayout()
        weapon_bottom_layout.addWidget(weapon_map)
        weapon_bottom_layout.addLayout(button_layout)
        weapon_sub_layout = QVBoxLayout()
        weapon_sub_layout.addWidget(weapon_group)
        weapon_sub_layout.addLayout(weapon_bottom_layout)
        weapon_sub_layout.addStretch()
        weapon_layout = QHBoxLayout()
        weapon_layout.addWidget(weapon_table)
        weapon_layout.addLayout(weapon_sub_layout)
        weapon_layout.addStretch()

        right_layout = QVBoxLayout()
        right_layout.addLayout(robot_layout)
        right_layout.addLayout(weapon_layout)

        main_layout = QHBoxLayout()
        main_layout.addWidget(robot_table, alignment=Qt.AlignTop)
        main_layout.addLayout(right_layout)
        main_layout.addStretch()
        self.setLayout(main_layout)

    def init_robot_table(self):
        group = QGroupBox('机体列表')
        self['机体列表'] = ArrayTable(
            self, '机体列表', {
                '机体': TextLine(None, '机体', ROBOT_STRUCTURE['机体'],
                               font="Yu Gothic UI"),
                'ＨＰ': ValueSpin(None, 'ＨＰ', ROBOT_STRUCTURE['ＨＰ'],
                                alignment=Qt.AlignRight),
                'ＥＮ': ValueSpin(None, 'ＥＮ', ROBOT_STRUCTURE['ＥＮ'],
                                alignment=Qt.AlignRight),
                '运动': ValueSpin(None, '运动', ROBOT_STRUCTURE['运动'],
                                alignment=Qt.AlignRight),
                '装甲': ValueSpin(None, '装甲', ROBOT_STRUCTURE['装甲'],
                                alignment=Qt.AlignRight),
                '限界': ValueSpin(None, '限界', ROBOT_STRUCTURE['限界'],
                                alignment=Qt.AlignRight),
            },
        )
        filter_line = QLineEdit()
        filter_layout = QHBoxLayout()
        filter_layout.addWidget(QLabel('筛选机体'))
        filter_layout.addWidget(filter_line)
        group_layout = QVBoxLayout()
        group_layout.addWidget(self['机体列表'])
        group_layout.addLayout(filter_layout)
        group.setLayout(group_layout)
        filter_line.textChanged[str].connect(self['机体列表'].filterChanged)
        filter_line.setFont('Yu Gothic UI')
        group.setFixedSize(630, 780)
        return group

    def init_move_group(self):
        group = QGroupBox('机体属性')
        self['移动类型'] = CheckCombo(self['机体列表'], '移动类型', ROBOT_STRUCTURE['移动类型'],
                                  EnumData.ROBOT['移动类型'])
        self['移动力'] = ValueSpin(self['机体列表'], '移动力', ROBOT_STRUCTURE['移动类型'],
                                alignment=Qt.AlignRight)
        self['空适应'] = MappingSpin(self['机体列表'], '空适应', ROBOT_STRUCTURE['空适应'],
                                  EnumData.ROBOT['适应'],
                                  alignment=Qt.AlignRight)
        self['陆适应'] = MappingSpin(self['机体列表'], '陆适应', ROBOT_STRUCTURE['陆适应'],
                                  EnumData.ROBOT['适应'],
                                  alignment=Qt.AlignRight)
        self['海适应'] = MappingSpin(self['机体列表'], '海适应', ROBOT_STRUCTURE['海适应'],
                                  EnumData.ROBOT['适应'],
                                  alignment=Qt.AlignRight)
        self['宇适应'] = MappingSpin(self['机体列表'], '宇适应', ROBOT_STRUCTURE['宇适应'],
                                  EnumData.ROBOT['适应'],
                                  alignment=Qt.AlignRight)
        self['尺寸'] = MappingSpin(self['机体列表'], '尺寸', ROBOT_STRUCTURE['尺寸'],
                                 EnumData.ROBOT['尺寸'],
                                 alignment=Qt.AlignRight)
        self['部件槽数'] = ValueSpin(self['机体列表'], '部件槽数', ROBOT_STRUCTURE['部件槽数'],
                                 alignment=Qt.AlignRight)
        form_layout = QFormLayout()
        form_layout.addRow('移动力', self['移动力'])
        form_layout.addRow('尺寸', self['尺寸'])
        form_layout.addRow('强化槽', self['部件槽数'])
        form_layout.addRow('空适应', self['空适应'])
        form_layout.addRow('陆适应', self['陆适应'])
        form_layout.addRow('海适应', self['海适应'])
        form_layout.addRow('宇适应', self['宇适应'])

        group_layout = QVBoxLayout()
        group_layout.addWidget(QLabel('移动类型'))
        group_layout.addWidget(self['移动类型'])
        group_layout.addLayout(form_layout)

        group.setLayout(group_layout)
        group.setFixedWidth(135)
        return group

    def init_deform_group(self):
        group = QGroupBox('变形合体、换装及机体价格')
        self['变形组号'] = ValueSpin(self['机体列表'], '变形组号', ROBOT_STRUCTURE['变形组号'],
                                 alignment=Qt.AlignRight)
        self['变形序号'] = ValueSpin(self['机体列表'], '变形序号', ROBOT_STRUCTURE['变形序号'],
                                 alignment=Qt.AlignRight)
        self['合体组号'] = ValueSpin(self['机体列表'], '合体组号', ROBOT_STRUCTURE['合体组号'],
                                 alignment=Qt.AlignRight)
        self['合体序号'] = ValueSpin(self['机体列表'], '合体序号', ROBOT_STRUCTURE['合体序号'],
                                 alignment=Qt.AlignRight)
        self['合体数量'] = ValueSpin(self['机体列表'], '合体数量', ROBOT_STRUCTURE['合体数量'],
                                 alignment=Qt.AlignRight)
        self['分离序号'] = RadioCombo(self['机体列表'], '分离序号', ROBOT_STRUCTURE['分离序号'],
                                  mapping=self.kwargs.get('robots', dict()) | {0xFFFF: 'ーー'},
                                  alignment=Qt.AlignRight, font='Yu Gothic UI')
        self['换装组'] = RadioCombo(self['机体列表'], '换装组', ROBOT_STRUCTURE['换装组'],
                                 mapping=EnumData.ROBOT['换装组'],
                                 alignment=Qt.AlignRight, font='Yu Gothic UI')
        self['修理费'] = ValueSpin(self['机体列表'], '修理费', ROBOT_STRUCTURE['修理费'],
                                alignment=Qt.AlignRight)
        self['资金'] = ValueSpin(self['机体列表'], '资金', ROBOT_STRUCTURE['资金'],
                               alignment=Qt.AlignRight)
        group_layout = QGridLayout()
        group_layout.addWidget(QLabel('变形组序'), 0, 0, 1, 1)
        group_layout.addWidget(self['变形组号'], 0, 1, 1, 1)
        group_layout.addWidget(self['变形序号'], 0, 2, 1, 1)
        group_layout.addWidget(QLabel('合体组序'), 1, 0, 1, 1)
        group_layout.addWidget(self['合体组号'], 1, 1, 1, 1)
        group_layout.addWidget(self['合体序号'], 1, 2, 1, 1)
        group_layout.addWidget(QLabel('合体数量'), 2, 0, 1, 1)
        group_layout.addWidget(self['合体数量'], 2, 1, 1, 1)
        group_layout.addWidget(QLabel('分离机体'), 3, 0, 1, 4)
        group_layout.addWidget(self['分离序号'], 4, 0, 1, 4)
        group_layout.addWidget(QLabel('换装系统'), 5, 0, 1, 4)
        group_layout.addWidget(self['换装组'], 6, 0, 1, 4)
        group_layout.addWidget(QLabel('击破资金'), 7, 0, 1, 1)
        group_layout.addWidget(self['资金'], 7, 1, 1, 3)
        group_layout.addWidget(QLabel('修理费'), 8, 0, 1, 1)
        group_layout.addWidget(self['修理费'], 8, 1, 1, 3)
        group.setLayout(group_layout)
        group.setFixedWidth(249)
        return group

    def init_transfer_group(self):
        group = QGroupBox('换乘系统')
        self['换乘系'] = CheckList(self['机体列表'], '换乘系', ROBOT_STRUCTURE['换乘系'],
                                EnumData.ROBOT['换乘系'],
                                font='Yu Gothic UI')
        group_layout = QVBoxLayout()
        group_layout.addWidget(self['换乘系'])
        group.setLayout(group_layout)
        group.setFixedWidth(180)
        return group

    def init_skill_group(self):
        group = QGroupBox('机体特殊能力')
        self['特殊能力'] = CheckList(self['机体列表'], '特殊能力', ROBOT_STRUCTURE['特殊能力'],
                                 item_list=EnumData.ROBOT['特殊能力'],
                                 font='Yu Gothic UI')
        group_layout = QHBoxLayout()
        group_layout.addWidget(self['特殊能力'])
        group.setLayout(group_layout)
        group.setFixedWidth(200)
        return group

    def init_bgm_group(self):
        group = QGroupBox('机体音乐')
        self['BGM'] = RadioCombo(self['机体列表'], 'BGM', ROBOT_STRUCTURE['BGM'],
                                 mapping={k: f'[{k:02X}] {v}' for k, v in EnumData.MUSIC.items()},
                                 font='Yu Gothic UI')
        self['BGM'].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        group_layout = QHBoxLayout()
        group_layout.addWidget(QLabel('选择BGM'))
        group_layout.addWidget(self['BGM'])

        group.setLayout(group_layout)
        return group

    def init_weapon_table(self):
        group = QGroupBox('武器列表')
        self['武器列表'] = ArrayTable(
            self['机体列表'], '武器列表', {
                '武器': TextLine(None, '武器', WEAPON_STRUCTURE['武器'],
                               font="Yu Gothic UI"),
                '分类': MappingSpin(None, '分类', WEAPON_STRUCTURE['分类'], EnumData.WEAPON['分类'],
                                  alignment=Qt.AlignRight, font='Yu Gothic UI'),
                '攻击力': ValueSpin(None, '攻击力', WEAPON_STRUCTURE['攻击力'],
                                 alignment=Qt.AlignRight),
            },
        )
        group_layout = QVBoxLayout()
        group_layout.addWidget(self['武器列表'])
        group.setLayout(group_layout)
        group.setFixedSize(390, 480)
        return group

    def init_weapon_group(self):
        group = QGroupBox('武器常规设置')
        self['属性'] = CheckCombo(self['武器列表'], '属性', WEAPON_STRUCTURE['属性'],
                                item_list=EnumData.WEAPON['属性'], dummy='', sep='  ', font='Yu Gothic UI')

        self['近射程'] = ValueSpin(self['武器列表'], '近射程', WEAPON_STRUCTURE['近射程'],
                                alignment=Qt.AlignRight)
        self['远射程'] = ValueSpin(self['武器列表'], '远射程', WEAPON_STRUCTURE['远射程'],
                                alignment=Qt.AlignRight)

        self['命中'] = ValueSpin(self['武器列表'], '命中', WEAPON_STRUCTURE['命中'],
                               alignment=Qt.AlignRight)
        self['会心'] = ValueSpin(self['武器列表'], '会心', WEAPON_STRUCTURE['会心'],
                               alignment=Qt.AlignRight)

        self['必要新人类Lv'] = ValueSpin(self['武器列表'], '必要新人类Lv', WEAPON_STRUCTURE['必要新人类Lv'],
                                    alignment=Qt.AlignRight)
        self['必要圣战士Lv'] = ValueSpin(self['武器列表'], '必要圣战士Lv', WEAPON_STRUCTURE['必要圣战士Lv'],
                                    alignment=Qt.AlignRight)
        self['必要气力'] = ValueSpin(self['武器列表'], '必要气力', WEAPON_STRUCTURE['必要气力'],
                                 alignment=Qt.AlignRight)

        self['改造类型'] = ValueSpin(self['武器列表'], '改造类型', WEAPON_STRUCTURE['改造类型'],
                                 alignment=Qt.AlignRight)
        self['改造追加'] = MappingSpin(self['武器列表'], '改造追加', WEAPON_STRUCTURE['改造追加'],
                                   mapping={i: f'[{i:X}]' for i in range(0x10)},
                                   alignment=Qt.AlignRight)

        self['初期弹数'] = ValueSpin(self['武器列表'], '初期弹数', WEAPON_STRUCTURE['初期弹数'],
                                 alignment=Qt.AlignRight)
        self['最大弹数'] = ValueSpin(self['武器列表'], '最大弹数', WEAPON_STRUCTURE['最大弹数'],
                                 alignment=Qt.AlignRight)
        self['消费EN'] = ValueSpin(self['武器列表'], '消费EN', WEAPON_STRUCTURE['消费EN'],
                                 alignment=Qt.AlignRight)

        group_layout = QGridLayout()
        group_layout.addWidget(QLabel('特性'), 0, 0, 1, 1)
        group_layout.addWidget(self['属性'], 0, 1, 1, 5)

        group_layout.addWidget(QLabel('近射程'), 1, 0, 1, 1)
        group_layout.addWidget(self['近射程'], 1, 1, 1, 1)
        group_layout.addWidget(QLabel('远射程'), 2, 0, 1, 1)
        group_layout.addWidget(self['远射程'], 2, 1, 1, 1)
        group_layout.addWidget(QLabel('命中'), 3, 0, 1, 1)
        group_layout.addWidget(self['命中'], 3, 1, 1, 1)
        group_layout.addWidget(QLabel('会心'), 4, 0, 1, 1)
        group_layout.addWidget(self['会心'], 4, 1, 1, 1)

        group_layout.addWidget(QLabel('初期弹数'), 1, 2, 1, 1)
        group_layout.addWidget(self['初期弹数'], 1, 3, 1, 1)
        group_layout.addWidget(QLabel('最大弹数'), 2, 2, 1, 1)
        group_layout.addWidget(self['最大弹数'], 2, 3, 1, 1)
        group_layout.addWidget(QLabel('改造类型'), 3, 2, 1, 1)
        group_layout.addWidget(self['改造类型'], 3, 3, 1, 1)
        group_layout.addWidget(QLabel('改造追加'), 4, 2, 1, 1)
        group_layout.addWidget(self['改造追加'], 4, 3, 1, 1)

        group_layout.addWidget(QLabel('消费EN'), 1, 4, 1, 1)
        group_layout.addWidget(self['消费EN'], 1, 5, 1, 1)
        group_layout.addWidget(QLabel('气力需求'), 2, 4, 1, 1)
        group_layout.addWidget(self['必要气力'], 2, 5, 1, 1)
        group_layout.addWidget(QLabel('新人类Lv'), 3, 4, 1, 1)
        group_layout.addWidget(self['必要新人类Lv'], 3, 5, 1, 1)
        group_layout.addWidget(QLabel('圣战士Lv'), 4, 4, 1, 1)
        group_layout.addWidget(self['必要圣战士Lv'], 4, 5, 1, 1)

        group.setLayout(group_layout)
        group.setFixedWidth(386)
        return group

    def init_weapon_map(self):
        group = QGroupBox('地图武器设置')
        self['MAP类型'] = RadioCombo(self['武器列表'], 'MAP类型', WEAPON_STRUCTURE['MAP类型'],
                                   mapping=EnumData.WEAPON['MAP类型'],
                                   font='Yu Gothic UI')
        self['MAP演出'] = ValueSpin(self['武器列表'], 'MAP演出', WEAPON_STRUCTURE['MAP演出'],
                                  alignment=Qt.AlignRight)
        self['MAP着弹范围'] = ValueSpin(self['武器列表'], 'MAP着弹范围', WEAPON_STRUCTURE['MAP着弹范围'],
                                    alignment=Qt.AlignRight)
        self['MAP范围'] = RangeCombo(self['武器列表'], 'MAP范围', WEAPON_STRUCTURE['MAP范围'])

        self['MAP类型'].currentIndexChanged.connect(self.charge_map)
        self['MAP演出'].setFixedSize(60, 28)
        self['MAP着弹范围'].setFixedSize(60, 28)

        group_layout = QGridLayout()
        group_layout.setObjectName('weapon_map')
        group_layout.addWidget(QLabel('地图武器类型'), 0, 0, 1, 2)
        group_layout.addWidget(self['MAP类型'], 1, 0, 1, 2)
        group_layout.addWidget(QLabel('地图武器演出效果'), 2, 0, 1, 1)
        group_layout.addWidget(self['MAP演出'], 2, 1, 1, 1)
        group_layout.addWidget(QLabel('着弾点指定型范围半径'), 3, 0, 1, 1)
        group_layout.addWidget(self['MAP着弹范围'], 3, 1, 1, 1)
        group_layout.addWidget(QLabel('方向指定型覆盖范围'), 4, 0, 1, 1)
        group_layout.addWidget(self['MAP范围'], 5, 0, 1, 2)
        group_layout.addItem(QSpacerItem(1, 1, QSizePolicy.Fixed, QSizePolicy.Expanding), 6, 0, 1, 2)
        group.setLayout(group_layout)
        group.setFixedSize(245, 289)
        return group

    def init_weapon_adaptation(self):
        group = QGroupBox('武器适应性')
        self['空'] = MappingSpin(self['武器列表'], '空适应', WEAPON_STRUCTURE['空适应'], EnumData.WEAPON['适应'],
                                alignment=Qt.AlignRight)
        self['陆'] = MappingSpin(self['武器列表'], '陆适应', WEAPON_STRUCTURE['陆适应'], EnumData.WEAPON['适应'],
                                alignment=Qt.AlignRight)
        self['海'] = MappingSpin(self['武器列表'], '海适应', WEAPON_STRUCTURE['海适应'], EnumData.WEAPON['适应'],
                                alignment=Qt.AlignRight)
        self['宇'] = MappingSpin(self['武器列表'], '宇适应', WEAPON_STRUCTURE['宇适应'], EnumData.WEAPON['适应'],
                                alignment=Qt.AlignRight)
        group_layout = QFormLayout()
        group_layout.addRow('空适应', self['空'])
        group_layout.addRow('陆适应', self['陆'])
        group_layout.addRow('海适应', self['海'])
        group_layout.addRow('宇适应', self['宇'])
        group.setLayout(group_layout)
        group.setFixedWidth(135)
        return group

    def charge_map(self):
        layout = self.findChild(QGridLayout, 'weapon_map')
        if self['MAP类型'].currentIndex() == 0:
            layout.itemAtPosition(2, 0).widget().setHidden(True)
            layout.itemAtPosition(3, 0).widget().setHidden(True)
            layout.itemAtPosition(4, 0).widget().setHidden(True)
            self['MAP演出'].setHidden(True)
            self['MAP着弹范围'].setHidden(True)
            self['MAP范围'].setHidden(True)
        elif self['MAP类型'].currentIndex() == 1:
            layout.itemAtPosition(2, 0).widget().setHidden(False)
            layout.itemAtPosition(3, 0).widget().setHidden(True)
            layout.itemAtPosition(4, 0).widget().setHidden(False)
            self['MAP演出'].setHidden(False)
            self['MAP着弹范围'].setHidden(True)
            self['MAP范围'].setHidden(False)
        elif self['MAP类型'].currentIndex() == 2:
            layout.itemAtPosition(2, 0).widget().setHidden(False)
            layout.itemAtPosition(3, 0).widget().setHidden(True)
            layout.itemAtPosition(4, 0).widget().setHidden(True)
            self['MAP演出'].setHidden(False)
            self['MAP着弹范围'].setHidden(True)
            self['MAP范围'].setHidden(True)
        elif self['MAP类型'].currentIndex() == 3:
            layout.itemAtPosition(2, 0).widget().setHidden(False)
            layout.itemAtPosition(3, 0).widget().setHidden(False)
            layout.itemAtPosition(4, 0).widget().setHidden(True)
            self['MAP演出'].setHidden(False)
            self['MAP着弹范围'].setHidden(False)
            self['MAP范围'].setHidden(True)

    def set_rom(self, rom: RobotRAF):
        self.rom = rom
        self.parse()

    def parse(self):
        self.rom.parse()
        self['分离序号'].init_mapping(self.rom.robots() | {0xFFFF: 'ーー'})
        self['机体列表'].install(self.rom.data)
        self.charge_map()

    def build(self):
        self.rom.build()
