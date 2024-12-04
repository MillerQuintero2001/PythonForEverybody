# Name: Miller Quintero
# Date: Dec 3, 2024
# Brief: Assigment to iterate through different HTML documents, a certain number of times and retrive data

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# This is to can access and scraping web sites that has Secure Socket Layer (SSL)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Function to get and URL from an anchor markup in a specific position
def getURLposition(URL_seed, position):
    # With '.read()' method, all string put together. it includes new lines
    html = urllib.request.urlopen(URL_seed, context=ctx).read()
    # Now, we use BeautifulSoup main function, indicating that the object is an HTML to parse
    parsedWeb = BeautifulSoup(html, 'html.parser')

    # Retrive all of the anchor tags '<a...>' with '.find_all('a')'
    anchorTags = parsedWeb.find_all('a')
    return str(anchorTags[position-1].get('href', None))
# End of the function 

url = input('Please, enter an URL: ')
pos = int(input('Please, enter the position of URL to retrive: '))
rep = int(input('Please, enter how many times you want to neast this process: '))

for i in range(rep):
    url = getURLposition(url, pos)
# Use regex to get tha name, and use '*' to decompress the list returned by the function
print(*re.findall('known_by_(.+)\.',url))

