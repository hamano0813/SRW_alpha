#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import Optional

from PySide6.QtCore import Qt, QModelIndex
from PySide6.QtWidgets import QGroupBox, QHBoxLayout, QTabWidget, QFrame, QGridLayout, QLabel, QVBoxLayout

from parameter import EnumData
from structure import SndataBIN, EnlistBIN, AiunpBIN
from structure.specific.enlist_bin import ENLIST_STRUCTURE, ENEMY_STRUCTURE
from structure.specific.aiunp_bin import AI_STRUCTURE
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

        self.init_ui()

    # noinspection PyAttributeOutsideInit
    def init_ui(self):
        scenario = self.init_scenario_table()

        tab_widget = QTabWidget()
        tab_widget.addTab(self.init_enemy_frame(), '敵設定')

        main_layout = QHBoxLayout()
        main_layout.addWidget(scenario)
        main_layout.addWidget(tab_widget)
        self.setLayout(main_layout)

    def init_scenario_table(self):
        group = QGroupBox('シナリオリスト')
        self['シナリオリスト'] = ScenarioTable(self, ('ルート', '話数', '[ステージ]タイトル'))
        self['シナリオリスト'].verticalHeader().setHidden(True)
        group_layout = QHBoxLayout()
        group_layout.addWidget(self['シナリオリスト'])
        group.setLayout(group_layout)
        group.setFixedWidth(447)
        return group

    def init_enemy_frame(self):
        enemy_frame = QFrame()

        self['敵設定'] = ArrayTable(self, '敵設定', {}, stretch=tuple())

        quantity_group = QGroupBox('数量設定')
        self['合計'] = ValueSpin(self['敵設定'], '合計', ENLIST_STRUCTURE['合計'], alignment=Qt.AlignRight)
        self['隊数'] = ValueSpin(self['敵設定'], '隊数', ENLIST_STRUCTURE['隊数'], alignment=Qt.AlignRight)
        quantity_layout = QGridLayout()
        quantity_layout.addWidget(QLabel('合計'), 0, 0, 1, 1)
        quantity_layout.addWidget(self['合計'], 0, 1, 1, 1)
        quantity_layout.addWidget(QLabel('隊数'), 1, 0, 1, 1)
        quantity_layout.addWidget(self['隊数'], 1, 1, 1, 1)

        self['合計'].setReadOnly(True)
        self['隊数'].setReadOnly(True)
        for idx in range(0, 16):
            self[f'隊{idx:02d}'] = ValueSpin(self['敵設定'], f'隊{idx:02d}', ENLIST_STRUCTURE[f'隊{idx:02d}'],
                                            alignment=Qt.AlignRight)
            quantity_layout.addWidget(QLabel(f'隊{idx:02d}'), 0 + idx // 8, 2 + idx % 8 * 2, 1, 1)
            quantity_layout.addWidget(self[f'隊{idx:02d}'], 0 + idx // 8, 3 + idx % 8 * 2, 1, 1)
            # noinspection PyUnresolvedReferences
            self[f'隊{idx:02d}'].valueChanged.connect(self.reset_count)
        quantity_group.setLayout(quantity_layout)

        self['敵リスト'] = ArrayTable(
            self['敵設定'], '敵リスト', {
                'パイロット': RadioCombo(None, 'パイロット', ENEMY_STRUCTURE['パイロット'],
                                    mapping=self.pilot_mapping | {0x0: '一一'}),
                '機体': RadioCombo(None, '機体', ENEMY_STRUCTURE['機体'], mapping=self.robot_mapping),
                '隊号': MappingSpin(None, '隊号', ENEMY_STRUCTURE['隊号'],
                                  mapping=self.group_mapping, alignment=Qt.AlignRight),
                'レベル': ValueSpin(None, 'レベル', ENEMY_STRUCTURE['レベル'], alignment=Qt.AlignRight),
                '機改': MappingSpin(None, '機改', ENEMY_STRUCTURE['機改'],
                                  mapping=self.upgrade_mapping, alignment=Qt.AlignRight),
                '武改': MappingSpin(None, '武改', ENEMY_STRUCTURE['武改'],
                                  mapping=self.upgrade_mapping, alignment=Qt.AlignRight),
                '座標X': ValueSpin(None, '座標X', ENEMY_STRUCTURE['座標X'], alignment=Qt.AlignRight),
                '座標Y': ValueSpin(None, '座標Y', ENEMY_STRUCTURE['座標Y'], alignment=Qt.AlignRight),
                'パーツ': RadioCombo(None, 'パーツ', ENEMY_STRUCTURE['パーツ'], mapping=EnumData.PART),
            }, sortable=False, stretch=(0, 1, 8),
        )
        self['敵リスト'].horizontalHeader().setObjectName('ENLIST')
        self['敵リスト'].horizontalHeader().setMinimumSectionSize(42)

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

            '開始': ValueSpin(None, '開始', AI_STRUCTURE['開始'], alignment=Qt.AlignRight),
            '不明1': ValueSpin(None, '不明1', AI_STRUCTURE['不明1'], alignment=Qt.AlignRight),
            '不明2': ValueSpin(None, '不明2', AI_STRUCTURE['不明2'], alignment=Qt.AlignRight),
            '不明3': ValueSpin(None, '不明3', AI_STRUCTURE['不明3'], alignment=Qt.AlignRight),
            '不明4': ValueSpin(None, '不明4', AI_STRUCTURE['不明4'], alignment=Qt.AlignRight),
            '有効': ValueSpin(None, '有効', AI_STRUCTURE['有効'], alignment=Qt.AlignRight),
        }, sortable=False, stretch=(0, 1), check=(9,))
        self['AIリスト'].horizontalHeader().setObjectName('ENLIST')
        # self['AIリスト'].horizontalHeader().setMinimumSectionSize(57)

        ai_layout = QHBoxLayout()
        ai_layout.addWidget(self['AIリスト'])
        ai_layout.setContentsMargins(0, 0, 0, 0)
        ai_frame.setLayout(ai_layout)

        enemy_tab = QTabWidget()
        enemy_tab.setTabPosition(QTabWidget.South)
        enemy_tab.addTab(ai_frame, '敵AI')
        enemy_tab.addTab(self['敵リスト'], '敵リスト')

        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(quantity_group)
        bottom_layout.addLayout(ButtonLayout(self))

        frame_layout = QVBoxLayout()
        frame_layout.addWidget(enemy_tab)
        frame_layout.addLayout(bottom_layout)
        enemy_frame.setLayout(frame_layout)
        return enemy_frame

    def reset_count(self):
        amout = count = 0
        for idx in range(0, 16):
            if (value := self[f'隊{idx:02d}'].value()) > 0:
                amout += value
                count += 1
        self['合計'].setValue(amout)
        self['隊数'].setValue(count)

    def control_scenario(self, index: QModelIndex):
        if not index.isValid():
            return False
        row = index.row()

        self['AI設定'].control_child(row)
        self['敵設定'].control_child(row)

        return True

    # noinspection PyUnresolvedReferences
    def set_roms(self, roms: list[SndataBIN, EnlistBIN, AiunpBIN]):
        self.sndata_rom, self.enlist_rom, self.aiunp_rom = roms
        self.parse()

        self['AI設定'].install(self.aiunp_rom.data)

        self['敵設定'].install(self.enlist_rom.data)

        self['シナリオリスト'].install(EnumData.SCENARIO)
        self['シナリオリスト'].setRowHidden(0x7E, True)
        self['シナリオリスト'].setRowHidden(0x82, True)
        self['シナリオリスト'].setRowHidden(0x83, True)
        self['シナリオリスト'].setRowHidden(0x84, True)
        self['シナリオリスト'].setRowHidden(0x85, True)
        self['シナリオリスト'].clicked[QModelIndex].connect(self.control_scenario)
        self['シナリオリスト'].selectionModel().currentChanged[QModelIndex, QModelIndex].connect(self.control_scenario)

    def parse(self):
        self.sndata_rom.parse()
        self.enlist_rom.parse()
        self.aiunp_rom.parse()

    def build(self):
        self.sndata_rom.build()
        self.enlist_rom.build()
        self.aiunp_rom.build()
