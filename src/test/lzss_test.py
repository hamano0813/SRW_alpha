#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from struct import unpack_from

from compression import LZSS

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
        ou_size = unpack_from('I', buf, 0)[0]
        # noinspection PyUnresolvedReferences
        decom = LZSS.decompress(buf[8:], ou_size)
        buffer += decom
        if not decom == s_data[0x2C4 * u_idx: 0x2C4 * (u_idx + 1)]:
            print(u_idx)
    return buffer


def test_compress():
    for u_idx in range(cnt):
        buf = o_data[off + ptrs[u_idx]: off + ptrs[u_idx + 1]]
        ou_size = unpack_from('I', buf, 0)[0]
        decom = LZSS.decompress(buf[8:], ou_size)
        com = LZSS.compress(decom)
        # print(decom == LZSS.decompress(com, ou_size))
        com = LZSS.compress(decom)
        # with open('d:/a01.bin', 'wb') as f:
        #     f.write(buf[8:])
        # with open('d:/b01.bin', 'wb') as f:
        #     f.write(com)
        # print(decom == s_data[0x2C4*u_idx: 0x2C4*u_idx+0x2C4])
        # print(decom == LZSS.decompress(com, ou_size))
        # if u_idx == 0:
        #     for i, d in enumerate(com):
        #         print(i, f"{d:02X}", f"{buf[8 + i]:02X}", d == buf[8 + i], sep='\t')


start = time.time()
test_compress()
end = time.time()

print(f"{end - start:.3f}")
