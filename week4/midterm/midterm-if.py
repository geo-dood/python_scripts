#!/usr/bin/env python3

# Author: George Maysack-Schlueter
# Description: This is a script for week 4 of python scripting class. This is the first of three scripts for the Midterm. This script is for the "Midterm-if [Question]"

# Per step 2, I am printing out my first and last name to the screen. 
print("Name: George Maysack-Schlueter")

Total = 0
with open("Midterm-if.txt", "rb") as midtermif:
    line = midtermif.read(10)
    while line:
        lineInfo = f"{count:03d}) [Length:{len(line):03d}] [Index: {midtermif.tell():04d}] {line}"
        print(lineInfo.strip())
        count += 1
        line = midtermif.readline()
