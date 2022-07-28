#!/usr/bin/env python3

# Author: George Maysack-schlueter 
# Description: Script for week 5 in python scripting class. This script is for the second script in the functions lab ' Temp Conversion'

#importing our module from script 1 so we can call the conversion function
import f2c
# asking for user to inpput an integer representing the degrees in fahrenheit they would like to convert to celsious
user_input = int(input("Enter Degrees in Fahrenheit to be Converted to Celsius: "))
# since we imported the module, we can pass the user input as an argument to the convert temp function, and wrap it in a print stateement. 
print(f2c.convert_temp(user_input))
