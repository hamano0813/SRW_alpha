#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon
from .resource import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('超级机器人大战α 静态修改器')
        self.setWindowIcon(QIcon(':image/icon.png'))
