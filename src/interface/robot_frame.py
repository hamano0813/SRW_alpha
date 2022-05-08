#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QLineEdit, QGroupBox, QHBoxLayout, QVBoxLayout

from structure import RobotRAF
from structure.specific.robot_raf import ROBOT_STRUCTURE, WEAPON_STRUCTURE
from widget import *


class RobotFrame(BackgroundFrame):
    def __init__(self, parent=None):
        super(RobotFrame, self).__init__(parent)
        self.rom: Optional[RobotRAF] = None
        robot_table_group = self.init_robot_table()
        weapon_table_group = self.init_weapon_table()

        move_group = self.init_move_group()
        robot_layout = QHBoxLayout()
        robot_layout.addWidget(move_group)
        robot_layout.addStretch()

        right_layout = QVBoxLayout()
        right_layout.addLayout(robot_layout)
        right_layout.addWidget(weapon_table_group)
        right_layout.addStretch()
        main_layout = QHBoxLayout()
        main_layout.addWidget(robot_table_group)
        main_layout.addLayout(right_layout)
        main_layout.addStretch()
        self.setLayout(main_layout)

    def init_robot_table(self):
        group = QGroupBox('机体列表')
        self['机体列表'] = ArrayTable(
            self, '机体列表', {
                '名称': TextLine(None, '名称', ROBOT_STRUCTURE['名称'], font="Yu Gothic UI Semibold"),
                'HP': ValueSpin(None, 'HP', ROBOT_STRUCTURE['HP'], alignment=Qt.AlignRight),
                'EN': ValueSpin(None, 'EN', ROBOT_STRUCTURE['EN'], alignment=Qt.AlignRight),
                '运动性': ValueSpin(None, '运动性', ROBOT_STRUCTURE['运动性'], alignment=Qt.AlignRight),
                '装甲': ValueSpin(None, '装甲', ROBOT_STRUCTURE['装甲'], alignment=Qt.AlignRight),
                '限界': ValueSpin(None, '限界', ROBOT_STRUCTURE['限界'], alignment=Qt.AlignRight),
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
        group.setFixedWidth(690)
        return group

    def init_move_group(self):
        move_group = QGroupBox('地形及移动')
        self['移动类型'] = CheckCombo(
            self['机体列表'], '移动类型', ROBOT_STRUCTURE['移动类型'], ['空', '陸', '海', '地'])

        group_layout = QVBoxLayout()
        group_layout.addWidget(QLabel('移动类型'))
        group_layout.addWidget(self['移动类型'])

        move_group.setLayout(group_layout)
        return move_group


    def init_weapon_table(self):
        group = QGroupBox('武器列表')
        self['武器列表'] = ArrayTable(
            self['机体列表'], '武器列表', {
                '名称': TextLine(None, '名称', WEAPON_STRUCTURE['名称'], font="Yu Gothic UI Semibold"),
                '攻击力': ValueSpin(None, '攻击力', WEAPON_STRUCTURE['攻击力'], alignment=Qt.AlignRight),
                '近射程': ValueSpin(None, '近射程', WEAPON_STRUCTURE['近射程'], alignment=Qt.AlignRight),
                '远射程': ValueSpin(None, '远射程', WEAPON_STRUCTURE['远射程'], alignment=Qt.AlignRight),
                '命中率': ValueSpin(None, '命中率', WEAPON_STRUCTURE['命中率'], alignment=Qt.AlignRight),
                '会心率': ValueSpin(None, '会心率', WEAPON_STRUCTURE['会心率'], alignment=Qt.AlignRight),
            },
        )
        group_layout = QVBoxLayout()
        group_layout.addWidget(self['武器列表'])
        group.setLayout(group_layout)
        group.setFixedSize(690, 546)
        return group

    def set_rom(self, rom: RobotRAF):
        self.rom = rom
        self.parse()

    def parse(self):
        self.rom.parse()
        self['机体列表'].install(self.rom.data)

    def build(self):
        self.rom.build()
