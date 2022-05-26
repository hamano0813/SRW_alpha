#!/usr/bin/env python
# -*- coding: utf-8 -*-

from struct import calcsize

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QFormLayout, QDialogButtonBox, QComboBox, QPushButton, QVBoxLayout, QLineEdit
from widget.command.command_explain import CommandExplain
from widget.command.param_widget import ParamWidget
from structure.specific.sndata_bin.command import Command


class CommandDialog(QDialog):
    def __init__(self, parent, command: dict = None, **kwargs):
        super(CommandDialog, self).__init__(parent, f=Qt.Dialog)
        self.command = command if command else {'Pos': 0, 'Code': 0, 'Count': 1, 'Param': list(), 'Data': ''}
        self.explain = CommandExplain(**kwargs)

        self.code_combo = QComboBox()
        for code, settings in self.explain.settings.items():
            self.code_combo.addItem(settings[2], code)

        self.edit_layout = QFormLayout()
        self.edit_layout.addRow('指令', self.code_combo)

        self.explain_line = QLineEdit()

        main_layout = QVBoxLayout()
        main_layout.addLayout(self.edit_layout)
        main_layout.addWidget(self.explain_line)
        main_layout.addWidget(self.init_button())

        self.setLayout(main_layout)

        self.code_combo.currentIndexChanged.connect(self.reset_widget)
        self.widgets = list()

    def get_command(self):
        code = self.command['Code']
        param = self.command['Param']
        self.code_combo.setCurrentIndex(list(self.explain.settings.keys()).index(code))
        self.install_param(param)
        if self.exec():
            self.build()
            return self.command

    def build(self):
        code = self.command['Code']
        fmt = Command.ARGV_FMT.get(code)
        self.command['Count'] = calcsize(fmt) // 2 + 1
        for idx, widget in enumerate(self.widgets):
            self.command['Param'][idx] = widget.data()

    def install_param(self, param: list):
        for idx, widget in enumerate(self.widgets):
            widget.install(param[idx])

    def reset_widget(self):
        self.clear_param()

        code = self.code_combo.currentData()
        if code != 0xB9:
            setting = self.explain.settings.get(code)[1]
            for argv in setting:
                name = argv.name
                widget: ParamWidget = argv.new()
                self.widgets.append(widget)
                self.edit_layout.addRow(name, widget)
                widget.install()
        else:
            setting = self.explain.settings.get(code)[1]
            for argv in setting:
                name = argv.name
                widget: ParamWidget = argv.new()
                self.widgets.append(widget)
                self.edit_layout.addRow(name, widget)
                widget.install()

    def clear_param(self):
        for idx in range(1, self.edit_layout.rowCount()):
            self.edit_layout.removeRow(idx)

        # for w in self.widgets:
        #     if w:
        #         w.close()
        #         del w

        self.widgets = list()

    def init_button(self):
        accept_button = QPushButton('确定')
        reject_button = QPushButton('取消')
        button_box = QDialogButtonBox()
        button_box.setOrientation(Qt.Horizontal)
        button_box.addButton(accept_button, QDialogButtonBox.AcceptRole)
        button_box.addButton(reject_button, QDialogButtonBox.RejectRole)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        return button_box
