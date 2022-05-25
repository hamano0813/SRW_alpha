#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex, QEvent
from PySide6.QtWidgets import QComboBox, QTableView, QAbstractButton, QStyleOptionHeader, QWidget, QStyle, QStylePainter

from widget.command.param_widget import ParamWidget

class MappingModel(QAbstractTableModel):
    def __init__(self, mapping: dict[int, str]):
        super(MappingModel, self).__init__(parent=None)
        self.mapping = mapping

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...):
        if role != Qt.DisplayRole:
            return None
        elif orientation == Qt.Horizontal:
            return section
        return list(self.mapping.keys())[section]

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self.mapping)

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return 1

    def data(self, index: QModelIndex, role: int = ...) -> any:
        key_value = self.headerData(index.row(), Qt.Vertical, Qt.DisplayRole)
        if role == Qt.DisplayRole:
            return self.mapping.get(key_value, 0)
        if role == Qt.UserRole:
            return key_value
        if role == Qt.TextAlignmentRole:
            return int(Qt.AlignLeft | Qt.AlignVCenter)
        return None

    def flags(self, index: QModelIndex):
        if not index.isValid():
            return None
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable


class MappingView(QTableView):
    def __init__(self):
        QTableView.__init__(self, parent=None)
        self.horizontalHeader().setHidden(True)
        self.horizontalHeader().setProperty('language', 'zh')
        self.setSelectionMode(QTableView.SingleSelection)
        self.setSelectionBehavior(QTableView.SelectRows)
        self.set_corner(' 序号')

    def set_corner(self, text: str):
        # noinspection PyTypeChecker
        corner_button: QAbstractButton = self.findChild(QAbstractButton)
        corner_button.setText(text)
        corner_button.setObjectName('Corner')
        corner_button.setProperty('language', 'zh')
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


class ParamRCombo(QComboBox, ParamWidget):
    def __init__(self, name: str, default: int, mapping: dict[int, str], **kwargs):
        QComboBox.__init__(self, parent=None)
        ParamWidget.__init__(self, name, default, **kwargs)
        self.mapping = mapping
        self.init_mapping()

    def init_mapping(self):
        model = MappingModel(self.mapping)
        view = MappingView()
        self.setModel(model)
        self.setView(view)

    def install(self, param: int = None):
        if param is not None:
            return self.setCurrentIndex(list(self.mapping.keys()).index(param))
        return self.setCurrentIndex(0)

    def data(self) -> int:
        return list(self.mapping.keys())[self.currentIndex()]

    def explain(self, param: int) -> str:
        try:
            return self.mapping.get(param).replace('\u3000', '')
        except:
            print(self.name, self.mapping, param)

    def new(self):
        return self.__class__(self.name, self.default, self.mapping, **self.kwargs)
