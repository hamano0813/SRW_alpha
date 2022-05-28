#!/usr/bin/env python
# -*- coding: utf-8 -*-

from struct import calcsize, pack, unpack

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QDialog, QFormLayout, QDialogButtonBox, QComboBox, QPushButton, QVBoxLayout,
                               QPlainTextEdit, QLabel, QApplication, QHBoxLayout)

from structure.specific.sndata_bin.command import Command
from widget.command.command_explain import CommandExplain
from widget.command.param_widget import ParamWidget


class CommandDialog(QDialog):
    def __init__(self, parent, command: dict = None, **kwargs):
        super(CommandDialog, self).__init__(parent, f=Qt.Dialog)
        self.setWindowTitle('编辑指令' if command else '插入指令')
        self.explain: CommandExplain = CommandExplain(**kwargs)
        self.widgets: list[ParamWidget] = list()

        self.code_combo = QComboBox()
        self.code_combo.setProperty('language', 'zhb')
        self.code_combo.setProperty('group', 'param')
        self.code_combo.setFixedWidth(400)
        for code, settings in self.explain.settings.items():
            self.code_combo.addItem(settings[2], code)

        self.explain_text = QPlainTextEdit()
        self.explain_text.setReadOnly(True)
        self.explain_text.setContextMenuPolicy(Qt.NoContextMenu)
        self.explain_text.setProperty('language', 'zh')
        self.explain_text.setFixedWidth(480)

        self.edit_layout = QFormLayout()

        left_layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        l1 = QLabel('指令选择')
        l1.setProperty('language', 'zhb')
        top_layout.addWidget(l1)
        top_layout.addWidget(self.code_combo)
        l2 = QLabel('指令释义')
        l2.setProperty('language', 'zhb')
        left_layout.addLayout(top_layout)
        left_layout.addWidget(l2)
        left_layout.addWidget(self.explain_text)

        right_layout = QVBoxLayout()
        right_layout.addLayout(self.edit_layout)
        right_layout.addStretch()
        right_layout.addWidget(self.init_button())

        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)
        self.setLayout(main_layout)

        self.init_widgets(command)
        # noinspection PyUnresolvedReferences
        self.code_combo.currentIndexChanged.connect(self.reset_widgets)

    def get_command(self) -> dict[str, int | list[int]]:
        if self.exec():
            return self.command()

    def command(self) -> dict[str, int | list[int]]:
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
    def generate_data(command: dict) -> None:
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

    def explain_command(self) -> None:
        self.explain_text.setPlainText(self.explain.explain(self.command()))

    def init_widgets(self, command: dict = None) -> None:
        code = 0 if not command else command['Code']
        param = [1] if not command else command['Param']

        param_widgets: list[ParamWidget] = self.explain.settings.get(code)[1]
        self.code_combo.setCurrentIndex(list(self.explain.settings.keys()).index(code))

        for param_widget in param_widgets:
            widget: ParamWidget = param_widget.new()
            if widget.name == '无效参数':
                # noinspection PyUnresolvedReferences
                widget.setEnabled(False)
            label = QLabel(widget.name)
            label.setProperty('language', 'zhb')
            label.setFixedWidth(72)
            self.edit_layout.addRow(label, widget)
            self.widgets.append(widget)

        if code == 0xB9:
            self.widgets[0].dataChanged[int].connect(self.adjust_b9)

        for idx, widget in enumerate(self.widgets):
            widget.install(param[idx])
            if idx > 0 or code != 0xB9:
                widget.dataChanged.connect(self.explain_command)

        self.explain_command()
        self.special_rule()
        self.resize_self()

    def reset_widgets(self) -> None:
        for i in range(len(self.widgets)):
            self.edit_layout.removeRow(0)
        self.widgets = list()

        code = self.code_combo.currentData()
        param_widgets: list[ParamWidget] = self.explain.settings.get(code)[1]
        for param_widget in param_widgets:
            widget: ParamWidget = param_widget.new()
            if widget.name == '无效参数':
                # noinspection PyUnresolvedReferences
                widget.setEnabled(False)
            label = QLabel(widget.name)
            label.setProperty('language', 'zhb')
            label.setFixedWidth(72)
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

    def resize_self(self) -> None:
        QApplication.processEvents()
        self.resize(self.minimumSizeHint())

    def adjust_b9(self, count: int) -> None:
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

    # TODO
    # noinspection PyUnresolvedReferences
    def special_rule(self) -> None:
        match self.code_combo.currentData():
            case 0xB9:
                self.widgets[0].setRange(1, 5)

    # noinspection PyUnresolvedReferences
    def init_button(self) -> QDialogButtonBox:
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
