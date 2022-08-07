#!/usr/bin/env python3

# Author: George Maysack-Schlueter
# Description: This is a script for week 7 of python scripting class. This script is for the "interacting with a website" lab.

import requests,bs4

res = requests.get('http://notpurple.com')
res.raise_for_status()

myHTML = bs4.BeautifulSoup(res.text,features="html.parser")

#printing title of page
print(myHTML.title.text)
#printing list of links on page
for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
    if link.has_attr('href'):
        print(link['href'])
