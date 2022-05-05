#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QLineEdit

from structure.generic import Text
from .abstract_widget import SingleWidget


class TextLine(SingleWidget, QLineEdit):
    def __init__(self, parent, data_name, structure: Text, **kwargs):
        QLineEdit.__init__(self, parent)
        SingleWidget.__init__(self, parent, data_name, structure, **kwargs)
        if extra := kwargs.get('extra'):
            self.structure.extra |= extra
        if alignment := kwargs.get('alignment'):
            self.setAlignment(alignment)

    # noinspection PyUnresolvedReferences
    def install(self, data_set: dict[str, int | str]) -> bool:
        self.disconnect(self)
        self.data_set = data_set
        text = self.data_set.get(self.data_name)
        if text:
            self.setText(text)
        self.editingFinished.connect(self.write)
        return True

    def write(self) -> bool:
        text = self.text().strip()
        self.data_set[self.data_name] = text
        return True

    def display(self, text: str) -> str:
        if text:
            return text
        return ''
