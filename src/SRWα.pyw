#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import qdarktheme
from PySide6.QtWidgets import QApplication
from interface.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    stylesheet = qdarktheme.load_stylesheet('dark', 'sharp')
    stylesheet = stylesheet.replace('QHeaderView::down-arrow', 'QHeaderView[orientation="horizontal"]::down-arrow')
    stylesheet = stylesheet.replace('QHeaderView::up-arrow', 'QHeaderView[orientation="horizontal"]::up-arrow')
    stylesheet = stylesheet.replace('* {', '* {font: 12px;')
    app.setStyleSheet(stylesheet)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
