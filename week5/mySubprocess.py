#!/usr/bin/env python3

import subprocess

# Author: George Maysack-Schlueter
# Description: This is a script for week 5 of python scripting class. This particular script is to practice concepts we learned regarding subprocesses

myProc = subprocess.run(['ps', '-axco', 'command'],stdout=subprocess.PIPE)
myProcString = myProc.stdout.decode().split('\n')

print(myProcString)
