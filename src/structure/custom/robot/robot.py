#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..rom import ROM


class ROBOT(ROM):
    count = 0x1E6

    def __init__(self):
        super(ROBOT, self).__init__()
        self.units: list = list()

    def parse(self) -> bool:
        pass

    def build(self) -> bool:
        pass

    def __getitem__(self, r_idx):
        if len(self.units) > r_idx:
            return self.units[r_idx]
        return None

    def __repr__(self):
        return f'ROBOT.RAF with {self.count} units'
