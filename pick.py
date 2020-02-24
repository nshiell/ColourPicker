#!/usr/bin/env python3

# This file is just here to make running the app easier
# so it can be run as a python script - without needing to install it
# you need to make sure all dependencies are installed manually though
# run with ./pick.py


import sys
from pick.__main__ import Main

m = Main()
m.app.run(sys.argv)
