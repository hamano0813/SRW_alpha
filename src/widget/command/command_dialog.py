#!/usr/bin/env python
# -*- coding: utf-8 -*-

from struct import calcsize, pack, unpack

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
        self.explain_text.setReadOnly(True)
        self.explain_text.setContextMenuPolicy(Qt.NoContextMenu)
        self.explain_text.setProperty('language', 'zh')
        self.explain_text.setFixedHeight(100)

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
        # noinspection PyUnresolvedReferences
        self.code_combo.currentIndexChanged.connect(self.reset_widgets)

    def get_command(self):
        if self.exec():
            return self.command()

    def command(self):
        command = {'Pos': 0, 'Code': 0, 'Count': 1, 'Param': list(), 'Data': ''}
        code = command['Code'] = self.code_combo.currentData()
        command['Param'] = [widget.data() for widget in self.widgets]
        if code == 0xB9:
            command['Count'] = command['Param'][0] * 4 + 5
        else:
            command['Count'] = calcsize(Command.ARGV_FMT.get(code, '')) // 2 + 1
        self.generate_data(command)
        return command

    @staticmethod
    def generate_data(command: dict):
        fmt = Command.ARGV_FMT.get(command['Code'], None)
        if fmt is None:
            fmt = 'h' * (command['Param'][0] * 4 + 4)
        p_buffer = pack(f'>{fmt}', *command['Param'])
        p_buffer = Command.reverse_buffer(p_buffer)
        length = len(p_buffer) + 2
        command['Count'] = length // 2

        c_buffer = bytearray(2)
        c_buffer[0] = command['Code']
        c_buffer[1] = command['Count']
        c_buffer += p_buffer
        command['Data'] = ' '.join([f'{d:04X}' for d in unpack('H' * command['Count'], c_buffer)])

    def explain_command(self):
        self.explain_text.setPlainText(self.explain.explain(self.command()))

    def init_widgets(self, command: dict = None):
        code = 0 if not command else command['Code']
        param = [1] if not command else command['Param']

        param_widgets: list[ParamWidget] = self.explain.settings.get(code)[1]
        self.code_combo.setCurrentIndex(list(self.explain.settings.keys()).index(code))

        for param_widget in param_widgets:
            widget: ParamWidget = param_widget.new()
            if widget.name == '无效':
                # noinspection PyUnresolvedReferences
                widget.setEnabled(False)
            label = QLabel(widget.name)
            label.setProperty('language', 'zh')
            self.edit_layout.addRow(label, widget)
            self.widgets.append(widget)

        if code == 0xB9:
            self.widgets[0].valueChanged[int].connect(self.adjust_b9)

        for idx, widget in enumerate(self.widgets):
            widget.install(param[idx])
            if idx > 0 or code != 0xB9:
                widget.dataChanged.connect(self.explain_command)

        self.explain_command()
        self.special_rule()
        self.resize_self()

    def reset_widgets(self):
        for i in range(len(self.widgets)):
            self.edit_layout.removeRow(2)
        self.widgets = list()

        code = self.code_combo.currentData()
        param_widgets: list[ParamWidget] = self.explain.settings.get(code)[1]
        for param_widget in param_widgets:
            widget: ParamWidget = param_widget.new()
            if widget.name == '无效':
                # noinspection PyUnresolvedReferences
                widget.setEnabled(False)
            label = QLabel(widget.name)
            label.setProperty('language', 'zh')
            self.edit_layout.addRow(label, widget)
            self.widgets.append(widget)

        if code == 0xB9:
            self.widgets[0].dataChanged[int].connect(self.adjust_b9)

        for idx, widget in enumerate(self.widgets):
            widget.install()
            if idx > 0 or code != 0xB9:
                widget.dataChanged.connect(self.explain_command)

        self.explain_command()
        self.special_rule()
        self.resize_self()

    def resize_self(self):
        QApplication.processEvents()
        self.resize(self.minimumSizeHint())

    def adjust_b9(self, count: int):
        adjust_count = count - (len(self.widgets) // 4 - 1)
        if adjust_count < 0:
            for i in range(abs(adjust_count) * 4):
                self.edit_layout.removeRow(self.edit_layout.rowCount() - 1)
            self.widgets = self.widgets[:adjust_count * 4]
            self.resize_self()
        else:
            start_idx = len(self.widgets)
            for i in range(adjust_count):
                self.widgets.extend([w.new() for w in self.widgets[-4:]])
            for widget in self.widgets[start_idx:]:
                label = QLabel(widget.name)
                label.setProperty('language', 'zh')
                self.edit_layout.addRow(label, widget)
                widget.dataChanged.connect(self.explain_command)
                widget.install()
        self.explain_command()

    def special_rule(self):
        match self.code_combo.currentData():
            case 0xB9:
                self.widgets[0].setRange(1, 5)

    # noinspection PyUnresolvedReferences
    def init_button(self):
        accept_button = QPushButton('确定')
        accept_button.setProperty('language', 'zh')
        accept_button.setProperty('group', 'param')
        reject_button = QPushButton('取消')
        reject_button.setProperty('language', 'zh')
        reject_button.setProperty('group', 'param')
        button_box = QDialogButtonBox()
        button_box.setOrientation(Qt.Horizontal)
        button_box.addButton(accept_button, QDialogButtonBox.AcceptRole)
        button_box.addButton(reject_button, QDialogButtonBox.RejectRole)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        return button_box
