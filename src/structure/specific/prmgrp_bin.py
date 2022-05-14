#!/usr/bin/env python
# -*- coding: utf-8 -*-

from parameter import HALF_TEXT_EXTRA
from structure.generic import Rom, Value, Text, Sequence, SEQUENCE

SPECIAL_STRUCTURE = {
    '誕生月': Value(0x0, 0x1),
    '誕生日': Value(0x1, 0x1),
    '血液型': Value(0x2, 0x1),
    'スキル': Value(0x3, 0x1),
    '精神リスト': Sequence({'精神': Value(0x0, 0x1)}, 0x4, 0x1, 0x6),
    '習得リスト': Sequence({'習得': Value(0x0, 0x1)}, 0xA, 0x1, 0x6),
}
ZODIAC_STRUCTURE = {
    '開始月': Value(0x0, 0x1),
    '開始日': Value(0x1, 0x1),
    '終了月': Value(0x2, 0x1),
    '終了日': Value(0x3, 0x1),
}
BLOOD_STRUCTURE = {
    '精神リスト': Sequence({'精神': Value(0x0, 0x1)}, 0x0, 0x1, 0x6),
    '習得リスト': Sequence({'習得': Value(0x0, 0x1)}, 0x6, 0x1, 0x6),
    'スキル': Value(0xC, 0x1),
}

PART_STRUCTURE = {
    'ＨＰ': Value(0x0, 0x1, (0, 4)),
    '装甲': Value(0x0, 0x1, (4, 8)),
    '運動性': Value(0x1, -0x1),
    '限界': Value(0x2, -0x1),
    '移動力': Value(0x3, -0x1, (0, 4)),
    '射程命中': Value(0x3, 0x1, (4, 6)),
    '空A': Value(0x3, 0x1, (6, 8)),
}

UPGRADE_STRUCTURE = {
    'ＨＰ改造': Sequence({'費用': Value(0x0, 0x2), '上昇値': Value(0x2, 0x2)}, 0x0, 0x4, 0xA),
    'ＥＮ改造': Sequence({'費用': Value(0x0, 0x2), '上昇値': Value(0x2, 0x2)}, 0x28, 0x4, 0xA),
    '運動性改造': Sequence({'費用': Value(0x0, 0x2), '上昇値': Value(0x2, 0x2)}, 0x50, 0x4, 0xA),
    '装甲改造': Sequence({'費用': Value(0x0, 0x2), '上昇値': Value(0x2, 0x2)}, 0x78, 0x4, 0xA),
    '限界改造': Sequence({'費用': Value(0x0, 0x2), '上昇値': Value(0x2, 0x2)}, 0xA0, 0x4, 0xA),
    '武器タイプ[A]': Sequence({'費用': Value(0x0, 0x2), '上昇値': Value(0x2, 0x2)}, 0xC8, 0x4, 0xA),
    '武器タイプ[B]': Sequence({'費用': Value(0x0, 0x2), '上昇値': Value(0x2, 0x2)}, 0xF0, 0x4, 0xA),
    '武器タイプ[C]': Sequence({'費用': Value(0x0, 0x2), '上昇値': Value(0x2, 0x2)}, 0x118, 0x4, 0xA),
    '武器タイプ[D]': Sequence({'費用': Value(0x0, 0x2), '上昇値': Value(0x2, 0x2)}, 0x140, 0x4, 0xA),
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
            '特殊誕生日': Sequence(SPECIAL_STRUCTURE, 0x25E98, 0x10, 0x2B),
            '星座範囲': Sequence(ZODIAC_STRUCTURE, 0x26158, 0x4, 0xC),
            '血液型A': Sequence(BLOOD_STRUCTURE, 0x26188, 0x40, 0xC),
            '血液型B': Sequence(BLOOD_STRUCTURE, 0x26198, 0x40, 0xC),
            '血液型AB': Sequence(BLOOD_STRUCTURE, 0x261A8, 0x40, 0xC),
            '血液型O': Sequence(BLOOD_STRUCTURE, 0x261B8, 0x40, 0xC),
            '精神名前': NameText(0x528, 0x118),
            '精神説明': NameText(0x67C, 0x64F),
            '精神消費': Sequence({'SP': Value(0x0, 0x1)}, 0x26898, 0x3, 0x23),
            'パーツ名前': NameText(0x2C, 0x148, HALF_TEXT_EXTRA | {'ｰ': 'ー'}),
            'パーツ説明': NameText(0x190, 0x368, HALF_TEXT_EXTRA | {'ｰ': 'ー', 'ー1': 'ｰ1', 'ー2': 'ｰ2'}),
            'パーツ属性': Sequence(PART_STRUCTURE, 0x266D4, 0x4, 0x1A),
            'スキル説明': NameText(0xE3C, 0x50, HALF_TEXT_EXTRA),
            'オプション': NameText(0x10D4, 0xAC, HALF_TEXT_EXTRA),
            '改造設定': Sequence(UPGRADE_STRUCTURE, 0x26494, 0x168, 0x1)
        }
