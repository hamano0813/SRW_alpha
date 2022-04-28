#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Rom:
    def __init__(self):
        self.path: str = ''
        self.buffer: bytearray = bytearray()
        self._data: dict = dict()

    def load(self, path: str = None) -> bool:
        if path:
            self.path = path
        if not self.path:
            return False
        with open(path, 'rb') as f:
            self.buffer = bytearray(f.read())
        self.parse()
        return True

    def save(self, path: str = None) -> bool:
        if path:
            self.path = path
        if not self.path:
            return False
        self.build()
        with open(path, 'rb') as f:
            f.write(self.buffer)
        return True

    def parse(self) -> bool:
        pass

    def build(self) -> bool:
        pass

    def __getitem__(self, item: str) -> list[dict[str, int | str | list[dict]]]:
        return self._data.get(item, None)

    def __setitem__(self, key: str, value: list[dict[str, int | str | list[dict]]]):
        self._data[key] = value

    def __repr__(self):
        return str(self._data)
