#!/usr/bin/env python
# -*- coding: utf-8 -*-

from struct import unpack_from, pack_into
from structure.generic import Rom
from .scenario import Scenario


class SndataBIN(Rom):
    header = 0x800
    count = 0x8C

    def __init__(self):
        super(SndataBIN, self).__init__()
        self._data: dict[str, list[int | Scenario]] = dict()

    def parse(self) -> bool:
        if not self.buffer:
            return False
        self._data['指针'] = list(unpack_from(f'{self.count + 1}L', self.buffer))
        self._data['场景设计'] = [
            Scenario(self.buffer[self._data['指针'][idx]:self._data['指针'][idx + 1]])
            for idx in range(self.count)]
        return True

    def build(self) -> bool:
        if not self._data['场景设计']:
            return False
        buffer = bytearray(self.header)
        offset = self.header
        pack_into('L', buffer, 0x0, offset)
        for idx, scenario in enumerate(self._data['场景设计']):
            scenario.build()
            offset += len(scenario)
            self._data['指针'][idx + 1] = offset
            pack_into('L', buffer, 0x4 + 0x4 * idx, offset)
            buffer += scenario.buffer
        self.buffer = buffer
        self.parse()
        return True

    def __getitem__(self, item: str) -> list[int, Scenario]:
        return self._data.get(item)

    def __repr__(self) -> str:
        return f'SNDATA.BIN with {self.count} Scenarios'
