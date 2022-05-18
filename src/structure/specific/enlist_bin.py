#!/usr/bin/env python
# -*- coding: utf-8 -*-

from structure.generic import Rom, Value, Sequence

ENEMY_STRUCTURE = {
    '機体': Value(0x0, 0x2),
    '機改': Value(0x2, 0x1),
    '武改': Value(0x3, 0x1),
    'パイロット': Value(0x4, 0x2),
    'レベル': Value(0x6, 0x2),
    '座標X': Value(0x8, -0x1),
    '座標Y': Value(0x9, -0x1),
    'パーツ': Value(0xA, 0x1),
    '隊号': Value(0xB, 0x1),
}

ENLIST_STRUCTURE = {
    '合計': Value(0x0, 0x2),
    '隊数': Value(0x2, 0x2),
    '隊00': Value(0x4, 0x1),
    '隊01': Value(0x5, 0x1),
    '隊02': Value(0x6, 0x1),
    '隊03': Value(0x7, 0x1),
    '隊04': Value(0x8, 0x1),
    '隊05': Value(0x9, 0x1),
    '隊06': Value(0xA, 0x1),
    '隊07': Value(0xB, 0x1),
    '隊08': Value(0xC, 0x1),
    '隊09': Value(0xD, 0x1),
    '隊10': Value(0xE, 0x1),
    '隊11': Value(0xF, 0x1),
    '隊12': Value(0x10, 0x1),
    '隊13': Value(0x11, 0x1),
    '隊14': Value(0x12, 0x1),
    '隊15': Value(0x13, 0x1),
    '敵リスト': Sequence(ENEMY_STRUCTURE, 0x14, 0xC, 0xA0),
}


class EnlistBIN(Rom):
    def __init__(self):
        super(EnlistBIN, self).__init__()
        self.structures = {
            '敵設定': Sequence(ENLIST_STRUCTURE, 0x0, 0x794, 0x96),
        }
