#!/usr/bin/env python3
# Author: George Maysack-Schlueter
# Description: This is a script that will be applying concepts from week 3 of python scripting. This is for the
# "File Data Interactions" Lab

# Creating variable etcPass that will open the /etc/passwd file w read only access - choosing assignment method
# since we will be refrencing the file the same way for the first two steps
etcPass = open("/etc/passwd", "r")

# Reading /etc/passwd as a single string, then printing the length of that string in characters. 
etcPassStr = etcPass.read()
print(len(etcPassStr))
print(
    "^ Here, the len() function is counting the amount of characters in the /etc/passwd file when read as a single "
    "string")
print(
    "***Use this when you want to view your file as a single string, or to view the total amount of characters in the "
    "file***")
print()
# Navigating back to start of /etc/passwd file, then using readlines to read /etc/passwd as a list, which stores
# each line as a string in said list.
etcPass.seek(0, 0)
etcPassList = etcPass.readlines()
print(len(etcPassList))
print(
    "^ Here, the len() function is counting the amount of items (strings) in the list version of our /etc/passwd "
    "file. This is also the amount of lines in the file.")
print(
    "***Use this when you want to end up with a separated list of items. Each line will generate an item in the "
    "created list. \n Can be converted to string format - can be used in for loops, as well***")
print()
# Closing /etc/passwd file
etcPass.close()

# Using a Function & a Loop to access and save /etc/passwd contents line by line, and printing number of characters. 
"""Using with open method to create while loop, and printing the final value of our "lineInfo" variable - which is 
the number of characters in the file. In this instance, we did not need to use the len() function, because the final 
value of our tell() function is indicative of the number of characters. So we just ended up printing the value of 
that tell function, once our while loop was completed. count = 0 """
count = 0

with open("/etc/passwd", "r") as etcPassLine:
    line = etcPassLine.read(10)
    while line:
        lineInfo = etcPassLine.tell()
        count += 1
        line = etcPassLine.readline()
    print(lineInfo)
print(
    "^ Here, the tell () function is tracking the position of our pointer in the /etc/passwd file - our while loop "
    "continues until the final character is hit, at which \n point, we simply print the final value of our position "
    "in the file")
print(
    "***Useful when we want to process one line at a time. With our example above, the entire contents of /etc/passwd "
    "\n were stored into a list in one step. \n in this example, our while look stepped through one line at a time "
    "until \n it reached the end of the file - similar output, but different use cases***")
