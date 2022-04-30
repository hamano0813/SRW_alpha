#!/usr/bin/env python
# -*- coding: utf-8 -*-

from structure.generic import Value, Sequence, SEQUENCE

AI_STRUCTURE = {
    'AI人物': Value(0x0, 0x2),
    '未知1': Value(0x2, 0x1),
    '未知2': Value(0x3, 0x1),
    '未知3': Value(0x4, 0x1),
    '有效': Value(0x5, 0x1, 0),
    '开始移动': Value(0x5, 0x1, (1, 4)),
    '未知4': Value(0x5, 0x1, (4, 8)),
    '目标人物': Value(0x6, 0x2),
    '坐标X': Value(0x8, 0x1),
    '坐标Y': Value(0x9, 0x1),
}

SETTING_STRUCTURE = {
    '空数据': Value(0x0, 0x2),
    'AI数量': Value(0x2, 0x2),
    'AI长度': Value(0x4, 0x2),
    'AI列表': Sequence(AI_STRUCTURE, 0x6, 0xA, 0x0)
}


class AiSetting(Sequence):
    def __init__(self, structures, offset, length, count):
        super(AiSetting, self).__init__(structures, offset, length, count)
        self.pointers: list[dict[str, int]] = list()

    def parse(self, buffer: bytearray) -> SEQUENCE:
        sequence = list()
        for idx in range(self.count):
            record = dict()
            _buffer = buffer[self._idx_range(idx)]
            record['空数据'] = self.structures['空数据'].parse(_buffer)
            record['AI数量'] = self.structures['AI列表'].count = self.structures['AI数量'].parse(_buffer)
            record['AI长度'] = self.structures['AI长度'].parse(_buffer)
            record['AI列表'] = self.structures['AI列表'].parse(_buffer)
            sequence.append(record)
        return sequence

    def build(self, sequence: SEQUENCE, buffer: bytearray) -> bytearray:
        for idx, record in enumerate(sequence):
            count = self.structures['AI列表'].count = record['AI数量'] = len(record['AI列表'])
            length = self._calc_length(0xA * count + 0x6)
            self.pointers[idx + 1]['指针'] = self.pointers[idx]['指针'] + length
            _buffer = bytearray(length)
            for key, data in record.items():
                self.structures[key].build(data, _buffer)
            buffer[self._idx_range(idx)] = _buffer
        return buffer

    def _idx_range(self, idx: int) -> slice:
        return slice(self.pointers[idx]['指针'], self.pointers[idx + 1]['指针'])

    @staticmethod
    def _calc_length(value: int, step: int = 0x4) -> int:
        return (value // step + bool(value % step)) * step
