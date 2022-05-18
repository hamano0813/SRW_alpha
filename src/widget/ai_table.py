#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QApplication, QStyle, QStyleOptionButton, QStyleOptionViewItem, QCheckBox
from PySide6.QtCore import Qt, QModelIndex, QEvent, QSortFilterProxyModel
from PySide6.QtGui import QPainter

from structure.generic import SEQUENCE
from .array_table import ArrayModel, ArrayDelegate, ArrayTable


class AiModel(ArrayModel):
    def __init__(self, parent, columns):
        super(AiModel, self).__init__(parent, columns)
        self.check_column = self.parent().kwargs.get('check', tuple())

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self.data_sequence) - 3


class AiDelegate(ArrayDelegate):
    def __init__(self, parent):
        super(AiDelegate, self).__init__(parent)

    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex) -> None:
        if index.column() in index.model().sourceModel().check_column:
            checkbox_option = QStyleOptionButton()
            checkbox_option.rect = option.rect
            checkbox_option.rect.moveLeft(option.rect.x() + option.rect.width() // 2 - 6)
            checkbox_option.state = QStyle.State_Enabled | QStyle.State_Active
            if index.data(Qt.EditRole):
                checkbox_option.state |= QStyle.State_On
            else:
                checkbox_option.state |= QStyle.State_Off
            return QApplication.style().drawControl(QStyle.CE_CheckBox, checkbox_option, painter, QCheckBox())
        return super(AiDelegate, self).paint(painter, option, index)

    def editorEvent(self, event: QEvent, model: AiModel | QSortFilterProxyModel, option, index: QModelIndex):
        if event.type() == QEvent.MouseButtonPress and option.rect.contains(event.pos()):
            if index.column() in model.sourceModel().check_column:
                value = index.data(Qt.EditRole)
                value = False if value else True
                return model.sourceModel().setData(index, value, Qt.EditRole)
        return super(AiDelegate, self).editorEvent(event, model, option, index)

    def createEditor(self, parent, option, index: QModelIndex):
        if index.column() in index.model().sourceModel().check_column:
            return None
        return super(AiDelegate, self).createEditor(parent, option, index)


class AiTable(ArrayTable):
    def __init__(self, parent, data_name, columns, **kwargs):
        super(AiTable, self).__init__(parent, data_name, columns, **kwargs)
        self.setItemDelegate(AiDelegate(self))

    # noinspection PyUnresolvedReferences
    def install(self, data_set: dict[str, int | str | SEQUENCE]) -> bool:
        array_model = AiModel(self, self.columns)
        array_model.install(data_set.get(self.data_name, list()))
        proxy = self.generate_proxy()
        proxy.setSourceModel(array_model)
        self.setModel(proxy)

        if self.kwargs.get('resizeColumns', True):
            self.resizeColumnsToContents()
        if self.kwargs.get('resizeRows', True):
            self.resizeRowsToContents()
        stretch_columns = self.kwargs.get('stretch', (0,))
        for column in stretch_columns:
            self.horizontalHeader().setSectionResizeMode(column, self.horizontalHeader().Stretch)

        self.data_set = data_set
        self.control_child(0)

        self.clicked[QModelIndex].connect(self.select_index)
        self.selectionModel().currentChanged[QModelIndex, QModelIndex].connect(self.select_index)
        return True
