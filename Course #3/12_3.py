# Name: Miller Quintero
# Date: Dec 3, 2024
# Brief: Learn how to use urlib

import urllib.request, urllib.parse, urllib.error

# This function opens the socket, do GET request and returns data in a file handle
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# Iterate through the file decoding the lines from UTF-8 to unicode
for line in fhand:
    print(line.decode().strip())

# To print HTTP's headers
print(f'\n{fhand.info()}')