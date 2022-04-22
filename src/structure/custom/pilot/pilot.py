#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..rom import ROM


class PILOT(ROM):
    count = 0x1D5

    def __init__(self):
        super(PILOT, self).__init__()
        self.chars: list = list()

    def parse(self) -> bool:
        pass

    def build(self) -> bool:
        pass

    def __getitem__(self, p_idx):
        if len(self.chars) > p_idx:
            return self.chars[p_idx]
        return None

    def __repr__(self):
        return f'PILOT.BIN with {self.count} characters'
