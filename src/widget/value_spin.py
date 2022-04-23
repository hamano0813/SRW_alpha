#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QSpinBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator
from widget.abstract.editable import EditableWidget


class ValueSpin(EditableWidget, QSpinBox):
    def __init__(self, **kwargs):
        super(QSpinBox, self).__init__(**kwargs)
        self.mapping: dict[int, str] = kwargs.get('mapping')
        self.init_range(self.mapping)
        self.lineEdit().setAlignment(Qt.AlignRight)

    def init_range(self, mapping):
        if mapping:
            self.setRange(min(mapping), max(mapping))
            self.setWrapping(True)
            self.lineEdit().setReadOnly(True)
            return
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
        self.setRange(minimum, maximum - 1)
        self.lineEdit().setValidator(QIntValidator(minimum, maximum - 1))

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

    def get_data(self):
        return self.value()

    def set_data(self, data: int):
        self.setValue(data)
