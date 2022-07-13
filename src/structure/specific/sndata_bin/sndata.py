#!/usr/bin/env python
# -*- coding: utf-8 -*-

from structure.generic import Rom
from structure.specific.sndata_bin.scenario import Scenario, SCENARIO_STRUCTURE


class SndataBIN(Rom):
    def __init__(self):
        super(SndataBIN, self).__init__()
        self.structures = {
            '场景设计': Scenario(SCENARIO_STRUCTURE, 0x800, 0x4048, 0x8C),
        }
