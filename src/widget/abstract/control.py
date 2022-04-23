#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ControlWidget:
    def __init__(self):
        self.control_targets: dict[str, any] = dict()

    def add_control_target(self, name: str, target):
        self.control_targets.update({name: target})

    def control_target(self, index: int):
        pass
