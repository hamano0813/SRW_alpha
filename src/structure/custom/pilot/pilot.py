#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..rom import ROM
from .char import Char


class PILOT(ROM):
    header = 0x4

    def __init__(self):
        super(PILOT, self).__init__()
        self.chars: list = list()

    def parse(self) -> bool:
        if not self.buffer:
            return False
        Char.count = int.from_bytes(self.buffer[:self.header], 'little')
        self.chars = [Char(self.buffer[self.header + Char.length * idx: self.header + Char.length * (1 + idx)])
                      for idx in range(Char.count)]
        return True

    def build(self) -> bool:
        if not self.chars:
            return False
        buffer = bytearray(Char.count.to_bytes(self.header, 'little'))
        for char in self.chars:
            char.build()
            buffer += char.buffer
        self.buffer = buffer
        return True

    def __getitem__(self, idx):
        if len(self.chars) > idx:
            return self.chars[idx]
        return None

    def __repr__(self):
        return f'PILOT.BIN with {Char.count} chars'
