#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

setuptools.setup(
    name="LZSS",
    version="0.0.1",
    author="Hamano0813",
    description="机战α使用的类LZSS压缩和解压算法",
    packages=setuptools.find_packages(),
    ext_modules=[setuptools.Extension("LZSS", ["LZSS\\LZSS.c"])],
)
