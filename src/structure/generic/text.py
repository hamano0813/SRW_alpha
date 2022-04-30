#!/usr/bin/env python
# -*- coding: utf-8 -*-

from struct import unpack_from, pack_into


class Text:
    def __init__(self, offset: int, length: int, code: str, extra: dict = None):
        self.offset = offset
        self.length = length
        self.code = code
        self.extra = extra

    def parse(self, buffer: bytearray) -> str:
        data = unpack_from(f'{self.length}s', buffer, self.offset)[0].split(b'\00')[0]
        return self._decode_text(data)

    def build(self, text: str, buffer: bytearray) -> bytearray:
        _buffer = bytearray(self.length)
        data = self._encode_text(text)[:self.length - 1] + b'\00'
        length = len(data)
        pack_into(f'{length}s', _buffer, self.offset, data)
        buffer[:] = _buffer
        return buffer

    def _decode_text(self, data: bytes) -> str:
        temp = data.decode(self.code)
        if self.extra:
            for old, new in self.extra.items():
                temp = temp.replace(old, new)
        print(temp)
        return temp

    def _encode_text(self, text: str) -> bytearray:
        temp = text
        if self.extra:
            for old, new in reversed(self.extra.items()):
                temp = temp.replace(new, old)
        return bytearray(temp.encode(self.code))
