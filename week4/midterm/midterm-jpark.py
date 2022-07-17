#!/usr/bin/env python3

# Author: George Maysack-Schlueter
# Description: This is a script for week 4 of python scripting class. This is for the midterm project " A python in jurrasic park" section. 

from itertools import count


print("George Maysack-Schlueter")

# setting up password database dictionary as per step 2 
password_database = {"Username":"dnedry","Password":"please"}

# setting up command database dictionary as per step 3
command_database = {"reboot":"OK. I will reboot all park systems.","shutdown":"OK. I will shut down all park systems.","done":"I hate all this hacker stuff."}

testing = True
# creating our white rabbit object and our counter object, and setting them to 0 as per step 4.
# Used to break out of the while loop
white_rabbit_object = 0
# used to count the number of failed authentication attempts
counter = 0

while testing:
    white_rabbit_object == 0
    counter < 3
    input_user = input("Username: ")
    input_password = input("Password: ")
    if input_user == password_database["Username"] and input_password == password_database["Password"]:
        white_rabbit_object += 1
        print("Hi, Dennis. You're still the best hacker in Jurrassic Park.")
        command_input = input(f"Please enter a command {command_database.keys()}--> ".replace('dict_keys',''))
        

        break
    else:
        counter += 1
    if counter == 3:
        # Mini for loop to print the line 25 times to a different line each time. 
        for i in range(25):
            print("You didn't say the magic word!") 




