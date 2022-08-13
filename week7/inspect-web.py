#!/usr/bin/env python3

# Author: George Maysack-Schlueter Description: This is a script for week 7 of python scripting class. This script is
# for the "interacting with a website" lab.

# Importing required modules - we will be using requests and beautifulsoup4
import bs4
import requests

# Initiating our request to the desired domain
res = requests.get('https://notpurple.com')
res.raise_for_status()

# Creating our variable to store the response as text and to use the HTML parser
myHTML = bs4.BeautifulSoup(res.text, "html.parser")

# printing title of page with some formatting
print('')
print(f'Here is the Title:\n{myHTML.title.text}\n')
print('___________________________________________________\n')
print('Here is the list of links:\n')

# printing list of links on page with some formatting
# Created a variable to store the returned values from parsing our page for 'a' tags (Links)
myLinks = myHTML.select('a')

# Using a for loop to say if the href value is NOT equal to NONE, then check if 'https' is in that link - if it
# is, print the link to the screen.
for link in myLinks:
    print(link.get_text())
    if link.get('href') is not None:
        if 'https://' in link.get('href'):
            print(link.get('href'))

print('')
