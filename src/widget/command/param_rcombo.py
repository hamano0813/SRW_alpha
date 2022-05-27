#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QComboBox

from widget.command.param_widget import ParamWidget


class ParamRCombo(QComboBox, ParamWidget):
    def __init__(self, name: str, default: int, mapping: dict[int, str], **kwargs):
        QComboBox.__init__(self, parent=None)
        ParamWidget.__init__(self, name, default, **kwargs)
        self.mapping = mapping
        for key, text in self.mapping.items():
            self.addItem(text.replace('\n', '').replace('\u3000', ''), key)
        # noinspection PyUnresolvedReferences
        self.currentIndexChanged.connect(self.data_change)

    def install(self, param: int = None):
        if param is not None:
            return self.setCurrentIndex(list(self.mapping.keys()).index(param))
        return self.setCurrentIndex(list(self.mapping.keys()).index(self.default))

    def data(self) -> int:
        return list(self.mapping.keys())[self.currentIndex()]

    def explain(self, param: int) -> str:
        return self.mapping.get(param).replace('\u3000', '')

    def new(self):
        return self.__class__(self.name, self.default, self.mapping, **self.kwargs)
