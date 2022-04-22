#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from PySide6.QtWidgets import QMainWindow, QMenu, QFileDialog
from PySide6.QtGui import QIcon, QAction
from .resource import *
from structure import ROM, ROBOT, PILOT, SNMSG, SNDATA, ENLIST, AIUNP, SCRIPT, PRMGRP


# noinspection PyTypeChecker
class MainWindow(QMainWindow):
    folder: str = ''

    def __init__(self, parent=None, flags=QtCore.Qt.MaximizeUsingFullscreenGeometryHint):
        super(MainWindow, self).__init__(parent, flags)

        self.robot = ROBOT()
        self.pilot = PILOT()
        self.snmsg = SNMSG()
        self.sndata = SNDATA()
        self.enlist = ENLIST()
        self.aiunp = AIUNP()
        self.script = SCRIPT()
        self.prmgrp = PRMGRP()

        self.setWindowTitle('超级机器人大战α 静态修改器')
        self.setWindowIcon(QIcon(':image/icon.png'))

        robot = self.create_action('UNCOMPRESS_ROBOT.RAF...', self.load_file('UNCOMPRESS_ROBOT.RAF', self.robot))
        pilot = self.create_action('PILOT.BIN...', self.load_file('PILOT.BIN', self.pilot))
        snmsg = self.create_action('SNMSG.BIN...', self.load_file('SNMSG.BIN', self.snmsg))
        sndata = self.create_action('SNDATA.BIN...', self.load_file('SNDATA.BIN', self.sndata))
        enlist = self.create_action('ENLIST.BIN...', self.load_file('ENLIST.BIN', self.enlist))
        aiunp = self.create_action('AIUNP.BIN...', self.load_file('AIUNP.BIN', self.aiunp))
        script = self.create_action('SCRIPT.BIN...', self.load_file('SCRIPT.BIN', self.script))
        prmgrp = self.create_action('PRM_GRP.BIN...', self.load_file('PRM_GRP.BIN', self.prmgrp))

        rom_menu = QMenu('文件', self)
        rom_menu.addActions([robot, pilot, snmsg, sndata, enlist, aiunp, script, prmgrp])
        self.save_action = self.create_action('保存', self.save_file)
        self.save_action.setEnabled(False)
        rom_menu.addSeparator()
        rom_menu.addAction(self.save_action)
        quit_action = self.create_action('退出', self.close)
        rom_menu.addSeparator()
        rom_menu.addAction(quit_action)
        self.menuBar().addMenu(rom_menu)

    def create_action(self, name: str, slot: callable = None) -> QAction:
        action = QAction(name, self)
        action.setObjectName(name)
        if slot:
            action.triggered.connect(slot)
        return action

    def load_file(self, file_name: str, structure: ROM) -> callable:
        def load():
            folder = self.folder if self.folder else sys.path[0]
            path = QFileDialog().getOpenFileName(None, file_name, folder, file_name,
                                                 options=QFileDialog.DontResolveSymlinks)[0]
            if path:
                with open(path, 'rb') as f:
                    buffer = bytearray(f.read())
                structure.set_path(path)
                structure.set_buffer(buffer)
                self.folder = os.path.split(path)[0]
            self.check_enable()

        return load

    def save_file(self):
        pass

    def check_enable(self):
        if any([self.robot, self.pilot, self.snmsg, self.sndata, self.enlist, self.script, self.prmgrp]):
            self.save_action.setEnabled(True)
