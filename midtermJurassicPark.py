#!/usr/bin/env python3

# Author: George Maysack-Schlueter
# Description: This is a script for week 4 of python scripting class. This is for the midterm project "
# A python in jurrasic park" section.

print("George Maysack-Schlueter")
print("")
# setting up password database dictionary as per step 2 
password_database = {"Username": "dnedry", "Password": "please"}

# setting up command database dictionary as per step 3
command_database = {"reboot": "OK. I will reboot all park systems.",
                    "shutdown": "OK. I will shut down all park systems.", "done": "I hate all this hacker stuff."}

testing = True
# creating our white rabbit object and our counter object, and setting them to 0 as per step 4.
# Used to break out of the while loop
white_rabbit_object = 0
# used to count the number of failed authentication attempts
counter = 0

# setting parameter as "testing" just for organizational purposes, and setting initial check for white rabbit
# counter being less than 3
while testing:
    var = white_rabbit_object == 0
    # noinspection PyRedeclaration
    var = counter < 3
    # getting user input for username and password, and storing them in matching variables
    input_user = input("Username: ")
    input_password = input("Password: ")
    # using if statement to compare user input for username/password, to the username/password
    # entry in our dictionary database
    if input_user == password_database["Username"] and input_password == password_database["Password"]:
        white_rabbit_object += 1
        # If user credentials match database, the following greeting,
        # and command prompt is provided, with three options.
        print("Hi, Dennis. You're still the best hacker in Jurrassic Park.")
        command_input = input(f"Please enter a command {command_database.keys()}--> ".replace('dict_keys', ''))
        if command_input == "reboot":
            print(command_database["reboot"])
            break
        if command_input == "shutdown":
            print(command_database["shutdown"])
            break
        if command_input == "done":
            print(command_database["done"])
            break
        # if user does not enter one of the three provided choices, this prompt will be given instead
        else:
            print("The Lysine Contingency has ben put into effect.")
            break
    # if user credentials do not match the database (either password, or username),
    # then the counter will add one to its count
    # once the counter reaches 3, a for loop is triggered to print a failure message 25 times on 25 lines.
    else:
        counter += 1
    if counter == 3:
        # Mini for loop to print the line 25 times to a different line each time. 
        for i in range(25):
            print("You didn't say the magic word!")
            # Once the counter is greater than 3, any subsequent attempts to log in with
            # improper credentials will trigger a visible count, with the same message.
    if counter > 3:
        print(f"You didn't say the magic word {counter} times!")
