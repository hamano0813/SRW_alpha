#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QFrame
from structure import ROBOT


class RobotFrame(QFrame):
    def __init__(self, robot: ROBOT):
        super(RobotFrame, self).__init__()
        self.robot = robot
