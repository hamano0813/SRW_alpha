#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QComboBox

from widget.abstract_widget import SingleWidget


class RangeCombo(SingleWidget, QComboBox):
    MAP_RANGE = {
        0x00: ((2, 7), (3, 7), (3, 8), (4, 8), (5, 8), (5, 7)),
        0x01: ((1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6)),
        0x02: ((1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)),
        0x03: ((1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6)),
        0x04: ((2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6), (9, 6), (10, 6), (11, 6)),
        0x05: ((2, 5), (3, 5), (4, 5), (5, 5),
               (1, 6), (2, 6), (3, 6), (4, 6), (5, 6),
               (2, 7), (3, 7), (4, 7), (5, 7)),
        0x06: ((1, 5), (2, 5), (3, 5), (4, 5),
               (1, 6), (2, 6), (3, 6), (4, 6), (5, 6),
               (1, 7), (2, 7), (3, 7), (4, 7)),
        0x07: ((1, 5), (2, 5), (3, 5), (4, 5), (5, 5),
               (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6),
               (1, 7), (2, 7), (3, 7), (4, 7), (5, 7)),
        0x08: ((2, 5), (3, 5), (4, 5), (5, 5), (6, 5),
               (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6),
               (2, 7), (3, 7), (4, 7), (5, 7), (6, 7)),
        0x09: ((2, 5), (3, 5),
               (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6),
               (2, 7), (3, 7)),
        0x0A: ((1, 5), (2, 5), (3, 5), (4, 5),
               (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6),
               (1, 7), (2, 7), (3, 7), (4, 7)),
        0x0B: ((3, 4), (4, 4), (5, 4),
               (2, 5), (3, 5), (4, 5), (5, 5),
               (1, 6), (2, 6), (3, 6), (4, 6), (5, 6),
               (2, 7), (3, 7), (4, 7), (5, 7),
               (3, 8), (4, 8), (5, 8)),
        0x0C: ((3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5),
               (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6), (9, 6), (10, 6),
               (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7)),
        0x0D: ((1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5),
               (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6),
               (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7)),
        0x0E: ((1, 4), (2, 4), (3, 4),
               (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5),
               (1, 6), (2, 6), (3, 6),
               (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7),
               (1, 8), (2, 8), (3, 8)),
        0x0F: ((4, 4),
               (3, 5), (4, 5),
               (2, 6), (3, 6), (4, 6),
               (3, 7), (4, 7),
               (4, 8)),
        0x10: ((5, 2),
               (4, 3), (5, 3),
               (3, 4), (4, 4), (5, 4),
               (2, 5), (3, 5), (4, 5), (5, 5),
               (1, 6), (2, 6), (3, 6), (4, 6), (5, 6),
               (2, 7), (3, 7), (4, 7), (5, 7),
               (3, 8), (4, 8), (5, 8),
               (4, 9), (5, 9),
               (5, 10)),
        0x11: ((5, 3), (6, 3),
               (3, 4), (4, 4),
               (1, 5), (2, 5),
               (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6),
               (1, 7), (2, 7),
               (3, 8), (4, 8),
               (5, 9), (6, 9)),
        0x12: ((1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5),
               (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6),
               (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7)),
        0x13: ((3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2),
               (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3),
               (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4), (9, 4),
               (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5),
               (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6), (9, 6),
               (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (9, 7),
               (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (9, 8),
               (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9),
               (3, 10), (4, 10), (5, 10), (6, 10), (7, 10), (8, 10), (9, 10)),
        0x14: ((1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2),
               (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3),
               (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4),
               (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5),
               (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6), (9, 6),
               (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7),
               (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8),
               (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9),
               (1, 10), (2, 10), (3, 10), (4, 10), (5, 10), (6, 10), (7, 10)),
        0x15: ((1, 4), (2, 4), (3, 4),
               (1, 5), (2, 5), (3, 5), (4, 5),
               (1, 6), (2, 6), (3, 6), (4, 6), (5, 6),
               (1, 7), (2, 7), (3, 7), (4, 7),
               (1, 8), (2, 8), (3, 8)),
    }

    def __init__(self, parent, data_name, structure, **kwargs):
        SingleWidget.__init__(self, parent, data_name, structure, **kwargs)
        QComboBox.__init__(self, parent)
        self.setIconSize(QSize(150, 100))
        self.setMaxVisibleItems(5)
        self.init_range()

    def init_range(self):
        for key, rect_list in self.MAP_RANGE.items():
            img = self.create_img(rect_list)
            self.addItem(QIcon(img), f'[0x{key:02X}]', key)

    @staticmethod
    def create_img(rect_list: tuple[tuple[int, int]]):
        img = Image.new('RGBA', (131, 131), 0xA0804040)
        draw = ImageDraw.Draw(img)
        for line in range(14):
            draw.line([(0, line * 10), (130, line * 10)], fill="black", width=1)
            draw.line([(line * 10, 0), (line * 10, 130)], fill="black", width=1)
        draw.rectangle(((1, 61), (9, 69)), fill="gold")
        for rect in rect_list:
            draw.rectangle(((10 * rect[0] + 1, 10 * rect[1] + 1), (10 * rect[0] + 9, 10 * rect[1] + 9)), fill="red")
        return img.rotate(45, resample=Image.BICUBIC, expand=True).resize((150, 100)).toqpixmap()

    def install(self, data_set: dict[str, int | str], delegate: bool = False) -> bool:
        self.disconnect(self)
        self.data_set = data_set
        value = self.data_set.get(self.data_name, 0)
        self.setCurrentIndex(value)
        # noinspection PyUnresolvedReferences
        self.currentIndexChanged.connect(self.overwrite)
        return True

    def overwrite(self) -> bool:
        self.data_set[self.data_name] = self.currentIndex()
        return True
