#!/usr/bin/env python
# -*- coding: utf-8 -*-

from struct import unpack_from, pack, iter_unpack

from structure.generic import Sequence, SEQUENCE


class Command(Sequence):
    ARGV_FMT = {
        0x00: 'h',
        0x01: '',
        0x02: 'h',
        0x03: 'h',
        0x04: 'h',
        0x05: 'h',
        0x06: 'h',
        0x08: 'h',
        0x09: 'h',
        0x0A: '',
        0x0B: 'hhh',
        0x0C: 'h',
        0x0D: 'h',
        0x0E: 'hh',
        0x0F: 'hh',
        0x10: 'hh',
        0x11: 'hh',
        0x12: 'hhh',
        0x13: 'hhh',
        0x14: '',
        0x15: '',
        0x16: '',
        0x17: 'hhh',
        0x18: 'hhh',
        0x19: 'hhhh',
        0x1A: 'hhhhhhhh',
        0x1B: 'hhh',
        0x1C: 'hhhh',
        0x1D: 'hhh',
        0x1E: 'hhhh',
        0x1F: 'hhh',
        0x21: 'h',
        0x22: 'h',
        0x23: '',
        0x24: 'h',
        0x25: 'hh',
        0x26: 'hhh',
        0x27: 'h',
        0x28: '',
        0x29: 'h',
        0x2A: 'h',
        0x2B: 'h',
        0x2C: 'hhh',
        0x2D: 'hhhh',
        0x2F: 'hhh',
        0x30: '',
        0x31: '',
        0x32: 'hh',
        0x33: 'h',
        0x34: 'h',
        0x35: 'h',
        0x36: 'hh',
        0x37: 'hh',
        0x38: 'h',
        0x39: 'h',
        0x3A: 'h',
        0x3B: 'hh',
        0x3C: 'h',
        0x3D: 'hhhh',
        0x3E: 'h',
        0x3F: 'h',
        0x40: 'h',
        0x41: 'h',
        0x42: 'h',
        0x43: 'hh',
        0x44: 'h',
        0x45: 'h',
        0x46: 'h',
        0x47: 'h',
        0x48: 'hh',
        0x49: 'h',
        0x4A: 'h',
        0x4B: 'h',
        0x4E: 'h',
        0x4F: '',
        0x50: '',
        0x51: 'hhh',
        0x52: 'hhhh',
        0x54: 'hhh',
        0x55: 'hhhh',
        0x57: 'hh',
        0x58: 'hhh',
        0x5A: 'hhh',
        0x5B: 'hhh',
        0x5C: 'hh',
        0x5D: 'hh',
        0x5E: 'hh',
        0x5F: 'h',
        0x60: 'hh',
        0x61: 'h',
        0x62: 'hh',
        0x63: 'h',
        0x64: 'l',
        0x65: 'h',
        0x66: 'h',
        0x67: 'hhh',
        0x68: 'hhhh',
        0x69: 'hHhh',
        0x6A: 'hh',
        0x6B: 'hhh',
        0x6C: 'hhh',
        0x6E: 'h',
        0x6F: 'h',
        0x70: 'H',
        0x71: 'h',
        0x72: 'h',
        0x73: 'h',
        0x74: 'hhhhh',
        0x75: 'hh',
        0x77: 'hh',
        0x78: 'h',
        0x79: 'hhh',
        0x7A: 'hhh',
        0x7B: 'hhh',
        0x7C: 'hhhhh',
        0x7D: 'Hhhhh',
        0x7E: 'hhhhh',
        0x80: 'hhhhh',
        0x81: 'hhhhh',
        0x82: 'hhh',
        0x83: 'hHh',
        0x84: 'hh',
        0x85: 'hh',
        0x86: 'hh',
        0x87: '',
        0x88: 'hh',
        0x89: 'hh',
        0x8B: 'hh',
        0x8C: 'hhh',
        0x8D: 'hh',
        0x8E: 'h',
        0x8F: 'h',
        0x90: 'hhh',
        0x91: 'Hhh',
        0x92: 'hhhhh',
        0x93: 'hHhhh',
        0x94: 'Hhhhh',
        0x96: 'hhhhhhhhhh',
        0x97: 'Hhhhhhhhhh',
        0x98: 'hHhhhhhhhh',
        0x99: '',
        0x9A: 'hh',
        0x9B: 'hh',
        0x9C: 'hh',
        0x9D: 'Hh',
        0x9E: 'hh',
        0x9F: 'h',
        0xA0: 'H',
        0xA1: 'h',
        0xA2: 'h',
        0xA3: 'h',
        0xA4: 'h',
        0xA5: 'hh',
        0xA6: 'h',
        0xA7: 'h',
        0xA8: 'hhhh',
        0xA9: 'hh',
        0xAA: 'h',
        0xAB: 'hh',
        0xAC: 'hH',
        0xAD: 'hh',
        0xAE: 'hH',
        0xAF: 'hh',
        0xB0: 'hH',
        0xB1: 'h',
        0xB2: 'H',
        0xB3: 'h',
        0xB4: 'h',
        0xB5: 'h',
        0xB6: 'hh',
        0xB7: 'h',
        0xB8: 'H',
        # 0xB9: '', 特殊变长指令
        0xBA: 'hhh',
        0xBB: 'hhhh',
    }

    def __init__(self, offset, length, count=None, structures=None):
        super(Command, self).__init__(structures, offset, length, count)

    def parse(self, buffer: bytearray) -> SEQUENCE:
        _buffer = buffer[self.offset:]
        commands = list()
        offset = 0x0
        while _buffer[offset] != 0xFF:
            length = _buffer[offset + 0x1] * 2
            c_buffer = _buffer[offset: offset + length]

            command: dict[str, int | list[int] | str] = dict()
            command['Pos'] = offset // 2
            command['Code'] = c_buffer[0]
            command['Count'] = c_buffer[1]
            fmt = self.ARGV_FMT.get(command['Code'], 'h' * (command['Count'] - 1))
            command['Param'] = list(unpack_from(f'>{fmt}', self.reverse_buffer(c_buffer), 0x2))
            command['Data'] = ' '.join([f'{d:04X}' for d in unpack_from('H' * command['Count'], c_buffer, 0x0)])

            commands.append(command)
            offset += length
        return commands

    def build(self, sequence: SEQUENCE, buffer: bytearray) -> bytearray:
        _buffer = bytearray([0xFF] * self.length)
        offset = 0x0
        for command in sequence:
            fmt = self.ARGV_FMT.get(command['Code'])
            if fmt is None:
                fmt = 'h' * (command['Param'][0] * 4 + 4)
            p_buffer = pack(f'>{fmt}', *command['Param'])
            p_buffer = self.reverse_buffer(p_buffer)
            length = len(p_buffer) + 2
            command['Count'] = length // 2

            c_buffer = bytearray(2)
            c_buffer[0] = command['Code']
            c_buffer[1] = command['Count']
            c_buffer += p_buffer

            _buffer[offset: offset + length] = c_buffer
            offset += length
        buffer[self.offset:] = _buffer
        return buffer

    @staticmethod
    def reverse_buffer(buffer: bytes | bytearray) -> bytearray:
        _buffer = bytearray()
        for unit in iter_unpack('h', buffer):
            _buffer += pack('>h', *unit)
        return _buffer
