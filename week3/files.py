#!/usr/bin/env python3

#Author: George Maysack-Schlueter
# Description: This is a script that will be applying concepts from week 3 of python scripting. This is for the "File Data Interactions" Lab

# Creating variable etcPass that will open the /etc/passwd file w read only access - choosing assignment method since we will be refrencing the file the same way for the first two steps
etcPass = open("/etc/passwd", "r")

# Reading /etc/passwd as a single string, then printing the length of that string in characters. 
etcPassStr = etcPass.read()
print(len(etcPassStr))
print("^ Here, the len() function is counting the amount of unicode characters in the /etc/passwd file when read as a single string")
print("***Use this read function when you want to view your file as a single string, or to view the total amount of characters in the file***")
print()

# Navigating back to start of /etc/passwd file, then using readlines to read /etc/passwd as a list, which stores each line as a string in said list.
etcPass.seek(0,0)
etcPassList = etcPass.readlines()
print(len(etcPassList))
print("^ Here, the len() function is counting the amount of items (strings) in the list version of our /etc/passwd file. This is also the amount of lines in the file.")
print("***Use this read function when you want to read each line as a seperate item in a list - can be used in for loops***")
print()

# Closing /etc/passwd file since we will be using the  "with open" method for step 3
etcPass.close() 

# Utilizing "with open" method so we can use a loop to save the contents line by line to our variable
count = 0
with open("/etc/passwd", "r") as etcPassLines:
    line = etcPassLines.read(10)
    while line:
        count += 1
        line = etcPassLines.readline()
        