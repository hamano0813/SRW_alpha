#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex, QEvent
from PySide6.QtGui import QMouseEvent, QCursor, QAction, QKeyEvent, QFont
from PySide6.QtWidgets import (QTableView, QApplication, QPushButton, QVBoxLayout, QFrame, QHBoxLayout, QAbstractButton,
                               QStyleOptionHeader, QWidget, QStyle, QStylePainter, QMenu)

from structure.generic import SEQUENCE
from widget.abstract_widget import ControlWidget, AbstractWidget
from widget.command.command_dialog import CommandDialog


class StageModel(QAbstractTableModel):
    def __init__(self, parent, **kwargs):
        super(StageModel, self).__init__(parent)
        self.commands: list[dict[str, int | str]] = list()
        self.columns = ('指令码', '指令释义')
        self.explain = CommandDialog(None, **kwargs)

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
            if index.column() == 1:
                # return EnumData.COMMAND['简介'].get(command)
                return self.explain.explain(command)
        if role == Qt.ToolTipRole:
            if index.column() == 0:
                return str(command)
        if role == Qt.FontRole:
            font = QFont()
            if index.column() == 1:
                font.setFamily('Microsoft Yahei UI')
                if command['Code'] <= 0x01:
                    font.setBold(True)
                    font.setLetterSpacing(QFont.PercentageSpacing, 150)
                    font.setFamily('Consolas')
                    font.setPointSize(12)
                if command['Code'] in (0x08, 0x09, 0x0A):
                    font.setUnderline(True)
                    font.setFamily('Consolas')
                    font.setPointSize(12)
                if command['Code'] in range(0x02, 0x08):
                    font.setItalic(True)
                    font.setFamily('Consolas')
                    font.setPointSize(12)
            return font
        return None

    def flags(self, index: QModelIndex):
        if not index.isValid():
            return None
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def find_target(self, pos: int):
        for idx, command in enumerate(self.commands):
            if command['Pos'] == pos:
                return idx
        return None

    def find_start(self, end_row: int):
        for row in range(end_row, 1, -1):
            if self.commands[row - 1]['Code'] in (0x01, 0x0A):
                pos = self.commands[row]['Pos']
                for idx, command in enumerate(self.commands):
                    if command['Code'] in (0x08, 0x09):
                        if command['Param'][0] == pos:
                            return idx
        return None

    def insert_command(self, row: int, command: dict[str, int | str | list]):
        self.beginInsertRows(QModelIndex(), row, row)
        command['Pos'] = self.commands[row]['Pos']
        for idx, _command in enumerate(self.commands):
            if idx >= row:
                _command['Pos'] += command['Count']
            if (_command['Code'] in (0x08, 0x09)) and (_command['Param'][0] > command['Pos']):
                _command['Param'][0] += command['Count']
        self.commands.insert(row, command)
        self.endInsertRows()

    def remove_command(self, row: int):
        self.beginRemoveRows(QModelIndex(), row, row)
        command = self.commands.pop(row)
        for idx, _command in enumerate(self.commands):
            if idx >= row:
                _command['Pos'] -= command['Count']
            if (_command['Code'] in (0x08, 0x09)) and (_command['Param'][0] > command['Pos']):
                _command['Param'][0] -= command['Count']
        self.endRemoveRows()

    def update_command(self, row: int, command: dict[str, int | str | list]):
        self.remove_command(row)
        self.insert_command(row, command)


class StageTable(QTableView, ControlWidget):
    def __init__(self, parent, data_name, **kwargs):
        QTableView.__init__(self, parent=None)
        ControlWidget.__init__(self, parent, data_name, **kwargs)
        self.jump_indexes = []

        self.horizontalHeader().setProperty('language', 'zh')
        self.verticalHeader().setFixedWidth(40)
        self.verticalHeader().setDefaultAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        # noinspection PyUnresolvedReferences
        self.customContextMenuRequested.connect(self.right_menu)

        if corner := self.kwargs.get('corner', False):
            self.set_corner(corner)

    def install(self, data_set: dict[str, int | str | SEQUENCE]) -> bool:
        model = StageModel(self, **self.kwargs)
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
        self.jump_indexes = []
        return True

    def select_index(self, index: QModelIndex) -> bool:
        if not index.isValid():
            return False
        self.control_child(index.row())
        return True

    def insert_command(self):
        if not self.selectedIndexes():
            row = self.model().rowCount()
        else:
            row = self.selectedIndexes()[0].row()
        print(row)

    def remove_command(self):
        if not self.selectedIndexes():
            return False
        row_set = set(map(lambda idx: idx.row(), self.selectedIndexes()))
        for row in row_set:
            self.model().remove_command(row)
        return True

    def update_command(self):
        if not self.selectedIndexes():
            return False
        row = self.selectedIndexes()[0].row()
        print(row)

    def right_menu(self) -> None:
        right_click_menu = QMenu()
        right_click_menu.setProperty('language', 'zh')
        copy_action = QAction('复制(C)', self)
        copy_action.triggered.connect(self.copy_range)
        right_click_menu.addActions([copy_action])
        right_click_menu.exec_(QCursor().pos())

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

    def back_jump(self):
        if self.jump_indexes:
            self.setCurrentIndex(self.jump_indexes.pop(-1))
            return True
        return False

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        index = self.indexAt(event.pos())
        text: str = index.data(Qt.DisplayRole)
        if text.startswith('GOTO') or text.startswith('RUN'):
            pos = int(text.split(' ')[-1])
            if row := self.model().find_target(pos):
                self.setCurrentIndex(self.model().createIndex(row, 1))
                self.jump_indexes.append(index)
        if text == 'BACK':
            if row := self.model().find_start(index.row()):
                self.setCurrentIndex(self.model().createIndex(row, 1))
                self.jump_indexes.append(index)

    def keyPressEvent(self, event: QKeyEvent) -> bool:
        if event.key() == Qt.Key_C and event.modifiers() == Qt.ControlModifier:
            return self.copy_range()
        if event.key() == Qt.Key_Backspace:
            return self.back_jump()
        super(StageTable, self).keyPressEvent(event)
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

        layout = QHBoxLayout()
        layout.addWidget(self.table)
        layout.addLayout(self.init_buttons())
        self.setLayout(layout)

    # noinspection PyUnresolvedReferences
    def init_buttons(self):
        edit_button = QPushButton('编辑')
        insert_button = QPushButton('插入')
        delete_button = QPushButton('删除')
        edit_button.clicked.connect(self.table.update_command)
        insert_button.clicked.connect(self.table.insert_command)
        delete_button.clicked.connect(self.table.remove_command)
        button_layout = QVBoxLayout()
        button_layout.addWidget(edit_button)
        button_layout.addWidget(insert_button)
        button_layout.addWidget(delete_button)
        button_layout.addStretch()
        return button_layout

    def install(self, data_set: dict[str, int | str | SEQUENCE]) -> bool:
        return self.table.install(data_set)
