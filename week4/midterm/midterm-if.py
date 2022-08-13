#!/usr/bin/env python3

# Author: George Maysack-Schlueter Description: This is a script for week 4 of python scripting class. This is the
# first of three scripts for the Midterm. This script is for the "Midterm-if [Question]"

# Per step 2, I am printing out my first and last name to the screen. 
print("Name: George Maysack-Schlueter")
print("")
# Setting up variable to keep track of line number sum, one to actually move the for loop forward, and a list of
# strings of the keywords we are searching for.
Total = 0
count = 0
words = ["gmeach18@ed.gov", "248.253.63.149", "Whiteland", "80.222.19.190", "Kayley", "dcassyqw@microsoft.com"]
# Opening our file in read only mode as midtermif
with open("/home/student/Documents/scripts-geo-dood/week4/midterm/Midterm-if.txt", "r") as midtermif:
    # for each line in midtermif, we are adding 1 to our count, which will keep track of the line number
    for line in midtermif:
        count += 1
        # for our words in our list, if they are found in the current line, the count number is added to our Total,
        # otherwise, we add nothing to the total. we subtract 1 from the count, because our text editors start on
        # line 1, but we start on 0.
        for word in words:
            if word in line:
                Total += count - 1
            else:
                var = Total + 0
# ensuring we close our midtermif file
midtermif.close()
# Printing our total to the screen, which is the sum of the line numbers we found our keywords on
print(f"The total is: {Total}")
