#!/usr/bin/env python
# -*- coding: utf-8 -*-

from parameter import SNMSG_TEXT_EXTRA
from structure.generic import Rom, Text, Sequence

SNMSG_STRUCTURE = {'文本': Text(0x0, 0x100, 'shiftjisx0213', SNMSG_TEXT_EXTRA)}


class SnmsgBIN(Rom):
    def __init__(self):
        super(SnmsgBIN, self).__init__()
        self.structures = {
            '文本列表': Sequence(SNMSG_STRUCTURE, 0x0, 0x100, 0x7F1F),
        }

    def messages(self):
        if not self.data:
            return dict()
        return {idx: f"[{idx:04X}] {node['文本']}" for idx, node in enumerate(self.data['文本列表'])}
