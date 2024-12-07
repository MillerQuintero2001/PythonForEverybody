# Name: Miller Quintero
# Date: Dec 6, 2024
# Brief: Assigment about retrive data from a XML document in the web

import urllib.request
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter location: ")
print(f'Retriving {url}...')
xml_string = urllib.request.urlopen(url, context=ctx).read().decode()
print(f'Retrieved {len(xml_string)} characters.')

xmlDataTree = ET.fromstring(xml_string)
counts =  xmlDataTree.findall('.//count')
# Can be done in this other way
# counts =  xmlDataTree.findall('comments/comment/count')
print(f'Count: {len(counts)}')
sum = 0
for count in counts:
    sum += int(count.text)

print('Sum:', sum)