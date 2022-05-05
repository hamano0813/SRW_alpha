#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QFrame
from PySide6.QtCore import Qt

from .abstract_widget import BackgroundWidget


class BackgroundFrame(BackgroundWidget, QFrame):
    def __init__(self, parent):
        QFrame.__init__(self, parent, Qt.Widget)
        BackgroundWidget.__init__(self)
