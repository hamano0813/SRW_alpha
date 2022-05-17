#!/usr/bin/env python
# -*- coding: utf-8 -*-

from parameter import SNMSG_TEXT_EXTRA
from structure.generic import Rom, Text, Sequence

SNMSG_STRUCTURE = {'メッセージ': Text(0x0, 0x100, 'shiftjisx0213', SNMSG_TEXT_EXTRA)}


class SnmsgBIN(Rom):
    def __init__(self):
        super(SnmsgBIN, self).__init__()
        self.structures = {
            'メッセージリスト': Sequence(SNMSG_STRUCTURE, 0x0, 0x100, 0x7F1F),
        }

    def messages(self):
        if not self.data:
            return dict()
        return {idx: f"[{idx:04X}] {node['メッセージ']}" for idx, node in enumerate(self.data['メッセージリスト'])}
