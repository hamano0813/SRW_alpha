#!/usr/bin/env python
# -*- coding: utf-8 -*-

from structure.generic import Value, Sequence


class Spirit(Sequence):
    def __init__(self, offset, length, count):
        super(Spirit, self).__init__(offset, length, count)
        self.structures = {
            '精神': Value(0x0, 0x1),
        }


class SpiritLv(Sequence):
    def __init__(self, offset, length, count):
        super(SpiritLv, self).__init__(offset, length, count)
        self.structures = {
            '精神Lv': Value(0x0, 0x1),
        }
