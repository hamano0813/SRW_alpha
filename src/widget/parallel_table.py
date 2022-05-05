#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QTableView

from .abstract_widget import ControlWidget


class ParallelTable(ControlWidget, QTableView):
    def __init__(self, father, data_name):
        ControlWidget.__init__(self, father, data_name)
        QTableView.__init__(self, father)
