# Name: Miller Quintero
# Date: Dec 3, 2024
# Brief: Create a dictionary from a text in a web page

import urllib.request, urllib.parse, urllib.error

# This function opens the socket, do GET request and returns data in a file handle
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

webDictionary = dict()
# Iterate through the file decoding the lines from UTF-8 to unicode
for line in fhand:
    words = line.strip().split()
    for word in words:
        webDictionary[word] = webDictionary.get(word, 0) + 1

print(webDictionary)
