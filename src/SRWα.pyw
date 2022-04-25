#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import qdarktheme
from PySide6.QtWidgets import QApplication
from interface.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    style_sheet = qdarktheme.load_stylesheet('dark', 'sharp')
    style_sheet = '''* {
    font-family: 'Segoe UI', 'Microsoft Yahei UI', monospace;
    font-size: 12pt;
    font-weight: 500;
}''' + style_sheet
    app.setStyleSheet(style_sheet)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
