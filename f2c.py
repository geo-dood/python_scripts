#!/usr/bin/env python3

# Author: George Maysack-schlueter Description: Script for week 5 in python scripting class. This script is for the
# first script in the functions' lab ' Convert Fahrenheit to Celsius'

# Defining our degree conversion function - setting it to take one argument, which is the degrees in fahrenheit to be
# converted
def convert_temp(degrees_fahrenheit):
    # degrees in fahrenheit (argument) passed to equation to turn it to degrees celsius, which we then return the
    # result of tto the program.
    degrees_celsius = (degrees_fahrenheit - 32) * 5 / 9
    return degrees_celsius


# Creating a main loop with an argument of 32 - which means 32 degrees fahrenheit will be being passed as an argument
# when we run this script locally. The result is printed to the screen.
def main():
    print(convert_temp(32))


if __name__ == "__main__":
    main()
