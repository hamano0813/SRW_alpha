#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import copy
from structure import RobotRAF, PilotBIN, SnmsgBIN, SndataBIN, EnlistBIN, AiunpBIN, ScriptBIN

paths = {
    'ROBOT': 'D:/Python/SRWα/resource/bin/UNCOMPRESS_ROBOT.RAF',
    'PILOT': 'D:/Python/SRWα/resource/bin/PILOT.BIN',
    'SNMSG': 'D:/Python/SRWα/resource/bin/SNMSG.BIN',
    'SNDATA': 'D:/Python/SRWα/resource/bin/SNDATA.BIN',
    'ENLIST': 'D:/Python/SRWα/resource/bin/ENLIST.BIN',
    'AIUNP': 'D:/Python/SRWα/resource/bin/AIUNP.BIN',
    'SCRIPT': 'D:/Python/SRWα/resource/bin/SCRIPT.BIN',
}

roms = {
    'ROBOT': RobotRAF,
    'PILOT': PilotBIN,
    'SNMSG': SnmsgBIN,
    'SNDATA': SndataBIN,
    'ENLIST': EnlistBIN,
    'AIUNP': AiunpBIN,
    'SCRIPT': ScriptBIN,
}

if __name__ == '__main__':
    for k, r in roms.items():
        rom = r()
        path = paths.get(k)
        parse_start = time.time()
        rom.load(path)
        parse_end = time.time()
        buf = copy.deepcopy(rom.buffer)
        build_start = time.time()
        rom.build()
        build_end = time.time()

        result = "successful!" if buf == rom.buffer else "failed!"
        parse_time = parse_end - parse_start
        build_time = build_end - build_start
        print(f'{r.__name__:<10s} test {result:<12s} parse time {parse_time:.3f}s, build time {build_time:.3f}s')
