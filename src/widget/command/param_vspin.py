#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QSpinBox

from widget.command.param_widget import ParamWidget


class ParamVSpin(QSpinBox, ParamWidget):
    def __init__(self, name: str, default: int, display: str = 'd', **kwargs):
        QSpinBox.__init__(self, parent=None)
        ParamWidget.__init__(self, name, default, **kwargs)
        self.display = display
        self.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.valueChanged.connect(self.data_change)

    def textFromValue(self, val: int) -> str:
        return f'{val:{self.display}}'

    def valueFromText(self, text: str) -> int:
        fmt = self.display.lower()
        if fmt.endswith('d'):
            return int(text)
        if fmt.endswith('x'):
            return int(text, 16)
        if fmt.endswith('b'):
            return int(text, 2)

    def install(self, param: int = None):
        if param is not None:
            return self.setValue(param)
        return self.setValue(self.default)

    def data(self) -> int:
        return self.value()

    def explain(self, param: int) -> str:
        return self.textFromValue(param)

    def new(self):
        return self.__class__(self.name, self.default, self.display, **self.kwargs)
