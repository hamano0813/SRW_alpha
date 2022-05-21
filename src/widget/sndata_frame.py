#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex, QEvent
from PySide6.QtWidgets import (QTableView, QApplication, QPushButton, QVBoxLayout, QFrame, QHBoxLayout, QAbstractButton,
                               QStyleOptionHeader, QWidget, QStyle, QStylePainter)

from structure.generic import SEQUENCE
from widget.abstract_widget import ControlWidget, AbstractWidget


class StageModel(QAbstractTableModel):
    def __init__(self, parent, **kwargs):
        super(StageModel, self).__init__(parent)
        self.commands: list[dict[str, int | str]] = list()
        self.columns = ('指令碼', '指令釋義')

    def install(self, commands: SEQUENCE) -> bool:
        self.beginResetModel()
        self.commands = commands
        self.endResetModel()
        return True

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...):
        if role != Qt.DisplayRole:
            return None
        elif orientation == Qt.Horizontal:
            return self.columns[section]
        return self.commands[section]["Pos"]

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self.commands)

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return 2

    def data(self, index: QModelIndex, role: int = ...) -> any:
        command = self.commands[index.row()]
        if role == Qt.DisplayRole:
            if index.column() == 0:
                return command['Data']
        if role == Qt.ToolTipRole:
            if index.column() == 0:
                return str(command)
        return None

    def flags(self, index: QModelIndex):
        if not index.isValid():
            return None
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable


class StageTable(QTableView, ControlWidget):
    def __init__(self, parent, data_name, **kwargs):
        QTableView.__init__(self, parent=None)
        ControlWidget.__init__(self, parent, data_name, **kwargs)
        self.verticalHeader().setFixedWidth(40)
        self.verticalHeader().setDefaultAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        if corner := self.kwargs.get('corner', False):
            self.set_corner(corner)

    def install(self, data_set: dict[str, int | str | SEQUENCE]) -> bool:
        model = StageModel(self)
        model.install(data_set.get(self.data_name, list()))
        self.setModel(model)
        self.resizeRowsToContents()
        self.resizeColumnsToContents()
        self.horizontalHeader().setSectionResizeMode(1, self.horizontalHeader().Stretch)
        self.data_set = data_set
        self.control_child(0)

        # noinspection PyUnresolvedReferences
        self.clicked[QModelIndex].connect(self.select_index)
        # noinspection PyUnresolvedReferences
        self.selectionModel().currentChanged[QModelIndex, QModelIndex].connect(self.select_index)
        return True

    def select_index(self, index: QModelIndex) -> bool:
        if not index.isValid():
            return False
        self.control_child(index.row())
        return True

    def copy_range(self) -> bool:
        if not self.selectedIndexes():
            return False
        row_set = set(map(lambda idx: idx.row(), self.selectedIndexes()))
        col_set = set(map(lambda idx: idx.column(), self.selectedIndexes()))
        row_count = max(row_set) - min(row_set) + 1
        col_count = max(col_set) - min(col_set) + 1
        data = [[''] * col_count for _ in range(row_count)]
        for index in self.selectedIndexes():
            data[index.row() - min(row_set)][index.column() - min(col_set)] = index.data(Qt.DisplayRole)
        text = '\n'.join(['\t'.join(row) for row in data])
        QApplication.clipboard().setText(text)
        return True

    def set_corner(self, text: str):
        # noinspection PyTypeChecker
        corner_button: QAbstractButton = self.findChild(QAbstractButton)
        corner_button.setText(text)
        corner_button.setObjectName('Corner')
        corner_button.installEventFilter(self)
        option = QStyleOptionHeader()
        option.text = corner_button.text()

    def eventFilter(self, obj: QWidget, event: QEvent) -> bool:
        if event.type() != QEvent.Paint or not isinstance(obj, QAbstractButton):
            return False
        option: QStyleOptionHeader = QStyleOptionHeader()
        option.initFrom(obj)
        style_state = QStyle.State_None
        if obj.isEnabled():
            style_state |= QStyle.State_Enabled
        if obj.isActiveWindow():
            style_state |= QStyle.State_Active
        if obj.isDown():
            style_state |= QStyle.State_Sunken
        option.state = style_state
        option.rect = obj.rect()
        option.text = obj.text()
        option.position = QStyleOptionHeader.OnlyOneSection
        painter = QStylePainter(obj)
        painter.drawControl(QStyle.CE_Header, option)
        return True


class StageFrame(QFrame, AbstractWidget):
    def __init__(self, parent, data_name, **kwargs):
        QFrame.__init__(self, parent)
        AbstractWidget.__init__(self, parent, data_name, **kwargs)
        self.table = StageTable(parent, data_name, **kwargs)

        edit_button = QPushButton('Edit')
        insert_button = QPushButton('Insert')
        delete_button = QPushButton('Delete')
        button_layout = QVBoxLayout()
        button_layout.addWidget(edit_button)
        button_layout.addWidget(insert_button)
        button_layout.addWidget(delete_button)
        button_layout.addStretch()

        layout = QHBoxLayout()
        layout.addWidget(self.table)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def install(self, data_set: dict[str, int | str | SEQUENCE]) -> bool:
        return self.table.install(data_set)
