#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..rom import ROM


class PRMGRP(ROM):
    count = 0x7F1F

    def __init__(self):
        super(PRMGRP, self).__init__()

    def parse(self) -> bool:
        pass

    def build(self) -> bool:
        pass
