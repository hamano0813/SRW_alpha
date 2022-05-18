#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QTabWidget, QFrame, QVBoxLayout, QFormLayout

from parameter import EnumData
from structure import SndataBIN, EnlistBIN, AiunpBIN
from structure.specific.aiunp_bin import AI_STRUCTURE
from structure.specific.enlist_bin import ENLIST_STRUCTURE, ENEMY_STRUCTURE
from widget import *


class ScenarioFrame(BackgroundFrame):
    def __init__(self, parent=None, **kwargs):
        super(ScenarioFrame, self).__init__(parent, **kwargs)
        self.sndata_rom: Optional[SndataBIN] = None
        self.enlist_rom: Optional[EnlistBIN] = None
        self.aiunp_rom: Optional[AiunpBIN] = None

        self.robot_mapping = kwargs.get('robots', dict()) | {0x0: '一一'}
        self.pilot_mapping = kwargs.get('pilots', dict()) | {0x7D0: '[7D0]主人公', 0x7D1: '[7D1]恋人', 0x7FA: '[7FA]？？？'}
        self.message_mapping = kwargs.get('messages', dict())
        self.group_mapping = {group: f'{group}' for group in range(0, 16)}
        self.lv_mapping = {lv: f'{lv}' for lv in range(1, 100)}
        self.upgrade_mapping = {upgrade: f'{upgrade}' for upgrade in range(1, 11)} | {0: '一'}
        self.pos_mapping = {pos: f'{pos}' for pos in range(1, 40)} | {0xFF: '一'}
        self.round_mapping = {round: f'{round}' for round in range(1, 20)} | {0: '一'}

        self.init_ui()

    # noinspection PyAttributeOutsideInit
    def init_ui(self):
        scenario = self.init_scenario_table()

        self.tab_widget = QTabWidget()
        self.tab_widget.addTab(self.init_enemy_frame(), '敵設定')
        self.tab_widget.addTab(self.init_ai_frame(), 'AI設定')

        main_layout = QVBoxLayout()
        main_layout.addLayout(scenario)
        main_layout.addWidget(self.tab_widget)
        self.setLayout(main_layout)

    def init_scenario_table(self):
        # noinspection PyTypeChecker
        self['シナリオリスト'] = ScenarioCombo(self)
        self['シナリオリスト'].setFixedWidth(1420)
        layout = QHBoxLayout()
        # layout.addWidget(QLabel('シナリオ'))
        layout.addWidget(self['シナリオリスト'])
        return layout

    def init_enemy_frame(self):
        enemy_frame = QFrame()

        self['敵設定'] = ArrayTable(self, '敵設定', {}, stretch=tuple())

        self['合計'] = ValueSpin(self['敵設定'], '合計', ENLIST_STRUCTURE['合計'], alignment=Qt.AlignRight)
        self['隊数'] = ValueSpin(self['敵設定'], '隊数', ENLIST_STRUCTURE['隊数'], alignment=Qt.AlignRight)
        quantity_layout = QFormLayout()
        quantity_layout.addRow('合計', self['合計'])
        quantity_layout.addRow('隊数', self['隊数'])

        self['合計'].setReadOnly(True)
        self['隊数'].setReadOnly(True)
        for idx in range(0, 16):
            self[f'隊{idx:02d}'] = ValueSpin(self['敵設定'], f'隊{idx:02d}', ENLIST_STRUCTURE[f'隊{idx:02d}'],
                                            alignment=Qt.AlignRight)
            quantity_layout.addRow(f'隊{idx:02d}', self[f'隊{idx:02d}'])
            # noinspection PyUnresolvedReferences
            self[f'隊{idx:02d}'].valueChanged.connect(self.reset_count)

        self['敵リスト'] = ArrayTable(
            self['敵設定'], '敵リスト', {
                'パイロット': RadioCombo(None, 'パイロット', ENEMY_STRUCTURE['パイロット'],
                                    mapping=self.pilot_mapping | {0x0: '一一'}),
                '機体': RadioCombo(None, '機体', ENEMY_STRUCTURE['機体'], mapping=self.robot_mapping),
                '隊号': MappingSpin(None, '隊号', ENEMY_STRUCTURE['隊号'],
                                  mapping=self.group_mapping, alignment=Qt.AlignRight),
                'レベル': ValueSpin(None, 'レベル', ENEMY_STRUCTURE['レベル'], alignment=Qt.AlignRight),
                '機体改造': MappingSpin(None, '機体改造', ENEMY_STRUCTURE['機体改造'],
                                    mapping=self.upgrade_mapping, alignment=Qt.AlignRight),
                '武器改造': MappingSpin(None, '武器改造', ENEMY_STRUCTURE['武器改造'],
                                    mapping=self.upgrade_mapping, alignment=Qt.AlignRight),
                '座標X': ValueSpin(None, '座標X', ENEMY_STRUCTURE['座標X'], alignment=Qt.AlignRight),
                '座標Y': ValueSpin(None, '座標Y', ENEMY_STRUCTURE['座標Y'], alignment=Qt.AlignRight),
                'パーツ': RadioCombo(None, 'パーツ', ENEMY_STRUCTURE['パーツ'], mapping=EnumData.PART),
            }, sortable=False, stretch=(0, 1, 8),
        )
        self['敵リスト'].horizontalHeader().setObjectName('ENLIST')

        enemy_layout = QHBoxLayout()
        enemy_layout.addWidget(self['敵リスト'])
        enemy_layout.addLayout(quantity_layout)
        enemy_frame.setLayout(enemy_layout)
        return enemy_frame

    def init_ai_frame(self):
        ai_frame = QFrame()
        self['AI設定'] = ArrayTable(self, 'AI設定', {}, stretch=tuple())
        self['AIリスト'] = AiTable(self['AI設定'], 'AIリスト', {
            'AI': RadioCombo(None, 'AI', AI_STRUCTURE['AI'], mapping=self.pilot_mapping | {0x0: '一一'}),
            'ターゲット': RadioCombo(None, 'ターゲット', AI_STRUCTURE['ターゲット'],
                                mapping=self.pilot_mapping | {0xFFFF: '一一'}),
            '目標X': MappingSpin(None, '目標X', AI_STRUCTURE['目標X'],
                               mapping=self.pos_mapping, alignment=Qt.AlignRight),
            '目標Y': MappingSpin(None, '目標Y', AI_STRUCTURE['目標Y'],
                               mapping=self.pos_mapping, alignment=Qt.AlignRight),
            '行動開始': MappingSpin(None, '行動開始', AI_STRUCTURE['行動開始'],
                                mapping=self.round_mapping, alignment=Qt.AlignRight),
            '不明1_0': ValueSpin(None, '不明1_0', AI_STRUCTURE['不明1_0'], alignment=Qt.AlignRight),
            '不明1_2': ValueSpin(None, '不明1_2', AI_STRUCTURE['不明1_2'], alignment=Qt.AlignRight),
            '不明1_3': ValueSpin(None, '不明1_3', AI_STRUCTURE['不明1_3'], alignment=Qt.AlignRight),
            '不明1_4': ValueSpin(None, '不明1_4', AI_STRUCTURE['不明1_4'], alignment=Qt.AlignRight),
            '不明1_5': ValueSpin(None, '不明1_5', AI_STRUCTURE['不明1_5'], alignment=Qt.AlignRight),
            '不明1_6': ValueSpin(None, '不明1_6', AI_STRUCTURE['不明1_6'], alignment=Qt.AlignRight),
            '不明1_7': ValueSpin(None, '不明1_7', AI_STRUCTURE['不明1_7'], alignment=Qt.AlignRight),
            '不明3_0': ValueSpin(None, '不明3_0', AI_STRUCTURE['不明3_0'], alignment=Qt.AlignRight),
            '不明3_1': ValueSpin(None, '不明3_1', AI_STRUCTURE['不明3_1'], alignment=Qt.AlignRight),
            '不明3_2': ValueSpin(None, '不明3_2', AI_STRUCTURE['不明3_2'], alignment=Qt.AlignRight),
            '不明3_4': ValueSpin(None, '不明3_4', AI_STRUCTURE['不明3_4'], alignment=Qt.AlignRight),
            '不明4_4': ValueSpin(None, '不明4_4', AI_STRUCTURE['不明4_4'], alignment=Qt.AlignRight),
            '不明4_5': ValueSpin(None, '不明4_5', AI_STRUCTURE['不明4_5'], alignment=Qt.AlignRight),
            '不明4_6': ValueSpin(None, '不明4_6', AI_STRUCTURE['不明4_6'], alignment=Qt.AlignRight),
            '不明4_7': ValueSpin(None, '不明4_7', AI_STRUCTURE['不明4_7'], alignment=Qt.AlignRight),
            '有効': ValueSpin(None, '有効', AI_STRUCTURE['有効'], alignment=Qt.AlignRight),
        }, check=(5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20),
                                sortable=False, stretch=(0, 1), )

        self['AIリスト'].horizontalHeader().setObjectName('ENLIST')
        self['AIリスト'].horizontalHeader().setMinimumSectionSize(56)

        ai_layout = QHBoxLayout()
        ai_layout.addWidget(self['AIリスト'])
        ai_frame.setLayout(ai_layout)
        return ai_frame

    def reset_count(self):
        amout = count = 0
        for idx in range(0, 16):
            if (value := self[f'隊{idx:02d}'].value()) > 0:
                amout += value
                count += 1
        self['合計'].setValue(amout)
        self['隊数'].setValue(count)

    def control_scenario(self, index: int):
        self['敵設定'].control_child(index)
        self['AI設定'].control_child(index)

        return True

    # noinspection PyUnresolvedReferences
    def set_roms(self, roms: list[SndataBIN, EnlistBIN, AiunpBIN]):
        self.sndata_rom, self.enlist_rom, self.aiunp_rom = roms
        self.parse()

        self['敵設定'].install(self.enlist_rom.data)
        self['AI設定'].install(self.aiunp_rom.data)

        self['シナリオリスト'].currentIndexChanged[int].connect(self.control_scenario)

    def parse(self):
        self.sndata_rom.parse()
        self.enlist_rom.parse()
        self.aiunp_rom.parse()

    def build(self):
        self.sndata_rom.build()
        self.enlist_rom.build()
        self.aiunp_rom.build()
