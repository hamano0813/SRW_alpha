#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..rom import ROM


class ENLIST(ROM):
    count = 0x7F1F

    def __init__(self):
        super(ENLIST, self).__init__()
        self.enemys: list = list()

    def parse(self) -> bool:
        pass

    def build(self) -> bool:
        pass

    def __getitem__(self, e_idx):
        if len(self.enemys) > e_idx:
            return self.enemys[e_idx]
        return None

    def __repr__(self):
        return f'ENLIST.BIN with {self.count} scenarios'
