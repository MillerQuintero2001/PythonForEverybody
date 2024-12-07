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
# In this case isn't much necessary decode data, is more necessary with XML and JSON
html = urlopen(url, context=ctx).read().decode()
soup = BeautifulSoup(html, "html.parser")

# With .select method we can take all data with, or also with .find_all
tags = soup.select('span.comments')
#tags = soup.find_all('span', class_='comments')
# List to save the numbers extracted from the website
numbersWeb = [int(tag.text) for tag in tags]

''' This is another way to do that '''
#numbersWeb = []
# Retrieve all of the 'tr' tags
# tags = soup('tr')
# for tag in tags:
#     # Take the second element of the tag, which contains the number, using a regex
#     number = re.findall('class="comments">(.+?)<', str(tag.contents[1]))
#     try:
#         numbersWeb.append(int(number[0]))
#     except:
#         print("The element wasn't a number.")

print(sum(numbersWeb))