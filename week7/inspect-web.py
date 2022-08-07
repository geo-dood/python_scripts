#!/usr/bin/env python3

# Author: George Maysack-Schlueter
# Description: This is a script for week 7 of python scripting class. This script is for the "interacting with a website" lab.

import requests,bs4

res = requests.get('http://notpurple.com')
res.raise_for_status()

myHTML = bs4.BeautifulSoup(res.text, "html.parser")

#printing title of page
print(f'Here is the Title: {myHTML.title.text}')
print('___________________________________________________')
print('Here is the list of links:\n')
#printing list of links on page
links = myHTML.select('a')

for link in links:
    print(link.get_text())
    if link.get('href') != None:
        if 'https://' in link.get('href'):
            print(link.get('href'))
        else:
            print(link.get('href'))
