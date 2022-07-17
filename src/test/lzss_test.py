#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from struct import unpack_from

from structure.destructor import LZSS

o_path = r'..\..\resource\bin\jp\ROBOT.RAF'
s_path = r'..\..\resource\bin\jp\UNCOMPRESS_ROBOT.RAF'

with open(o_path, 'rb') as o_file:
    o_data = bytearray(o_file.read())

with open(s_path, 'rb') as s_file:
    s_data = bytearray(s_file.read())

cnt = unpack_from('I', o_data, 0x0)[0]
off = (cnt + 1) * 4
ptrs = list(unpack_from('I' * cnt, o_data, 0x4))
ptrs.append(len(o_data))


def test_decompress():
    buffer = bytearray()
    for u_idx in range(cnt):
        buf = o_data[off + ptrs[u_idx]: off + ptrs[u_idx + 1]]
        # noinspection PyUnresolvedReferences
        decom = LZSS.decompress(buf[8:])
        buffer += decom
        if not decom == s_data[0x2C4 * u_idx: 0x2C4 * (u_idx + 1)]:
            print(u_idx)
    return buffer


def test_compress():
    for u_idx in range(cnt):
        buf = o_data[off + ptrs[u_idx]: off + ptrs[u_idx + 1]]
        decom = LZSS.decompress(buf[8:])
        com = LZSS.compress(decom)
        print(u_idx, buf[8:] == com, decom == LZSS.decompress(com))
        # if u_idx == 31:
        #     with open('d:/a031.bin', 'wb') as f:
        #         f.write(LZSS.decompress(com, ou_size))


start = time.time()
test_compress()
test_decompress()
end = time.time()

print(f"{end - start:.3f}")
