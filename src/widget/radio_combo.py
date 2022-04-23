#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QComboBox
from widget.abstract.editable import EditableWidget


class RadioCombo(EditableWidget, QComboBox):
    def __init__(self, **kwargs):
        super(RadioCombo, self).__init__(**kwargs)
        self.mapping: dict[int, str] = kwargs.get('mapping')
        self.init_mapping(self.mapping)

    def init_mapping(self, mapping: dict[int, str] = None):
        if mapping:
            for k, v in mapping.items():
                self.addItem(v, k)

    def get_data(self):
        return self.currentData()

    def set_data(self, data: int):
        self.setCurrentText(self.mapping.get(data, 0))
