#!/usr/bin/env python3
# George D. Maysack-Schlueter
import argparse
import sys

parserName = argparse.ArgumentParser(description="Hello World!")

parserName.add_argument('-e', '--email', dest='emailAddress', default="johndoe42@email.com", type=str, help="Enter "
                                                                                                            "email "
                                                                                                            "address")
parserName.add_argument('-n', '--name', dest='fullName', default="John Doe", type=str, help="Enter full name")
parserName.add_argument('-p', '--phone', dest='phoneNumber', default="6084440101", type=int, help="Enter phone")
parserName.add_argument('-l', '--height', dest='heightInches', default="68", metavar='[height in inches]', type=int,
                        help="Enter height in inches as integer")
parserName.add_argument('-w', '--weight', dest='weightPounds', default=197.9, metavar='[weight in pounds]', type=float,
                        required=True, help="Enter weight in lbs w/ decimal")
parserName.add_argument('-i', '--international', dest='internationalCust', default=False, action='store_true',
                        help="Include if not located in U.S.A.")
parserName.add_argument('-f', '--foods', dest='favoriteFoods', nargs='+', help="Specify your favorite foods")
parserName.add_argument('-v', '--version', action='version', version="%(prog)s 1.0")
myArguments = parserName.parse_args()

if len(sys.argv) == 1:
    print(parserName.print_help())
else:
    print(parserName.parse_args())

print(myArguments)
print(myArguments.emailAddress)
print(myArguments.phoneNumber)
print(type(myArguments.weightPounds))
print(type(myArguments.heightInches))
print(type(myArguments.internationalCust))
print(parserName.parse_args().favoriteFoods)
