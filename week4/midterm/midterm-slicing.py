#!/usr/bin/env python3

# Author: George Maysack-Schlueter
# Description: This is a script for week 4 of python scripting class. This is for the midterm script "Slicing"

print("George Maysack-Schlueter")
print("")

sliceFile = open("/home/student/Documents/scripts-geo-dood/week4/midterm/slicing-file.txt", "r")
thirdFromEnd = sliceFile.read()[126:133:1]
sliceFile.seek(0,0)
thirdThroughFifth = sliceFile.read()[16:29:1]
sliceFile.seek(0,0)
tenthFromEndPlusTwo = sliceFile.readlines()[17:12:-2]
sliceFile.seek(0,0)
elevenThroughThirteen = sliceFile.read()[57:72:1]
sliceFile.seek(0,0)
nineTeenThroughTwentyOneFromEnd = sliceFile.readlines()[8:5:-1]
sliceFile.seek(0,0)
rawquote = f"{thirdFromEnd} {thirdThroughFifth} {tenthFromEndPlusTwo} {elevenThroughThirteen} {nineTeenThroughTwentyOneFromEnd}".replace("\n"," ").replace("\\n"," ").replace(" ['"," ")
print(rawquote)
sliceFile.close()