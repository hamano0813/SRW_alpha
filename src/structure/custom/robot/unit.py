#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Union
from ...common import Value, Text
from parameter import TEXT
from .arm import Arm


class Unit:
    length = 0x2C4

    def __init__(self, buffer: bytearray):
        self.buffer = buffer
        self.settings = {
            '名前': Text(0x0, 0x1A, 'shiftjisx0213', TEXT, bytearray([0x20] * 0xC) + bytearray(range(0xA0, 0xAE))),
            'コード': Value(0x1A, 0x2),
            '移動タイプ': Value(0x1C, 0x1, (0, 4)),
            '移動力': Value(0x1D, 0x1),
            'ＨＰ': Value(0x1E, 0x2),
            'ＥＮ': Value(0x20, 0x2),
            '運動性': Value(0x22, 0x2),
            '装甲': Value(0x24, 0x2),
            '限界': Value(0x26, 0x2),
            'サイズ': Value(0x28, 0x1),
            'パーツスロット数': Value(0x29, 0x1),
            '乗り換え系': Value(0x2A, 0x2, (0, 10)),
            '特殊能力': Value(0x2C, 0x4, (0, 31)),
            '修理費': Value(0x30, 0x2),
            '資金': Value(0x32, 0x2),
            '变形グループ': Value(0x34, 0x1),
            '变形番号': Value(0x35, 0x1),
            '合体グループ': Value(0x36, 0x1),
            '合体番号': Value(0x37, 0x1),
            '分離機体番号': Value(0x38, 0x2),
            '合体数': Value(0x3A, 0x1),
            '換装グループ': Value(0x3B, 0x1),
            'ＢＧＭ': Value(0x3C, 0x1),
            '空適応': Value(0x40, 0x1),
            '陸適応': Value(0x41, 0x1),
            '海適応': Value(0x42, 0x1),
            '宇適応': Value(0x43, 0x1),
        }
        self._propertys: dict[str: Union[str, int, list[Arm]]] = dict()
        self.parse()

    @property
    def propertys(self) -> list[str]:
        return list(self._propertys.keys())

    def parse(self) -> bool:
        if not self.buffer:
            return False
        for k, s in self.settings.items():
            self._propertys[k] = s.get(self.buffer)
        self._propertys['武装'] = [Arm(self.buffer[0x44 + Arm.length * idx: 0x44 + Arm.length * (idx + 1)])
                                 for idx in range(Arm.count)]
        return True

    def build(self) -> bool:
        if not self.buffer:
            return False
        buffer = self.buffer[:0x44]
        if not self._propertys:
            return False
        for k, s in self.settings.items():
            s.set(self._propertys.get(k), buffer)
        for weapon in self._propertys['武装']:
            weapon.build()
            buffer += weapon.buffer
        self.buffer = buffer
        return True

    def __getitem__(self, property_name: str):
        return self._propertys.get(property_name)

    def __setitem__(self, property_name: str, property_data: Union[str, int, list[Arm]]):
        self._propertys[property_name] = property_data

    def __repr__(self):
        return f'Unit {self._propertys["名前"]} with {len(self.settings)} propertys'
