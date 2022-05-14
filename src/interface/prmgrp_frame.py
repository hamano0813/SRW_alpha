#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import Optional

from PySide6.QtCore import Qt, QModelIndex
from PySide6.QtWidgets import QGroupBox, QHBoxLayout, QLabel, QVBoxLayout, QTabWidget, QFrame

from parameter.enum_data import EnumData
from structure import PrmgrpBIN
from structure.specific.prmgrp_bin import (SPECIAL_STRUCTURE, ZODIAC_STRUCTURE, BLOOD_STRUCTURE, PART_STRUCTURE)
from widget import *



class PrmgrpFrame(BackgroundFrame):
    def __init__(self, parent=None, **kwargs):
        super(PrmgrpFrame, self).__init__(parent, **kwargs)
        self.rom: Optional[PrmgrpBIN] = None
        self.skill = {idx: f'{idx:02d}.{skill}' for idx, skill in enumerate(EnumData.PILOT['特殊技能'][:8])}
        self.spirit = [{'精神': spirit} for spirit in EnumData.SPIRIT.values()][:-1]
        self.part = [{'パーツ': part} for part in EnumData.PART.values()][1:]
        self.init_ui()

    # noinspection PyAttributeOutsideInit
    def init_ui(self):
        spirit_group = self.init_spirit_group()
        part_group = self.init_part_group()
        constellation_group = self.init_constellation_group()
        special_group = self.init_special_group()

        spirit_group.setFixedWidth(226)
        part_group.setFixedWidth(710)

        tab_widget = QTabWidget()

        self.sppart_tab = QFrame()
        sppart_layout = QHBoxLayout()
        sppart_layout.addWidget(spirit_group)
        sppart_layout.addWidget(part_group)
        sppart_layout.addStretch()
        self.sppart_tab.setLayout(sppart_layout)

        self.birthday_tab = QFrame()
        birthday_layout = QHBoxLayout()
        birthday_layout.addWidget(special_group)
        birthday_layout.addWidget(constellation_group)
        birthday_layout.addStretch()
        self.birthday_tab.setLayout(birthday_layout)

        tab_widget.addTab(self.birthday_tab, '誕生日')
        tab_widget.addTab(self.sppart_tab, '精神消費＆パーツ属性')

        main_layout = QVBoxLayout()
        main_layout.addWidget(tab_widget)

        self.setLayout(main_layout)

    def init_special_group(self):
        group = QGroupBox('特殊誕生日')
        self['特殊誕生日'] = ArrayTable(
            self, '特殊誕生日', {
                '誕生月': ValueSpin(None, '誕生月', SPECIAL_STRUCTURE['誕生月'], alignment=Qt.AlignRight),
                '誕生日': ValueSpin(None, '誕生日', SPECIAL_STRUCTURE['誕生日'], alignment=Qt.AlignRight),
                '血液型': MappingSpin(None, '血液型', SPECIAL_STRUCTURE['血液型'],
                                   mapping={0: 'A', 1: 'B', 2: 'AB', 3: 'O'}, alignment=Qt.AlignRight),
            },
            stretch=tuple(), single=True,
        )
        self['特殊精神'] = ParallelTable(
            self['特殊誕生日'], ('精神リスト', '習得リスト'), {
                '精神': RadioCombo(None, '精神', SPECIAL_STRUCTURE['精神リスト']['精神'], mapping=EnumData.SPIRIT),
                '習得': ValueSpin(None, '習得', SPECIAL_STRUCTURE['習得リスト']['習得'], alignment=Qt.AlignRight),
            }
        )
        self['特殊スキル'] = RadioCombo(self['特殊誕生日'], 'スキル', SPECIAL_STRUCTURE['スキル'],
                                   mapping=self.skill,
                                   alignment=Qt.AlignRight)

        self['特殊誕生日'].setFixedWidth(231)
        self['特殊誕生日'].verticalHeader().setHidden(True)
        self['特殊精神'].setFixedSize(148, 189)

        group_layout = QHBoxLayout()

        spirit_layout = QVBoxLayout()
        spirit_layout.addWidget(self['特殊精神'])
        spirit_layout.addWidget(self['特殊スキル'])
        spirit_layout.addStretch()

        group_layout.addWidget(self['特殊誕生日'])
        group_layout.addLayout(spirit_layout)
        group.setLayout(group_layout)
        return group

    def init_constellation_group(self):
        group = QGroupBox('星座誕生日')
        self['星座範囲'] = ArrayTable(
            self, '星座範囲', {
                '開始月': ValueSpin(None, '開始月', ZODIAC_STRUCTURE['開始月'], alignment=Qt.AlignRight),
                '開始日': ValueSpin(None, '開始日', ZODIAC_STRUCTURE['開始日'], alignment=Qt.AlignRight),
                '終了月': ValueSpin(None, '終了月', ZODIAC_STRUCTURE['終了月'], alignment=Qt.AlignRight),
                '終了日': ValueSpin(None, '終了日', ZODIAC_STRUCTURE['終了日'], alignment=Qt.AlignRight),
            },
            sortable=False, stretch=tuple(), single=True,
        )
        self['血液型A'] = ArrayTable(self, '血液型A', {'スキル': ValueSpin(None, 'スキル', BLOOD_STRUCTURE['スキル'])})
        self['血液型B'] = ArrayTable(self, '血液型B', {'スキル': ValueSpin(None, 'スキル', BLOOD_STRUCTURE['スキル'])})
        self['血液型AB'] = ArrayTable(self, '血液型AB', {'スキル': ValueSpin(None, 'スキル', BLOOD_STRUCTURE['スキル'])})
        self['血液型O'] = ArrayTable(self, '血液型O', {'スキル': ValueSpin(None, 'スキル', BLOOD_STRUCTURE['スキル'])})

        self['血液型A精神'] = ParallelTable(
            self['血液型A'], ('精神リスト', '習得リスト'), {
                '精神': RadioCombo(None, '精神', BLOOD_STRUCTURE['精神リスト']['精神'], mapping=EnumData.SPIRIT),
                '習得': ValueSpin(None, '習得', BLOOD_STRUCTURE['習得リスト']['習得'], alignment=Qt.AlignRight),
            }
        )
        self['血液型B精神'] = ParallelTable(
            self['血液型B'], ('精神リスト', '習得リスト'), {
                '精神': RadioCombo(None, '精神', BLOOD_STRUCTURE['精神リスト']['精神'], mapping=EnumData.SPIRIT),
                '習得': ValueSpin(None, '習得', BLOOD_STRUCTURE['習得リスト']['習得'], alignment=Qt.AlignRight),
            }
        )
        self['血液型AB精神'] = ParallelTable(
            self['血液型AB'], ('精神リスト', '習得リスト'), {
                '精神': RadioCombo(None, '精神', BLOOD_STRUCTURE['精神リスト']['精神'], mapping=EnumData.SPIRIT),
                '習得': ValueSpin(None, '習得', BLOOD_STRUCTURE['習得リスト']['習得'], alignment=Qt.AlignRight),
            }
        )
        self['血液型O精神'] = ParallelTable(
            self['血液型O'], ('精神リスト', '習得リスト'), {
                '精神': RadioCombo(None, '精神', BLOOD_STRUCTURE['精神リスト']['精神'], mapping=EnumData.SPIRIT),
                '習得': ValueSpin(None, '習得', BLOOD_STRUCTURE['習得リスト']['習得'], alignment=Qt.AlignRight),
            }
        )
        self['血液型Aスキル'] = RadioCombo(self['血液型A'], 'スキル', BLOOD_STRUCTURE['スキル'],
                                     mapping=self.skill, alignment=Qt.AlignRight)
        self['血液型Bスキル'] = RadioCombo(self['血液型B'], 'スキル', BLOOD_STRUCTURE['スキル'],
                                     mapping=self.skill, alignment=Qt.AlignRight)
        self['血液型ABスキル'] = RadioCombo(self['血液型AB'], 'スキル', BLOOD_STRUCTURE['スキル'],
                                      mapping=self.skill, alignment=Qt.AlignRight)
        self['血液型Oスキル'] = RadioCombo(self['血液型O'], 'スキル', BLOOD_STRUCTURE['スキル'],
                                     mapping=self.skill, alignment=Qt.AlignRight)
        self['星座範囲'].clicked[QModelIndex].connect(self.control_blood)

        self['星座範囲'].verticalHeader().setHidden(True)
        self['星座範囲'].setFixedSize(286, 345)
        self['血液型A精神'].setFixedSize(148, 189)
        self['血液型B精神'].setFixedSize(148, 189)
        self['血液型AB精神'].setFixedSize(148, 189)
        self['血液型O精神'].setFixedSize(148, 189)
        group_layout = QHBoxLayout()

        birth_layout = QVBoxLayout()
        birth_layout.addWidget(QLabel('星座範囲'))
        birth_layout.addWidget(self['星座範囲'])
        birth_layout.addStretch()

        a_layout = QVBoxLayout()
        a_layout.addWidget(QLabel('血液型A'))
        a_layout.addWidget(self['血液型A精神'])
        a_layout.addWidget(self['血液型Aスキル'])
        a_layout.addStretch()

        b_layout = QVBoxLayout()
        b_layout.addWidget(QLabel('血液型B'))
        b_layout.addWidget(self['血液型B精神'])
        b_layout.addWidget(self['血液型Bスキル'])
        b_layout.addStretch()

        ab_layout = QVBoxLayout()
        ab_layout.addWidget(QLabel('血液型AB'))
        ab_layout.addWidget(self['血液型AB精神'])
        ab_layout.addWidget(self['血液型ABスキル'])
        ab_layout.addStretch()

        o_layout = QVBoxLayout()
        o_layout.addWidget(QLabel('血液型O'))
        o_layout.addWidget(self['血液型O精神'])
        o_layout.addWidget(self['血液型Oスキル'])
        o_layout.addStretch()

        group_layout.addLayout(birth_layout)
        group_layout.addLayout(a_layout)
        group_layout.addLayout(b_layout)
        group_layout.addLayout(ab_layout)
        group_layout.addLayout(o_layout)

        group.setLayout(group_layout)
        return group

    def init_spirit_group(self):
        group = QGroupBox('精神消費')
        self['精神消費'] = ArrayTable(
            self, '精神消費', {
                '精神': TextLine(None, '精神', PrmgrpBIN().structures['精神名前'].structures['名称']),
                'SP': ValueSpin(None, 'SP', PrmgrpBIN().structures['精神消費']['SP'], alignment=Qt.AlignRight),
            }
        )
        group_layout = QHBoxLayout()
        group_layout.addWidget(self['精神消費'])
        group.setLayout(group_layout)
        return group

    def init_part_group(self):
        group = QGroupBox('パーツ属性')
        self['パーツ属性'] = ArrayTable(
            self, 'パーツ属性', {
                'パーツ': TextLine(None, 'パーツ', PrmgrpBIN().structures['パーツ名前'].structures['名称']),
                'ＨＰ': ValueSpin(None, 'ＨＰ', PART_STRUCTURE['ＨＰ'], multiple=100, alignment=Qt.AlignRight),
                '装甲': ValueSpin(None, '装甲', PART_STRUCTURE['装甲'], multiple=50, alignment=Qt.AlignRight),
                '運動性': ValueSpin(None, '運動性', PART_STRUCTURE['運動性'], alignment=Qt.AlignRight),
                '限界': ValueSpin(None, '限界', PART_STRUCTURE['限界'], alignment=Qt.AlignRight),
                '移動力': ValueSpin(None, '移動力', PART_STRUCTURE['移動力'], alignment=Qt.AlignRight),
                '射程命中': RadioCombo(None, '射程命中', PART_STRUCTURE['射程命中'],
                                   mapping={0: '', 0b1: '射程+1', 0b11: '命中+30%'},
                                   alignment=Qt.AlignLeft),
                '空A': MappingSpin(None, '空A', PART_STRUCTURE['空A'],
                                  mapping={0: '', 0x1: '⚪'},
                                  alignment=Qt.AlignLeft),
            }, stretch=(6,),
        )
        group_layout = QHBoxLayout()
        group_layout.addWidget(self['パーツ属性'])
        group.setLayout(group_layout)
        return group

    def control_blood(self, index: QModelIndex):
        if not index.isValid():
            return False
        row = self['星座範囲'].model().mapToSource(index).row()
        self['血液型A'].control_child(row)
        self['血液型B'].control_child(row)
        self['血液型AB'].control_child(row)
        self['血液型O'].control_child(row)
        return True

    def set_rom(self, rom: PrmgrpBIN):
        self.rom = rom
        self.parse()

    def parse(self):
        self.rom.parse()
        for idx, spirit in enumerate(self.spirit):
            self.rom['精神消費'][idx] |= spirit
        self['精神消費'].install(self.rom.data)
        for idx, part in enumerate(self.part):
            self.rom['パーツ属性'][idx] |= part
        self['パーツ属性'].install(self.rom.data)
        self['特殊誕生日'].install(self.rom.data)
        self['星座範囲'].install(self.rom.data)
        self['血液型A'].install(self.rom.data)
        self['血液型B'].install(self.rom.data)
        self['血液型AB'].install(self.rom.data)
        self['血液型O'].install(self.rom.data)
        self['星座範囲'].selectionModel().currentChanged[QModelIndex, QModelIndex].connect(self.control_blood)

    def build(self):
        self.rom.build()
