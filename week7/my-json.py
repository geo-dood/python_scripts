#!/usr/bin/env python3

# Author: George Maysack-Schlueter
# Description: This is a script for week 7 of python scripting class. This is for the JSON Lab.

# Importing our required modules
import argparse
import json
import requests
import sys

# setting up a parser with a single argument, so we can get a user to input an ip address
myParser = argparse.ArgumentParser(description='IP Address Lookup Tool')
myParser.add_argument('--ipaddress', action='store', dest='ipAddress', metavar='[Desired IP Address]',
                      help="Enter the "
                           "flag "
                           "'--ipaddress' "
                           "followed by "
                           "the IPv4 "
                           "address you "
                           "would like "
                           "to look up")
ipArg = myParser.parse_args()
searchAddress = ipArg.ipAddress

# Checking if the length of the argument is nothing - if it is, we want to display the help message.
if len(sys.argv) == 1:
    myParser.print_help()
# Otherwise, we are going to initiate our json request to the IP info API, and get the required key/value pair printed
else:
    jsonRequest = requests.get(f"http://ipinfo.io/{searchAddress}/json")
    myDict = json.loads(jsonRequest.text)
    for key in myDict:
        print(f"{key} : {myDict[key]}")
