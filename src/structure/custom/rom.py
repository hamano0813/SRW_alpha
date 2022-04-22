#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ROM:
    def __init__(self):
        self.path: str = ''
        self.buffer: bytearray = bytearray()

    def set_path(self, path: str):
        self.path = path

    def set_buffer(self, buffer: bytearray):
        self.buffer = buffer
        self.parse()

    def get_buffer(self) -> bytearray:
        self.build()
        return self.buffer

    def parse(self) -> bool:
        pass

    def build(self) -> bool:
        pass

    @property
    def length(self) -> int:
        return len(self.buffer)

    def __bool__(self):
        return bool(self.buffer)

    def __len__(self):
        return len(self.buffer)
