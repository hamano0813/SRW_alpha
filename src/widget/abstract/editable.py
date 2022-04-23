#!/usr/bin/env python
# -*- coding: utf-8 -*-


class EditableWidget:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.structure = kwargs.get('structure')

    def get_data(self):
        pass

    def set_data(self, data: any):
        pass

    def __repr__(self):
        return f'{self.name}'
