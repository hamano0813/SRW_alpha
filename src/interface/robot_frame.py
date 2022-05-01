#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QFrame

from structure import RobotRAF


class RobotFrame(QFrame):
    def __init__(self, robot: RobotRAF):
        super(RobotFrame, self).__init__()
        self.robot = robot
