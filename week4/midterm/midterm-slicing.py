#!/usr/bin/env python3

# Author: George Maysack-Schlueter
# Description: This is a script for week 4 of python scripting class. This is for the midterm script "Slicing"

print("George Maysack-Schlueter")
print("")

sliceFile = open("/home/student/Documents/scripts-geo-dood/week4/midterm/slicing-file.txt", "r")
thirdFromEnd = print(f"{sliceFile.read()}"[126:133:1])
sliceFile.seek(0,0)
thirdThroughFifth = print(f"{sliceFile.read()}"[16:29:1])
sliceFile.seek(0,0)
tenthFromEndPlusTwo = print(f"{sliceFile.readlines()[17:12:-2]}")
sliceFile.seek(0,0)
elevenThroughThirteen = print(f"{sliceFile.read()}"[57:72:1])
sliceFile.seek(0,0)
nineTeenThroughTwentyOneFromEnd = print(f"{sliceFile.readlines()[8:5:-1]}")
sliceFile.seek(0,0)
quote = print(f"Hello {thirdFromEnd}")
sliceFile.close()