#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import qdarktheme
from PySide6.QtWidgets import QApplication
from interface.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    style_sheet = qdarktheme.load_stylesheet('dark', 'sharp')
    style_sheet = style_sheet.replace('* {', '* {\n    font: "Inziu Iosevka SC";')
    app.setStyleSheet(style_sheet)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
