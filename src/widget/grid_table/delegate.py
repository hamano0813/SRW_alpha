#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Union
from PySide6.QtWidgets import QStyledItemDelegate
from PySide6.QtCore import Qt, QModelIndex
from ..value_spin import ValueSpin
from ..text_line import TextLine
from ..radio_combo import RadioCombo


class Delegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        QStyledItemDelegate.__init__(self, parent)

    def createEditor(self, parent, option, index: QModelIndex):
        column = index.model().headerData(index.column(), Qt.Horizontal)
        data = index.data(Qt.EditRole)
        if mapping := index.model().mapping.get(column):
            editor = RadioCombo(name=column, structure=index.data(Qt.UserRole), mapping=mapping)
        elif isinstance(data, str):
            editor = TextLine(name=column, structure=index.data(Qt.UserRole))
        else:
            editor = ValueSpin(name=column, structure=index.data(Qt.UserRole))
        return editor

    def setEditorData(self, editor: Union[TextLine, ValueSpin], index: QModelIndex) -> None:
        data = index.data(Qt.EditRole)
        editor.set_data(data)

    def setModelData(self, editor: Union[TextLine, ValueSpin], model, index: QModelIndex):
        index.model().setData(index, editor.get_data(), Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index: QModelIndex):
        editor.setGeometry(option.rect)
