#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import Optional

from PySide6.QtCore import Qt, QModelIndex
from PySide6.QtWidgets import QGroupBox, QHBoxLayout, QTabWidget, QFormLayout, QFrame

from structure import SndataBIN, EnlistBIN, AiunpBIN
from structure.specific.enlist_bin import ENLIST_STRUCTURE, ENEMY_STRUCTURE
from widget import *
from parameter import EnumData


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
        self['敵合計'] = ValueSpin(self['敵設定'], '敵合計', ENLIST_STRUCTURE['敵合計'], alignment=Qt.AlignRight)
        self['バッチ数'] = ValueSpin(self['敵設定'], 'バッチ数', ENLIST_STRUCTURE['バッチ数'], alignment=Qt.AlignRight)
        self['バッチ00'] = ValueSpin(self['敵設定'], 'バッチ00', ENLIST_STRUCTURE['バッチ00'], alignment=Qt.AlignRight)
        self['バッチ01'] = ValueSpin(self['敵設定'], 'バッチ01', ENLIST_STRUCTURE['バッチ01'], alignment=Qt.AlignRight)
        self['バッチ02'] = ValueSpin(self['敵設定'], 'バッチ02', ENLIST_STRUCTURE['バッチ02'], alignment=Qt.AlignRight)
        self['バッチ03'] = ValueSpin(self['敵設定'], 'バッチ03', ENLIST_STRUCTURE['バッチ03'], alignment=Qt.AlignRight)
        self['バッチ04'] = ValueSpin(self['敵設定'], 'バッチ04', ENLIST_STRUCTURE['バッチ04'], alignment=Qt.AlignRight)
        self['バッチ05'] = ValueSpin(self['敵設定'], 'バッチ05', ENLIST_STRUCTURE['バッチ05'], alignment=Qt.AlignRight)
        self['バッチ06'] = ValueSpin(self['敵設定'], 'バッチ06', ENLIST_STRUCTURE['バッチ06'], alignment=Qt.AlignRight)
        self['バッチ07'] = ValueSpin(self['敵設定'], 'バッチ07', ENLIST_STRUCTURE['バッチ07'], alignment=Qt.AlignRight)
        self['バッチ08'] = ValueSpin(self['敵設定'], 'バッチ08', ENLIST_STRUCTURE['バッチ08'], alignment=Qt.AlignRight)
        self['バッチ09'] = ValueSpin(self['敵設定'], 'バッチ09', ENLIST_STRUCTURE['バッチ09'], alignment=Qt.AlignRight)
        self['バッチ10'] = ValueSpin(self['敵設定'], 'バッチ10', ENLIST_STRUCTURE['バッチ10'], alignment=Qt.AlignRight)
        self['バッチ11'] = ValueSpin(self['敵設定'], 'バッチ11', ENLIST_STRUCTURE['バッチ11'], alignment=Qt.AlignRight)
        self['バッチ12'] = ValueSpin(self['敵設定'], 'バッチ12', ENLIST_STRUCTURE['バッチ12'], alignment=Qt.AlignRight)
        self['バッチ13'] = ValueSpin(self['敵設定'], 'バッチ13', ENLIST_STRUCTURE['バッチ13'], alignment=Qt.AlignRight)
        self['バッチ14'] = ValueSpin(self['敵設定'], 'バッチ14', ENLIST_STRUCTURE['バッチ14'], alignment=Qt.AlignRight)
        self['バッチ15'] = ValueSpin(self['敵設定'], 'バッチ15', ENLIST_STRUCTURE['バッチ15'], alignment=Qt.AlignRight)
        quantity_layout = QFormLayout()
        quantity_layout.addRow('敵合計', self['敵合計'])
        quantity_layout.addRow('バッチ数', self['バッチ数'])
        for idx in range(0, 16):
            quantity_layout.addRow(f'バッチ{idx:02d}', self[f'バッチ{idx:02d}'])
        quantity_group.setLayout(quantity_layout)
        quantity_group.setFixedWidth(120)

        enemy_group = QGroupBox('敵リスト')
        self['敵リスト'] = ArrayTable(
            self['敵設定'], '敵リスト', {
                '機体': RadioCombo(None, '機体', ENEMY_STRUCTURE['機体'], mapping=self.robots),
                '機改': ValueSpin(None, '機改', ENEMY_STRUCTURE['機改'], alignment=Qt.AlignRight),
                '武改': ValueSpin(None, '武改', ENEMY_STRUCTURE['武改'], alignment=Qt.AlignRight),
                'パイロット': RadioCombo(None, 'パイロット', ENEMY_STRUCTURE['パイロット'], mapping=self.pilots),
                'レベル': ValueSpin(None, 'レベル', ENEMY_STRUCTURE['レベル'], alignment=Qt.AlignRight),
                '座標X': ValueSpin(None, '座標X', ENEMY_STRUCTURE['座標X'], alignment=Qt.AlignRight),
                '座標Y': ValueSpin(None, '座標Y', ENEMY_STRUCTURE['座標Y'], alignment=Qt.AlignRight),
                'パーツ': RadioCombo(None, 'パーツ', ENEMY_STRUCTURE['パーツ'], mapping=EnumData.PART),
                'バッチ': ValueSpin(None, 'バッチ', ENEMY_STRUCTURE['バッチ'], alignment=Qt.AlignRight),
            }, sortable=False, resizeRows=True, resizeColumns=False, stretch=tuple(),
        )
        self['敵リスト'].horizontalHeader().setObjectName('ENLIST')
        self['敵リスト'].horizontalHeader().setMinimumSectionSize(40)

        enemy_layout = QHBoxLayout()
        enemy_layout.addWidget(self['敵リスト'])
        enemy_group.setLayout(enemy_layout)

        frame_layout = QHBoxLayout()
        frame_layout.addWidget(quantity_group)
        frame_layout.addWidget(enemy_group)
        enemy_frame.setLayout(frame_layout)
        return enemy_frame

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
        self['シナリオリスト'].clicked[QModelIndex].connect(self.control_scenario)
        self['シナリオリスト'].selectionModel().currentChanged[QModelIndex, QModelIndex].connect(self.control_scenario)
        for idx, width in enumerate([210, 40, 40, 150, 40, 40, 40, 130, 40]):
            self['敵リスト'].setColumnWidth(idx, width)

    def parse(self):
        self.sndata_rom.parse()
        self.enlist_rom.parse()
        self.aiunp_rom.parse()

    def build(self):
        self.sndata_rom.build()
        self.enlist_rom.build()
        self.aiunp_rom.build()
