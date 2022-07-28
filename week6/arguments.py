#!/usr/bin/env python3

#Author: George Maysack-Schlueter
#Description: This is a script for week 6 of python scripting class. This script is for the 'Using Argparse' Lab. 

#importing argparse so we can use it in our script
import argparse
import sys
#setting descripting as per instructions and ensuring that help page is added
parser = argparse.ArgumentParser(description='This is George Maysack-schlueter\'s script', add_help=True)
#====================================================================================================================================================================
parser.add_argument('-m', dest='BASIC', help='Enter some text')
parser.add_argument('-i', '--integer', dest='varInteger', metavar='[an integer]', default=10, type=int, required=False, help='<required> Enter a simple Integer')
parser.add_argument('-d', '--float', dest='varFloat', metavar='[a float]', default=10.0, type=float, required=False, help='Enter a simple Float')
parser.add_argument('-s', '--string', dest='varString', metavar='[a string]', default='hello', type=str, required=False, help='Enter a simple String')
parser.add_argument('-l', dest='varList', metavar='[strings]', default=[], nargs='+', required=False, help='Enter a list of strings (space delimited)')
parser.add_argument('-t', '--set-true', dest='bool_t', default=False, action='store_true', required=False, help='Toggle from default False to True')
parser.add_argument('-f', '--setfalse', dest='bool_f', default=True, action='store_false', required=False, help='Toggle from default True to False')
parser.add_argument('-v','--version', action='version', version='%(prog)s 1.0')
#================================================================================================================================================================================

#Now we can use the parser that we have set up above
args = parser.parse_args()
#checking for arguments - if none passed, help screen will be displayed
if len(sys.argv) == 1:
    print(parser.print_help())
    exit(0)
#printing value of integer, string, and float arguments given
print("The value of your '-i' arg is: " + str(args.varInteger))
print("The value of your '-s' arg is: " + str(args.varString))
print("The value of your '-d' arg is: " + str(args.varFloat))
#printing list arguments and list one by one
print("=== Here is the List ===")
print(args.varList)
for arg in args.varList:
    print(arg)
