#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGroupBox, QHBoxLayout, QLineEdit, QLabel, QVBoxLayout

from parameter import SNMSG_TEXT_EXTRA
from structure import SnmsgBIN
from structure.specific.snmsg_bin import SNMSG_STRUCTURE
from widget import *


class SnmsgFrame(BackgroundFrame):
    def __init__(self, parent=None, **kwargs):
        super(SnmsgFrame, self).__init__(parent, **kwargs)
        self.rom: Optional[SnmsgBIN] = None
        self.init_ui()

    def init_ui(self):
        snmsg_table = self.init_snmsg_table
        main_layout = QHBoxLayout()
        main_layout.addWidget(snmsg_table)
        self.setLayout(main_layout)

    @property
    def init_snmsg_table(self):
        group = QGroupBox('シナリオメッセージ')
        self['メッセージリスト'] = ArrayTable(
            self, 'メッセージリスト',
            {
                'メッセージ': TextMulti(None, 'メッセージ', SNMSG_STRUCTURE['メッセージ'],
                                   extra=SNMSG_TEXT_EXTRA, ),
            }, sortable=False, alignment=Qt.AlignTop, resizeRows=False)
        self['メッセージリスト'].setObjectName('MessageList')
        self['メッセージリスト'].verticalHeader().setMinimumSectionSize(62)
        layout = QHBoxLayout()
        layout.addWidget(self['メッセージリスト'])
        filter_line = QLineEdit()
        filter_layout = QHBoxLayout()
        filter_layout.addWidget(QLabel('メッセージ検索'))
        filter_layout.addWidget(filter_line)
        group_layout = QVBoxLayout()
        group_layout.addWidget(self['メッセージリスト'])
        group_layout.addLayout(filter_layout)
        group.setLayout(group_layout)
        # noinspection PyUnresolvedReferences
        filter_line.textChanged[str].connect(self['メッセージリスト'].filterChanged)
        return group

    def set_roms(self, roms: list[SnmsgBIN]):
        self.rom = roms[0]
        self.parse()

    def parse(self):
        self.rom.parse()
        self['メッセージリスト'].install(self.rom.data)

    def build(self):
        self.rom.build()
