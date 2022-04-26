#!/usr/bin/env python
# -*- coding: utf-8 -*-

from struct import unpack, pack_into


class Command:
    def __init__(self, buffer: bytearray = None, pos: int = 0x0):
        super().__init__()
        self.buffer = buffer
        self.pos = pos
        self.code: int = 0x00
        self.count: int = 0x1
        self.argv: list[int] = list()
        self.parse()

    def parse(self) -> bool:
        if not self.buffer:
            return False
        self.code = self.buffer[0]
        self.count = self.buffer[1]
        self.argv = list(unpack('H' * (self.count - 1), self.buffer[2:]))
        return True

    def build(self) -> bool:
        count = len(self.argv) + 1
        buffer = bytearray(count * 2)
        buffer[0] = self.code
        buffer[1] = count
        pack_into('H' * (count - 1), buffer, 0x2, *self.argv)
        self.buffer = buffer
        return self.parse()

    @property
    def length(self) -> int:
        return len(self.buffer)

    def __getitem__(self, idx: int) -> str:
        if idx == 0:
            return f'<0x{self.pos:04X}>'
        elif idx == 1:
            return ' '.join(map(lambda x: f'{x:04X}', self.argv))
        elif idx == 2:
            # TODO
            return ''

    def __repr__(self):
        return f'0x{self.pos:04X} <0x{self.code:02X}> ' + \
               ' '.join([f'{argv:04X}' for argv in self.argv])
