#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import Optional

from PySide6.QtCore import Qt, QModelIndex
from PySide6.QtWidgets import QGroupBox, QHBoxLayout, QTabWidget, QFrame, QGridLayout, QLabel, QVBoxLayout

from parameter import EnumData
from structure import SndataBIN, EnlistBIN, AiunpBIN
from structure.specific.enlist_bin import ENLIST_STRUCTURE, ENEMY_STRUCTURE
from widget import *


class ScenarioFrame(BackgroundFrame):
    def __init__(self, parent=None, **kwargs):
        super(ScenarioFrame, self).__init__(parent, **kwargs)
        self.sndata_rom: Optional[SndataBIN] = None
        self.enlist_rom: Optional[EnlistBIN] = None
        self.aiunp_rom: Optional[AiunpBIN] = None

        self.robots = kwargs.get('robots', dict()) | {0x0: '一一'}
        self.pilots = kwargs.get('pilots', dict()) | {0: '一一', 0x7D0: '[7D0]主人公', 0x7D1: '[7D1]恋人', 0x7FA: '[7FA]？？？'}
        self.messages = kwargs.get('messages', dict())

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
            self[f'隊{idx:02d}'].valueChanged.connect(self.reset_count)
        quantity_group.setLayout(quantity_layout)

        self['敵リスト'] = ArrayTable(
            self['敵設定'], '敵リスト', {
                'パイロット': RadioCombo(None, 'パイロット', ENEMY_STRUCTURE['パイロット'], mapping=self.pilots),
                '機体': RadioCombo(None, '機体', ENEMY_STRUCTURE['機体'], mapping=self.robots),
                '隊号': ValueSpin(None, '隊号', ENEMY_STRUCTURE['隊号'], alignment=Qt.AlignRight),
                'レベル': ValueSpin(None, 'レベル', ENEMY_STRUCTURE['レベル'], alignment=Qt.AlignRight),
                '機改': ValueSpin(None, '機改', ENEMY_STRUCTURE['機改'], alignment=Qt.AlignRight),
                '武改': ValueSpin(None, '武改', ENEMY_STRUCTURE['武改'], alignment=Qt.AlignRight),
                '座標X': ValueSpin(None, '座標X', ENEMY_STRUCTURE['座標X'], alignment=Qt.AlignRight),
                '座標Y': ValueSpin(None, '座標Y', ENEMY_STRUCTURE['座標Y'], alignment=Qt.AlignRight),
                'パーツ': RadioCombo(None, 'パーツ', ENEMY_STRUCTURE['パーツ'], mapping=EnumData.PART),
            }, sortable=False, stretch=(0, 1, 8),
        )
        self['敵リスト'].horizontalHeader().setObjectName('ENLIST')
        self['敵リスト'].horizontalHeader().setMinimumSectionSize(40)

        enemy_tab = QTabWidget()
        enemy_tab.setTabPosition(QTabWidget.South)
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

        self['敵設定'].control_child(row)

        return True

    # noinspection PyUnresolvedReferences
    def set_roms(self, roms: list[SndataBIN, EnlistBIN, AiunpBIN]):
        self.sndata_rom, self.enlist_rom, self.aiunp_rom = roms
        self.parse()

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
