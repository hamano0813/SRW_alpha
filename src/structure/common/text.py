#!/usr/bin/env python
# -*- coding: utf-8 -*-

from struct import unpack_from, pack_into


class Text:
    def __init__(self, offset, length, aliases, additional=None, dummy=None):
        self.offset: int = offset
        self.length: int = length
        self.aliases: str = aliases
        self.additional: dict = additional
        self.dummy: bytearray = dummy

    def get_data(self, buffer: bytearray) -> str:
        data = unpack_from(f'{self.length}s', buffer, self.offset)[0]
        return self._decode_text(data)

    def set_data(self, text: str, buffer: bytearray) -> str:
        data = self._encode_text(text)[:self.length - 1] + b'\00'
        data += self.dummy[min(len(data), self.length):]
        pack_into(f'{self.length}s', buffer, self.offset, data)
        return self._decode_text(data)

    def _decode_text(self, data: bytes) -> str:
        temp = data.split(b'\00')[0].replace(b'\r', b'\n').decode(self.aliases)
        if self.additional:
            for old, new in self.additional.items():
                temp = temp.replace(old, new)
        return temp

    def _encode_text(self, text: str) -> bytes:
        temp = text
        for old, new in reversed(self.additional.items()):
            temp = temp.replace(new, old)
        return temp.replace('ー', '-').encode(self.aliases).replace(b'\n', b'\r')
