# -*- coding: utf-8 -*-
import os
import sys
import json
basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True

# a buncha lines
with open("inferno.txt", "r") as f:
    INFERNO = [i.strip() for i in f.readlines()]

# epithet: that's what I know
with open("epithets.txt", "r") as f:
    EPITHETS = [i.strip() for i in f.readlines()]

# got to get you some email
try:
    with open(os.path.join(basedir, "mail_config.json"), "rb") as f:
        mail_config = json.loads(f.read())
        MAIL_SERVER = mail_config["MAIL_SERVER"]
        MAIL_PORT = mail_config["MAIL_PORT"]
        MAIL_USE_SSL = mail_config["MAIL_USE_SSL"]
        MAIL_USERNAME = mail_config["MAIL_USERNAME"]
        MAIL_PASSWORD = mail_config["MAIL_PASSWORD"]
except Exception as error:
    print(error)
    print("did you set up email?")
    sys.exit(1)

# default brutality. Brutal.
SONG = {
    "stanzas": 5,
    "lines": 3
}

del os
