#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import qdarktheme
from PySide6.QtWidgets import QApplication
from editors.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarktheme.load_stylesheet('dark', 'sharp'))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
