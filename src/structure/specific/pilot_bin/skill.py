#!/usr/bin/env python
# -*- coding: utf-8 -*-

from structure.generic import Value, Sequence


class Skill(Sequence):
    def __init__(self, offset, length, count):
        super(Skill, self).__init__(offset, length, count)
        self.structures = {
            '技能': Value(0x0, 0x1),
            'Lv1': Value(0x1, 0x1),
            'Lv2': Value(0x2, 0x1),
            'Lv3': Value(0x3, 0x1),
            'Lv4': Value(0x4, 0x1),
            'Lv5': Value(0x5, 0x1),
            'Lv6': Value(0x6, 0x1),
            'Lv7': Value(0x7, 0x1),
            'Lv8': Value(0x8, 0x1),
            'Lv9': Value(0x9, 0x1),
        }
