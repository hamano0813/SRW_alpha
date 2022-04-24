#!/usr/bin/env python
# -*- coding: utf-8 -*-

from structure.generic import Rom, Value, Sequence
from .char import Char


class PilotBIN(Rom):
    def __init__(self):
        super(PilotBIN, self).__init__()
        self.structures: dict[str, Sequence] = {
            '数量': Value(0x0, 0x4),
            '机师': Char(0x4, 0x70, 0x1D5)
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
        # self._data['数量'] = self.structures['机师'].count
        for pname, data in self._data.items():
            self.structures[pname].build(data, self.buffer)
        return True

    def __repr__(self):
        return f'PILOT.BIN with {self._data["数量"]} chars'
