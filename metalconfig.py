# -*- coding: utf-8 -*-
import os
_basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True

# a buncha lines
with open("inferno.txt", "r") as f:
    INFERNO = [i.strip() for i in f.readlines()]

# epithet: that's what I know
with open("epithets.txt", "r") as f:
    EPITHETS = [i.strip() for i in f.readlines()]

# default brutality. Brutal.
SONG = {
    "stanzas": 5,
    "lines": 3
}

del os
