#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QLineEdit, QGroupBox, QHBoxLayout, QVBoxLayout, QFormLayout, QGridLayout

from parameter.enum_data import EnumData
from structure import PilotBIN
from structure.specific.pilot_bin import PILOT_STRUCTURE, SKILL_STRUCTURE
from widget import *


class PilotFrame(BackgroundFrame):
    def __init__(self, parent=None, **kwargs):
        super(PilotFrame, self).__init__(parent, **kwargs)
        self.rom: Optional[PilotBIN] = None
        self.lv_mapping = {lv: f'{lv}' for lv in range(1, 100)}

        self.init_ui()

    def init_ui(self):
        pilot_table = self.init_pilot_table()
        skill_table = self.init_skill_table()

        pilot_sprite = self.init_pilot_spirit()
        pilot_skill = self.init_pilot_skill()
        pilot_transfer = self.init_pilot_transfer()
        pilot_adaptation = self.init_pilot_adaptation()

        pilot_table.setFixedWidth(1070)
        skill_table.setFixedHeight(297)
        pilot_sprite.setFixedHeight(220)
        pilot_skill.setFixedSize(135, 220)
        pilot_adaptation.setFixedWidth(135)

        main_layout = QHBoxLayout()
        main_layout.addWidget(pilot_table)
        grid_layout = QGridLayout()
        grid_layout.addWidget(skill_table, 0, 0, 1, 2)
        grid_layout.addWidget(pilot_sprite, 1, 0, 1, 1)
        grid_layout.addWidget(pilot_skill, 1, 1, 1, 1)
        grid_layout.addWidget(pilot_transfer, 2, 0, 2, 1)
        grid_layout.addWidget(pilot_adaptation, 2, 1, 1, 1)
        main_layout.addLayout(grid_layout)
        main_layout.addStretch()
        self.setLayout(main_layout)

    def init_pilot_table(self):
        group = QGroupBox('パイロットリスト')
        self['パイロットリスト'] = ArrayTable(
            self, 'パイロットリスト', {
                'パイロット': TextLine(None, 'パイロット', PILOT_STRUCTURE['パイロット']),
                '名前': TextLine(None, '名前', PILOT_STRUCTURE['名前']),
                '格闘': ValueSpin(None, '格闘', PILOT_STRUCTURE['格闘'], alignment=Qt.AlignRight),
                '射撃': ValueSpin(None, '射撃', PILOT_STRUCTURE['射撃'], alignment=Qt.AlignRight),
                '回避': ValueSpin(None, '回避', PILOT_STRUCTURE['回避'], alignment=Qt.AlignRight),
                '命中': ValueSpin(None, '命中', PILOT_STRUCTURE['命中'], alignment=Qt.AlignRight),
                '反応': ValueSpin(None, '反応', PILOT_STRUCTURE['反応'], alignment=Qt.AlignRight),
                '技量': ValueSpin(None, '技量', PILOT_STRUCTURE['技量'], alignment=Qt.AlignRight),
                '性格': RadioCombo(self['パイロットリスト'], '性格', PILOT_STRUCTURE['性格'],
                                 mapping=EnumData.PILOT['性格']),
                'ＳＰ': ValueSpin(None, 'ＳＰ', PILOT_STRUCTURE['ＳＰ'], alignment=Qt.AlignRight),
                '２回行動': ValueSpin(None, '２回行動', PILOT_STRUCTURE['２回行動'], alignment=Qt.AlignRight),
                'チーム': ValueSpin(self['パイロットリスト'], 'チーム', PILOT_STRUCTURE['チーム'], alignment=Qt.AlignRight),
            },
            stretch=(1,)
        )
        filter_line = QLineEdit()
        filter_layout = QHBoxLayout()
        filter_layout.addWidget(QLabel('パイロット検索'))
        filter_layout.addWidget(filter_line)
        group_layout = QVBoxLayout()
        group_layout.addWidget(self['パイロットリスト'])
        group_layout.addLayout(filter_layout)
        group.setLayout(group_layout)
        filter_line.textChanged[str].connect(self['パイロットリスト'].filterChanged)
        return group

    def init_skill_table(self):
        group = QGroupBox('レベルアップ技能')
        self['技能'] = TransposeTable(
            self['パイロットリスト'], '技能リスト', {
                '技能': RadioCombo(None, '技能', SKILL_STRUCTURE['技能'],
                                 mapping=EnumData.PILOT['技能'], alignment=Qt.AlignLeft),
                'L1': MappingSpin(None, 'L1', SKILL_STRUCTURE['L1'],
                                  mapping=self.lv_mapping | {0xFF: '一'}, alignment=Qt.AlignRight),
                'L2': MappingSpin(None, 'L2', SKILL_STRUCTURE['L2'],
                                  mapping=self.lv_mapping | {0xFF: '一'}, alignment=Qt.AlignRight),
                'L3': MappingSpin(None, 'L3', SKILL_STRUCTURE['L3'],
                                  mapping=self.lv_mapping | {0xFF: '一'}, alignment=Qt.AlignRight),
                'L4': MappingSpin(None, 'L4', SKILL_STRUCTURE['L4'],
                                  mapping=self.lv_mapping | {0xFF: '一'}, alignment=Qt.AlignRight),
                'L5': MappingSpin(None, 'L5', SKILL_STRUCTURE['L5'],
                                  mapping=self.lv_mapping | {0xFF: '一'}, alignment=Qt.AlignRight),
                'L6': MappingSpin(None, 'L6', SKILL_STRUCTURE['L6'],
                                  mapping=self.lv_mapping | {0xFF: '一'}, alignment=Qt.AlignRight),
                'L7': MappingSpin(None, 'L7', SKILL_STRUCTURE['L7'],
                                  mapping=self.lv_mapping | {0xFF: '一'}, alignment=Qt.AlignRight),
                'L8': MappingSpin(None, 'L8', SKILL_STRUCTURE['L8'],
                                  mapping=self.lv_mapping | {0xFF: '一'}, alignment=Qt.AlignRight),
                'L9': MappingSpin(None, 'L9', SKILL_STRUCTURE['L9'],
                                  mapping=self.lv_mapping | {0xFF: '一'}, alignment=Qt.AlignRight),
            }
        )
        group_layout = QVBoxLayout()
        group_layout.addWidget(self['技能'])
        group.setLayout(group_layout)
        return group

    def init_pilot_skill(self):
        group = QGroupBox('特殊技能')
        self['特殊技能'] = CheckList(self['パイロットリスト'], '特殊技能', PILOT_STRUCTURE['特殊技能'],
                                 item_list=EnumData.PILOT['特殊技能'])
        group_layout = QVBoxLayout()
        group_layout.addWidget(self['特殊技能'])
        group.setLayout(group_layout)
        return group

    def init_pilot_transfer(self):
        group = QGroupBox('乗り換え系')
        self['乗り換え系'] = CheckList(self['パイロットリスト'], '乗り換え系', PILOT_STRUCTURE['乗り換え系'],
                                  EnumData.PILOT['乗り換え系'])
        group_layout = QVBoxLayout()
        group_layout.addWidget(self['乗り換え系'])
        group.setLayout(group_layout)
        return group

    def init_pilot_adaptation(self):
        group = QGroupBox('地形適応')
        self['空適応'] = MappingSpin(self['パイロットリスト'], '空適応', PILOT_STRUCTURE['空適応'], EnumData.PILOT['適応'])
        self['陸適応'] = MappingSpin(self['パイロットリスト'], '陸適応', PILOT_STRUCTURE['陸適応'], EnumData.PILOT['適応'])
        self['海適応'] = MappingSpin(self['パイロットリスト'], '海適応', PILOT_STRUCTURE['海適応'], EnumData.PILOT['適応'])
        self['宇適応'] = MappingSpin(self['パイロットリスト'], '宇適応', PILOT_STRUCTURE['宇適応'], EnumData.PILOT['適応'])
        group_layout = QFormLayout()
        group_layout.addRow('空適応', self['空適応'])
        group_layout.addRow('陸適応', self['陸適応'])
        group_layout.addRow('海適応', self['海適応'])
        group_layout.addRow('宇適応', self['宇適応'])
        group.setLayout(group_layout)
        return group

    def init_pilot_spirit(self):
        group = QGroupBox('精神リスト')
        self['精神リスト'] = ParallelTable(
            self['パイロットリスト'], ('精神リスト', '習得リスト'), {
                '精神': RadioCombo(None, '精神', PILOT_STRUCTURE['精神リスト']['精神'], mapping=EnumData.SPIRIT),
                '習得': MappingSpin(None, '習得', PILOT_STRUCTURE['習得リスト']['習得'],
                                  mapping=self.lv_mapping | {0xFF: '一'}, alignment=Qt.AlignRight),
            }
        )
        group_layout = QVBoxLayout()
        group_layout.addWidget(self['精神リスト'])
        group.setLayout(group_layout)
        return group

    def set_roms(self, roms: list[PilotBIN]):
        self.rom = roms[0]
        self.parse()

    def parse(self):
        self.rom.parse()
        self['パイロットリスト'].install(self.rom.data)

    def build(self):
        self.rom.build()
