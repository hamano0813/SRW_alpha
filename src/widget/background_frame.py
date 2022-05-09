#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame

from .abstract_widget import BackgroundWidget


class BackgroundFrame(BackgroundWidget, QFrame):
    def __init__(self, parent, **kwargs):
        QFrame.__init__(self, parent, Qt.Widget)
        BackgroundWidget.__init__(self, **kwargs)
