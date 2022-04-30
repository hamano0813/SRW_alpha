#!/usr/bin/env python
# -*- coding: utf-8 -*-

from structure.generic import Rom, Value, Text, Sequence
from parameter import HALF_TEXT_EXTRA

SKILL_STRUCTURE = {
    '技能': Value(0x0, 0x1),
    'Lv1': Value(0x1, 0x1),
    'Lv2': Value(0x2, 0x1),
    'Lv3': Value(0x3, 0x1),
    'Lv4': Value(0x4, 0x1),
    'Lv5': Value(0x5, 0x1),
    'Lv6': Value(0x6, 0x1),
    'Lv7': Value(0x7, 0x1),
    'Lv8': Value(0x8, 0x1),
    'Lv9': Value(0x9, 0x1),
}

PILOT_STRUCTURE = {
    'CODE': Value(0x0, 0x2),
    '换乘系': Value(0x2, 0x2, bit=(0, 10)),
    '机师名': Text(0x4, 0x14, code='shiftjisx0213', extra=HALF_TEXT_EXTRA),
    '爱称': Text(0x29, 0xC, code='shiftjisx0213', extra=HALF_TEXT_EXTRA),
    '格斗': Value(0x36, 0x1),
    '射击': Value(0x37, 0x1),
    '回避': Value(0x38, 0x1),
    '命中': Value(0x39, 0x1),
    '反应': Value(0x3A, 0x1),
    '技量': Value(0x3B, 0x1),
    '精神列表': Sequence({'精神': Value(0x0, 0x1)}, 0x3C, 0x1, 0x6),
    '习得列表': Sequence({'等级': Value(0x0, 0x1)}, 0x42, 0x1, 0x6),
    '技能列表': Sequence(SKILL_STRUCTURE, 0x48, 0xA, 0x3),
    'SP': Value(0x66, 0x1),
    '两动等级': Value(0x67, 0x1),
    '特技': Value(0x68, 0x1),
    '分类': Value(0x69, 0x1, bit=(4, 8)),
    '性格': Value(0x6A, 0x1),
    '气力补正组': Value(0x6B, 0x1),
    '空适应': Value(0x6C, 0x1),
    '陆适应': Value(0x6D, 0x1),
    '海适应': Value(0x6E, 0x1),
    '宇适应': Value(0x6F, 0x1),
}


class PilotBIN(Rom):
    def __init__(self):
        super(PilotBIN, self).__init__()
        self.structures = {
            '机师列表': Sequence(PILOT_STRUCTURE, 0x4, 0x70, 0x1D5),
        }
