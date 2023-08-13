#!/usr/bin/env python3

# Author: George Maysack-Schlueter
# Description: This is a script for week 4 of python scripting. This script will be applying concepts we learned
# regarding dictionaries in python.

# defining our dictionary with domain names/Ip addresses. Line break used for readability
dictionary = {"server1.testlab.com": "192.168.1.10", "server2.testlab.com": "192.168.1.11",
              "server3.testlab.com": "192.168.1.12", "server4.testlab.com": "192.168.1.13",
              "server5.testlab.com": "192.168.1.14", "server6.testlab.com": "192.168.1.15",
              "server7.testlab.com": "192.168.1.16", "server8.testlab.com": "192.168.1.17"}

# Printing dictionary keys (FQDN's in this case). Accessing keys with <dictionaryname>.keys() and putting that inside
# of a print function. Empty print statements added for formatting.
print("")
print(f"KEYS: {dictionary.keys()}")
print("")
# Printing dictionary values (IP addresses in this case). Accessing values with <dictionaryname>.values() and putting
# that inside of a print function.
print(f"IP ADDRESSES: {dictionary.values()}")
print("")
# Printing dictionary keys and values together (FQDN + IP Address in this case). Accessing key/value pairs with
# <dictionaryname>.items() and putting that inside of a print function.
print(f"FULL RECORDS: {dictionary.items()}")
print("")
# using an if statement to check if server2.testlab.com exists in our dictionary - which will then print to screen
# whether it appears or not.
if "server2.testlab.com" in dictionary:
    print("FQDN 'server2.testlab.com' was found in dictionary!")
else:
    print("FQDN 'server2.testlab.com' was not found in dictionary!")
print("")
# using an if statement to check if server10.testlab.com exists in our dictionary - which will then print to screen
# whether it appears or not.
if "server10.testlab.com" in dictionary:
    print("FQDN 'server10.testlab.com' was found in dictionary!")
else:
    print("FQDN 'server10.testlab.com' was not found in dictionary!")
print("")
