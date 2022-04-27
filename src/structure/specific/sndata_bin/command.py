#!/usr/bin/env python
# -*- coding: utf-8 -*-

from struct import pack, unpack
from .explain import Explain


class Command:
    def __init__(self, buffer: bytearray = None, pos: int = 0x0):
        super().__init__()
        self.buffer = buffer
        self._data: dict[str, int | list[int]] = {'定位': pos, '指令码': 0x01, '参数': list()}
        self.count: int = 0x1
        self.explain = Explain()
        self.parse()

    def parse(self) -> bool:
        if not self.buffer:
            return False
        self._data['指令码'] = self.buffer[0]
        self.count = self.buffer[1]
        argv_buffer = self.buffer[2:]
        argv_struct = self.explain.argv_struct[self._data['指令码']][0]
        if self._data['指令码'] == 0xB9:
            argv_struct = 'h' * (self.count - 1)
        self._data['参数'] = list(unpack(argv_struct, argv_buffer))
        return True

    def build(self) -> bool:
        argv_struct = self.explain.argv_struct[self._data['指令码']][0]
        if self._data['指令码'] == 0xB9:
            argv_struct = 'h' * (len(self._data['参数']))
        argv_buffer = pack(argv_struct, *self._data['参数'])
        self.count = len(argv_buffer) // 2 + 1
        code_buffer = bytearray(2)
        code_buffer[0] = self._data['指令码']
        code_buffer[1] = self.count
        self.buffer = code_buffer + argv_buffer
        return self.parse()

    @property
    def length(self) -> int:
        return len(self.buffer)

    def __getitem__(self, item: str) -> int | str | list:
        if item == '参数码':
            argv_buffer = self.buffer[2:]
            return ' '.join([f'{argv:04X}' for argv in unpack('h' * (self.count - 1), argv_buffer)])
        if item == '注释':
            return ''
        return self._data.get(item)

    def __repr__(self) -> str:
        return ' '.join([f'0x{self["定位"]:04X}', f'<0x{self["指令码"]:02X}>', f'{self["参数码"]}', f'{self["注释"]}'])
