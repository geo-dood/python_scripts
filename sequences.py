#!/usr/bin/env python3

# Author: George Maysack-Schlueter
# Description: Python script to apply some concepts learned in week 2, specifically regarding different Data types,
# string slicing, and for loops


# Variable Library - Sourced from step 1 in the lab
varString = "Here is a nice string to slice"
varList = ["Here", "is", "a", "nice", "list", "to", "slice"]

# Using slicing on varString to recreate output from step 2
print(varString[3::1])
print(varString[0:3:1])
print(varString[3:12:1])
print(varString[::2])
print(varString[::-1])

# Using slicing on varList to recreate output from step 3
print(varList[::-1])
print(varList[2::-1])
print(varList[2:4:1])
print(varList[0::3])
print(varList[1::1])

# For loop to print each element of varString one line at a time (step 4)
for element in varString:
    print(element)

# For loop to print out each element of varList one line at a time (step 5)
for element in varList:
    print(element)
