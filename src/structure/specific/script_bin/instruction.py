#!/usr/bin/env python
# -*- coding: utf-8 -*-

from structure.generic import Value, Text, Sequence, SEQUENCE
from parameter import SCRIPT_TEXT_EXTRA

INSTRUCTION_STRUCTURE = {
    '指令码': Value(0x0, 0x2),
    '参数一': Value(0x2, 0x2),
    '参数二': Value(0x4, 0x2),
    '扩展字节': Value(0x6, 0x2),
    '扩展文本': Text(0x8, 0x0, 'shiftjisx0213', SCRIPT_TEXT_EXTRA),
}


class Instruction(Sequence):
    def __init__(self, structures, offset, length, count):
        super(Instruction, self).__init__(structures, offset, length, count)

    def parse(self, buffer: bytearray) -> SEQUENCE:
        sequence = list()
        offset = self.offset
        for idx in range(self.count):
            record = dict()
            _buffer = buffer[offset:offset + 0xFF]
            record['指令码'] = self.structures['指令码'].parse(_buffer)
            record['参数一'] = self.structures['参数一'].parse(_buffer)
            record['参数二'] = self.structures['参数二'].parse(_buffer)
            record['扩展字节'] = self.structures['扩展文本'].length = self.structures['扩展字节'].parse(_buffer)
            record['扩展文本'] = self.structures['扩展文本'].parse(_buffer)
            length = self._calc_length(0x8 + record['扩展字节'])
            offset += length
            sequence.append(record)
        return sequence

    def build(self, sequence: SEQUENCE, buffer: bytearray) -> bytearray:
        for idx, record in enumerate(sequence):
            length = self.structures['扩展文本'].length = record['扩展字节']
            _buffer = bytearray(0x8 + length)
            for key, data in record.items():
                self.structures[key].build(data, _buffer)
            complement_buf = bytearray([0x0, 0xD4, 0x41])[0: self._calc_length(length) - length]
            _buffer += complement_buf
            buffer += _buffer
        return buffer

    @staticmethod
    def _calc_length(value: int, step: int = 0x4) -> int:
        return (value // step + bool(value % step)) * step
