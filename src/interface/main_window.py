#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import qdarktheme
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QFileDialog

from structure import Rom, RobotRAF, PilotBIN, SnmsgBIN, SndataBIN, EnlistBIN, AiunpBIN, ScriptBIN, PrmgrpBIN
from widget import BackgroundFrame
from . import RobotFrame, PilotFrame, SnmsgFrame, PrmgrpFrame
from .resource import *


class MainWindow(QMainWindow):
    folder: str = ''

    def __init__(self, parent=None, flags=QtCore.Qt.WindowCloseButtonHint):
        super(MainWindow, self).__init__(parent, flags)

        self.roms = {
            'UNCOMPRESS_ROBOT.RAF': RobotRAF(),
            'PILOT.BIN': PilotBIN(),
            'SNMSG.BIN': SnmsgBIN(),
            'SNDATA.BIN': SndataBIN(),
            'ENLIST.BIN': EnlistBIN(),
            'AINUP.BIN': AiunpBIN(),
            'SCRIPT.BIN': ScriptBIN(),
            'PRM_GRP.BIN': PrmgrpBIN(),
        }
        self.frames = {
            '機体': (RobotFrame, ('UNCOMPRESS_ROBOT.RAF',),
                   {'robots': self.roms['UNCOMPRESS_ROBOT.RAF'].robots}),
            'パイロット': (PilotFrame, ('PILOT.BIN',),),
            'メッセージ': (SnmsgFrame, ('SNMSG.BIN',),),
            'その他': (PrmgrpFrame, ('PRM_GRP.BIN',),),
        }

        self.init_file_menu()
        self.init_edit_menu()
        self.init_option_menu()

        self.setWindowTitle('超级机器人大战α 静态修改器')
        self.setWindowIcon(QIcon(':image/icon.png'))
        self.setMinimumSize(1440, 870)
        self.check_enable()

    def init_file_menu(self):
        file_menu = QMenu('文件', self)
        for name, rom in self.roms.items():
            action = self.create_action(name, self.load_file(name, rom))
            file_menu.addAction(action)

        save_action = self.create_action('保存', self.save_file)
        file_menu.addSeparator()
        file_menu.addAction(save_action)
        quit_action = self.create_action('退出', self.close)
        file_menu.addSeparator()
        file_menu.addAction(quit_action)
        self.menuBar().addMenu(file_menu)

    def init_edit_menu(self):
        edit_menu = QMenu('編輯', self)
        edit_list = []
        for frame_name, frame_setting in self.frames.items():
            action = self.create_action(frame_name, self.open_frame(*frame_setting))
            edit_list.append(action)
        edit_menu.addActions(edit_list)
        self.menuBar().addMenu(edit_menu)

        tool_bar = self.addToolBar('')
        tool_bar.addActions(edit_list)
        tool_bar.setMovable(False)

    def init_option_menu(self):
        option_menu = QMenu('選項', self)

        style_menu = QMenu('界面主題', self)
        light_action = self.create_action('淺色', self.charge_style)
        dark_action = self.create_action('深色', self.charge_style)
        style_menu.addActions([light_action, dark_action])

        option_menu.addMenu(style_menu)
        self.menuBar().addMenu(option_menu)
        dark_action.trigger()

    def create_action(self, name: str, slot: callable = None) -> QAction:
        action = QAction(name, self)
        action.setObjectName(name)
        if slot:
            action.triggered.connect(slot)
        return action

    def load_file(self, file_name: str, rom: Rom) -> callable:
        def wrapper():
            folder = self.folder if self.folder else sys.path[0]
            path = QFileDialog().getOpenFileName(None, file_name, folder, file_name,
                                                 options=QFileDialog.DontResolveSymlinks)[0]
            if path:
                rom.load(path)
                self.folder = os.path.split(path)[0]
            self.check_enable()

        return wrapper

    def open_frame(self, frame_class: type(BackgroundFrame), roms: tuple[str], parameter: dict[str, callable] = None):
        def wrapper():
            if parameter:
                kwargs = {k: v() for k, v in parameter.items()}
            else:
                kwargs = dict()
            if not isinstance(self.centralWidget(), frame_class):
                frame = frame_class(**kwargs)
                frame.set_roms([self.roms[name] for name in roms])
                self.setCentralWidget(frame)
            else:
                # noinspection PyUnresolvedReferences
                self.centralWidget().parse()

        return wrapper

    def save_file(self):
        pass

    # noinspection PyUnresolvedReferences
    def check_enable(self):
        self.findChild(QAction, '保存').setEnabled(any(map(bool, self.roms.values())))
        self.findChild(QAction, '機体').setEnabled(bool(self.roms.get('UNCOMPRESS_ROBOT.RAF')))
        self.findChild(QAction, 'パイロット').setEnabled(bool(self.roms.get('PILOT.BIN')))
        self.findChild(QAction, 'メッセージ').setEnabled(bool(self.roms.get('SNMSG.BIN')))
        self.findChild(QAction, 'その他').setEnabled(bool(self.roms.get('PRM_GRP.BIN')))

    def charge_style(self):
        if self.sender().objectName() == '深色':
            style_sheet = qdarktheme.load_stylesheet('dark', 'sharp')
        else:
            style_sheet = qdarktheme.load_stylesheet('light', 'sharp')
        sheet_change = {
            'QHeaderView::down-arrow': 'QHeaderView[orientation="horizontal"]::down-arrow',
            'QHeaderView::up-arrow': 'QHeaderView[orientation="horizontal"]::up-arrow',
            'margin: -2px -6px -6px -6px;': 'margin: -2px -3px -6px -6px;position:right;',
            '* {': '* {font: 10pt "Yu Gothic UI Semibold";',
            'rgba(255.000, 255.000, 255.000, 0.000)': '#ffffff',
        }
        for old, new in sheet_change.items():
            style_sheet = style_sheet.replace(old, new)
        sheet_expand = [
            'QComboBox QAbstractItemView::item {height: 25px;}',
            'QAbstractItemView RadioCombo {padding: -3px 0px 0px -2px;}',
            'QAbstractItemView ValueSpin {padding-top: -2px; padding-right: -1px; padding-left: 0px;}',
            'QAbstractItemView MappingSpin, QAbstractItemView TextLine {padding-top: -2px; padding-right: -1px;}',
            'RadioCombo, CheckCombo {padding: -2px 0px 0px -2px;}',
            'QAbstractSpinBox::up-button, QAbstractSpinBox::down-button {width: 6px; padding: 3px 1px 3px -1px;}',
            'RangeCombo QAbstractItemView::item {height: 105px;}',
            'QHeaderView::section {padding: -1px -2px 0 3px;}',
            'CheckCombo QLineEdit {padding: 0px 5px 0px 5px;}',
            'QAbstractItemView TextMulti {padding-top: -2px;}',
            '#MessageList::item {padding-top: 3px;padding-left: 3px;}',
            '#Corner::section {padding-top: 5px;padding-left: 5px;}',
        ]
        for expand in sheet_expand:
            style_sheet += expand
        # print(style_sheet)
        QApplication.instance().setStyleSheet(style_sheet)
