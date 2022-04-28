#!/usr/bin/env python
# -*- coding: utf-8 -*-

from structure.generic import Value, Sequence
from .command import Command, COMMAND_STRUCTURE

SCENARIO_STRUCTURE = {
    '指针数量': Value(0x0, 0x4),
    '指针长度': Value(0x4, 0x4),
    '指针列表': Sequence(Value(0x0, 0x4), 0x8, 0x0, 0x0),
    '指令列表': Command(COMMAND_STRUCTURE, 0x48, 0x0, 0x0),
}


class Scenario(Sequence):
    header: int = 0x48

    def __init__(self, structures, offset, length, count):
        super(Scenario, self).__init__(structures, offset, length, count)
        self.length_list: list[int] = list()

    def parse(self, buffer: bytearray) -> list[dict[str, int | str | list[dict]]]:
        sequence = list()
        for idx in range(self.count):
            record = dict()
            _buffer = buffer[self._index_range(idx)]
            for pname, structure in self.structures.items():
                record[pname] = structure.parse(_buffer)
            sequence.append(record)
        return sequence

    def build(self, sequence: list[dict[str, int | str | list[dict]]], buffer: bytearray = None) -> bytearray:
        buffer = bytearray()
        for scenario in sequence:
            _buffer = bytearray(0x48)
            c_buffer = self.structures['指令列表'].build(scenario['指令列表'], buffer)

    def _index_range(self, idx: int) -> slice:
        index_range: list[slice] = list()
        offset = self.offset
        for length in self.length_list:
            index_range.append(slice(offset, offset + length))
            offset += length
        return index_range[idx]
