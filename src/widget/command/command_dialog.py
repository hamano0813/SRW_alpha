#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QFormLayout
from widget.command.command_explain import CommandExplain


class CommandDialog(QDialog):
    def __init__(self, parent, command: dict = None, **kwargs):
        super(CommandDialog, self).__init__(parent, f=Qt.Dialog)
        self.command = command if command else {'Pos': 0, 'Code': 0, 'Count': 1, 'Param': list(), 'Data': ''}
        self.explain = CommandExplain(**kwargs)
        self.widgets = list()

    def get_command(self):
        self.init_edit()

    def init_edit(self):
        self.widgets = list()
        code = self.command['Code']

        edit_layout = QFormLayout()
        edit_layout.addRow('指令', )
