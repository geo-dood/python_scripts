#!/usr/bin/env python3

# Author: George Maysack-Schlueter
# Description: This is the final exam script for python scripting class. 

# Importing our required modules.
import argparse
import json
import socket

import bs4
import requests

# ---------------------------------------------------------------------------------------------------------------------
# *****PARSER*****
""" 
As per step one, we are setting up our script to accept two arguments
- The first argument will be a string for entering the desired IP address
- The second argument will be an integer for entering a question which will be tied to a number between 1-5
"""
# Our fist step will be to initialize our parser by giving it a name. I thought 'finalParser' was fitting in this case. 
finalParser = argparse.ArgumentParser(description="This is the parser for the Final Exam of Python Scripting",
                                      add_help=True)

# Next, we are going to add our string ip address argument. We want it to be required, and have a short flag of -i
# and a long flag of --ipaddress Included a metavar and help value to assist user, and ensured to set our action to
# store the input to a variable called 'ip_address'
finalParser.add_argument('-i', '--ipaddress', action='store', dest='ip_address', metavar='[Desired IP Address]',
                         type=str, required=True, help="Enter desired IPv4 address")

# Next, we will add our required integer argument, with a short flag of '-q' and a long flag of '--question',
# which will serve as a selection menu between 5 options. Included some help information, and set the action to store
# user input in a variable called function_number
finalParser.add_argument('-q', '--question', action='store', dest='function_number',
                         metavar='[Desired Function Number]', type=int, required=True,
                         help="1 = get_response function, 2 = parse_string function, 3 = parse_header function, "
                              "4 = parse_json function, 5 = socket_client function")

# Parsing our arguments for use - storing in finalArguments variable.
finalArguments = finalParser.parse_args()

ipAddress = finalArguments.ip_address
functionNumber = finalArguments.function_number
# --------------------------------------------------------------------------------------------------------------------
URL = f"https://{ipAddress}/q{functionNumber}"
print("")
print("George D. Maysack-Schlueter")
print("")
print(URL)

# ---------------------------------------------------------------------------------------------------------------------
if functionNumber == 1:
    get_response = requests.get(URL)
    print("")
    print(get_response.text)
    print("")

# *Function 2* - parse_string
if functionNumber == 2:
    parse_string = requests.get(URL)
    # Creating our variable to store the response as text and to use the HTML parser
    finalSoup = bs4.BeautifulSoup(parse_string.text, "html.parser")
    # printing list of links on page with some formatting
    # Created a variable to store the returned values from parsing our page for 'a' tags (Links)
    finalHeaders = finalSoup.select('h2')
    for link in finalHeaders:
        print("")
        print(f"{link.get_text()}"[7:32:3] + " George D. Maysack-Schlueter")
        print("")

# *Function 3* - parse_header
if functionNumber == 3:
    # creating parse_header function which is a simple requests.get to our URL.
    parse_header = requests.get(URL)
    # Then, we are printing a formatted string grabbing only the headers from our parse_headers variable,
    # and then only the 'FINAL HEADER' header entry.
    print("")
    print(f"Answer: {parse_header.headers['FINAL-HEADER']}")
    print("")

# *Function 4* - parse_json
if functionNumber == 4:
    parse_json = requests.get(URL)
    json_dict = json.loads(parse_json.text)

    for key in json_dict:
        theShining = json.dumps(json_dict["Music And Books"][3])
        print("")
        print(f"ANSWER: {theShining[61:65]}")
        print("")

# *Function 5* - socket_client
if functionNumber == 5:
    socket_client = ipAddress
    remotePortRange = range(5000, 7000)
    timeout = 10

    for RPORT in remotePortRange:

        C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        C_SOCK.settimeout(timeout)

        try:
            C_SOCK.connect((socket_client, RPORT))
            C_SOCK.send(bytearray("secret", 'utf8'))
            receivedData = C_SOCK.recv(4096)
            print("")
            print(f"Answer: {receivedData.decode()}\r")
            print(f"\rPort: {RPORT}")
            C_SOCK.close()
        except socket.error as e:
            C_SOCK.close()
