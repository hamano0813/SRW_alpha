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

        main_layout = QHBoxLayout()
        main_layout.addWidget(pilot_table)
        main_layout.addStretch()
        self.setLayout(main_layout)

    def init_pilot_table(self):
        group = QGroupBox('机师列表')
        self['机师列表'] = ArrayTable(
            self, '机师列表', {
                '机师': TextLine(None, '机师', PILOT_STRUCTURE['机师'],
                               font="Yu Gothic UI"),
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
            }
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
        filter_line.setFont('Yu Gothic UI')
        group.setFixedSize(840, 780)
        return group

    def set_rom(self, rom: PilotBIN):
        self.rom = rom
        self.parse()

    def parse(self):
        self.rom.parse()
        self['机师列表'].install(self.rom.data)

    def build(self):
        self.rom.build()
