#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..rom import ROM
from .unit import Unit


class ROBOT(ROM):
    count = 0x1E6

    def __init__(self):
        super(ROBOT, self).__init__()
        self.units: list[Unit] = list()

    def parse(self) -> bool:
        if not self.buffer:
            return False
        self.units = [Unit(self.buffer[Unit.length * idx: Unit.length * (1 + idx)]) for idx in range(self.count)]
        return True

    def build(self) -> bool:
        if not self.units:
            return False
        buffer = bytearray()
        for unit in self.units:
            unit.build()
            buffer += unit.buffer
        self.buffer = buffer
        return True

    def __getitem__(self, r_idx):
        if len(self.units) > r_idx:
            return self.units[r_idx]
        return None

    def __repr__(self):
        return f'ROBOT.RAF with {self.count} units'
