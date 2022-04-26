#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Union, Optional
from .value import Value
from .text import Text

RECORD = Union[int, str, list[dict[str, Optional["RECORD"]]]]


class Sequence:
    def __init__(self, structures, offset: int, length: int, count: int = 0x1):
        self.structures: dict[str, Value | Text | Optional["Sequence"]] = structures
        self.offset = offset
        self.length = length
        self.count = count

    def parse(self, buffer: bytearray) -> list[dict[str, RECORD]]:
        sequence = list()
        for idx in range(self.count):
            record = dict()
            _buffer = buffer[self._index_range(idx)]
            for pname, structure in self.structures.items():
                record[pname] = structure.parse(_buffer)
            sequence.append(record)
        return sequence

    def build(self, sequence: list[dict[str, RECORD]], buffer: bytearray) -> bytearray:
        for idx, record in enumerate(sequence):
            if idx < self.count:
                _buffer = buffer[self._index_range(idx)]
            else:
                _buffer = bytearray(self.length)
            for pname, data in record.items():
                self.structures[pname].build(data, _buffer)
            if idx < self.count:
                buffer[self._index_range(idx)] = _buffer
            else:
                buffer += _buffer
                self.count += 1
        return buffer

    def _index_range(self, idx: int) -> slice:
        return slice(self.offset + self.length * idx, self.offset + self.length * (idx + 1))

    @property
    def property(self) -> list[str]:
        return list(self.structures)

    def mapping(self, pname: str, buffer: bytearray) -> dict[int, str]:
        structure = self.structures.get(pname, None)
        if not structure:
            raise KeyError
        return {idx: structure.parse(buffer[self._index_range(idx)]) for idx in range(self.count)}
