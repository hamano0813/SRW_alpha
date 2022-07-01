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

bufs = []
def test_decompress():
    buffer = bytearray()
    for u_idx in range(cnt):
        buf = o_data[off + ptrs[u_idx]: off + ptrs[u_idx + 1]]
        ou_size = unpack_from('I', buf, 0)[0]
        # noinspection PyUnresolvedReferences
        buffer += LZSS.decompress(buf[8:], ou_size)
        bufs.append(buf[8:])
    return buffer

start = time.time()
t_data = test_decompress()
end = time.time()

print(t_data == s_data)
print(f'{end - start:.4f}')
u_data = t_data[0:0x2C4]
