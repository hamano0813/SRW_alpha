#!/usr/bin/env python
# -*- coding: utf-8 -*-

from structure.generic import Rom, Value, Sequence
from .scenario import Scenario, SCENARIO_STRUCTURE


class SndataBIN(Rom):
    header = 0x800

    def __init__(self):
        super(SndataBIN, self).__init__()
        self.structures: dict[str, Value | Sequence | Scenario] = {
            '指针列表': Sequence({'指针': Value(0x0, 0x4)}, 0x0, 0x4, 0x8D),
            '场景列表': Scenario(SCENARIO_STRUCTURE, 0x800, 0x0, 0x8C),
        }

    def parse(self) -> bool:
        if not self.buffer:
            return False
        self['指针列表'] = self.structures['指针列表'].parse(self.buffer)
        for idx in range(self.structures['场景列表'].count):
            length = self['指针列表'][idx + 1]['指针'] - self['指针列表'][idx]['指针']
            self.structures['场景列表'].length_list.append(length)
        self['场景列表'] = self.structures['场景列表'].parse(self.buffer)
        return True

    def build(self) -> bool:
        if not self._data:
            return False
        offset = self.structures['场景列表'].offset
        self['指针列表'] = [{'指针': offset}]
        for length in self.structures['场景列表'].length_list:
            offset += length
            self['指针列表'].append({'指针': offset})
        buffer = bytearray([0xFF] * self.header)
        self.structures['指针列表'].build(self['指针列表'], buffer)
        self.buffer = buffer + self.structures['场景列表'].build(self['场景列表'])
        return True
