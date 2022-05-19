#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from typing import Optional

import qdarktheme
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QFileDialog, QToolBar, QPushButton, QWidget

from structure import Rom, RobotRAF, PilotBIN, SnmsgBIN, SndataBIN, EnlistBIN, AiunpBIN, ScriptBIN, PrmgrpBIN
from widget import BackgroundFrame
from . import RobotFrame, PilotFrame, SnmsgFrame, ScenarioFrame, PrmgrpFrame
from .resource import *


class MainWindow(QMainWindow):
    folder: str = ''

    def __init__(self, parent=None, flags=QtCore.Qt.WindowCloseButtonHint):
        super(MainWindow, self).__init__(parent, flags)
        self.tool_bar: Optional[QToolBar] = None

        self.roms = {
            'UNCOMPRESS_ROBOT.RAF': RobotRAF(),
            'PILOT.BIN': PilotBIN(),
            'SNMSG.BIN': SnmsgBIN(),
            'SNDATA.BIN': SndataBIN(),
            'ENLIST.BIN': EnlistBIN(),
            'AIUNP.BIN': AiunpBIN(),
            'SCRIPT.BIN': ScriptBIN(),
            'PRM_GRP.BIN': PrmgrpBIN(),
        }
        self.frames = {
            '機体': (RobotFrame, ('UNCOMPRESS_ROBOT.RAF',),
                   {'robots': self.roms['UNCOMPRESS_ROBOT.RAF'].robots}),
            'パイロット': (PilotFrame, ('PILOT.BIN',),),
            'メッセージ': (SnmsgFrame, ('SNMSG.BIN',),),
            'シナリオ': (ScenarioFrame, ('SNDATA.BIN', 'ENLIST.BIN', 'AIUNP.BIN'),
                     {'robots': self.roms['UNCOMPRESS_ROBOT.RAF'].robots,
                      'pilots': self.roms['PILOT.BIN'].pilots,
                      'messages': self.roms['SNMSG.BIN'].messages},
                     ),
            'その他': (PrmgrpFrame, ('PRM_GRP.BIN',),),
        }

        self.init_tool_bar()
        self.init_file_menu()
        self.init_edit_menu()
        self.init_option_menu()
        self.init_menu_action()

        self.setWindowTitle('超级机器人大战α 静态修改器')
        self.setWindowIcon(QIcon(':image/icon.png'))
        self.setMinimumSize(1440, 870)
        self.test_load()
        self.check_enable()

    def init_tool_bar(self):
        self.tool_bar = self.addToolBar('')
        self.tool_bar.setMovable(False)
        parse_action = self.create_action('刷新')
        build_action = self.create_action('写入')
        parse_action.setEnabled(False)
        build_action.setEnabled(False)
        self.tool_bar.addActions([parse_action, build_action])
        self.tool_bar.addSeparator()

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

        self.tool_bar.addActions(edit_list)

    def init_option_menu(self):
        option_menu = QMenu('選項', self)

        style_menu = QMenu('主題', self)
        light_action = self.create_action('淺色', self.charge_style)
        dark_action = self.create_action('深色', self.charge_style)
        style_menu.addActions([light_action, dark_action])

        option_menu.addMenu(style_menu)
        self.menuBar().addMenu(option_menu)
        dark_action.trigger()

    def init_menu_action(self):
        corner_button = QPushButton('', self.menuBar())
        corner_button.setObjectName('ConnerButton')
        style = '''
        #ConnerButton,#ConnerButton:hover,#ConnerButton:pressed
        {padding-top:-32px;font:30pt;border:0;background:transparent;}
        '''
        corner_button.setStyleSheet(style)
        corner_button.clicked.connect(self.charge_toolbar)
        self.menuBar().setCornerWidget(corner_button)
        corner_button.click()

    def create_action(self, name: str, slot: callable = None, icon=None) -> QAction:
        action = QAction(name, self)
        action.setObjectName(name)
        if icon:
            action.setIcon(icon)
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
                frame = frame_class(self, **kwargs)
                frame.set_roms([self.roms[name] for name in roms])
                self.setCentralWidget(frame)

                self.findChild(QAction, '刷新').setEnabled(True)
                self.findChild(QAction, '刷新').triggered.connect(self.centralWidget().parse)
                self.findChild(QAction, '写入').setEnabled(True)
                self.findChild(QAction, '写入').triggered.connect(self.centralWidget().build)
            else:
                self.centralWidget().parse()

        return wrapper

    def centralWidget(self) -> QWidget | RobotFrame | PilotFrame | SnmsgFrame | ScenarioFrame | PrmgrpFrame:
        return super(MainWindow, self).centralWidget()

    def save_file(self):
        for rom in self.roms.values():
            rom.save()

    def check_enable(self):
        self.findChild(QAction, '保存').setEnabled(any(map(bool, self.roms.values())))
        self.findChild(QAction, '機体').setEnabled(bool(self.roms.get('UNCOMPRESS_ROBOT.RAF')))
        self.findChild(QAction, 'パイロット').setEnabled(bool(self.roms.get('PILOT.BIN')))
        self.findChild(QAction, 'メッセージ').setEnabled(bool(self.roms.get('SNMSG.BIN')))
        self.findChild(QAction, 'シナリオ').setEnabled(all(map(bool,
                                                           (self.roms.get('UNCOMPRESS_ROBOT.RAF'),
                                                            self.roms.get('PILOT.BIN'),
                                                            self.roms.get('SNMSG.BIN'),
                                                            self.roms.get('SNDATA.BIN'),
                                                            self.roms.get('ENLIST.BIN'),
                                                            self.roms.get('AIUNP.BIN'),
                                                            ))))
        self.findChild(QAction, 'その他').setEnabled(bool(self.roms.get('PRM_GRP.BIN')))

    def charge_toolbar(self):
        if self.sender().text() == '˯':
            self.sender().setText('˰')
            self.tool_bar.setVisible(True)
        else:
            self.sender().setText('˯')
            self.tool_bar.setVisible(False)

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
            '#ENLIST::section {padding: -1px -15px 0px 0px;}',
        ]
        for expand in sheet_expand:
            style_sheet += expand
        # print(style_sheet)
        QApplication.instance().setStyleSheet(style_sheet)

    def test_load(self):
        self.roms['UNCOMPRESS_ROBOT.RAF'].load(r'D:\Python\SRWα\resource\bin\UNCOMPRESS_ROBOT.RAF')
        self.roms['PILOT.BIN'].load(r'D:\Python\SRWα\resource\bin\PILOT.BIN')
        self.roms['SNMSG.BIN'].load(r'D:\Python\SRWα\resource\bin\SNMSG.BIN')
        self.roms['SNDATA.BIN'].load(r'D:\Python\SRWα\resource\bin\SNDATA.BIN')
        self.roms['ENLIST.BIN'].load(r'D:\Python\SRWα\resource\bin\ENLIST.BIN')
        self.roms['AIUNP.BIN'].load(r'D:\Python\SRWα\resource\bin\AIUNP.BIN')
        self.roms['SCRIPT.BIN'].load(r'D:\Python\SRWα\resource\bin\SCRIPT.BIN')
        self.roms['PRM_GRP.BIN'].load(r'D:\Python\SRWα\resource\bin\PRM_GRP.BIN')
