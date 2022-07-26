#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from struct import unpack_from

from structure.destructor import LZSS


def diff_print(l_buf: bytes | bytearray, r_buf: bytes | bytearray = None):
    li_list = list()
    ri_list = list()
    if r_buf is None:
        r_buf = bytearray()
    for i_idx in range(max(li_size := len(l_buf), ri_size := len(r_buf))):
        if i_idx < li_size and i_idx < ri_size:
            if l_buf[i_idx] == r_buf[i_idx]:
                li_list.append(f" {l_buf[i_idx]:02X}")
                ri_list.append(f" {r_buf[i_idx]:02X}")
            else:
                li_list.append(f" \033[1;39;47m{l_buf[i_idx]:02X}\033[0m")
                ri_list.append(f" \033[1;39;47m{r_buf[i_idx]:02X}\033[0m")
        elif i_idx >= li_size:
            li_list.append(f"   ")
            ri_list.append(f" \033[4m{r_buf[i_idx]:02X}\033[0m")
        elif i_idx >= ri_size:
            li_list.append(f" \033[4m{l_buf[i_idx]:02X}\033[0m")
            ri_list.append(f"   ")
    for p_idx in range(0x10 - i_idx % 0x10 - 1):
        li_list.append(f"   ")
        ri_list.append(f"   ")

    lt_list = [
        f"\033[7m {i:>08X}h: \033[0m " + " ".join(li_list[i: i + 0x10])
        for i in range(0, len(li_list), 0x10)
    ]
    rt_list = [
        f"\033[7m {i:>08X}h: \033[0m " + " ".join(ri_list[i: i + 0x10])
        for i in range(0, len(ri_list), 0x10)
    ]
    size = max(lt_size := len(lt_list), rt_size := len(rt_list))

    header = " ".join([f"\033[7m{h_idx:^3X}\033[0m" for h_idx in range(0x10)])
    print(" " * 13 + header + "\t" + " " * 13 + header)
    for t_idx in range(size):
        if t_idx >= lt_size:
            print(" " * 64 + f"{rt_list[t_idx]}")
        elif t_idx >= rt_size:
            print(f"{lt_list[t_idx]}")
        else:
            print(f"{lt_list[t_idx]}\t{rt_list[t_idx]}")


def lzss_print(buf: bytes | bytearray):
    idx = 8
    data = [f"\033[1m{h:02X}\033[0m" for h in buf[:4]]
    data.extend([f"\033[8m{h:02X}\033[0m" for h in buf[4:8]])
    while idx < (size := len(buf)):
        f = buf[idx]
        data.append(f"\033[1m\033[5m\033[4;36m{f:02X}\033[0m")
        idx += 1
        for bit_idx in range(8):
            if idx == size:
                break
            if f & (1 << bit_idx):
                d = buf[idx]
                data.append(f"{d:02X}")
                idx += 1
            else:
                n1 = buf[idx]
                data.append(f"\033[0;32m{n1:02X}\033[0m")
                idx += 1
                n2 = (buf[idx] & 0xF0) >> 4
                n3 = buf[idx] & 0xF
                data.append(f"\033[0;32m{n2:X}\033[0m\033[0;35m{n3:X}\033[0m")
                idx += 1

    text = [
        f"\033[7m{i:>08X}h:\033[0m " + " ".join(data[i: i + 0x10])
        for i in range(0, len(data), 0x10)
    ]
    header = " " * 11 + " ".join([f"\033[7m{s}\033[0m" for s in "０１２３４５６７８９ＡＢＣＤＥＦ"])
    print(header)
    print(*text, sep="\n")


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
        decom = LZSS.decompress(buf)
        buffer += decom
        if not decom == s_data[0x2C4 * u_idx: 0x2C4 * (u_idx + 1)]:
            print(u_idx)
    return buffer


def test_compress():
    for u_idx in range(cnt):
        s_buf = s_data[0x2C4 * u_idx: 0x2C4 * (u_idx + 1)]
        com = LZSS.compress(s_buf)
        # print(u_idx, com == o_data[off + ptrs[u_idx]: off + ptrs[u_idx + 1]])
        # buf = o_data[off + ptrs[u_idx]: off + ptrs[u_idx + 1]]
        # print(u_idx, buf == com, LZSS.decompress(com) == s_data[0x2C4 * u_idx: 0x2C4 * (u_idx + 1)])


start = time.time()
# test_compress()
test_decompress()
end = time.time()

print(f"{end - start:.3f}")
