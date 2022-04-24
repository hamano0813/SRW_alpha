#!/usr/bin/env python
# -*- coding: utf-8 -*-

from structure.generic import Rom, Sequence
from .unit import Unit


class RobotRAF(Rom):
    def __init__(self):
        super(RobotRAF, self).__init__()
        self.structures: dict[str, Sequence] = {
            '机体': Unit(0x0, 0x2C4, 0x1E6)
        }

    def parse(self) -> bool:
        if not self.buffer:
            return False
        for pname, structure in self.structures.items():
            self._data[pname] = structure.parse(self.buffer)
        return True

    def build(self) -> bool:
        if not self._data:
            return False
        for pname, data in self._data.items():
            self.structures[pname].build(data, self.buffer)
        return True

    def __repr__(self):
        return f'ROBOT.RAF with {self.structures["机体"].count} units'
