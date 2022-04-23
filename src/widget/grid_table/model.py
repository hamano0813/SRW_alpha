#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex


class Model(QAbstractTableModel):
    def __init__(self, structures: list[dict[str, list]], titles: list[str], mapping: dict[str, dict], parent):
        QAbstractTableModel.__init__(self, parent)
        self.structures = structures
        self.titles = titles
        self.mapping = mapping

    def rowCount(self, parent=None, *args, **kwargs):
        if not self.structures:
            return 0
        return len(self.structures)

    def columnCount(self, parent=None, *args, **kwargs):
        return len(self.titles)

    def headerData(self, section: int, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.titles[section]
        elif orientation == Qt.Vertical and role == Qt.DisplayRole:
            return f'[{section:0{len(str(len(self.structures)))}X}]'

    def data(self, index: QModelIndex, role=None):
        if not index.isValid():
            return None
        column = self.titles[index.column()]
        data = self.structures[index.row()][column]
        if role == Qt.DisplayRole:
            if mapping := self.mapping.get(column):
                return mapping.get(data)
            return data
        if role == Qt.EditRole:
            return data
        if role == Qt.UserRole:
            return self.structures[index.row().settings.get(column)]
        if role == Qt.TextAlignmentRole:
            if self.mapping.get(column) or isinstance(data, str):
                return Qt.AlignLeft | Qt.AlignVCenter
            return Qt.AlignRight | Qt.AlignVCenter

    def setData(self, index: QModelIndex, data, role=Qt.EditRole):
        if index.isValid() and role == Qt.EditRole and data is not None:
            column = self.titles[index.column()]
            self.structures[index.row()][column] = data

    def flags(self, index: QModelIndex):
        if not index.isValid():
            return None
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable
