#!/usr/bin/env python
# -*- coding: utf-8 -*-

from structure.generic import Rom, Value, Text, Sequence
from parameter import TEXT

SPIRIT = {
    '精神': Value(0x0, 0x1),
}

SPIRITLV = {
    '等级': Value(0x0, 0x1),
}

SKILL = {
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

PILOT = {
    'CODE': Value(0x0, 0x2),
    '换乘系': Value(0x2, 0x2, bit=(0, 10)),
    '机师名': Text(0x4, 0x14, code='shiftjisx0213', extra=TEXT),
    '爱称': Text(0x29, 0xC, code='shiftjisx0213', extra=TEXT),
    '格斗': Value(0x36, 0x1),
    '射击': Value(0x37, 0x1),
    '回避': Value(0x38, 0x1),
    '命中': Value(0x39, 0x1),
    '反应': Value(0x3A, 0x1),
    '技量': Value(0x3B, 0x1),
    '精神': Sequence(SPIRIT, 0x3C, 0x1, 0x6),
    '习得': Sequence(SPIRITLV, 0x42, 0x1, 0x6),
    '技能': Sequence(SKILL, 0x48, 0xA, 0x3),
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
        self.structures: dict[str, Value | Sequence] = {
            '数量': Value(0x0, 0x4),
            '机师': Sequence(PILOT, 0x4, 0x70, 0x1D5),
        }

    def parse(self) -> bool:
        if not self.buffer:
            return False
        for pname, structure in self.structures.items():
            if pname == '机师':
                structure.count = self._data['数量']
            self._data[pname] = structure.parse(self.buffer)
        return True

    def build(self) -> bool:
        if not self._data:
            return False
        self._data['数量'] = self.structures['机师'].count
        for pname, data in self._data.items():
            self.structures[pname].build(data, self.buffer)
        return True
