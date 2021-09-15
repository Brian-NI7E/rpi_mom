#! /usr/bin/env python3

import os
import subprocess

startDir = os.getcwd()
os.chdir('/home/bigboy/py')

launch = subprocess.Popen(['python3', 'stats.py'])

os.chdir(startDir)
