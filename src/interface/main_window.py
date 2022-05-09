#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import qdarktheme
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QFileDialog

from structure import Rom, RobotRAF, PilotBIN, SnmsgBIN, SndataBIN, EnlistBIN, AiunpBIN, ScriptBIN, PrmgrpBIN
from .resource import *
from . import RobotFrame, PilotFrame
from widget import BackgroundFrame


# noinspection PyTypeChecker
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
            '机体': (RobotFrame, 'UNCOMPRESS_ROBOT.RAF',
                   {'robots': self.roms['UNCOMPRESS_ROBOT.RAF'].robots}),
            '机师': (PilotFrame, 'PILOT.BIN',),
        }

        self.init_file_menu()
        self.init_edit_menu()
        self.init_option_menu()

        self.setWindowTitle('超级机器人大战α 静态修改器')
        self.setWindowIcon(QIcon(':image/icon.png'))
        self.setFixedSize(1440, 860)
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
        edit_menu = QMenu('编辑', self)
        edit_list = []
        for name, frame_setting in self.frames.items():
            action = self.create_action(name, self.open_frame(*frame_setting))
            edit_list.append(action)
        edit_menu.addActions(edit_list)
        self.menuBar().addMenu(edit_menu)

        tool_bar = self.addToolBar('')
        tool_bar.addActions(edit_list)
        tool_bar.setMovable(False)

    def init_option_menu(self):
        option_menu = QMenu('选项', self)

        style_menu = QMenu('界面主题', self)
        light_action = self.create_action('浅色', self.charge_style)
        dark_action = self.create_action('深色', self.charge_style)
        style_menu.addActions([light_action, dark_action])

        option_menu.addMenu(style_menu)
        self.menuBar().addMenu(option_menu)
        light_action.trigger()

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

    def open_frame(self, frame_class: type(BackgroundFrame), rom_name: str, parameter: dict[str, callable] = None):
        def wrapper():
            if parameter:
                kwargs = {k: v() for k, v in parameter.items()}
            else:
                kwargs = dict()
            frame = frame_class(**kwargs)
            frame.set_rom(self.roms[rom_name])
            self.setCentralWidget(frame)

        return wrapper

    def save_file(self):
        pass

    # noinspection PyUnresolvedReferences
    def check_enable(self):
        self.findChild(QAction, '保存').setEnabled(any([self.roms.values()]))
        self.findChild(QAction, '机体').setEnabled(bool(self.roms.get('UNCOMPRESS_ROBOT.RAF')))
        self.findChild(QAction, '机师').setEnabled(bool(self.roms.get('PILOT.BIN')))

    def charge_style(self):
        if self.sender().objectName() == '深色':
            style_sheet = qdarktheme.load_stylesheet('dark', 'sharp')
        else:
            style_sheet = qdarktheme.load_stylesheet('light', 'sharp')
        sheet_change = {
            'QHeaderView::down-arrow': 'QHeaderView[orientation="horizontal"]::down-arrow',
            'QHeaderView::up-arrow': 'QHeaderView[orientation="horizontal"]::up-arrow',
            'margin: -2px -6px -6px -6px;': 'margin: -2px -1px -6px -6px;position:right;',
            '* {': '* {font: 10pt;',
        }
        for old, new in sheet_change.items():
            style_sheet = style_sheet.replace(old, new)
        sheet_expand = [
            'QComboBox QAbstractItemView::item {height: 24px;}',
            'QAbstractSpinBox::up-button, QAbstractSpinBox::down-button {width: 6px; padding: 3px 1px 3px -1px;}',
            'RangeCombo QAbstractItemView::item {height: 105px;}',
        ]
        for expand in sheet_expand:
            style_sheet += expand
        # print(style_sheet)
        QApplication.instance().setStyleSheet(style_sheet)
