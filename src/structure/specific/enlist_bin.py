#!/usr/bin/env python
# -*- coding: utf-8 -*-

from structure.generic import Rom, Value, Sequence

ENEMY_STRUCTURE = {
    '机体': Value(0x0, 0x2),
    '机体改造': Value(0x2, 0x1),
    '武器改造': Value(0x3, 0x1),
    '机师': Value(0x4, 0x2),
    '机师等级': Value(0x6, 0x2),
    '坐标X': Value(0x8, 0x1),
    '坐标Y': Value(0x9, 0x1),
    '携带道具': Value(0xA, 0x1),
    '所属批次': Value(0xB, 0x1),
}

ENLIST_STRUCTURE = {
    '总机体数': Value(0x0, 0x2),
    '批次数': Value(0x2, 0x2),
    '第00批': Value(0x4, 0x1),
    '第01批': Value(0x5, 0x1),
    '第02批': Value(0x6, 0x1),
    '第03批': Value(0x7, 0x1),
    '第04批': Value(0x8, 0x1),
    '第05批': Value(0x9, 0x1),
    '第06批': Value(0xA, 0x1),
    '第07批': Value(0xB, 0x1),
    '第08批': Value(0xC, 0x1),
    '第09批': Value(0xD, 0x1),
    '第10批': Value(0xE, 0x1),
    '第11批': Value(0xF, 0x1),
    '第12批': Value(0x10, 0x1),
    '第13批': Value(0x11, 0x1),
    '第14批': Value(0x12, 0x1),
    '第15批': Value(0x13, 0x1),
    '机体列表': Sequence(ENEMY_STRUCTURE, 0x14, 0xC, 0xA0),
}


class EnlistBIN(Rom):
    def __init__(self):
        super(EnlistBIN, self).__init__()
        self.structures: dict[str, Value | Sequence] = {
            '敌方列表': Sequence(ENLIST_STRUCTURE, 0x0, 0x794, 0x96),
        }

    def parse(self) -> bool:
        if not self.buffer:
            return False
        for pname, structure in self.structures.items():
            self._data[pname] = structure.parse(self.buffer)
        return True

    def build(self) -> bool:
        if not self._data:
            return False
        for pname, data in self._data.items():
            self.structures[pname].build(data, self.buffer)
        return True
