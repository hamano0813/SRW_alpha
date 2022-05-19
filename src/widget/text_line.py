#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QLineEdit

from structure.generic import Text
from .abstract_widget import SingleWidget


class TextLine(SingleWidget, QLineEdit):
    def __init__(self, parent, data_name, structure: Text, extra: dict[str, str] = None, **kwargs):
        QLineEdit.__init__(self, parent)
        SingleWidget.__init__(self, parent, data_name, structure, **kwargs)
        if extra:
            self.structure.extra |= extra
        if alignment := kwargs.get('alignment'):
            self.setAlignment(alignment)
        if font := self.kwargs.get('font'):
            self.setFont(font)

    def install(self, data_set: dict[str, int | str], delegate: bool = False) -> bool:
        self.disconnect(self)
        self.data_set = data_set
        text = self.data_set.get(self.data_name)
        self.setText(self.display(text))
        if not delegate:
            self.editingFinished.connect(self.overwrite)
        return True

    def display(self, text: str) -> str:
        if text is not None:
            return text
        return ''

    def interpret(self, text: str) -> str:
        return text.strip()

    def delegate(self):
        return self.interpret(self.text())
