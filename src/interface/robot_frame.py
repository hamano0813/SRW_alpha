#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Optional
from PySide6.QtWidgets import QLabel, QLineEdit, QGroupBox, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt
from structure import RobotRAF
from structure.specific.robot_raf import ROBOT_STRUCTURE, WEAPON_STRUCTURE
from widget import *


class RobotFrame(BackgroundFrame):
    def __init__(self, parent=None):
        super(RobotFrame, self).__init__(parent)
        self.rom: Optional[RobotRAF] = None
        robot_table_group = self.init_robot_table()
        weapon_table_group = self.init_weapon_table()

        right_layout = QVBoxLayout()
        right_layout.addWidget(weapon_table_group)
        main_layout = QHBoxLayout()
        main_layout.addWidget(robot_table_group)
        main_layout.addLayout(right_layout)
        main_layout.addStretch()
        self.setLayout(main_layout)

    def init_robot_table(self):
        group = QGroupBox('机体列表')
        self['机体列表'] = ArrayTable(
            self, '机体列表', {
                '名称': TextLine(None, '名称', ROBOT_STRUCTURE['名称'], alignment=Qt.AlignLeft | Qt.AlignVCenter),
                'HP': ValueSpin(None, 'HP', ROBOT_STRUCTURE['HP'], alignment=Qt.AlignRight | Qt.AlignVCenter),
                'EN': ValueSpin(None, 'EN', ROBOT_STRUCTURE['EN'], alignment=Qt.AlignRight | Qt.AlignVCenter),
                '运动性': ValueSpin(None, '运动性', ROBOT_STRUCTURE['运动性'], alignment=Qt.AlignRight | Qt.AlignVCenter),
                '装甲': ValueSpin(None, '装甲', ROBOT_STRUCTURE['装甲'], alignment=Qt.AlignRight | Qt.AlignVCenter),
                '限界': ValueSpin(None, '限界', ROBOT_STRUCTURE['限界'], alignment=Qt.AlignRight | Qt.AlignVCenter),
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
        group.setFixedWidth(705)
        return group

    def init_weapon_table(self):
        group = QGroupBox('武器列表')
        self['武器列表'] = ArrayTable(
            self['机体列表'], '武器列表', {
                '名称': TextLine(None, '名称', WEAPON_STRUCTURE['名称'], alignment=Qt.AlignLeft | Qt.AlignVCenter),
                '攻击力': ValueSpin(None, '攻击力', WEAPON_STRUCTURE['攻击力'], alignment=Qt.AlignRight | Qt.AlignVCenter),
                '近射程': ValueSpin(None, '近射程', WEAPON_STRUCTURE['近射程'], alignment=Qt.AlignRight | Qt.AlignVCenter),
                '远射程': ValueSpin(None, '远射程', WEAPON_STRUCTURE['远射程'], alignment=Qt.AlignRight | Qt.AlignVCenter),
                '命中率': ValueSpin(None, '命中率', WEAPON_STRUCTURE['命中率'], alignment=Qt.AlignRight | Qt.AlignVCenter),
                '会心率': ValueSpin(None, '会心率', WEAPON_STRUCTURE['会心率'], alignment=Qt.AlignRight | Qt.AlignVCenter),
            },
        )
        group_layout = QVBoxLayout()
        group_layout.addWidget(self['武器列表'])
        group.setLayout(group_layout)
        group.setFixedSize(705, 546)
        return group

    def set_rom(self, rom: RobotRAF):
        self.rom = rom
        self.parse()

    def parse(self):
        self.rom.parse()
        self['机体列表'].install(self.rom.data)

    def build(self):
        self.rom.build()
