#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

setuptools.setup(
    name="Data Parser",
    version="0.1.0",
    author="Hamano0813",
    description="机战α数据解析器",
    packages=setuptools.find_packages(),
    ext_modules=[
        setuptools.Extension("LZSS", [
            "compressor\\lzss.c",
        ]
        ),
        setuptools.Extension("SNMSG", [
            "parser\\util.c",
            "parser\\snmsg.c",
        ]),
    ],
)
