#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Union
from ...common import Value, Text
from parameter import TEXT


class Arm:
    count = 0x10
    length = 0x28

    def __init__(self, buffer: bytearray):
        self.buffer = buffer
        self.settings = {
            'コード': Value(0x0, 0x1, (0, 4)),
            'ニュータイプＬｖ': Value(0x0, 0x1, (4, 6)),
            '聖戦士Ｌｖ': Value(0x0, 0x1, (6, 8)),
            '気力': Value(0x1, 0x1),
            '改造タイプ': Value(0x2, 0x1, (0, 2)),
            '近射程': Value(0x2, 0x1, (2, 4)),
            '遠射程': Value(0x2, 0x1, (4, 8)),
            'ＭＡＰタイプ': Value(0x3, 0x1, (0, 2)),
            'ＭＡＰ着弾範囲': Value(0x3, 0x1, (2, 5)),
            '攻撃力': Value(0x4, 0x2),
            '分類': Value(0x6, 0x1, 0),
            '属性': Value(0x6, 0x1, (1, 8)),
            '改造追加': Value(0x7, 0x1, (4, 8)),
            '名前': Text(0x8, 0x15, 'shiftjisx0213', TEXT, bytearray([0x20] * 0x15)),
            'ＭＡＰ範囲': Value(0x1D, 0x1),
            'ＭＡＰ演出': Value(0x1E, 0x1),
            'ＥＮ': Value(0x1F, 0x1),
            '命中': Value(0x20, -0x1),
            'クリティカル': Value(0x21, -0x1),
            '初期弾数': Value(0x22, 0x1),
            '最大弾数': Value(0x23, 0x1),
            '空適応': Value(0x24, 0x1),
            '陸適応': Value(0x25, 0x1),
            '海適応': Value(0x26, 0x1),
            '宇適応': Value(0x27, 0x1)
        }
        self._data: dict[str: Union[str, int]] = dict()
        self.parse()

    @property
    def propertys(self) -> list[str]:
        return list(self._data.keys())

    def parse(self) -> bool:
        if not self.buffer:
            return False
        for k, s in self.settings.items():
            self._data[k] = s.get_data(self.buffer)
        return True

    def build(self) -> bool:
        if not self.buffer or not self._data:
            return False
        for k, s in self.settings.items():
            s.set_data(self._data.get(k), self.buffer)
        return True

    def __getitem__(self, item: Union[str, int]):
        if isinstance(item, str):
            return self._data.get(item)
        return self._data.get(self.propertys[item])

    def __setitem__(self, data: Union[str, int], item: Union[str, int]):
        if isinstance(item, str):
            self._data[item] = data
        else:
            self._data[self.propertys[item]] = data

    def __repr__(self):
        text = '\nArm Info:'
        for k, v in self._data.items():
            text += f'\n{k}：{v}'
        return text
