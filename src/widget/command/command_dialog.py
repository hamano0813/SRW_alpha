#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog


class CommandDialog(QDialog):
    def __init__(self, parent, command: dict = None):
        super(CommandDialog, self).__init__(parent, f=Qt.Dialog)
        self.command = command if command else {'Pos': 0, 'Code': 0, 'Count': 1, 'Param': list(), 'Data': ''}

