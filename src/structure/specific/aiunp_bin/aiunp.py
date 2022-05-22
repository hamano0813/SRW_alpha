#!/usr/bin/env python
# -*- coding: utf-8 -*-

from structure.generic import Rom, Value, Sequence
from structure.specific.aiunp_bin.ai import AiSetting, SETTING_STRUCTURE


class AiunpBIN(Rom):
    def __init__(self):
        super(AiunpBIN, self).__init__()
        self.structures = {
            '指针列表': Sequence({'指针': Value(0x0, 0x4)}, 0x0, 0x4, 0x8D),
            'AI设计': AiSetting(SETTING_STRUCTURE, 0x800, 0x0, 0x8C),
        }

    def parse(self) -> bool:
        if not self.buffer:
            return False
        self['指针列表'] = self.structures['AI设计'].pointers = self.structures['指针列表'].parse(self.buffer)
        self['AI设计'] = self.structures['AI设计'].parse(self.buffer)
        return True
