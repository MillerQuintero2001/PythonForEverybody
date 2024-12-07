# Name: Miller Quintero
# Date: Dec 6, 2024
# Brief: Assigment about scrapping web data from a JSON

import urllib.request
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Input documment/data JSON URL
urlAdress = input('Enter location: ')
print('Retrieving:', urlAdress)
# Read data raw
rawData = urllib.request.urlopen(urlAdress, context=ctx).read().decode()
print(f'Retrieved {len(rawData)} characters.')
# Parsing with json.loads
jsonData = json.loads(rawData)

sumCount = 0
# Iterate through the list of comments
for comment in jsonData['comments']:
    sumCount += int(comment['count'])
print('Count:',len(jsonData['comments']))
print('Sum:', sumCount)
