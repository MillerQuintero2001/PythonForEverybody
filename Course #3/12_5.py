# Name: Miller Quintero
# Date: Dec 3, 2024
# Brief: Introduction to using BeautifulSoup to parse HTML's

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# This is to can access and scraping web sites that has Secure Socket Layer (SSL)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Please, enter an URL: ')

# With '.read()' method, all string put together. it includes new lines
html = urllib.request.urlopen(url, context=ctx).read()
# Now, we use BeautifulSoup main function, indicating that the object is an HTML to parse
parsedWeb = BeautifulSoup(html, 'html.parser')

# Retrive all of the anchor tags '<a...>' with ('a')
tags = parsedWeb('a')
for tag in tags:
    # Getting the URL's inside HTML's anchor
    print(tag.get('href', None))

