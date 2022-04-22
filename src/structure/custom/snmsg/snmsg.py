#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..rom import ROM


class SNMSG(ROM):
    count = 0x7F1F

    def __init__(self):
        super(SNMSG, self).__init__()
        self.msgs: list = list()

    def parse(self) -> bool:
        pass

    def build(self) -> bool:
        pass

    def __getitem__(self, m_idx):
        if len(self.msgs) > m_idx:
            return self.msgs[m_idx]
        return None

    def __repr__(self):
        return f'SNMSG.BIN with {self.count} messages'
