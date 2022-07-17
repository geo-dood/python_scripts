#!/usr/bin/env python3

# Author: George Maysack-Schlueter
# Description: This is a script for week 4 of python scripting class. This is for the midterm script "Slicing" We will be slicing up a file, and then joining it back together. 

print("George Maysack-Schlueter")
print("")

#opening file in this method so we can reference it a few times in a row easily. 
sliceFile = open("/home/student/Documents/scripts-geo-dood/week4/midterm/slicing-file.txt", "r")
# Step A - 3rd word from end of file
thirdFromEnd = sliceFile.read()[126:133:1]
sliceFile.seek(0,0)
# Step B - 3rd through 5th word in file
thirdThroughFifth = sliceFile.read()[16:29:1]
sliceFile.seek(0,0)
# Step C - 10th word from end of file, and every other, until 3 words total
tenthFromEndPlusTwo = sliceFile.readlines()[17:12:-2]
sliceFile.seek(0,0)
# Step D - 11th through 13th Words from the file
elevenThroughThirteen = sliceFile.read()[57:72:1]
sliceFile.seek(0,0)
# Step E - 19th through 21st words from the end of the file
nineTeenThroughTwentyOneFromEnd = sliceFile.readlines()[8:5:-1]
sliceFile.seek(0,0)
# formatting the full quote. Replace got a little messy, but got it organized for readability. 
quote = f"{thirdFromEnd} {thirdThroughFifth} {tenthFromEndPlusTwo} {elevenThroughThirteen}, {nineTeenThroughTwentyOneFromEnd}" \
                          .replace("\n"," ").replace("\\n"," ").replace("['","").replace("', '","").replace(" ']","")
# printing out formatted quote
print(quote)
# closing the file
sliceFile.close()