#!/usr/bin/env python
# -*- coding: utf-8 -*-

from struct import unpack, pack_into


class Command:
    def __init__(self, buffer: bytearray = None, pos: int = 0x0):
        super().__init__()
        self.buffer = buffer
        self.pos = pos
        self.code: int = 0xFF
        self.count: int = 0x0
        self.argv: list[int] = list()
        self.parse()

    def parse(self):
        if not self.buffer:
            return
        self.code = self.buffer[0]
        self.count = self.buffer[1]
        self.argv = list(unpack('H' * (self.count - 1), self.buffer[2:]))

    def build(self):
        count = len(self.argv) + 1
        buffer = bytearray(count * 2)
        buffer[0] = self.code
        buffer[1] = count
        pack_into('H' * (count - 1), buffer, 0x2, *self.argv)
        self.buffer = buffer
        self.parse()

    @property
    def length(self):
        return len(self.buffer)

    def __getitem__(self, idx: int):
        if idx == 0:
            return f'<0x{self.pos:04X}>'
        return ' '.join(map(lambda x: f'{x:04X}', self.argv))

    def __repr__(self):
        return f'0x{self.pos:04X} <0x{self.code:02X}> ' + \
               ' '.join([f'{argv:04X}' for argv in self.argv])
