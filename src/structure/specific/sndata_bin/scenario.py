#!/usr/bin/env python
# -*- coding: utf-8 -*-

from structure.generic import Value, Sequence, SEQUENCE
from .command import Command

SCENARIO_STRUCTURE = {
    '指针数量': Value(0x0, 0x4),
    '指针长度': Value(0x4, 0x4),
    '指针列表': Sequence({'指针': Value(0x0, 0x4)}, 0x8, 0x4, 0x0B),
    '指令列表': Command(0x48, 0x4000),
}


class Scenario(Sequence):
    def __init__(self, structures, offset, length, count):
        super(Scenario, self).__init__(structures, offset, length, count)

    def build(self, sequence: SEQUENCE, buffer: bytearray = None) -> bytearray:
        for idx, scenario in enumerate(sequence):
            for command in scenario['指令列表']:
                if command['指令码'] == 0x00:
                    block_idx = command['参数列表'][0]
                    scenario['指针列表'][block_idx]['指针'] = command['定位']
            _buffer = bytearray([0xFF] * self.length)
            for key, data in scenario.items():
                self.structures[key].build(data, _buffer)
            buffer[self._idx_range(idx)] = _buffer
        return buffer
