#!/user/bin/env python3

# Author: George Maysack-schlueter 
# Description: Script for week 5 in python scripting class. This script is for the first script in the functions lab ' Convert Fahrenheit to Celsius'

def convert_temp(degrees_fahrenheit):
    degrees_celsius = (degrees_fahrenheit - 32) * 5/9
    return degrees_celsius

def main():
    print(convert_temp(32))

if __name__ == "__main__":
    main()
