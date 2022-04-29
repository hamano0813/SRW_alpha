#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .sequence import Value, Sequence, SEQUENCE


class Rom:
    def __init__(self):
        self.path: str = ''
        self.buffer: bytearray = bytearray()
        self.structures: dict[str, Value | Sequence] = dict()
        self._data: dict = dict()

    def load(self, path: str = None) -> bool:
        if path:
            self.path = path
        if not self.path:
            return False
        with open(self.path, 'rb') as f:
            self.buffer = bytearray(f.read())
        self.parse()
        return True

    def save(self, path: str = None) -> bool:
        if path:
            self.path = path
        if not self.path:
            return False
        self.build()
        with open(self.path, 'wb') as f:
            f.write(self.buffer)
        return True

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

    def __getitem__(self, item: str) -> SEQUENCE:
        return self._data.get(item, None)

    def __setitem__(self, key: str, value: SEQUENCE):
        self._data[key] = value

    def __repr__(self):
        return str(self._data)
