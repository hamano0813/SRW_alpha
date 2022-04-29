#!/usr/bin/env python
# -*- coding: utf-8 -*-

from struct import unpack_from, pack_into


class Text:
    def __init__(self, offset: int, length: int, code: str, extra: dict = None, dummy: bytearray = None):
        self.offset = offset
        self.length = length
        self.code = code
        self.extra = extra
        self.dummy = dummy

    def parse(self, buffer: bytearray) -> str:
        data = unpack_from(f'{self.length}s', buffer, self.offset)[0].split(b'\00')[0]
        return self._decode_text(data)

    def build(self, text: str, buffer: bytearray) -> bytearray:
        data = self._encode_text(text)[:self.length - 1] + b'\00'
        length = len(data)
        if self.dummy:
            data += self.dummy[length:]
            length = self.length
        pack_into(f'{length}s', buffer, self.offset, data)
        return buffer

    def _decode_text(self, data: bytes) -> str:
        temp = data.replace(b'\r', b'\n').replace(b'\x81@', b' ').decode(self.code)
        if self.extra:
            for old, new in self.extra.items():
                temp = temp.replace(old, new)
        return temp

    def _encode_text(self, text: str) -> bytearray:
        temp = text
        for old, new in reversed(self.extra.items()):
            temp = temp.replace(new, old)
        return bytearray(temp.encode(self.code).replace(b'\n', b'\r').replace(b' ', b'\x81@'))
