#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QSpinBox

from structure.generic import Value
from .abstract_widget import SingleWidget


class ValueSpin(SingleWidget, QSpinBox):
    def __init__(self, parent, data_name: str, structure: Value, **kwargs):
        QSpinBox.__init__(self, parent)
        SingleWidget.__init__(self, parent, data_name, structure, **kwargs)
        self.mapping = kwargs.get('mapping')
        self.multiple = kwargs.get('multiple')
        if alignment := kwargs.get('alignment'):
            self.setAlignment(alignment)
        self.init_range()

    def init_range(self) -> bool:
        if self.mapping:
            self.setRange(min(self.mapping), max(self.mapping))
            self.setWrapping(True)
            self.lineEdit().setReadOnly(True)
            return True
        if (length := self.structure.length) > 0:
            maximum = 0x100 ** length
        else:
            maximum = 0x100 ** abs(length) // 2
        minimum = maximum - 0x100 ** abs(length)
        if self.structure.bit is not None:
            minimum = 0
            if isinstance(self.structure, int):
                maximum = 2
            else:
                maximum = (1 << (self.structure.bit[1] - self.structure.bit[0]))
        maximum -= 1
        if self.multiple:
            minimum *= self.multiple
            maximum *= self.multiple
            self.setSingleStep(self.multiple)
        self.setRange(minimum, maximum)
        self.lineEdit().setValidator(QIntValidator(minimum, maximum))
        return True

    def textFromValue(self, value: int) -> str:
        if self.mapping:
            return self.mapping.get(value, str(value))
        if self.structure.length < 0:
            return f'{value:+d}'
        return str(value)

    def valueFromText(self, text: str) -> int:
        if self.mapping:
            return {value: key for key, value in self.mapping.items()}.get(text, 0)
        try:
            return int(text)
        except ValueError:
            return self.value()

    # noinspection PyUnresolvedReferences
    def install(self, data_set: dict[str, int]) -> bool:
        self.disconnect(self)
        self.data_set = data_set
        value = self.data_set.get(self.data_name, 0)
        if self.multiple:
            self.setValue(value * self.multiple)
        else:
            self.setValue(value)
        self.valueChanged.connect(self.write)
        return True

    def write(self) -> bool:
        value = self.value() // self.multiple if self.multiple else self.value()
        self.data_set[self.data_name] = value
        return True

    def display(self, value: int) -> str:
        return '     ' + self.textFromValue(value) + '      '
