#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import qdarktheme
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QFileDialog

from structure import Rom, RobotRAF, PilotBIN, SnmsgBIN, SndataBIN, EnlistBIN, AiunpBIN, ScriptBIN, PrmgrpBIN
from .resource import *
from .robot_frame import RobotFrame


# noinspection PyTypeChecker
class MainWindow(QMainWindow):
    folder: str = ''

    def __init__(self, parent=None, flags=QtCore.Qt.MaximizeUsingFullscreenGeometryHint):
        super(MainWindow, self).__init__(parent, flags)

        self.robot = RobotRAF()
        self.pilot = PilotBIN()
        self.snmsg = SnmsgBIN()
        self.sndata = SndataBIN()
        self.enlist = EnlistBIN()
        self.aiunp = AiunpBIN()
        self.script = ScriptBIN()
        self.prmgrp = PrmgrpBIN()

        self.init_file_menu()
        self.init_edit_menu()
        self.init_option_menu()

        self.setWindowTitle('超级机器人大战α 静态修改器')
        self.setWindowIcon(QIcon(':image/icon.png'))
        self.check_enable()

    def init_file_menu(self):
        file_menu = QMenu('文件', self)

        robot = self.create_action('UNCOMPRESS_ROBOT.RAF', self.load_file('UNCOMPRESS_ROBOT.RAF', self.robot))
        pilot = self.create_action('PILOT.BIN', self.load_file('PILOT.BIN', self.pilot))
        snmsg = self.create_action('SNMSG.BIN', self.load_file('SNMSG.BIN', self.snmsg))
        sndata = self.create_action('SNDATA.BIN', self.load_file('SNDATA.BIN', self.sndata))
        enlist = self.create_action('ENLIST.BIN', self.load_file('ENLIST.BIN', self.enlist))
        aiunp = self.create_action('AIUNP.BIN', self.load_file('AIUNP.BIN', self.aiunp))
        script = self.create_action('SCRIPT.BIN', self.load_file('SCRIPT.BIN', self.script))
        prmgrp = self.create_action('PRM_GRP.BIN', self.load_file('PRM_GRP.BIN', self.prmgrp))
        file_menu.addActions([robot, pilot, snmsg, sndata, enlist, aiunp, script, prmgrp])

        save_action = self.create_action('保存', self.save_file)
        file_menu.addSeparator()
        file_menu.addAction(save_action)

        quit_action = self.create_action('退出', self.close)
        file_menu.addSeparator()
        file_menu.addAction(quit_action)

        self.menuBar().addMenu(file_menu)

    def init_edit_menu(self):
        edit_menu = QMenu('编辑', self)

        unit = self.create_action('机体', self.edit_unit)
        edit_menu.addActions([unit, ])

        self.menuBar().addMenu(edit_menu)

    def init_option_menu(self):
        option_menu = QMenu('选项', self)

        style_menu = QMenu('选择颜色', self)
        light_action = self.create_action('浅色', self.charge_style)
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

    def save_file(self):
        pass

    # noinspection PyUnresolvedReferences
    def check_enable(self):
        save = any([self.robot, self.pilot, self.snmsg, self.sndata, self.enlist, self.script, self.prmgrp])
        self.findChild(QAction, '保存').setEnabled(save)
        robot = bool(self.robot)
        self.findChild(QAction, '机体').setEnabled(robot)

    def edit_unit(self):
        robot_frame = RobotFrame(robots=self.robot.robots())
        robot_frame.set_rom(self.robot)
        self.setCentralWidget(robot_frame)

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
            'QAbstractSpinBox::up-button, QAbstractSpinBox::down-button {width: 6px; padding: 3px 1px 3px -1px;}'
        ]
        for expand in sheet_expand:
            style_sheet += expand
        print(style_sheet)
        QApplication.instance().setStyleSheet(style_sheet)
