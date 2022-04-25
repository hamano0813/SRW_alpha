#!/usr/bin/env python
# -*- coding: utf-8 -*-

from structure.generic import Rom, Value, Text, Sequence
from parameter import TEXT

SNMSG = {
    '文本': Text(0x0, 0x100, 'shiftjisx0213', TEXT),
}


class SnmsgBIN(Rom):
    def __init__(self):
        super(SnmsgBIN, self).__init__()
        self.structures: dict[str, Value | Sequence] = {
            '场景文本': Sequence(SNMSG, 0x0, 0x100, 0x7F1F),
        }

    def parse(self) -> bool:
        if not self.buffer:
            return False
        for pname, structure in self.structures.items():
            self._data[pname] = structure.parse(self.buffer)
        return True

    def build(self) -> bool:
        if not self._data:
            return False
        for pname, data in self._data.items():
            self.structures[pname].build(data, self.buffer)
        return True
