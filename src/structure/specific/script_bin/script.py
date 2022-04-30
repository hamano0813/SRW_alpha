#!/usr/bin/env python
# -*- coding: utf-8 -*-

from structure.generic import Rom, Value, Sequence
from .screenplay import ScreenPlay, SCREENPLAY_STRUCTURE


class ScriptBIN(Rom):
    def __init__(self):
        super(ScriptBIN, self).__init__()
        self.structures = {
            '指针列表': Sequence({'指针': Value(0x0, 0x4)}, 0x0, 0x4, 0xFF),
            '剧本列表': ScreenPlay(SCREENPLAY_STRUCTURE, 0x3FC, 0x0, 0xFE),
        }

    def parse(self) -> bool:
        if not self.buffer:
            return False
        self._data['指针列表'] = self.structures['剧本列表'].pointers = self.structures['指针列表'].parse(self.buffer)
        self._data['剧本列表'] = self.structures['剧本列表'].parse(self.buffer)
        return True
