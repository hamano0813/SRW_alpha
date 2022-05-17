#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import time

from structure import RobotRAF, PilotBIN, SnmsgBIN, SndataBIN, EnlistBIN, AiunpBIN, ScriptBIN, PrmgrpBIN

paths = {
    'ROBOT': 'D:/Python/SRWα/resource/bin/UNCOMPRESS_ROBOT.RAF',
    'PILOT': 'D:/Python/SRWα/resource/bin/PILOT.BIN',
    'SNMSG': 'D:/Python/SRWα/resource/bin/SNMSG.BIN',
    'SNDATA': 'D:/Python/SRWα/resource/bin/SNDATA.BIN',
    'ENLIST': 'D:/Python/SRWα/resource/bin/ENLIST.BIN',
    'AIUNP': 'D:/Python/SRWα/resource/bin/AIUNP.BIN',
    'SCRIPT': 'D:/Python/SRWα/resource/bin/SCRIPT.BIN',
    'PRMGRP': 'D:/Python/SRWα/resource/bin/PRM_GRP.BIN',
}

roms = {
    # 'ROBOT': RobotRAF,
    # 'PILOT': PilotBIN,
    # 'SNMSG': SnmsgBIN,
    'SNDATA': SndataBIN,
    # 'ENLIST': EnlistBIN,
    # 'AIUNP': AiunpBIN,
    # 'SCRIPT': ScriptBIN,
    # 'PRMGRP': PrmgrpBIN,
}

if __name__ == '__main__':
    for k, r in roms.items():
        rom = r()
        path = paths.get(k)
        parse_start = time.time()
        rom.load(path)
        parse_end = time.time()
        buf = copy.deepcopy(rom.buffer)
        data = copy.deepcopy(rom.data)
        build_start = time.time()
        rom.build()
        build_end = time.time()
        rom.parse()

        if buf == rom.buffer:
            result = "buffer successful!"
        elif data == rom.data:
            result = "  data successful!"
        else:
            result = "failed!"

        parse_time = parse_end - parse_start
        build_time = build_end - build_start
        print(f'{r.__name__:<10s} {result:<12s}  parse time {parse_time:.3f}s, build time {build_time:.3f}s')
        print(rom.data.keys())
