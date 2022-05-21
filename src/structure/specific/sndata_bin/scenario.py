#!/usr/bin/env python
# -*- coding: utf-8 -*-

from structure.generic import Value, Sequence, SEQUENCE
from structure.specific.sndata_bin.command import Command

SCENARIO_STRUCTURE = {
    'Index Quantity': Value(0x0, 0x4),
    'Index Length': Value(0x4, 0x4),
    'Indexes': Sequence({'Index': Value(0x0, 0x4)}, 0x8, 0x4, 0x0B),
    'Commands': Command(0x48, 0x4000),
}


class Scenario(Sequence):
    def __init__(self, structures, offset, length, count):
        super(Scenario, self).__init__(structures, offset, length, count)

    def build(self, sequence: SEQUENCE, buffer: bytearray = None) -> bytearray:
        for idx, scenario in enumerate(sequence):
            for command in scenario['Commands']:
                if command['Code'] == 0x00:
                    block_idx = command['Param'][0]
                    scenario['Indexes'][block_idx]['Index'] = command['Pos']
            _buffer = bytearray([0xFF] * self.length)
            for key, data in scenario.items():
                self.structures[key].build(data, _buffer)
            buffer[self._idx_range(idx)] = _buffer
        return buffer
