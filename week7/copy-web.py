#!/usr/bin/env python3

# Author: George Maysack-Schlueter
# Description: This is a script for week 7 of python scripting class. This script is for the "interacting with a website" lab.

import requests,bs4

# Step 1 - Copying a webpage and saving it to a file
#Importing our required module - only requests is needed here.
import requests

#saving our html response to a variable using the get function
response = requests.get("https://notpurple.com")

# Opening a file with write accesses, and writing the text response from the webpage above to it before saving
with open("my_web_file.html", "w") as hFile:
    hFile.write(response.text)

# printing completion message for visibility
print("Copy page to file complete! Check file 'my_web_file.html for results.")
