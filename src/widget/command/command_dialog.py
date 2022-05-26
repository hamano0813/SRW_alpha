#!/usr/bin/env python
# -*- coding: utf-8 -*-

from struct import calcsize

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QDialog, QFormLayout, QDialogButtonBox, QComboBox, QPushButton, QVBoxLayout,
                               QPlainTextEdit, QLabel, QApplication)

from structure.specific.sndata_bin.command import Command
from widget.command.command_explain import CommandExplain
from widget.command.param_widget import ParamWidget


class CommandDialog(QDialog):
    def __init__(self, parent, command: dict = None, **kwargs):
        super(CommandDialog, self).__init__(parent, f=Qt.Dialog)
        self.setWindowTitle('编辑指令' if command else '插入指令')
        self.explain = CommandExplain(**kwargs)
        self.widgets = list()
        self.setFixedWidth(800)

        self.code_combo = QComboBox()
        self.code_combo.setProperty('language', 'zhb')
        self.code_combo.setProperty('group', 'param')
        for code, settings in self.explain.settings.items():
            self.code_combo.addItem(settings[2], code)

        self.explain_text = QPlainTextEdit()
        self.explain_text.setProperty('language', 'zh')
        self.explain_text.setFixedHeight(80)

        self.edit_layout = QFormLayout()
        l1 = QLabel('指令选择')
        l2 = QLabel('指令释义')
        l1.setProperty('language', 'zh')
        l2.setProperty('language', 'zh')
        self.edit_layout.addRow(l1, self.code_combo)
        self.edit_layout.addRow(l2, self.explain_text)

        main_layout = QVBoxLayout()
        main_layout.addLayout(self.edit_layout)
        main_layout.addWidget(self.init_button())
        self.setLayout(main_layout)

        self.init_widgets(command)
        self.code_combo.currentIndexChanged.connect(self.reset_widgets)

    def get_command(self):
        if self.exec():
            return self.command()

    def command(self):
        command = {'Pos': 0, 'Code': 0, 'Count': 1, 'Param': list(), 'Data': ''}
        code = command['Code'] = self.code_combo.currentData()
        command['Param'] = [widget.data() for widget in self.widgets]
        if code == 0xB9:
            command['Count'] = command['Param'] * 4 + 5
        else:
            command['Count'] = calcsize(Command.ARGV_FMT.get(code))
        return command

    def init_widgets(self, command: dict = None):
        if not command:
            code = 0
            param = [0]
        else:
            code: int = command['Code']
            param: list[int] = command['Param']

        param_widgets: list[ParamWidget] = self.explain.settings.get(code)[1]
        self.code_combo.setCurrentIndex(list(self.explain.settings.keys()).index(code))

        for param_widget in param_widgets:
            widget: ParamWidget = param_widget.new()
            label = QLabel(widget.name)
            label.setProperty('language', 'zh')
            self.edit_layout.addRow(label, widget)
            self.widgets.append(widget)

        if code == 0xB9:
            self.widgets[0].setRange(1, 5)
            self.widgets[0].valueChanged[int].connect(self.adjust_b9)
            self.adjust_b9(param[0])

        for idx, widget in enumerate(self.widgets):
            widget.install(param[idx])

        self.resize_self()

    def reset_widgets(self):
        for idx in range(len(self.widgets) + 1, 1, -1):
            self.edit_layout.removeRow(idx)
        self.widgets = list()

        code = self.code_combo.currentData()
        param_widgets: list[ParamWidget] = self.explain.settings.get(code)[1]
        for param_widget in param_widgets:
            widget: ParamWidget = param_widget.new()
            label = QLabel(widget.name)
            label.setProperty('language', 'zh')
            self.edit_layout.addRow(label, widget)
            self.widgets.append(widget)

        if code == 0xB9:
            # noinspection PyUnresolvedReferences
            self.widgets[0].setRange(1, 5)
            self.widgets[0].dataChanged[int].connect(self.adjust_b9)

        for widget in self.widgets:
            widget.install()

        self.resize_self()

    def resize_self(self):
        for i in range(0, 10):
            QApplication.processEvents()
        self.resize(self.minimumSizeHint())

    def adjust_b9(self, count: int):
        adjust_count = count - (len(self.widgets) // 4 - 1)
        if adjust_count < 0:
            self.widgets = self.widgets[:adjust_count * 4]
        else:
            self.widgets.extend([w.new() for w in self.widgets[-4:]] * adjust_count)

    # noinspection PyUnresolvedReferences
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
