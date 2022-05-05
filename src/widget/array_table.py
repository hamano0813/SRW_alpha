#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Optional

from PySide6.QtCore import Qt, QAbstractTableModel, QSortFilterProxyModel, QModelIndex, QRegularExpression, QRect
from PySide6.QtWidgets import QWidget, QTableView, QStyledItemDelegate, QStyleOptionViewItem

from structure.generic import SEQUENCE
from .abstract_widget import ControlWidget, SingleWidget


class ArrayModel(QAbstractTableModel):
    def __init__(self, parent: Optional['ArrayTable'], columns: dict[str, SingleWidget]):
        super(ArrayModel, self).__init__(parent)
        self.data_sequence: SEQUENCE = list()
        self.columns = columns

    def install(self, data_sequence: SEQUENCE) -> bool:
        self.beginResetModel()
        self.data_sequence = data_sequence
        self.endResetModel()
        return True

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...):
        if role != Qt.DisplayRole:
            return None
        elif orientation == Qt.Horizontal:
            return tuple(self.columns.keys())[section]
        return f'[{section:0{len(hex(len(self.data_sequence))) - 2}X}]'

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self.data_sequence)

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return len(self.columns)

    def data(self, index: QModelIndex, role: int = ...) -> any:
        column_name = tuple(self.columns.keys())[index.column()]
        data = self.data_sequence[index.row()][column_name]
        if role == Qt.DisplayRole:
            return self.columns[column_name].display(data)
        if role == Qt.TextAlignmentRole:
            return int(self.columns[column_name].kwargs.get('alignment', Qt.AlignVCenter))
        if role == Qt.EditRole:
            return data
        if role == Qt.UserRole:
            return self.data_sequence[index.row()], self.columns[column_name]
        return None

    def flags(self, index: QModelIndex):
        if not index.isValid():
            return None
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable


class ArrayDelegate(QStyledItemDelegate):
    def __init__(self, parent):
        super(ArrayDelegate, self).__init__(parent)

    def createEditor(self, parent, option: QStyleOptionViewItem, index: QModelIndex) -> SingleWidget:
        editor = index.model().data(index, Qt.UserRole)[1].new(parent)
        return editor

    def setEditorData(self, editor: SingleWidget, index: QModelIndex) -> None:
        data_set = index.model().data(index, Qt.UserRole)[0]
        editor.install(data_set)

    def setModelData(self, editor: SingleWidget, model, index: QModelIndex) -> None:
        pass

    def updateEditorGeometry(self, editor, option, index: QModelIndex):
        editor.setGeometry(option.rect.adjusted(-1, -1, 1, 1))


class ArrayTable(ControlWidget, QTableView):
    def __init__(self, parent, data_name, columns: dict[str, SingleWidget | QWidget]):
        QTableView.__init__(self, parent=None)
        ControlWidget.__init__(self, parent, data_name)
        self.columns = columns
        self.array_delegate = ArrayDelegate(self)
        self.setItemDelegate(self.array_delegate)
        self.proxy_model = QSortFilterProxyModel(self)
        self.proxy_model.setSortRole(Qt.EditRole)
        self.setSortingEnabled(True)
        self.horizontalHeader().setSortIndicatorClearable(True)
        self.horizontalHeader().setProperty('orientation', 'horizontal')

    def install(self, data_set: dict[str, int | str | SEQUENCE]) -> bool:
        array_model = ArrayModel(self, self.columns)
        array_model.install(data_set.get(self.data_name, list()))
        self.proxy_model.setSourceModel(array_model)
        self.setModel(self.proxy_model)
        self.resizeColumnsToContents()
        self.data_set = data_set
        self.control_child(0)
        return True

    def filterChanged(self, text: str) -> None:
        filter_text = text.strip()
        if filter_text:
            pattern = QRegularExpression.wildcardToRegularExpression(f'*{filter_text}*')
            regexp = QRegularExpression(pattern)
            options = regexp.patternOptions() | QRegularExpression.CaseInsensitiveOption
            regexp.setPatternOptions(options)
            self.proxy_model.setFilterRegularExpression(regexp)
        else:
            self.proxy_model.setFilterRegularExpression('')
