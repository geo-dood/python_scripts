#!/usr/bin/env python3
# importing subprocess module so we can use it
import subprocess

# Author: George Maysack-Schlueter
# Description: This is a script for week 5 of python scripting class. This particular script is to practice concepts we learned regarding subprocesses

# creating object called myProc that will run 'ps -axco command' and pipe the results to stdout - this will generate a list of processes with some 'Filters'
myProc = subprocess.run(['ps', '-axco', 'command'], stdout=subprocess.PIPE)
# creating object named myProcString which will take the final piped value from myProc, and turn it into a useable string
myProcString = myProc.stdout.decode()
# Creating an object name myProclist which will take the output (string) from myProcString, and will remove the newline characters, and the first line (header)
myProcList = myProcString.split('\n')[1:]

# for loop to loop over each line (process), and print it as well, stops once there is no more text/lines
for process in myProcList:
    if "" in process:
        print(process)
# printing the length of the list of proceses minus the header - this is the amount of processes returned from our command
print(len(myProcList))
