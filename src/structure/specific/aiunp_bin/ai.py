#!/usr/bin/env python
# -*- coding: utf-8 -*-

from structure.generic import Value, Sequence, SEQUENCE

AI_STRUCTURE = {
    'AI': Value(0x0, 0x2),
    '不明1_0': Value(0x2, 0x1, 0),
    '不明1_1': Value(0x2, 0x1, 1),
    '不明1_2': Value(0x2, 0x1, 2),
    '不明1_3': Value(0x2, 0x1, 3),
    '不明1_4': Value(0x2, 0x1, 4),
    '不明1_5': Value(0x2, 0x1, 5),
    '不明1_6': Value(0x2, 0x1, 6),
    '不明1_7': Value(0x2, 0x1, 7),
    '不明2': Value(0x3, 0x1),
    '不明3_0': Value(0x4, 0x1, 0),
    '不明3_1': Value(0x4, 0x1, 1),
    '不明3_2': Value(0x4, 0x1, 2),
    '不明3_3': Value(0x4, 0x1, 3),
    '不明3_4': Value(0x4, 0x1, 4),
    '不明3_5': Value(0x4, 0x1, 5),
    '不明3_6': Value(0x4, 0x1, 6),
    '不明3_7': Value(0x4, 0x1, 7),
    '有効': Value(0x5, 0x1, 0),
    '行動開始': Value(0x5, 0x1, (1, 4)),
    '不明4_4': Value(0x5, 0x1, 4),
    '不明4_5': Value(0x5, 0x1, 5),
    '不明4_6': Value(0x5, 0x1, 6),
    '不明4_7': Value(0x5, 0x1, 7),
    'ターゲット': Value(0x6, 0x2),
    '目標X': Value(0x8, 0x1),
    '目標Y': Value(0x9, 0x1),
}

SETTING_STRUCTURE = {
    'ダミー': Value(0x0, 0x2),
    'AI数': Value(0x2, 0x2),
    'AI長': Value(0x4, 0x2),
    'AIリスト': Sequence(AI_STRUCTURE, 0x6, 0xA, 0x0)
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
            record['ダミー'] = self.structures['ダミー'].parse(_buffer)
            record['AI数'] = self.structures['AIリスト'].count = self.structures['AI数'].parse(_buffer)
            record['AI長'] = self.structures['AI長'].parse(_buffer)
            record['AIリスト'] = self.structures['AIリスト'].parse(_buffer)
            sequence.append(record)
        return sequence

    def build(self, sequence: SEQUENCE, buffer: bytearray) -> bytearray:
        for idx, record in enumerate(sequence):
            count = self.structures['AIリスト'].count = record['AI数'] = len(record['AIリスト'])
            length = self._calc_length(0xA * count + 0x6)
            self.pointers[idx + 1]['指針'] = self.pointers[idx]['指針'] + length
            _buffer = bytearray(length)
            for key, data in record.items():
                self.structures[key].build(data, _buffer)
            buffer[self._idx_range(idx)] = _buffer
        return buffer

    def _idx_range(self, idx: int) -> slice:
        return slice(self.pointers[idx]['指針'], self.pointers[idx + 1]['指針'])

    @staticmethod
    def _calc_length(value: int, step: int = 0x4) -> int:
        return (value // step + bool(value % step)) * step
