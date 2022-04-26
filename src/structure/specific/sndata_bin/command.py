#!/usr/bin/env python
# -*- coding: utf-8 -*-

from struct import unpack, pack_into




class Command:
    def __init__(self, buffer: bytearray = None, pos: int = 0x0):
        super().__init__()
        self.buffer = buffer
        self._data: dict[str, int | list[int]] = {'定位': pos, '指令码': 0x01, '指令长度': 0x1, '参数': list(), '释义': ''}
        self.parse()

    def parse(self) -> bool:
        if not self.buffer:
            return False
        self._data['指令码'] = self.buffer[0]
        self._data['长度'] = self.buffer[1]
        self._data['参数'] = list(unpack('H' * (self._data['长度'] - 1), self.buffer[2:]))
        return True

    def build(self) -> bool:
        count = len(self._data['参数']) + 1
        buffer = bytearray(count * 2)
        buffer[0] = self._data['指令码']
        buffer[1] = count
        pack_into('H' * (count - 1), buffer, 0x2, *self._data['参数'])
        self.buffer = buffer
        return self.parse()

    @property
    def length(self) -> int:
        return len(self.buffer)

    def __getitem__(self, item: str) -> int | list:
        return self._data.get(item)

    def __repr__(self):
        return f'0x{self._data["定位"]:04X} <0x{self._data["指令码"]:02X}> ' + \
               ' '.join([f'{argv:04X}' for argv in self._data['参数']])
