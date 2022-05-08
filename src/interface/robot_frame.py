#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QLineEdit, QGroupBox, QHBoxLayout, QVBoxLayout, QFormLayout, QGridLayout, \
    QSizePolicy

from structure import RobotRAF
from structure.specific.robot_raf import ROBOT_STRUCTURE, WEAPON_STRUCTURE
from widget import *
from parameter.enum_data import EnumData


class RobotFrame(BackgroundFrame):
    def __init__(self, parent=None, **kwargs):
        super(RobotFrame, self).__init__(parent)
        self.rom: Optional[RobotRAF] = None
        self.kwargs = kwargs
        robot_table_group = self.init_robot_table()
        weapon_table_group = self.init_weapon_table()

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

        weapon_layout = QHBoxLayout()
        weapon_layout.addWidget(weapon_table_group)

        weapon_layout.addStretch()

        right_layout = QVBoxLayout()
        right_layout.addLayout(robot_layout)
        right_layout.addLayout(weapon_layout)
        right_layout.addStretch()

        main_layout = QHBoxLayout()
        main_layout.addWidget(robot_table_group, alignment=Qt.AlignTop)
        main_layout.addLayout(right_layout)
        main_layout.addStretch()
        self.setLayout(main_layout)

    def init_robot_table(self):
        group = QGroupBox('机体列表')
        self['机体列表'] = ArrayTable(
            self, '机体列表', {
                '名称': TextLine(None, '名称', ROBOT_STRUCTURE['名称'],
                               font="Yu Gothic UI Semibold"),
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
        # noinspection PyUnresolvedReferences
        filter_line.textChanged[str].connect(self['机体列表'].filterChanged)
        filter_line.setFont('Yu Gothic UI Semibold')
        group.setFixedSize(630, 792)
        return group

    def init_move_group(self):
        move_group = QGroupBox('机体属性')
        self['移动类型'] = CheckCombo(self['机体列表'], '移动类型', ROBOT_STRUCTURE['移动类型'], EnumData.ROBOT['移动类型'])
        self['移动力'] = ValueSpin(self['机体列表'], '移动力', ROBOT_STRUCTURE['移动类型'],
                                alignment=Qt.AlignRight)
        self['空适应'] = MappingSpin(self['机体列表'], '空适应', ROBOT_STRUCTURE['空适应'], EnumData.ROBOT['空适应'],
                                  alignment=Qt.AlignRight)
        self['陆适应'] = MappingSpin(self['机体列表'], '陆适应', ROBOT_STRUCTURE['陆适应'], EnumData.ROBOT['陆适应'],
                                  alignment=Qt.AlignRight)
        self['海适应'] = MappingSpin(self['机体列表'], '海适应', ROBOT_STRUCTURE['海适应'], EnumData.ROBOT['海适应'],
                                  alignment=Qt.AlignRight)
        self['宇适应'] = MappingSpin(self['机体列表'], '宇适应', ROBOT_STRUCTURE['宇适应'], EnumData.ROBOT['宇适应'],
                                  alignment=Qt.AlignRight)
        self['尺寸'] = MappingSpin(self['机体列表'], '尺寸', ROBOT_STRUCTURE['尺寸'], EnumData.ROBOT['尺寸'],
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

        move_group.setLayout(group_layout)
        move_group.setFixedWidth(135)
        return move_group

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
                                  alignment=Qt.AlignRight, font='Yu Gothic UI Semibold')
        self['换装组'] = RadioCombo(self['机体列表'], '换装组', ROBOT_STRUCTURE['换装组'],
                                 mapping=EnumData.ROBOT['换装组'],
                                 alignment=Qt.AlignRight, font='Yu Gothic UI Semibold')
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
        group = QGroupBox('换乘系统及机体BGM')
        self['换乘系'] = CheckList(self['机体列表'], '换乘系', ROBOT_STRUCTURE['换乘系'], EnumData.ROBOT['换乘系'],
                                font='Yu Gothic UI Semibold')
        group_layout = QVBoxLayout()
        group_layout.addWidget(self['换乘系'])
        group.setLayout(group_layout)
        group.setFixedWidth(180)
        return group

    def init_skill_group(self):
        group = QGroupBox('机体特殊能力')
        self['特殊能力'] = CheckList(self['机体列表'], '特殊能力', ROBOT_STRUCTURE['特殊能力'], EnumData.ROBOT['特殊能力'],
                                 font='Yu Gothic UI Semibold')
        group_layout = QHBoxLayout()
        group_layout.addWidget(self['特殊能力'])
        group.setLayout(group_layout)
        group.setFixedWidth(200)
        return group

    def init_bgm_group(self):
        group = QGroupBox('机体音乐')
        self['BGM'] = RadioCombo(self['机体列表'], 'BGM', ROBOT_STRUCTURE['BGM'], EnumData.MUSIC,
                                 font='Yu Gothic UI Semibold')
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
                '名称': TextLine(None, '名称', WEAPON_STRUCTURE['名称'],
                               font="Yu Gothic UI Semibold"),
                '分类': MappingSpin(None, '分类', WEAPON_STRUCTURE['分类'], EnumData.WEAPON['分类'],
                                  alignment=Qt.AlignRight, font='Yu Gothic UI Semibold'),
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
        group = QGroupBox('武器属性')
        self['近射程'] = ValueSpin(self['武器列表'], '近射程', WEAPON_STRUCTURE['近射程'],
                                alignment=Qt.AlignRight)
        self['远射程'] = ValueSpin(self['武器列表'], '远射程', WEAPON_STRUCTURE['远射程'],
                                alignment=Qt.AlignRight)
        self['命中'] = ValueSpin(self['武器列表'], '命中', WEAPON_STRUCTURE['命中'],
                               alignment=Qt.AlignRight)
        self['会心'] = ValueSpin(self['武器列表'], '会心', WEAPON_STRUCTURE['会心'],
                               alignment=Qt.AlignRight)
        group_layout = QGridLayout()
        return group

    def set_rom(self, rom: RobotRAF):
        self.rom = rom
        self.parse()

    def parse(self):
        self.rom.parse()
        self['机体列表'].install(self.rom.data)

    def build(self):
        self.rom.build()
