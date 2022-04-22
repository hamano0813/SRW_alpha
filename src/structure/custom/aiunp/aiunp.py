#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..rom import ROM


class AIUNP(ROM):
    count = 0x7F1F

    def __init__(self):
        super(AIUNP, self).__init__()
        self.ai: list = list()

    def parse(self) -> bool:
        pass

    def build(self) -> bool:
        pass

    def __getitem__(self, e_idx):
        if len(self.ai) > e_idx:
            return self.ai[e_idx]
        return None

    def __repr__(self):
        return f'AIUNP.BIN with {self.count} scenarios'
