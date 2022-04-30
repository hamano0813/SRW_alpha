#!/usr/bin/env python
# -*- coding: utf-8 -*-

from structure.generic import Value, Sequence, SEQUENCE

AI_STRUCTURE = {
    '空数据': Value(0x0, 0x2),
    'AI数量': Value(0x2, 0x2),
    'AI长度': Value(0x4, 0x2),
    'AI列表'
}


class Ai(Sequence):
    def __init__(self, structures, offset, length, count):
        super(Ai, self).__init__(structures, offset, length, count)
        self.pointers: list[int] = list()

    def parse(self, buffer: bytearray) -> SEQUENCE:
        sequence = list()
        return sequence

    def build(self, sequence: SEQUENCE, buffer: bytearray) -> bytearray:
        pass

    def _idx_range(self, idx: int) -> slice:
        return slice(self.pointers[idx], self.pointers[idx + 1])
