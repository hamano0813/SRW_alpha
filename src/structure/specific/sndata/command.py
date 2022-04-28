#!/usr/bin/env python
# -*- coding: utf-8 -*-

from structure.generic import Sequence

COMMAND_STRUCTURE = {

}


class Command(Sequence):
    def __init__(self, structures, offset, length, count):
        super(Command, self).__init__(structures, offset, length, count)
