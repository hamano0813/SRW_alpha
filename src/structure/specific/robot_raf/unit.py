#!/usr/bin/env python
# -*- coding: utf-8 -*-

from structure.generic import Value, Text, Sequence
from parameter import TEXT
from .arm import Arm


class Unit(Sequence):
    def __init__(self, offset, length, count):
        super(Unit, self).__init__(offset, length, count)
        self.structures = {
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
            '武装': Arm(0x44, 0x28, 0x10),
        }
