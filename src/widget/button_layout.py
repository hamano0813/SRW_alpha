#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QPushButton, QVBoxLayout


class ButtonLayout(QVBoxLayout):
    def __init__(self, frame, parent=None):
        super(ButtonLayout, self).__init__(parent)
        parse_button = QPushButton('刷新')
        build_button = QPushButton('写入')
        parse_button.clicked.connect(frame.parse)
        build_button.clicked.connect(frame.build)
        parse_button.setFixedSize(135, 40)
        build_button.setFixedSize(135, 40)
        self.addWidget(parse_button)
        self.addWidget(build_button)
