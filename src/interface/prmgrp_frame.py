#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy
from typing import Optional

from PySide6.QtCore import Qt, QModelIndex
from PySide6.QtWidgets import QGroupBox, QHBoxLayout, QLabel, QVBoxLayout, QTabWidget, QFrame

from parameter.enum_data import EnumData
from structure import PrmgrpBIN
from structure.specific.prmgrp_bin import (SPECIAL_STRUCTURE, ZODIAC_STRUCTURE, BLOOD_STRUCTURE, PART_STRUCTURE,
                                           UPGRADE_STRUCTURE)
from widget import *


class PrmgrpFrame(BackgroundFrame):
    def __init__(self, parent=None, **kwargs):
        super(PrmgrpFrame, self).__init__(parent, **kwargs)
        self.rom: Optional[PrmgrpBIN] = None
        self.skill_mapping = {idx: f' {idx:02d}.{skill}' for idx, skill in enumerate(EnumData.PILOT['特殊技能'][:8])}
        self.spirit_sequence = [{'精神': spirit} for spirit in EnumData.SPIRIT.values()][:-1]
        self.part_sequence = [{'パーツ': part} for part in EnumData.PART.values()][1:]
        self.lv_mapping = {lv: f'{lv}' for lv in range(1, 100)}
        self.month_mapping = {month: f'{month}' for month in range(1, 13)}
        self.day_mapping = {day: f'{day}' for day in range(1, 32)}

        self.init_ui()

    def init_ui(self):
        tab_widget = QTabWidget()

        tab_widget.addTab(self.init_upgrade_frame(), '改造')
        tab_widget.addTab(self.init_birthday_frame(), '誕生日')
        tab_widget.addTab(self.init_sppart_frame(), '精神消費＆パーツ属性')

        main_layout = QHBoxLayout()
        main_layout.addWidget(tab_widget)
        self.setLayout(main_layout)

    def init_upgrade_frame(self):
        frame = QFrame()

        robot_group = QGroupBox('機体改造')

        self['ＨＰ改造'] = ArrayTable(
            self, 'ＨＰ改造', {
                '費用': ValueSpin(None, '費用', UPGRADE_STRUCTURE['ＨＰ改造']['費用'], alignment=Qt.AlignRight),
                '上昇値': ValueSpin(None, '上昇値', UPGRADE_STRUCTURE['ＨＰ改造']['上昇値'], alignment=Qt.AlignRight),
            }, sortable=False, stretch=tuple(), corner='   ＨＰ',
        )
        self['ＨＰ改造'].verticalHeader().setFixedWidth(60)
        self['ＨＰ改造'].setFixedSize(206, 293)

        self['ＥＮ改造'] = ArrayTable(
            self, 'ＥＮ改造', {
                '費用': ValueSpin(None, '費用', UPGRADE_STRUCTURE['ＥＮ改造']['費用'], alignment=Qt.AlignRight),
                '上昇値': ValueSpin(None, '上昇値', UPGRADE_STRUCTURE['ＥＮ改造']['上昇値'], alignment=Qt.AlignRight),
            }, sortable=False, stretch=tuple(), corner='   ＥＮ',
        )
        self['ＥＮ改造'].verticalHeader().setFixedWidth(60)
        self['ＥＮ改造'].setFixedSize(206, 293)

        self['運動改造'] = ArrayTable(
            self, '運動改造', {
                '費用': ValueSpin(None, '費用', UPGRADE_STRUCTURE['運動改造']['費用'], alignment=Qt.AlignRight),
                '上昇値': ValueSpin(None, '上昇値', UPGRADE_STRUCTURE['運動改造']['上昇値'], alignment=Qt.AlignRight),
            }, sortable=False, stretch=tuple(), corner='   運動',
        )
        self['運動改造'].verticalHeader().setFixedWidth(60)
        self['運動改造'].setFixedSize(206, 293)

        self['装甲改造'] = ArrayTable(
            self, '装甲改造', {
                '費用': ValueSpin(None, '費用', UPGRADE_STRUCTURE['装甲改造']['費用'], alignment=Qt.AlignRight),
                '上昇値': ValueSpin(None, '上昇値', UPGRADE_STRUCTURE['装甲改造']['上昇値'], alignment=Qt.AlignRight),
            }, sortable=False, stretch=tuple(), corner='   装甲',
        )
        self['装甲改造'].verticalHeader().setFixedWidth(60)
        self['装甲改造'].setFixedSize(206, 293)

        self['限界改造'] = ArrayTable(
            self, '限界改造', {
                '費用': ValueSpin(None, '費用', UPGRADE_STRUCTURE['限界改造']['費用'], alignment=Qt.AlignRight),
                '上昇値': ValueSpin(None, '上昇値', UPGRADE_STRUCTURE['限界改造']['上昇値'], alignment=Qt.AlignRight),
            }, sortable=False, stretch=tuple(), corner='   限界',
        )
        self['限界改造'].verticalHeader().setFixedWidth(60)
        self['限界改造'].setFixedSize(206, 293)

        robot_layout = QHBoxLayout()
        robot_layout.addWidget(self['ＨＰ改造'])
        robot_layout.addWidget(self['ＥＮ改造'])
        robot_layout.addWidget(self['運動改造'])
        robot_layout.addWidget(self['装甲改造'])
        robot_layout.addWidget(self['限界改造'])
        robot_group.setLayout(robot_layout)

        weapon_group = QGroupBox('武器改造')

        self['タイプ[A]'] = ArrayTable(
            self, 'タイプ[A]', {
                '費用': ValueSpin(None, '費用', UPGRADE_STRUCTURE['タイプ[A]']['費用'],
                                multiple=10, alignment=Qt.AlignRight),
                '上昇値': ValueSpin(None, '上昇値', UPGRADE_STRUCTURE['タイプ[A]']['上昇値'], alignment=Qt.AlignRight),
            }, sortable=False, stretch=tuple(), corner='タイプ[A]',
        )
        self['タイプ[A]'].verticalHeader().setFixedWidth(60)
        self['タイプ[A]'].setFixedSize(206, 293)

        self['タイプ[B]'] = ArrayTable(
            self, 'タイプ[B]', {
                '費用': ValueSpin(None, '費用', UPGRADE_STRUCTURE['タイプ[B]']['費用'],
                                multiple=10, alignment=Qt.AlignRight),
                '上昇値': ValueSpin(None, '上昇値', UPGRADE_STRUCTURE['タイプ[B]']['上昇値'], alignment=Qt.AlignRight),
            }, sortable=False, stretch=tuple(), corner='タイプ[B]',
        )
        self['タイプ[B]'].verticalHeader().setFixedWidth(60)
        self['タイプ[B]'].setFixedSize(206, 293)

        self['タイプ[C]'] = ArrayTable(
            self, 'タイプ[C]', {
                '費用': ValueSpin(None, '費用', UPGRADE_STRUCTURE['タイプ[C]']['費用'],
                                multiple=10, alignment=Qt.AlignRight),
                '上昇値': ValueSpin(None, '上昇値', UPGRADE_STRUCTURE['タイプ[C]']['上昇値'], alignment=Qt.AlignRight),
            }, sortable=False, stretch=tuple(), corner='タイプ[C]',
        )
        self['タイプ[C]'].verticalHeader().setFixedWidth(60)
        self['タイプ[C]'].setFixedSize(206, 293)

        self['タイプ[D]'] = ArrayTable(
            self, 'タイプ[D]', {
                '費用': ValueSpin(None, '費用', UPGRADE_STRUCTURE['タイプ[D]']['費用'],
                                multiple=10, alignment=Qt.AlignRight),
                '上昇値': ValueSpin(None, '上昇値', UPGRADE_STRUCTURE['タイプ[D]']['上昇値'], alignment=Qt.AlignRight),
            }, sortable=False, stretch=tuple(), corner='タイプ[D]',
        )
        self['タイプ[D]'].verticalHeader().setFixedWidth(60)
        self['タイプ[D]'].setFixedSize(206, 293)

        weapon_layout = QHBoxLayout()
        weapon_layout.addWidget(self['タイプ[A]'])
        weapon_layout.addWidget(self['タイプ[B]'])
        weapon_layout.addWidget(self['タイプ[C]'])
        weapon_layout.addWidget(self['タイプ[D]'])
        weapon_group.setLayout(weapon_layout)

        frame_layout = QVBoxLayout()
        frame_layout.addWidget(robot_group, alignment=Qt.AlignLeft)
        frame_layout.addWidget(weapon_group, alignment=Qt.AlignLeft)
        frame_layout.addStretch()
        frame.setLayout(frame_layout)
        return frame

    def init_birthday_frame(self):
        frame = QFrame()

        special_group = QGroupBox('特殊誕生日')
        self['特殊誕生日'] = ArrayTable(
            self, '特殊誕生日', {
                '誕生月': MappingSpin(None, '誕生月', SPECIAL_STRUCTURE['誕生月'],
                                   mapping=self.month_mapping, alignment=Qt.AlignRight),
                '誕生日': MappingSpin(None, '誕生日', SPECIAL_STRUCTURE['誕生日'],
                                   mapping=self.day_mapping, alignment=Qt.AlignRight),
                '血液型': MappingSpin(None, '血液型', SPECIAL_STRUCTURE['血液型'],
                                   mapping={0: 'A', 1: 'B', 2: 'AB', 3: 'O'}, alignment=Qt.AlignRight),
            }, sortable=False, stretch=tuple(), single=True,
        )
        self['特殊精神'] = ParallelTable(
            self['特殊誕生日'], ('精神リスト', '習得リスト'), {
                '精神': RadioCombo(None, '精神', SPECIAL_STRUCTURE['精神リスト']['精神'], mapping=EnumData.SPIRIT),
                '習得': MappingSpin(None, '習得', SPECIAL_STRUCTURE['習得リスト']['習得'],
                                  mapping=self.lv_mapping, alignment=Qt.AlignRight),
            }
        )
        self['特殊スキル'] = RadioCombo(self['特殊誕生日'], 'スキル', SPECIAL_STRUCTURE['スキル'],
                                   mapping=self.skill_mapping,
                                   alignment=Qt.AlignRight)

        self['特殊誕生日'].setFixedWidth(231)
        self['特殊誕生日'].verticalHeader().setHidden(True)
        self['特殊精神'].setFixedSize(148, 189)

        special_layout = QHBoxLayout()

        spirit_layout = QVBoxLayout()
        spirit_layout.addWidget(self['特殊精神'])
        spirit_layout.addWidget(self['特殊スキル'])
        spirit_layout.addStretch()
        special_layout.addWidget(self['特殊誕生日'])
        special_layout.addLayout(spirit_layout)
        special_group.setLayout(special_layout)

        constellation_group = QGroupBox('星座誕生日')
        self['星座範囲'] = ArrayTable(
            self, '星座範囲', {
                '開始月': MappingSpin(None, '開始月', ZODIAC_STRUCTURE['開始月'],
                                   mapping=self.month_mapping, alignment=Qt.AlignRight),
                '開始日': MappingSpin(None, '開始日', ZODIAC_STRUCTURE['開始日'],
                                   mapping=self.day_mapping, alignment=Qt.AlignRight),
                '終了月': MappingSpin(None, '終了月', ZODIAC_STRUCTURE['終了月'],
                                   mapping=self.month_mapping, alignment=Qt.AlignRight),
                '終了日': MappingSpin(None, '終了日', ZODIAC_STRUCTURE['終了日'],
                                   mapping=self.day_mapping, alignment=Qt.AlignRight),
            },
            sortable=False, stretch=tuple(), single=True,
        )
        self['血液型A'] = ArrayTable(self, '血液型A', {}, stretch=tuple())
        self['血液型B'] = ArrayTable(self, '血液型B', {}, stretch=tuple())
        self['血液型AB'] = ArrayTable(self, '血液型AB', {}, stretch=tuple())
        self['血液型O'] = ArrayTable(self, '血液型O', {}, stretch=tuple())

        self['血液型A精神'] = ParallelTable(
            self['血液型A'], ('精神リスト', '習得リスト'), {
                '精神': RadioCombo(None, '精神', BLOOD_STRUCTURE['精神リスト']['精神'], mapping=EnumData.SPIRIT),
                '習得': MappingSpin(None, '習得', BLOOD_STRUCTURE['習得リスト']['習得'],
                                  mapping=self.lv_mapping, alignment=Qt.AlignRight),
            }
        )
        self['血液型B精神'] = ParallelTable(
            self['血液型B'], ('精神リスト', '習得リスト'), {
                '精神': RadioCombo(None, '精神', BLOOD_STRUCTURE['精神リスト']['精神'], mapping=EnumData.SPIRIT),
                '習得': MappingSpin(None, '習得', BLOOD_STRUCTURE['習得リスト']['習得'],
                                  mapping=self.lv_mapping, alignment=Qt.AlignRight),
            }
        )
        self['血液型AB精神'] = ParallelTable(
            self['血液型AB'], ('精神リスト', '習得リスト'), {
                '精神': RadioCombo(None, '精神', BLOOD_STRUCTURE['精神リスト']['精神'], mapping=EnumData.SPIRIT),
                '習得': MappingSpin(None, '習得', BLOOD_STRUCTURE['習得リスト']['習得'],
                                  mapping=self.lv_mapping, alignment=Qt.AlignRight),
            }
        )
        self['血液型O精神'] = ParallelTable(
            self['血液型O'], ('精神リスト', '習得リスト'), {
                '精神': RadioCombo(None, '精神', BLOOD_STRUCTURE['精神リスト']['精神'], mapping=EnumData.SPIRIT),
                '習得': MappingSpin(None, '習得', BLOOD_STRUCTURE['習得リスト']['習得'],
                                  mapping=self.lv_mapping, alignment=Qt.AlignRight),
            }
        )
        self['血液型Aスキル'] = RadioCombo(self['血液型A'], 'スキル', BLOOD_STRUCTURE['スキル'],
                                     mapping=self.skill_mapping, alignment=Qt.AlignRight)
        self['血液型Bスキル'] = RadioCombo(self['血液型B'], 'スキル', BLOOD_STRUCTURE['スキル'],
                                     mapping=self.skill_mapping, alignment=Qt.AlignRight)
        self['血液型ABスキル'] = RadioCombo(self['血液型AB'], 'スキル', BLOOD_STRUCTURE['スキル'],
                                      mapping=self.skill_mapping, alignment=Qt.AlignRight)
        self['血液型Oスキル'] = RadioCombo(self['血液型O'], 'スキル', BLOOD_STRUCTURE['スキル'],
                                     mapping=self.skill_mapping, alignment=Qt.AlignRight)
        # noinspection PyUnresolvedReferences
        self['星座範囲'].clicked[QModelIndex].connect(self.control_blood)

        self['星座範囲'].verticalHeader().setHidden(True)
        self['星座範囲'].setFixedSize(286, 345)
        self['血液型A精神'].setFixedSize(148, 189)
        self['血液型B精神'].setFixedSize(148, 189)
        self['血液型AB精神'].setFixedSize(148, 189)
        self['血液型O精神'].setFixedSize(148, 189)
        constellation_layout = QHBoxLayout()

        birth_layout = QVBoxLayout()
        birth_layout.addWidget(QLabel('星座範囲'))
        birth_layout.addWidget(self['星座範囲'])
        birth_layout.addStretch()

        a_layout = QVBoxLayout()
        a_layout.addWidget(QLabel('血液型A'))
        a_layout.addWidget(self['血液型A精神'])
        a_layout.addWidget(self['血液型Aスキル'])

        b_layout = QVBoxLayout()
        b_layout.addWidget(QLabel('血液型B'))
        b_layout.addWidget(self['血液型B精神'])
        b_layout.addWidget(self['血液型Bスキル'])

        a_layout.addWidget(QLabel('血液型AB'))
        a_layout.addWidget(self['血液型AB精神'])
        a_layout.addWidget(self['血液型ABスキル'])
        a_layout.addStretch()

        b_layout.addWidget(QLabel('血液型O'))
        b_layout.addWidget(self['血液型O精神'])
        b_layout.addWidget(self['血液型Oスキル'])
        b_layout.addStretch()

        constellation_layout.addLayout(birth_layout)
        constellation_layout.addLayout(a_layout)
        constellation_layout.addLayout(b_layout)

        constellation_group.setLayout(constellation_layout)

        frame_layout = QHBoxLayout()
        frame_layout.addWidget(special_group)
        frame_layout.addWidget(constellation_group)
        frame_layout.addStretch()
        frame.setLayout(frame_layout)
        return frame

    def init_sppart_frame(self):
        frame = QFrame()

        sp_group = QGroupBox('精神消費')
        self['精神消費'] = ArrayTable(
            self, '精神消費', {
                '精神': TextLine(None, '精神', PrmgrpBIN().structures['精神名前'].structures['名称']),
                'SP': ValueSpin(None, 'SP', PrmgrpBIN().structures['精神消費']['SP'], alignment=Qt.AlignRight),
            }, sortable=False,
        )
        sp_layout = QHBoxLayout()
        sp_layout.addWidget(self['精神消費'])
        sp_group.setLayout(sp_layout)

        part_group = QGroupBox('パーツ属性')
        self['パーツ属性'] = ArrayTable(
            self, 'パーツ属性', {
                'パーツ': TextLine(None, 'パーツ', PrmgrpBIN().structures['パーツ名前'].structures['名称']),
                'ＨＰ': ValueSpin(None, 'ＨＰ', PART_STRUCTURE['ＨＰ'], multiple=100, alignment=Qt.AlignRight),
                '装甲': ValueSpin(None, '装甲', PART_STRUCTURE['装甲'], multiple=50, alignment=Qt.AlignRight),
                '運動性': ValueSpin(None, '運動性', PART_STRUCTURE['運動性'], alignment=Qt.AlignRight),
                '限界': ValueSpin(None, '限界', PART_STRUCTURE['限界'], alignment=Qt.AlignRight),
                '移動力': ValueSpin(None, '移動力', PART_STRUCTURE['移動力'], alignment=Qt.AlignRight),
                '射程命中': RadioCombo(None, '射程命中', PART_STRUCTURE['射程命中'],
                                   mapping={0: '', 0b1: '射程+1', 0b11: '命中+30%'}, alignment=Qt.AlignLeft),
                '空A': ValueSpin(None, '空A', PART_STRUCTURE['空A'], alignment=Qt.AlignLeft),
            }, sortable=False, stretch=(6,), check=(7,)
        )
        part_layout = QHBoxLayout()
        part_layout.addWidget(self['パーツ属性'])
        part_group.setLayout(part_layout)

        sp_group.setFixedWidth(226)
        part_group.setFixedWidth(710)

        frame_layout = QHBoxLayout()
        frame_layout.addWidget(sp_group)
        frame_layout.addWidget(part_group)
        frame_layout.addStretch()
        frame.setLayout(frame_layout)
        return frame

    def control_blood(self, index: QModelIndex):
        if not index.isValid():
            return False
        row = self['星座範囲'].model().mapToSource(index).row()
        self['血液型A'].control_child(row)
        self['血液型B'].control_child(row)
        self['血液型AB'].control_child(row)
        self['血液型O'].control_child(row)
        return True

    def set_roms(self, roms: list[PrmgrpBIN]):
        self.rom = roms[0]
        self.parse()

    def parse(self):
        self.rom.parse()

        self['ＨＰ改造'].install(self.rom['改造設定'][0])
        self['ＥＮ改造'].install(self.rom['改造設定'][0])
        self['運動改造'].install(self.rom['改造設定'][0])
        self['装甲改造'].install(self.rom['改造設定'][0])
        self['限界改造'].install(self.rom['改造設定'][0])
        self['タイプ[A]'].install(self.rom['改造設定'][0])
        self['タイプ[B]'].install(self.rom['改造設定'][0])
        self['タイプ[C]'].install(self.rom['改造設定'][0])
        self['タイプ[D]'].install(self.rom['改造設定'][0])

        for idx, spirit in enumerate(self.spirit_sequence):
            self.rom['精神消費'][idx] |= spirit
        self['精神消費'].install(self.rom.data)
        for idx, part in enumerate(self.part_sequence):
            self.rom['パーツ属性'][idx] |= part
        self['パーツ属性'].install(self.rom.data)

        self['特殊誕生日'].install(self.rom.data)
        self['星座範囲'].install(self.rom.data)
        self['血液型A'].install(self.rom.data)
        self['血液型B'].install(self.rom.data)
        self['血液型AB'].install(self.rom.data)
        self['血液型O'].install(self.rom.data)
        # noinspection PyUnresolvedReferences
        self['星座範囲'].selectionModel().currentChanged[QModelIndex, QModelIndex].connect(self.control_blood)

        self.original_data = deepcopy(self.rom.data)

    def build(self):
        self.rom.build()

    def builded(self) -> bool:
        if self.original_data == self.rom.data:
            return True
        return False
