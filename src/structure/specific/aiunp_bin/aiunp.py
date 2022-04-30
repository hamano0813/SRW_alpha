#!/usr/bin/env python
# -*- coding: utf-8 -*-

from structure.generic import Rom, Value, Sequence
from .ai import Ai, AI_STRUCTURE


class AiunpBIN(Rom):
    def __init__(self):
        super(AiunpBIN, self).__init__()
        self.structures = {
            '指针列表': Sequence({'指针': Value(0x0, 0x4)}, 0x0, 0x4, 0x8C),
            '场景列表': Ai(AI_STRUCTURE, 0x800, 0x0, 0x8B),
        }

    def parse(self) -> bool:
        if not self.buffer:
            return False
        self._data['指针列表'] = self.structures['场景列表'].pointers = self.structures['指针列表'].parse(self.buffer)
        self._data['场景列表'] = self.structures['AI列表'].parse(self.buffer)
        return True
