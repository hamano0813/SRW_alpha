#!/usr/bin/env python
# -*- coding: utf-8 -*-

from struct import unpack_from, pack_into
from ..rom import ROM
from .scenario import Scenario


class SNDATA(ROM):
    header = 0x800
    count = 0x8C

    def __init__(self):
        super(SNDATA, self).__init__()
        self.pointer: list[int] = list()
        self.scenario: list[Scenario] = list()

    def parse(self) -> bool:
        if not self.buffer:
            return False
        self.pointer = list(unpack_from(f'{self.count + 1}L', self.buffer))
        self.scenario = [Scenario(self.buffer[self.pointer[idx]:self.pointer[idx + 1]]) for idx in range(self.count)]
        return True

    def build(self) -> bool:
        if not self.scenario:
            return False
        buffer = bytearray(self.header)
        offset = self.header
        pack_into('L', buffer, 0x0, offset)
        for idx, scenario in enumerate(self.scenario):
            scenario.build()
            offset += len(scenario)
            self.pointer[idx + 1] = offset
            pack_into('L', buffer, 0x4 + 0x4 * idx, offset)
            buffer += scenario.buffer
        self.buffer = buffer
        self.parse()
        return True

    def __getitem__(self, idx: int):
        if len(self.scenario) > idx:
            return self.scenario[idx]
        return None

    def __repr__(self):
        return f'SNDATA.BIN with {self.count} Scenarios'
