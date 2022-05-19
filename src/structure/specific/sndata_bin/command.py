#!/usr/bin/env python
# -*- coding: utf-8 -*-

from struct import unpack_from, pack_into

from structure.generic import Sequence, SEQUENCE
from structure.specific.sndata_bin.explain import Explain


class Command(Sequence):
    def __init__(self, offset, length, count=None, structures=None):
        super(Command, self).__init__(structures, offset, length, count)
        self.explain = Explain()

    def parse(self, buffer: bytearray) -> SEQUENCE:
        _buffer = buffer[self.offset:]
        commands = list()
        offset = 0x0
        while _buffer[offset] != 0xFF:
            length = _buffer[offset + 0x1] * 2
            command_buffer = _buffer[offset: offset + length]

            command: dict[str, int | list[int]] = dict()
            command['定位'] = offset // 2
            command['指令码'] = command_buffer[0]
            command['长度'] = command_buffer[1]
            fmt = self.explain.argv_fmt[command['指令码']][0]
            if command['指令码'] == 0xB9:
                fmt = 'h' * (command['长度'] - 1)
            command['参数列表'] = list(unpack_from(fmt, command_buffer, 0x2))

            commands.append(command)
            offset += length
        return commands

    def build(self, sequence: SEQUENCE, buffer: bytearray) -> bytearray:
        _buffer = bytearray([0xFF] * self.length)
        offset = 0x0
        for command in sequence:
            length = command['长度'] * 2
            c_buffer = bytearray(length)

            c_buffer[0] = command['指令码']
            c_buffer[1] = command['长度']
            fmt = self.explain.argv_fmt[command['指令码']][0]
            if command['指令码'] == 0xB9:
                fmt = 'h' * (command['长度'] - 1)
            pack_into(fmt, c_buffer, 0x2, *command['参数列表'])

            _buffer[offset: offset + length] = c_buffer
            offset += length
        buffer[self.offset:] = _buffer
        return buffer
