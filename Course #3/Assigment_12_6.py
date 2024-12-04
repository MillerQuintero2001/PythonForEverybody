# Name: Miller Quintero
# Date: Dec 3, 2024
# Brief: Assigment about do web scraping an HTML page to get the total sum of a numerical table data

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# List to save the numbers extracted from the website
numbersWeb = []
# Retrieve all of the anchor tags
tags = soup('tr')
for tag in tags:
    # Take the second element of the tag, which contains the number, using a regex
    number = re.findall('class="comments">(.+?)<', str(tag.contents[1]))
    try:
        numbersWeb.append(int(number[0]))
    except:
        print("The element wasn't a number.")
print(sum(numbersWeb))
