#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Union
from ...common import Value


class Skill:
    count = 0x3
    length = 0xA

    def __init__(self, buffer: bytearray):
        self.buffer = buffer
        self.settings = {
            '技能': Value(0x0, 0x1),
            'Lv１': Value(0x1, 0x1),
            'Lv２': Value(0x2, 0x1),
            'Lv３': Value(0x3, 0x1),
            'Lv４': Value(0x4, 0x1),
            'Lv５': Value(0x5, 0x1),
            'Lv６': Value(0x6, 0x1),
            'Lv７': Value(0x7, 0x1),
            'Lv８': Value(0x8, 0x1),
            'Lv９': Value(0x9, 0x1),
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
        text = '\nSkill Info:'
        for k, v in self._data.items():
            text += f'\n{k}：{v}'
        return text
