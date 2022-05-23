#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ParamWidget:
    def __init__(self, name: str, default: int, **kwargs):
        self.name = name
        self.default = default
        self.kwargs = kwargs

    def install(self, param: int = None):
        pass

    def data(self) -> int:
        pass

    def explain(self, param: int) -> str:
        pass

    def new(self):
        return self.__class__(self.name, self.default, **self.kwargs)

    def __del__(self):
        # noinspection PyUnresolvedReferences
        self.close()
        del self
