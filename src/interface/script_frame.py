#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Optional

from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout

from structure import ScriptBIN
from widget import *


class ScriptFrame(BackgroundFrame):
    def __init__(self, parent=None, **kwargs):
        super(ScriptFrame, self).__init__(parent, **kwargs)
        self.sndata_rom: Optional[ScriptBIN] = None

        self.init_ui()

    def init_ui(self):
        script = self.init_script_table()

        main_layout = QVBoxLayout()
        main_layout.addLayout(script)
        self.setLayout(main_layout)

    def init_script_table(self):
        # noinspection PyTypeChecker
        self['脚本列表'] = ScriptCombo(self)
        self['脚本列表'].setFixedWidth(1420)
        layout = QHBoxLayout()
        layout.addWidget(self['脚本列表'])
        return layout
