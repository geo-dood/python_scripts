#!/usr/bin/env python3

# Author: George Maysack-Schlueter
# Description: This is the final exam script for python scripting class. 

# Importing our required modules. 
import argparse, requests, bs4, json


# *****PARSER*****
""" 
As per step one, we are setting up our script to accept two arguments
- The first argument will be a string for entering the desired IP address
- The second argument will be an integer for entering a question which will be tied to a number between 1-5
"""
# Our fist step will be to initialize our parser by giving it a name. I thought 'finalParser' was fitting in this case. 
finalParser = argparse.ArgumentParser(description="This is the parser for the Final Exam of Python Scripting", add_help=True)

# Next, we are going to add our string ip address argument. We want it to be required, and have a short flag of -i and a long flag of --ipaddress
# Included a metavar and help value to assist user, and ensured to set our action to store the input to a variable called 'ip_address'
finalParser.add_argument('-i', '--ipaddress', action='store', dest='ip_address', metavar='[Desired IP Address]', type=str, required=True, help="Enter desired IP address")

# Next, we will add our required integer argument, with a short flag of '-q' and a long flag of '--question', which will serve as a selection menu between 5 options.
# Included some help information, and set the action to store user input in a varible called function_number
finalParser.add_argument('-q', '--question', action='store', dest='function_number', metavar='[Desired Function Number]', type=int, required=True, help="Enter desired function number")

# Parsing our arguments for use - storing in finalArguments varible.
finalArguments = finalParser.parse_args()

ipAddress = finalArguments.ip_address
functionNumber = finalArguments.function_number


# *****PRINTING URL & NAME*****

# Creating a formatted string to combine the IP address and the function number starting with 'http://', and storing it in a variable called URL which we then print to the screen
# Including a quick signature, as per the instructions
URL = f"http://{ipAddress}/q{functionNumber}"
print("George D. Maysack-Schlueter")
print(URL)

# ******FUNCTIONS*****

# Function 1 - get_response

# Checking if our function number is 1. If it is, we initiate a request using the specified URL, and print the text value of the response
if functionNumber == 1:
    get_response = requests.get(URL)
    print(get_response.text)

# Function 2 - parse_string
if functionNumber == 2:
    parse_string = requests.get(URL)
    # Creating our variable to store the response as text and to use the HTML parser
    finalSoup = bs4.BeautifulSoup(parse_string.text, "html.parser")

# printing list of links on page with some formatting
# Created a variable to store the returned values from parsing our page for 'a' tags (Links)
    finalHeaders = finalSoup.select('h2')

    for link in finalHeaders:
        print(f"{link.get_text()}"[7:32:3] + " George D. Maysack-Schlueter")


# Function 3 - parse_header
if functionNumber == 3:
    # creating parse_header function which is a simple requests.get to our URL.
    parse_header = requests.get(URL)
    # Then, we are printing a formatted string grabbing only the headers from our parse_headers variable, and then only the 'FINAL HEADER' header entry. 
    print(f"Answer: {parse_header.headers['FINAL-HEADER']}")
    

# Function 4 - parse_json
if functionNumber == 4:
    parse_json = requests.get(URL)
    json_dict = json.loads(parse_json.text)

    for key in json_dict:
        theShining = json.dumps(json_dict["Music And Books"][3])
        print(f"ANSWER: {theShining[61:65]}")

# Function 5 - socket_client
if functionNumber == 5:
    socket_client = True
