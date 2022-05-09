#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QLabel, QLineEdit, QGroupBox, QHBoxLayout, QVBoxLayout, QFormLayout, QGridLayout,
                               QSizePolicy, QPushButton, QSpacerItem)

from parameter.enum_data import EnumData
from structure import PilotBIN
from structure.specific.pilot_bin import PILOT_STRUCTURE, SKILL_STRUCTURE
from widget import *


# noinspection PyUnresolvedReferences
class PilotFrame(BackgroundFrame):
    def __init__(self, parent=None, **kwargs):
        super(PilotFrame, self).__init__(parent, **kwargs)
        self.rom: Optional[PilotBIN] = None
        self.init_ui()

    def init_ui(self):
        pilot_table = self.init_pilot_table()
        pilot_group = self.init_pilot_group()
        skill_table = self.init_skill_table()

        top_layout = QHBoxLayout()
        top_layout.addWidget(pilot_group)
        right_layout = QVBoxLayout()
        right_layout.addLayout(top_layout)
        right_layout.addWidget(skill_table)

        main_layout = QHBoxLayout()
        main_layout.addWidget(pilot_table)
        main_layout.addLayout(right_layout)
        main_layout.addStretch()
        self.setLayout(main_layout)

    def init_pilot_table(self):
        group = QGroupBox('机师列表')
        self['机师列表'] = ArrayTable(
            self, '机师列表', {
                '机师': TextLine(None, '机师', PILOT_STRUCTURE['机师'],
                               font='Yu Gothic UI semibold'),
                '全名': TextLine(None, '全名', PILOT_STRUCTURE['全名'],
                               font='Yu Gothic UI semibold'),
                '格斗': ValueSpin(None, '格斗', PILOT_STRUCTURE['格斗'],
                                alignment=Qt.AlignRight),
                '射击': ValueSpin(None, '射击', PILOT_STRUCTURE['射击'],
                                alignment=Qt.AlignRight),
                '回避': ValueSpin(None, '回避', PILOT_STRUCTURE['回避'],
                                alignment=Qt.AlignRight),
                '命中': ValueSpin(None, '命中', PILOT_STRUCTURE['命中'],
                                alignment=Qt.AlignRight),
                '反应': ValueSpin(None, '反应', PILOT_STRUCTURE['反应'],
                                alignment=Qt.AlignRight),
                '技量': ValueSpin(None, '技量', PILOT_STRUCTURE['技量'],
                                alignment=Qt.AlignRight),
                'SP': ValueSpin(None, 'SP', PILOT_STRUCTURE['SP'],
                                alignment=Qt.AlignRight),
                '两动': ValueSpin(None, '两动', PILOT_STRUCTURE['两动'],
                                alignment=Qt.AlignRight),
            },
            stretch=(1,)
        )
        filter_line = QLineEdit()
        filter_layout = QHBoxLayout()
        filter_layout.addWidget(QLabel('筛选机师'))
        filter_layout.addWidget(filter_line)
        group_layout = QVBoxLayout()
        group_layout.addWidget(self['机师列表'])
        group_layout.addLayout(filter_layout)
        group.setLayout(group_layout)
        filter_line.textChanged[str].connect(self['机师列表'].filterChanged)
        filter_line.setFont('Yu Gothic UI semibold')
        group.setFixedSize(960, 780)
        return group

    def init_pilot_group(self):
        group = QGroupBox('机师属性')
        self['性格'] = RadioCombo(self['机师列表'], '性格', PILOT_STRUCTURE['性格'],
                                mapping=EnumData.PILOT['性格'],
                                alignment=Qt.AlignRight, font='Yu Gothic UI semibold')
        self['气力补正组'] = ValueSpin(self['机师列表'], '气力补正组', PILOT_STRUCTURE['气力补正组'],
                                  alignment=Qt.AlignRight)
        self['分类'] = CheckCombo(self['机师列表'], '分类', PILOT_STRUCTURE['分类'],
                                item_list=EnumData.PILOT['分类'],
                                dummy='', sep=' ', font='Yu Gothic UI semibold')

        group_layout = QGridLayout()
        group_layout.addWidget(QLabel('身份'), 0, 0, 1, 1)
        group_layout.addWidget(self['分类'], 0, 1, 1, 3)
        group_layout.addWidget(QLabel('性格'), 1, 0, 1, 1)
        group_layout.addWidget(self['性格'], 1, 1, 1, 1)
        group_layout.addWidget(QLabel('气力补正组'), 1, 2, 1, 1)
        group_layout.addWidget(self['气力补正组'], 1, 3, 1, 1)
        group.setLayout(group_layout)
        return group

    def init_skill_table(self):
        group = QGroupBox('特殊技能')
        lv_mapping = {lv: f'{lv}' for lv in range(1, 100)} | {0xFF: 'ー'}
        self['特殊技能'] = TransposeTable(
            self['机师列表'], '技能列表', {
                '技能': RadioCombo(None, '技能', SKILL_STRUCTURE['技能'],
                                 mapping=EnumData.PILOT['特殊技能'],
                                 alignment=Qt.AlignLeft, font='Yu Gothic UI semibold'),
                'Lv1': MappingSpin(None, 'Lv1', SKILL_STRUCTURE['Lv1'],
                                   mapping=lv_mapping,
                                   readonly=False,
                                   alignment=Qt.AlignRight),
                'Lv2': MappingSpin(None, 'Lv2', SKILL_STRUCTURE['Lv2'],
                                   mapping=lv_mapping,
                                   readonly=False,
                                   alignment=Qt.AlignRight),
                'Lv3': MappingSpin(None, 'Lv3', SKILL_STRUCTURE['Lv3'],
                                   mapping=lv_mapping,
                                   readonly=False,
                                   alignment=Qt.AlignRight),
                'Lv4': MappingSpin(None, 'Lv4', SKILL_STRUCTURE['Lv4'],
                                   mapping=lv_mapping,
                                   readonly=False,
                                   alignment=Qt.AlignRight),
                'Lv5': MappingSpin(None, 'Lv5', SKILL_STRUCTURE['Lv5'],
                                   mapping=lv_mapping,
                                   readonly=False,
                                   alignment=Qt.AlignRight),
                'Lv6': MappingSpin(None, 'Lv6', SKILL_STRUCTURE['Lv6'],
                                   mapping=lv_mapping,
                                   readonly=False,
                                   alignment=Qt.AlignRight),
                'Lv7': MappingSpin(None, 'Lv7', SKILL_STRUCTURE['Lv7'],
                                   mapping=lv_mapping,
                                   readonly=False,
                                   alignment=Qt.AlignRight),
                'Lv8': MappingSpin(None, 'Lv8', SKILL_STRUCTURE['Lv8'],
                                   mapping=lv_mapping,
                                   readonly=False,
                                   alignment=Qt.AlignRight),
                'Lv9': MappingSpin(None, 'Lv9', SKILL_STRUCTURE['Lv9'],
                                   mapping=lv_mapping,
                                   readonly=False,
                                   alignment=Qt.AlignRight),
            }
        )
        group_layout = QVBoxLayout()
        group_layout.addWidget(self['特殊技能'])
        group.setFixedWidth(450)
        group.setLayout(group_layout)
        return group

    def set_rom(self, rom: PilotBIN):
        self.rom = rom
        self.parse()

    def parse(self):
        self.rom.parse()
        self['机师列表'].install(self.rom.data)

    def build(self):
        self.rom.build()
