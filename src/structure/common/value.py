#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Union
from struct import unpack_from, pack_into


class Value:
    length_format = {0x1: 'B', 0x2: 'H', 0x4: 'I', 0x8: 'Q', -0x1: 'b', -0x2: 'h', -0x4: 'i', -0x8: 'q'}

    def __init__(self, offset, length, bit=None):
        self.offset: int = offset
        self.fmt = self.length_format[length]
        self.bit: Union[int, tuple] = bit

    def get(self, buffer: bytearray) -> int:
        data = unpack_from(self.fmt, buffer, self.offset)[0]
        if self.bit is not None:
            return self._load_bin(data)
        return data

    def set(self, value: int, buffer: bytearray) -> int:
        if self.bit is not None:
            data = self._save_bin(unpack_from(self.fmt, buffer, self.offset)[0], value)
        else:
            data = value
        pack_into(self.fmt, buffer, self.offset, data)
        return data

    def _load_bin(self, value: int) -> int:
        if isinstance(self.bit, int):
            return (value & (1 << self.bit)) >> self.bit
        return (value & ((1 << self.bit[1]) - 1)) >> self.bit[0]

    def _save_bin(self, data: int, value: int) -> int:
        if isinstance(self.bit, int):
            return data | (1 << self.bit) if value else data & ~ (1 << self.bit)
        return ((data >> self.bit[1]) << self.bit[1]) | (data & ((1 << self.bit[0]) - 1)) | (value << self.bit[0])
