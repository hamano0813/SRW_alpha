#!/usr/bin/env python
# -*- coding: utf-8 -*-

from compressor import decompress

path = r'D:\Python\SRWalpha\resource\bin\jp\ROBOT.RAF'

with open(path, 'rb') as f:
    data = bytearray(f.read())

pointers = decompress(data)

print(hex(len(pointers)))
print([f'{p:08X}' for p in pointers])
