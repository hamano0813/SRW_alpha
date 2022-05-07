#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QComboBox

from structure.generic import Value
from .abstract_widget import SingleWidget


class MappingSpin(SingleWidget, QComboBox):
    def __init__(self, parent, data_name: str, structure: Value, mapping: dict[int, str], **kwargs):
        QComboBox.__init__(self, parent)
        SingleWidget.__init__(self, parent, data_name, structure, **kwargs)
        self.mapping = mapping

    def init_mapping(self):
        for data, text in self.mapping.items():
            self.addItem(text, data)

    # noinspection PyUnresolvedReferences
    def install(self, data_set: dict[str, int | str], delegate: bool = False) -> bool:
        self.disconnect(self)
        self.data_set = data_set
        value = self.data_set.get(self.data_name, 0)
        self.setCurrentIndex(list(self.mapping.keys()).index(value))
        if not delegate:
            self.currentIndexChanged.connect(self.overwrite)
        return True

    def display(self, value: int) -> str:
        return '      ' + self.mapping.get(value, '') + '      '

    def interpret(self, text: str) -> int:
        mapping = {value: key for key, value in self.mapping.items()}
        return mapping.get(text, self.data_set.get(self.data_name, 0))

    def delegate(self) -> int | str:
        return self.interpret(self.currentText())
