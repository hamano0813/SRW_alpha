#!/usr/bin/env python
# -*- coding: utf-8 -*-

from structure.generic import Value, Sequence, SEQUENCE
from .instruction import Instruction, INSTRUCTION_STRUCTURE

SCREENPLAY_STRUCTURE = {
    '指令数量': Value(0x0, 0x4),
    '指令列表': Instruction(INSTRUCTION_STRUCTURE, 0x0, 0x0, 0x0),
}


class ScreenPlay(Sequence):
    def __init__(self, structures, offset, length, count):
        super(ScreenPlay, self).__init__(structures, offset, length, count)
        self.pointers: list[dict[str, int]] = list()

    def parse(self, buffer: bytearray) -> SEQUENCE:
        sequence = list()
        for idx in range(self.count):
            record = dict()
            _buffer = buffer[self._idx_range(idx)]
            record['指令数量'] = self.structures['指令列表'].count = self.structures['指令数量'].parse(_buffer)
            record['指令列表'] = self.structures['指令列表'].parse(_buffer)
            sequence.append(record)
        return sequence

    def build(self, sequence: SEQUENCE, buffer: bytearray) -> bytearray:
        for idx, record in enumerate(sequence):
            _buffer = bytearray(0x4)
            record['指令数量'] = self.structures['指令列表'].count = len(record['指令列表'])
            self.structures['指令数量'].build(record['指令数量'], _buffer)
            self.structures['指令列表'].build(record['指令列表'], _buffer)
            buffer[self._idx_range(idx)] = _buffer
        return buffer

    def _idx_range(self, idx: int) -> slice:
        return slice(self.pointers[idx]['指针'], self.pointers[idx + 1]['指针'])
