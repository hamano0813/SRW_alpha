#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide6.QtCore import Signal


class ParamWidget:
    dataChanged = Signal(int)

    # noinspection PyUnresolvedReferences
    def __init__(self, name: str, default: int, **kwargs):
        self.name = name
        self.default = default
        self.kwargs = kwargs
        self.setProperty('language', 'zh')
        self.setProperty('group', 'param')

    def install(self, param: int = None):
        pass

    def data(self) -> int:
        pass

    def explain(self, param: int) -> str:
        pass

    def data_change(self):
        # noinspection PyUnresolvedReferences
        self.dataChanged.emit(self.data())

    def new(self):
        return self.__class__(self.name, self.default, **self.kwargs)
