#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque
from typing import Optional

from PySide6.QtCore import Qt, QAbstractTableModel, QSortFilterProxyModel, QModelIndex, QRegularExpression
from PySide6.QtGui import QAction, QCursor, QKeyEvent
from PySide6.QtWidgets import QApplication, QWidget, QTableView, QMenu, QStyledItemDelegate, QStyleOptionViewItem

from structure.generic import SEQUENCE
from .abstract_widget import ControlWidget, SingleWidget

HALF_FONT = 'Yu Gothic UI Semibold'


class ArrayModel(QAbstractTableModel):
    def __init__(self, parent: Optional['ArrayTable'], columns: dict[str, SingleWidget]):
        super(ArrayModel, self).__init__(parent)
        self.data_sequence: SEQUENCE = list()
        self.columns = columns
        self.history = list()
        self.history = deque(maxlen=100)

    def install(self, data_sequence: SEQUENCE) -> bool:
        self.beginResetModel()
        self.data_sequence = data_sequence
        self.endResetModel()
        return True

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...):
        if role != Qt.DisplayRole:
            return None
        elif orientation == Qt.Horizontal:
            return '      ' + tuple(self.columns.keys())[section] + ' '
        return f'  [{section:0{len(hex(len(self.data_sequence))) - 2}X}]'

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
            return int(self.columns[column_name].kwargs.get('alignment', Qt.AlignLeft) | Qt.AlignVCenter)
        if role == Qt.EditRole:
            return data
        if role == Qt.UserRole:
            return self.data_sequence[index.row()], self.columns[column_name]
        if role == Qt.FontRole:
            if not hasattr(self.columns[column_name], 'init_range'):
                return HALF_FONT
        return None

    def setData(self, index: QModelIndex, data: int | str, role: int = ...) -> bool:
        if not index.isValid():
            return False
        column_name = tuple(self.columns.keys())[index.column()]
        previos_data = self.data_sequence[index.row()][column_name]
        if role == Qt.EditRole:
            _data = self.data_sequence[index.row()][column_name] = data
            if not _data == previos_data:
                self.history.append((index, previos_data))
            return True
        if role == Qt.UserRole:
            _data = self.data_sequence[index.row()][column_name] = self.columns[column_name].interpret(data)
            if not _data == previos_data:
                self.history.append((index, previos_data))
            return True
        return False

    def flags(self, index: QModelIndex):
        if not index.isValid():
            return None
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def undo(self):
        if self.history:
            index, data = self.history.pop()
            column_name = tuple(self.columns.keys())[index.column()]
            self.data_sequence[index.row()][column_name] = data


class ArrayDelegate(QStyledItemDelegate):
    def __init__(self, parent):
        super(ArrayDelegate, self).__init__(parent)

    def createEditor(self, parent, option: QStyleOptionViewItem, index: QModelIndex) -> SingleWidget:
        editor = index.data(Qt.UserRole)[1].new(parent)
        return editor

    def setEditorData(self, editor: SingleWidget, index: QModelIndex) -> None:
        data_set = index.data(Qt.UserRole)[0]
        editor.install(data_set, True)

    def setModelData(self, editor: SingleWidget, model, index: QModelIndex) -> None:
        data = editor.delegate()
        model.setData(index, data, Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index: QModelIndex):
        editor.setGeometry(option.rect.adjusted(-1, -1, 1, 1))


class ArrayTable(ControlWidget, QTableView):
    def __init__(self, parent, data_name, columns: dict[str, SingleWidget | QWidget], **kwargs):
        QTableView.__init__(self, parent=None)
        ControlWidget.__init__(self, parent, data_name, **kwargs)
        self.columns = columns
        self.setItemDelegate(ArrayDelegate(self))
        self.horizontalHeader().setProperty('orientation', 'horizontal')

        self.check_kwargs()

    # noinspection PyUnresolvedReferences
    def install(self, data_set: dict[str, int | str | SEQUENCE]) -> bool:
        array_model = ArrayModel(self, self.columns)
        array_model.install(data_set.get(self.data_name, list()))
        proxy = self.generate_proxy()
        proxy.setSourceModel(array_model)
        self.setModel(proxy)

        self.resizeColumnsToContents()
        self.horizontalHeader().setSectionResizeMode(0, self.horizontalHeader().Stretch)

        self.data_set = data_set
        self.control_child(0)

        self.clicked[QModelIndex].connect(self.select_index)
        self.selectionModel().currentChanged[QModelIndex, QModelIndex].connect(self.select_index)
        return True

    def generate_proxy(self) -> QSortFilterProxyModel:
        proxy = QSortFilterProxyModel(self)
        if self.kwargs.get('sortable', True):
            proxy.setSortRole(Qt.EditRole)
            self.setSortingEnabled(True)
            self.horizontalHeader().setSortIndicatorClearable(True)
        if self.kwargs.get('editable', False):
            proxy.flags = lambda x: Qt.ItemIsEnabled | Qt.ItemIsSelectable
        return proxy

    def select_index(self, index: QModelIndex) -> bool:
        if not index.isValid():
            return False
        self.control_child(self.model().mapToSource(index).row())
        return True

    # noinspection PyUnresolvedReferences
    def check_kwargs(self):
        if self.kwargs.get('single', False):
            self.setSelectionMode(QTableView.SingleSelection)
            self.setSelectionBehavior(QTableView.SelectRows)
        if self.kwargs.get('copy', True):
            self.setContextMenuPolicy(Qt.CustomContextMenu)
            self.customContextMenuRequested.connect(self.copy_paste)

    def keyPressEvent(self, event: QKeyEvent) -> bool:
        if self.kwargs.get('copy', True):
            if event.key() == Qt.Key_C and event.modifiers() == Qt.ControlModifier:
                return self.copy_range()
            elif event.key() == Qt.Key_V and event.modifiers() == Qt.ControlModifier:
                return self.paste_range()
            elif event.key() == Qt.Key_Z and event.modifiers() == Qt.ControlModifier:
                self.model().sourceModel().undo()
                self.reset()
                return True
        super(ArrayTable, self).keyPressEvent(event)
        return True

    def filterChanged(self, text: str) -> None:
        filter_text = text.strip()
        if filter_text:
            pattern = QRegularExpression.wildcardToRegularExpression(f'*{filter_text}*')
            regexp = QRegularExpression(pattern)
            options = regexp.patternOptions() | QRegularExpression.CaseInsensitiveOption
            regexp.setPatternOptions(options)
            self.model().setFilterRegularExpression(regexp)
        else:
            self.model().setFilterRegularExpression('')

    def copy_paste(self) -> None:
        right_click_menu = QMenu()
        copy_action = QAction('复制(C)', self)
        copy_action.triggered.connect(self.copy_range)
        paste_action = QAction('粘贴(V)', self)
        paste_action.triggered.connect(self.paste_range)
        right_click_menu.addActions([copy_action, paste_action])
        right_click_menu.exec_(QCursor().pos())

    def copy_range(self) -> bool:
        if not self.selectedIndexes():
            return False
        indexes = tuple(map(self.model().mapToSource, self.selectedIndexes()))
        row_set = set(map(lambda idx: idx.row(), indexes))
        col_set = set(map(lambda idx: idx.column(), indexes))
        row_count = max(row_set) - min(row_set) + 1
        col_count = max(col_set) - min(col_set) + 1
        data = [[''] * col_count for _ in range(row_count)]
        for index in indexes:
            data[index.row() - min(row_set)][index.column() - min(col_set)] = index.data(Qt.DisplayRole)
        text = '\n'.join(['\t'.join(row) for row in data])
        QApplication.clipboard().setText(text)
        return True

    def paste_range(self) -> bool:
        if not self.selectedIndexes():
            return False
        if not (text := QApplication.clipboard().text().rstrip()):
            return False
        internal_id = self.selectedIndexes()[0].internalId()
        data = [row.split('\t') for row in text.split('\n')]
        min_row = min(map(lambda idx: idx.row(), self.selectedIndexes()))
        min_col = min(map(lambda idx: idx.column(), self.selectedIndexes()))
        for rid, row in enumerate(data):
            for cid, text in enumerate(row):
                index = self.model().createIndex(min_row + rid, min_col + cid, internal_id)
                source_index = self.model().mapToSource(index)
                self.model().sourceModel().setData(source_index, text, Qt.UserRole)
        self.reset()
        return True
