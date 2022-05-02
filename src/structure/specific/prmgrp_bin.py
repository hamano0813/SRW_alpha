#!/usr/bin/env python
# -*- coding: utf-8 -*-

from parameter import HALF_TEXT_EXTRA
from structure.generic import Rom, Value, Text, Sequence, SEQUENCE

SPECIAL_STRUCTURE = {
    '出生月': Value(0x0, 0x1),
    '出生日': Value(0x1, 0x1),
    '血型': Value(0x2, 0x1),
    '特技': Value(0x3, 0x1),
    '精神列表': Sequence({'精神': Value(0x0, 0x1)}, 0x4, 0x1, 0x6),
    '习得列表': Sequence({'等级': Value(0x0, 0x1)}, 0xA, 0x1, 0x6),
}
ZODIAC_STRUCTURE = {
    '起始月': Value(0x0, 0x1),
    '起始日': Value(0x1, 0x1),
    '结束月': Value(0x2, 0x1),
    '结束日': Value(0x3, 0x1),
}
A_STRUCTURE = {
    '精神列表': Sequence({'精神': Value(0x0, 0x1)}, 0x0, 0x1, 0x6),
    '习得列表': Sequence({'等级': Value(0x0, 0x1)}, 0x6, 0x1, 0x6),
    '特技': Value(0xC, 0x1),
}
B_STRUCTURE = {
    '精神列表': Sequence({'精神': Value(0x0, 0x1)}, 0x0, 0x1, 0x6),
    '习得列表': Sequence({'等级': Value(0x0, 0x1)}, 0x6, 0x1, 0x6),
    '特技': Value(0xC, 0x1),
}
AB_STRUCTURE = {
    '精神列表': Sequence({'精神': Value(0x0, 0x1)}, 0x0, 0x1, 0x6),
    '习得列表': Sequence({'等级': Value(0x0, 0x1)}, 0x6, 0x1, 0x6),
    '特技': Value(0xC, 0x1),
}
O_STRUCTURE = {
    '精神列表': Sequence({'精神': Value(0x0, 0x1)}, 0x0, 0x1, 0x6),
    '习得列表': Sequence({'等级': Value(0x0, 0x1)}, 0x6, 0x1, 0x6),
    '特技': Value(0xC, 0x1),
}

PART_STRUCTURE = {
    'HP*100': Value(0x0, 0x1, (0, 4)),
    '装甲*50': Value(0x0, 0x1, (4, 8)),
    '运动性': Value(0x1, -0x1),
    '限界': Value(0x2, -0x1),
    '移动力': Value(0x3, -0x1, (0, 4)),
    '射程/命中率': Value(0x3, 0x1, (4, 6)),
    '空飞/空A': Value(0x3, 0x1, (6, 8)),
}


class NameText(Sequence):
    def __init__(self, offset, length, extra=None, count=None, structures=None):
        super(NameText, self).__init__(structures, offset, length, count)
        self.structures = {
            '名称': Text(0x0, 0x0, 'shiftjisx0213', extra),
        }

    def parse(self, buffer: bytearray) -> SEQUENCE:
        sequence = list()
        _buffer = buffer[self.offset: self.offset + self.length]
        buf_list = _buffer.replace(b'\00\00', b'\00').replace(b'\00\00', b'\00').strip(b'\00').split(b'\00')
        for buf in buf_list:
            self.structures['名称'].length = len(buf)
            sequence.append({'名称': self.structures['名称'].parse(buf)})
        return sequence

    def build(self, sequence: SEQUENCE, buffer: bytearray) -> bytearray:
        pass


class PrmgrpBIN(Rom):
    def __init__(self):
        super(PrmgrpBIN, self).__init__()
        self.structures = {
            '特殊主角列表': Sequence(SPECIAL_STRUCTURE, 0x25E98, 0x10, 0x2B),
            '星座范围列表': Sequence(ZODIAC_STRUCTURE, 0x26158, 0x4, 0xC),
            'A型血主角列表': Sequence(A_STRUCTURE, 0x26188, 0x40, 0xC),
            'B型血主角列表': Sequence(A_STRUCTURE, 0x26198, 0x40, 0xC),
            'AB型血主角列表': Sequence(A_STRUCTURE, 0x261A8, 0x40, 0xC),
            'O型血主角列表': Sequence(A_STRUCTURE, 0x261B8, 0x40, 0xC),
            '精神名称列表': NameText(0x528, 0x118),
            '精神描述列表': NameText(0x67C, 0x64F),
            '精神消耗列表': Sequence({'SP': Value(0x0, 0x1)}, 0x26898, 0x3, 0x23),
            '部件名称列表': NameText(0x2C, 0x148, HALF_TEXT_EXTRA | {'ｰ': 'ー'}),
            '部件描述列表': NameText(0x190, 0x368, HALF_TEXT_EXTRA | {'ｰ': 'ー', 'ー1': 'ｰ1', 'ー2': 'ｰ2'}),
            '部件属性列表': Sequence(PART_STRUCTURE, 0x266D4, 0x4, 0x1A),
            '特技描述列表': NameText(0xE3C, 0x50, HALF_TEXT_EXTRA),
            '单位菜单列表': NameText(0x10D4, 0xAC, HALF_TEXT_EXTRA),
        }
