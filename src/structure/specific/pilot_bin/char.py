#!/usr/bin/env python
# -*- coding: utf-8 -*-

from structure.generic import Value, Text, Sequence
from parameter import TEXT
from .spirit import Spirit, SpiritLv
from .skill import Skill


class Char(Sequence):
    def __init__(self, offset, length, count):
        super(Char, self).__init__(offset, length, count)
        self.structures = {
            'コード': Value(0x0, 0x2),
            '乗り換え系': Value(0x2, 0x2, bit=(0, 10)),
            '名前': Text(0x4, 0x14, code='shiftjisx0213', extra=TEXT),
            '愛称': Text(0x29, 0xC, code='shiftjisx0213', extra=TEXT),
            '格闘': Value(0x36, 0x1),
            '射撃': Value(0x37, 0x1),
            '回避': Value(0x38, 0x1),
            '命中': Value(0x39, 0x1),
            '反応': Value(0x3A, 0x1),
            '技量': Value(0x3B, 0x1),
            '精神': Spirit(0x3C, 0x1, 0x6),
            '精神Lv' : SpiritLv(0x42, 0x1, 0x6),
            '技能': Skill(0x48, 0xA, 0x3),
            'ＳＰ': Value(0x66, 0x1),
            '２回行動': Value(0x67, 0x1),
            '特技': Value(0x68, 0x1),
            '分類': Value(0x69, 0x1, bit=(4, 8)),
            '性格': Value(0x6A, 0x1),
            '気力補正組': Value(0x6B, 0x1),
            '空適応': Value(0x6C, 0x1),
            '陸適応': Value(0x6D, 0x1),
            '海適応': Value(0x6E, 0x1),
            '宇適応': Value(0x6F, 0x1),
        }
