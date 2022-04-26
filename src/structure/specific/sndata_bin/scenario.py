#!/usr/bin/env python
# -*- coding: utf-8 -*-

from struct import unpack_from, pack_into, pack
from .command import Command


class Scenario:
    header = 0x48
    length = 0x4048

    def __init__(self, buffer: bytearray):
        self.buffer = buffer
        self._data: dict[str, list[int | Command]] = dict()
        self.parse()

    def parse(self) -> bool:
        if not self.buffer:
            return False
        self._data['头部设定']: list[int] = list(unpack_from('2L', self.buffer, 0x0))
        self._data['区块定位']: list[int] = list(unpack_from('16L', self.buffer, 0x8))
        self._data['指令集']: list[Command] = list()
        offset = self.header
        while self.buffer[offset] != 0xFF:
            length = self.buffer[offset + 0x1] * 2
            buffer = self.buffer[offset: offset + length]
            self._data['指令集'].append(Command(buffer, (offset - self.header) // 2))
            offset += length
        return True

    def build(self) -> bool:
        buffer = bytearray([0xFF] * self.length)
        pack_into('2L', buffer, 0x0, *self._data['头部设定'])
        offset = self.header
        for command in self._data['指令集']:
            buffer[offset: offset + command.length] = command.buffer
            offset += command.length
            if command['指令码'] == 0x00:
                block_idx = command.argv[0]
                self._data['区块定位'][block_idx] = command['定位']
        pack_into('16L', self.buffer, 0x8, *self._data['区块定位'])
        self.buffer = buffer
        return self.parse()

    def insert(self, command_idx: int, command: Command):
        command.build()
        command.pos = self._data['指令集'][command_idx]['定位']
        for idx in range(command_idx, self.count):
            self._data['指令集'][idx]['定位'] += command['长度']
        self._data['指令集'].insert(command_idx, command)

    def append(self, command: Command):
        command.build()
        command.pos = self._data['指令集'][-1]['定位'] + self._data['指令集'][-1]['长度']
        self._data['指令集'].append(command)

    def delete(self, command_idx: int):
        count = self._data['指令集'].pop(command_idx)['长度']
        for idx in range(command_idx, self.count):
            self._data['指令集'][idx]['定位'] -= count

    def update(self, command_idx: int, command: Command):
        self.delete(command_idx)
        self.insert(command_idx, command)

    @property
    def count(self) -> int:
        return len(self._data['指令集'])

    def __getitem__(self, item: str) -> list[int | Command]:
        return self._data.get(item)

    def __len__(self) -> int:
        return len(self.buffer)

    def __repr__(self):
        return f'Scenario buffer with {self.count} Command'
