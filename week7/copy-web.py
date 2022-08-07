#!/usr/bin/env python3

# Author: George Maysack-Schlueter
# Description: This is a script for week 7 of python scripting class. This script is for the "interacting with a website" lab.

import requests,bs4

# Step 1 - Copying a webpage and saving it to a file
import requests

response = requests.get("https://notpurple.com")

with open("my_web_file.html", "w") as hFile:
    hFile.write(response.text)

print("Copy page to file complete! Check file 'my_web_file.html for results.")
