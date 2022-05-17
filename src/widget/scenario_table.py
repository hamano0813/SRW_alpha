#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex, QEvent
from PySide6.QtWidgets import QTableView, QAbstractButton, QStyleOptionHeader, QStylePainter, QStyle, QWidget
from widget.abstract_widget import ControlWidget


class ScenarioModel(QAbstractTableModel):
    def __init__(self, parent, columns: tuple[str, str, str], scenario_data: dict[str, tuple[str, str, str]]):
        super(ScenarioModel, self).__init__(parent)
        self.columns = columns
        self.scenario_data = scenario_data

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...):
        if role != Qt.DisplayRole:
            return None
        elif orientation == Qt.Horizontal:
            return self.columns[section]
        return f'  [{section:0{len(hex(len(self.scenario_data) - 1)) - 2}X}]'

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self.scenario_data)

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return len(self.columns)

    def data(self, index: QModelIndex, role: int = ...) -> any:
        if role == Qt.DisplayRole:
            return self.scenario_data[index.row()][index.column()]
        return None

    def flags(self, index: QModelIndex):
        if not index.isValid():
            return None
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable


class ScenarioTable(ControlWidget, QTableView):
    def __init__(self, parent, columns: tuple[str, str, str], **kwargs):
        QTableView.__init__(self, parent=None)
        ControlWidget.__init__(self, parent, data_name='', **kwargs)
        self.columns = columns
        self.horizontalHeader().setProperty('orientation', 'horizontal')
        self.setSelectionMode(QTableView.SingleSelection)
        self.setSelectionBehavior(QTableView.SelectRows)
        self.set_corner(' コード')

    def install(self, scenario_data: dict[str, tuple[str, str, str]]):
        scenario_model = ScenarioModel(self, self.columns, scenario_data)
        self.setModel(scenario_model)
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

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
