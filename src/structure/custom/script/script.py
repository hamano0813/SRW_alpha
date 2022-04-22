#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..rom import ROM


class SCRIPT(ROM):
    count = 0x7F1F

    def __init__(self):
        super(SCRIPT, self).__init__()
        self.scripts: list = list()

    def parse(self) -> bool:
        pass

    def build(self) -> bool:
        pass

    def __getitem__(self, s_idx):
        if len(self.scripts) > s_idx:
            return self.scripts[s_idx]
        return None

    def __repr__(self):
        return f'SCRIPT.BIN with {self.count} scripts'
