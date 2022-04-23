#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QLineEdit
from widget.abstract.editable import EditableWidget


class TextLine(EditableWidget, QLineEdit):
    def __init__(self, **kwargs):
        super(TextLine, self).__init__(**kwargs)

    def get_data(self):
        return self.text().strip()

    def set_data(self, data: str):
        self.setText(data)
