#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QLabel, QLineEdit, QGroupBox, QHBoxLayout, QVBoxLayout, QFormLayout, QGridLayout,
                               QSizePolicy, QSpacerItem)

from parameter.enum_data import EnumData
from structure import RobotRAF
from structure.specific.robot_raf import ROBOT_STRUCTURE, WEAPON_STRUCTURE
from widget import *


class RobotFrame(BackgroundFrame):
    def __init__(self, parent=None, **kwargs):
        super(RobotFrame, self).__init__(parent, **kwargs)
        self.rom: Optional[RobotRAF] = None
        self.init_ui()
        self.robots = kwargs.get('robots', dict())

    def init_ui(self):
        robot_table = self.init_robot_table()
        robot_data = self.init_robot_data()
        robot_special = self.init_robot_special()
        robot_transfer = self.init_robot_transfer()
        robot_skill = self.init_robot_skill()
        robot_bgm = self.init_robot_bgm()

        weapon_table = self.init_weapon_table()
        weapon_data = self.init_weapon_data()
        weapon_map = self.init_weapon_map()
        weapon_adaptation = self.init_weapon_adaptation()

        robot_table.setFixedWidth(630)
        robot_data.setFixedWidth(135)
        weapon_adaptation.setFixedWidth(135)

        top_left_layout = QHBoxLayout()
        top_left_layout.addWidget(robot_data)
        top_left_layout.addWidget(robot_special)

        top_right_layout = QGridLayout()
        top_right_layout.addWidget(robot_transfer, 0, 0, 1, 1)
        top_right_layout.addWidget(robot_skill, 0, 1, 1, 1)
        top_right_layout.addWidget(robot_bgm, 1, 0, 1, 2)

        bottom_right_layout = QGridLayout()
        bottom_right_layout.addWidget(weapon_data, 0, 0, 1, 2)
        bottom_right_layout.addWidget(weapon_map, 1, 0, 2, 1)
        bottom_right_layout.addWidget(weapon_adaptation, 1, 1, 1, 1)

        main_layout = QHBoxLayout()
        grid_layout = QGridLayout()
        grid_layout.addLayout(top_left_layout, 0, 0, 1, 1)
        grid_layout.addLayout(top_right_layout, 0, 1, 1, 1)
        grid_layout.addWidget(weapon_table, 1, 0, 1, 1)
        grid_layout.addLayout(bottom_right_layout, 1, 1, 1, 1)
        main_layout.addWidget(robot_table)
        main_layout.addLayout(grid_layout)
        main_layout.addStretch()

        self.setLayout(main_layout)

    def init_robot_table(self):
        group = QGroupBox('機体リスト')
        self['機体リスト'] = ArrayTable(
            self, '機体リスト', {
                '機体': TextLine(None, '機体', ROBOT_STRUCTURE['機体']),
                'ＨＰ': ValueSpin(None, 'ＨＰ', ROBOT_STRUCTURE['ＨＰ'], alignment=Qt.AlignRight),
                'ＥＮ': ValueSpin(None, 'ＥＮ', ROBOT_STRUCTURE['ＥＮ'], alignment=Qt.AlignRight),
                '運動性': ValueSpin(None, '運動性', ROBOT_STRUCTURE['運動性'], alignment=Qt.AlignRight),
                '装甲': ValueSpin(None, '装甲', ROBOT_STRUCTURE['装甲'], alignment=Qt.AlignRight),
                '限界': ValueSpin(None, '限界', ROBOT_STRUCTURE['限界'], alignment=Qt.AlignRight),
            },
        )
        filter_line = QLineEdit()
        filter_layout = QHBoxLayout()
        filter_layout.addWidget(QLabel('機体検索'))
        filter_layout.addWidget(filter_line)
        group_layout = QVBoxLayout()
        group_layout.addWidget(self['機体リスト'])
        group_layout.addLayout(filter_layout)
        group.setLayout(group_layout)
        filter_line.textChanged[str].connect(self['機体リスト'].filterChanged)
        return group

    def init_robot_data(self):
        group = QGroupBox('機体データ')
        self['タイプ'] = CheckCombo(self['機体リスト'], 'タイプ', ROBOT_STRUCTURE['タイプ'],
                                 EnumData.ROBOT['タイプ'])
        self['移動力'] = ValueSpin(self['機体リスト'], '移動力', ROBOT_STRUCTURE['移動力'])
        self['空適応'] = MappingSpin(self['機体リスト'], '空適応', ROBOT_STRUCTURE['空適応'],
                                  EnumData.ROBOT['適応'])
        self['陸適応'] = MappingSpin(self['機体リスト'], '陸適応', ROBOT_STRUCTURE['陸適応'],
                                  EnumData.ROBOT['適応'])
        self['海適応'] = MappingSpin(self['機体リスト'], '海適応', ROBOT_STRUCTURE['海適応'],
                                  EnumData.ROBOT['適応'])
        self['宇適応'] = MappingSpin(self['機体リスト'], '宇適応', ROBOT_STRUCTURE['宇適応'],
                                  EnumData.ROBOT['適応'])
        self['サイズ'] = MappingSpin(self['機体リスト'], 'サイズ', ROBOT_STRUCTURE['サイズ'],
                                  EnumData.ROBOT['サイズ'])
        self['パーツ'] = ValueSpin(self['機体リスト'], 'パーツ', ROBOT_STRUCTURE['パーツ'])
        form_layout = QFormLayout()
        form_layout.addRow('移動力', self['移動力'])
        form_layout.addRow('サイズ', self['サイズ'])
        form_layout.addRow('パーツ', self['パーツ'])
        form_layout.addRow('空適応', self['空適応'])
        form_layout.addRow('陸適応', self['陸適応'])
        form_layout.addRow('海適応', self['海適応'])
        form_layout.addRow('宇適応', self['宇適応'])

        group_layout = QVBoxLayout()
        group_layout.addWidget(QLabel('タイプ'))
        group_layout.addWidget(self['タイプ'])
        group_layout.addLayout(form_layout)
        group_layout.addStretch()
        group.setLayout(group_layout)
        return group

    def init_robot_special(self):
        group = QGroupBox('機体スペシャル')
        self['变形チーム'] = ValueSpin(self['機体リスト'], '变形チーム', ROBOT_STRUCTURE['变形チーム'], )
        self['变形番号'] = ValueSpin(self['機体リスト'], '变形番号', ROBOT_STRUCTURE['变形番号'])
        self['合体チーム'] = ValueSpin(self['機体リスト'], '合体チーム', ROBOT_STRUCTURE['合体チーム'])
        self['合体番号'] = ValueSpin(self['機体リスト'], '合体番号', ROBOT_STRUCTURE['合体番号'])
        self['合体数'] = ValueSpin(self['機体リスト'], '合体数', ROBOT_STRUCTURE['合体数'])
        self['分離機体'] = RadioCombo(self['機体リスト'], '分離機体', ROBOT_STRUCTURE['分離機体'],
                                  mapping=self.kwargs.get('robots', dict()) | {0xFFFF: '一一'})
        self['換装システム'] = RadioCombo(self['機体リスト'], '換装システム', ROBOT_STRUCTURE['換装システム'],
                                    mapping=EnumData.ROBOT['換装システム'])
        self['修理費'] = ValueSpin(self['機体リスト'], '修理費', ROBOT_STRUCTURE['修理費'])
        self['資金'] = ValueSpin(self['機体リスト'], '資金', ROBOT_STRUCTURE['資金'])
        group_layout = QGridLayout()
        group_layout.addWidget(QLabel('变形グループ'), 0, 0, 1, 1)
        group_layout.addWidget(self['变形チーム'], 0, 1, 1, 1)
        group_layout.addWidget(self['变形番号'], 0, 2, 1, 1)
        group_layout.addWidget(QLabel('合体グループ'), 1, 0, 1, 1)
        group_layout.addWidget(self['合体チーム'], 1, 1, 1, 1)
        group_layout.addWidget(self['合体番号'], 1, 2, 1, 1)
        group_layout.addWidget(QLabel('合体数'), 2, 0, 1, 1)
        group_layout.addWidget(self['合体数'], 2, 1, 1, 1)
        group_layout.addWidget(QLabel('分離機体'), 3, 0, 1, 4)
        group_layout.addWidget(self['分離機体'], 4, 0, 1, 4)
        group_layout.addWidget(QLabel('換装システム'), 5, 0, 1, 4)
        group_layout.addWidget(self['換装システム'], 6, 0, 1, 4)
        group_layout.addWidget(QLabel('資金'), 7, 0, 1, 1)
        group_layout.addWidget(self['資金'], 7, 1, 1, 3)
        group_layout.addWidget(QLabel('修理費'), 8, 0, 1, 1)
        group_layout.addWidget(self['修理費'], 8, 1, 1, 3)
        group_layout.addItem(QSpacerItem(1, 1, QSizePolicy.Fixed, QSizePolicy.Expanding), 9, 0, 1, 1)
        group.setLayout(group_layout)
        return group

    def init_robot_transfer(self):
        group = QGroupBox('乗り換え系')
        self['乗り換え系'] = CheckList(self['機体リスト'], '乗り換え系', ROBOT_STRUCTURE['乗り換え系'],
                                  EnumData.ROBOT['乗り換え系'])
        group_layout = QVBoxLayout()
        group_layout.addWidget(self['乗り換え系'])
        group.setLayout(group_layout)
        return group

    def init_robot_skill(self):
        group = QGroupBox('機体特性')
        self['特性'] = CheckList(self['機体リスト'], '特性', ROBOT_STRUCTURE['特性'],
                               item_list=EnumData.ROBOT['特性'])
        group_layout = QHBoxLayout()
        group_layout.addWidget(self['特性'])
        group.setLayout(group_layout)
        return group

    def init_robot_bgm(self):
        group = QGroupBox('機体音楽')
        self['機体BGM'] = RadioCombo(self['機体リスト'], '機体BGM', ROBOT_STRUCTURE['機体BGM'],
                                   mapping={k: f'[{k:02X}] {v}' for k, v in EnumData.MUSIC.items()})
        self['機体BGM'].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        group_layout = QGridLayout()
        group_layout.addWidget(QLabel('ＢＧＭ'), 0, 0, 1, 1)
        group_layout.addWidget(self['機体BGM'], 0, 1, 1, 6)

        group.setLayout(group_layout)
        return group

    def init_weapon_table(self):
        group = QGroupBox('武器リスト')
        self['武器リスト'] = ArrayTable(
            self['機体リスト'], '武器リスト', {
                '武器': TextLine(None, '武器', WEAPON_STRUCTURE['武器']),
                '分類': MappingSpin(None, '分類', WEAPON_STRUCTURE['分類'], EnumData.WEAPON['分類'], alignment=Qt.AlignRight),
                '攻撃力': ValueSpin(None, '攻撃力', WEAPON_STRUCTURE['攻撃力'], alignment=Qt.AlignRight),
            },
        )
        group_layout = QVBoxLayout()
        group_layout.addWidget(self['武器リスト'])
        group.setLayout(group_layout)
        group.setFixedSize(390, 480)
        return group

    def init_weapon_data(self):
        group = QGroupBox('武器データ')
        self['属性'] = CheckCombo(self['武器リスト'], '属性', WEAPON_STRUCTURE['属性'],
                                item_list=EnumData.WEAPON['属性'], dummy='')
        self['近射程'] = ValueSpin(self['武器リスト'], '近射程', WEAPON_STRUCTURE['近射程'])
        self['遠射程'] = ValueSpin(self['武器リスト'], '遠射程', WEAPON_STRUCTURE['遠射程'])
        self['命中'] = ValueSpin(self['武器リスト'], '命中', WEAPON_STRUCTURE['命中'])
        self['ＣＴ'] = ValueSpin(self['武器リスト'], 'ＣＴ', WEAPON_STRUCTURE['ＣＴ'])
        self['ニュータイプ'] = ValueSpin(self['武器リスト'], 'ニュータイプ', WEAPON_STRUCTURE['ニュータイプ'])
        self['聖戦士'] = ValueSpin(self['武器リスト'], '聖戦士', WEAPON_STRUCTURE['聖戦士'])
        self['気力'] = ValueSpin(self['武器リスト'], '気力', WEAPON_STRUCTURE['気力'])
        self['改造タイプ'] = MappingSpin(self['武器リスト'], '改造タイプ', WEAPON_STRUCTURE['改造タイプ'],
                                    mapping=EnumData.WEAPON['改造タイプ'])
        self['改造追加'] = MappingSpin(self['武器リスト'], '改造追加', WEAPON_STRUCTURE['改造追加'],
                                   mapping={i: f'[{i:X}]' for i in range(0x10)})
        self['初期弾数'] = ValueSpin(self['武器リスト'], '初期弾数', WEAPON_STRUCTURE['初期弾数'])
        self['最大弾数'] = ValueSpin(self['武器リスト'], '最大弾数', WEAPON_STRUCTURE['最大弾数'])
        self['ＥＮ'] = ValueSpin(self['武器リスト'], 'ＥＮ', WEAPON_STRUCTURE['ＥＮ'])

        group_layout = QGridLayout()
        group_layout.addWidget(QLabel('属性'), 0, 0, 1, 1)
        group_layout.addWidget(self['属性'], 0, 1, 1, 5)

        group_layout.addWidget(QLabel('近射程'), 1, 0, 1, 1)
        group_layout.addWidget(self['近射程'], 1, 1, 1, 1)
        group_layout.addWidget(QLabel('遠射程'), 2, 0, 1, 1)
        group_layout.addWidget(self['遠射程'], 2, 1, 1, 1)
        group_layout.addWidget(QLabel('命中'), 3, 0, 1, 1)
        group_layout.addWidget(self['命中'], 3, 1, 1, 1)
        group_layout.addWidget(QLabel('ＣＴ'), 4, 0, 1, 1)
        group_layout.addWidget(self['ＣＴ'], 4, 1, 1, 1)

        group_layout.addWidget(QLabel('初期弾数'), 1, 2, 1, 1)
        group_layout.addWidget(self['初期弾数'], 1, 3, 1, 1)
        group_layout.addWidget(QLabel('最大弾数'), 2, 2, 1, 1)
        group_layout.addWidget(self['最大弾数'], 2, 3, 1, 1)
        group_layout.addWidget(QLabel('改造タイプ'), 3, 2, 1, 1)
        group_layout.addWidget(self['改造タイプ'], 3, 3, 1, 1)
        group_layout.addWidget(QLabel('改造追加'), 4, 2, 1, 1)
        group_layout.addWidget(self['改造追加'], 4, 3, 1, 1)

        group_layout.addWidget(QLabel('ＥＮ'), 1, 4, 1, 1)
        group_layout.addWidget(self['ＥＮ'], 1, 5, 1, 1)
        group_layout.addWidget(QLabel('気力'), 2, 4, 1, 1)
        group_layout.addWidget(self['気力'], 2, 5, 1, 1)
        group_layout.addWidget(QLabel('ニュータイプ'), 3, 4, 1, 1)
        group_layout.addWidget(self['ニュータイプ'], 3, 5, 1, 1)
        group_layout.addWidget(QLabel('聖戦士'), 4, 4, 1, 1)
        group_layout.addWidget(self['聖戦士'], 4, 5, 1, 1)

        group.setLayout(group_layout)
        return group

    def init_weapon_map(self):
        group = QGroupBox('マップ武器')
        self['マップ分類'] = RadioCombo(self['武器リスト'], 'マップ分類', WEAPON_STRUCTURE['マップ分類'],
                                   mapping=EnumData.WEAPON['マップ分類'])
        self['マップ演出'] = ValueSpin(self['武器リスト'], 'マップ演出', WEAPON_STRUCTURE['マップ演出'])
        self['着弾点指定型攻撃半径'] = ValueSpin(self['武器リスト'], '着弾点指定型攻撃半径', WEAPON_STRUCTURE['着弾点指定型攻撃半径'])
        self['方向指定型範囲'] = RangeCombo(self['武器リスト'], '方向指定型範囲', WEAPON_STRUCTURE['方向指定型範囲'])

        self['マップ分類'].currentIndexChanged.connect(self.switch_maptype)
        self['マップ演出'].setFixedSize(60, 28)
        self['着弾点指定型攻撃半径'].setFixedSize(60, 28)

        group_layout = QGridLayout()
        group_layout.setObjectName('weapon_map')
        group_layout.addWidget(QLabel('分類'), 0, 0, 1, 2)
        group_layout.addWidget(self['マップ分類'], 1, 0, 1, 2)
        group_layout.addWidget(QLabel('演出'), 2, 0, 1, 1)
        group_layout.addWidget(self['マップ演出'], 2, 1, 1, 1)
        group_layout.addWidget(QLabel('着弾点指定型攻撃半径'), 3, 0, 1, 1)
        group_layout.addWidget(self['着弾点指定型攻撃半径'], 3, 1, 1, 1)
        group_layout.addWidget(QLabel('方向指定型範囲'), 4, 0, 1, 1)
        group_layout.addWidget(self['方向指定型範囲'], 5, 0, 1, 2)
        group_layout.addItem(QSpacerItem(1, 1, QSizePolicy.Fixed, QSizePolicy.Expanding), 6, 0, 1, 2)
        group.setLayout(group_layout)
        return group

    def init_weapon_adaptation(self):
        group = QGroupBox('武器適応')
        self['空'] = MappingSpin(self['武器リスト'], '空適応', WEAPON_STRUCTURE['空適応'], EnumData.WEAPON['適応'])
        self['陸'] = MappingSpin(self['武器リスト'], '陸適応', WEAPON_STRUCTURE['陸適応'], EnumData.WEAPON['適応'])
        self['海'] = MappingSpin(self['武器リスト'], '海適応', WEAPON_STRUCTURE['海適応'], EnumData.WEAPON['適応'])
        self['宇'] = MappingSpin(self['武器リスト'], '宇適応', WEAPON_STRUCTURE['宇適応'], EnumData.WEAPON['適応'])
        group_layout = QFormLayout()
        group_layout.addRow('空適応', self['空'])
        group_layout.addRow('陸適応', self['陸'])
        group_layout.addRow('海適応', self['海'])
        group_layout.addRow('宇適応', self['宇'])
        group.setLayout(group_layout)
        return group

    def switch_maptype(self):
        layout: QGridLayout = self.findChild(QGridLayout, 'weapon_map')
        if self['マップ分類'].currentIndex() == 0:
            layout.itemAtPosition(2, 0).widget().setHidden(True)
            layout.itemAtPosition(3, 0).widget().setHidden(True)
            layout.itemAtPosition(4, 0).widget().setHidden(True)
            self['マップ演出'].setHidden(True)
            self['着弾点指定型攻撃半径'].setHidden(True)
            self['方向指定型範囲'].setHidden(True)
        elif self['マップ分類'].currentIndex() == 1:
            layout.itemAtPosition(2, 0).widget().setHidden(False)
            layout.itemAtPosition(3, 0).widget().setHidden(True)
            layout.itemAtPosition(4, 0).widget().setHidden(False)
            self['マップ演出'].setHidden(False)
            self['着弾点指定型攻撃半径'].setHidden(True)
            self['方向指定型範囲'].setHidden(False)
        elif self['マップ分類'].currentIndex() == 2:
            layout.itemAtPosition(2, 0).widget().setHidden(False)
            layout.itemAtPosition(3, 0).widget().setHidden(True)
            layout.itemAtPosition(4, 0).widget().setHidden(True)
            self['マップ演出'].setHidden(False)
            self['着弾点指定型攻撃半径'].setHidden(True)
            self['方向指定型範囲'].setHidden(True)
        elif self['マップ分類'].currentIndex() == 3:
            layout.itemAtPosition(2, 0).widget().setHidden(False)
            layout.itemAtPosition(3, 0).widget().setHidden(False)
            layout.itemAtPosition(4, 0).widget().setHidden(True)
            self['マップ演出'].setHidden(False)
            self['着弾点指定型攻撃半径'].setHidden(False)
            self['方向指定型範囲'].setHidden(True)

    def set_roms(self, roms: list[RobotRAF]):
        self.rom = roms[0]
        self.parse()

    def parse(self):
        self.rom.parse()
        self['分離機体'].init_mapping(self.robots | {0xFFFF: 'ーー'})
        self['機体リスト'].install(self.rom.data)
        self.switch_maptype()

    def build(self):
        self.rom.build()
