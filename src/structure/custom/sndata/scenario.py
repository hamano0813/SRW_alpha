#!/usr/bin/env python
# -*- coding: utf-8 -*-

from struct import unpack_from, pack_into, pack
from .command import Command


class Scenario:
    header = 0x48
    length = 0x4048

    def __init__(self, buffer: bytearray):
        self.buffer = buffer
        self.setting: list[int] = list()
        self.pointer: list[int] = list()
        self.command: list[Command] = list()
        self.parse()

    def parse(self):
        if not self.buffer:
            return
        self.setting = list(unpack_from('2L', self.buffer, 0x0))
        self.pointer = list(unpack_from('16L', self.buffer, 0x8))
        command_offset = self.header
        while self.buffer[command_offset] != 0xFF:
            command_length = self.buffer[command_offset + 0x1] * 2
            command_buffer = self.buffer[command_offset: command_offset + command_length]
            self.command.append(Command(command_buffer, (command_offset - self.header) // 2))
            command_offset += command_length

    def build(self):
        buffer = pack(f'{self.length}B', *(0xFF,) * self.length)
        pack_into('2L', self.buffer, 0x0, *self.setting)
        command_offset = self.length
        for command in self.command:
            buffer[command_offset: command_offset + command.length] = command.buffer
            command_offset += command.length
            if command.code == 0x00:
                block_idx = command.argv[0]
                self.pointer[block_idx] = command.pos
        pack_into('16L', self.buffer, 0x8, *self.pointer)
        self.buffer = buffer
        self.parse()

    def insert(self, command_idx: int, command: Command):
        command.build()
        command.pos = self.command[command_idx].pos
        for idx in range(command_idx, self.count):
            self.command[idx].pos += command.count
        self.command.insert(command_idx, command)

    def append(self, command: Command):
        command.build()
        command.pos = self.command[-1].pos + self.command[-1].count
        self.command.append(command)

    def delete(self, command_idx: int):
        count = self.command.pop(command_idx).count
        for idx in range(command_idx, self.count):
            self.command[idx].pos -= count

    def update(self, command_idx: int, command: Command):
        self.delete(command_idx)
        self.insert(command_idx, command)

    @property
    def count(self):
        return len(self.command)

    def __getitem__(self, row_idx: int):
        return self.command[row_idx]

    def __len__(self):
        return len(self.buffer)

    def __repr__(self):
        return f'Scenario buffer with {self.count} Command'
