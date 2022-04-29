#!/usr/bin/env python
# -*- coding: utf-8 -*-

from structure.generic import Rom, Value, Text, Sequence
from parameter import TEXT

SNMSG_STRUCTURE = {'文本': Text(0x0, 0x100, 'shiftjisx0213', TEXT)}


class SnmsgBIN(Rom):
    def __init__(self):
        super(SnmsgBIN, self).__init__()
        self.structures = {
            '文本列表': Sequence(SNMSG_STRUCTURE, 0x0, 0x100, 0x7F1F),
        }
