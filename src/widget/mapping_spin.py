#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QSpinBox

from structure.generic import Value
from .abstract_widget import SingleWidget


class MappingSpin(SingleWidget, QSpinBox):
    def __init__(self, parent, data_name: str, structure: Value, mapping: dict[int, str], **kwargs):
        QSpinBox.__init__(self, parent)
        SingleWidget.__init__(self, parent, data_name, structure, **kwargs)
        self.mapping = mapping
        if alignment := kwargs.get('alignment'):
            self.setAlignment(alignment)
        if font := kwargs.get('font'):
            self.setFont(font)
        self.init_mapping()

    def init_mapping(self) -> bool:
        self.setRange(min(self.mapping), max(self.mapping))
        self.setWrapping(True)
        self.lineEdit().setReadOnly(True)
        return True

    def textFromValue(self, value: int) -> str:
        return self.mapping.get(value, str(value))

    def valueFromText(self, text: str) -> int:
        return {value: key for key, value in self.mapping.items()}.get(text)

    # noinspection PyUnresolvedReferences
    def install(self, data_set: dict[str, int | str], delegate: bool = False) -> bool:
        self.disconnect(self)
        self.data_set = data_set
        value = self.data_set.get(self.data_name, 0)
        self.setValue(value)
        if not delegate:
            self.valueChanged.connect(self.overwrite)
        return True

    def display(self, value: int) -> str:
        return '      ' + self.textFromValue(value) + '      '

    def interpret(self, text: str) -> int:
        return self.valueFromText(text)

    def delegate(self) -> int:
        return self.value()
