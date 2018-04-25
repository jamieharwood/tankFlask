#!/usr/bin/pithon3

import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/home/pi/code/flask/")

from init import app as application
application.secret_key = 'qwertyuiop'
