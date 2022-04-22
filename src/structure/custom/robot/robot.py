#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Optional
from ..rom import ROM
from .unit import Unit


class ROBOT(ROM):
    def __init__(self):
        super(ROBOT, self).__init__()
        self.units: list[Unit] = list()

    def parse(self) -> bool:
        if not self.buffer:
            return False
        self.units = [Unit(self.buffer[Unit.length * idx: Unit.length * (1 + idx)])
                      for idx in range(Unit.count)]
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

    def __getitem__(self, idx) -> Optional[Unit]:
        if len(self.units) > idx:
            return self.units[idx]
        return None

    def __repr__(self) -> str:
        return f'ROBOT.RAF with {Unit.count} units'
