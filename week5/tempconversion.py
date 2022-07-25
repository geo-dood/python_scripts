#!/user/bin/env python3

# Author: George Maysack-schlueter 
# Description: Script for week 5 in python scripting class. This script is for the second script in the functions lab ' Temp Conversion'

import f2c

user_input = int(input("Enter Degrees in Fahrenheit to be Converted to Celsius: "))
print(f2c.convert_temp(user_input))