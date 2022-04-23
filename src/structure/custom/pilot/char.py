#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Union
from ...common import Value, Text
from parameter import TEXT
from .spirit import Spirit
from .skill import Skill


class Char:
    count = 0x1D5
    length = 0x70
    _spirit = 0x3C
    _skill = 0x48

    def __init__(self, buffer: bytearray):
        self.buffer = buffer
        self.settings = {
            'コード': Value(0x0, 0x2),
            '乗り換え系': Value(0x2, 0x2, bit=(0, 10)),
            '名前': Text(0x4, 0x14, aliases='shiftjisx0213', additional=TEXT),
            '愛称': Text(0x29, 0xC, aliases='shiftjisx0213', additional=TEXT),
            '格闘': Value(0x36, 0x1),
            '射撃': Value(0x37, 0x1),
            '回避': Value(0x38, 0x1),
            '命中': Value(0x39, 0x1),
            '反応': Value(0x3A, 0x1),
            '技量': Value(0x3B, 0x1),
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
        self._data: dict[str: Union[str, int, list[Spirit, Skill]]] = dict()
        self.parse()

    @property
    def propertys(self) -> list[str]:
        return list(self._data.keys())

    def parse(self):
        if not self.buffer:
            return False
        for k, s in self.settings.items():
            self._data[k] = s.get_data(self.buffer)
        self._data['精神'] = [Spirit(
            self.buffer[self._spirit + idx: self._spirit + idx + 1] +
            self.buffer[self._spirit + idx + Spirit.count: self._spirit + idx + Spirit.count + 1])
            for idx in range(Spirit.count)]
        self._data['技能'] = [
            Skill(self.buffer[self._skill + Skill.length * idx: self._skill + Skill.length * (idx + 1)])
            for idx in range(Skill.count)]
        return True

    def build(self) -> bool:
        if not self.buffer or not self._data:
            return False
        buffer = self.buffer[:self._spirit]
        for spirit in self._data['精神']:
            spirit.build()
            buffer += spirit.buffer[0]
        for spirit in self._data['精神']:
            buffer += spirit.buffer[1]
        for skill in self._data['技能']:
            skill.build()
            buffer += skill.buffer
        buffer += self.buffer[self._skill + Skill.length * Skill.count:]
        for k, s in self.settings.items():
            s.set_data(self._data.get(k), buffer)
        self.buffer = buffer
        return True

    def __getitem__(self, item: Union[str, int]):
        if isinstance(item, str):
            return self._data.get(item)
        return self._data.get(self.propertys[item])

    def __setitem__(self, item: Union[str, int], data: Union[str, int, list[Spirit, Skill]]):
        if isinstance(item, str):
            self._data[item] = data
        else:
            self._data[self.propertys[item]] = data

    def __repr__(self):
        text = '\nChar Info:'
        for k, v in self._data.items():
            text += f'\n{k}：{v}'
        return text
