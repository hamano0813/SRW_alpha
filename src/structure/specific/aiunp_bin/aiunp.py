#!/usr/bin/env python
# -*- coding: utf-8 -*-

from structure.generic import Rom, Value, Sequence
from .ai import AiSetting, SETTING_STRUCTURE


class AiunpBIN(Rom):
    def __init__(self):
        super(AiunpBIN, self).__init__()
        self.structures = {
            '指針リスト': Sequence({'指針': Value(0x0, 0x4)}, 0x0, 0x4, 0x8D),
            'AI設定': AiSetting(SETTING_STRUCTURE, 0x800, 0x0, 0x8C),
        }

    def parse(self) -> bool:
        if not self.buffer:
            return False
        self['指針リスト'] = self.structures['AI設定'].pointers = self.structures['指針リスト'].parse(self.buffer)
        self['AI設定'] = self.structures['AI設定'].parse(self.buffer)
        return True
