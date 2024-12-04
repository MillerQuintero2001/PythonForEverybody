# Name: Miller Quintero
# Date: Dec 2, 2024
# Brief: First practice with regular expression using findall function

import re

string = "Ah, my favorite 2 numbers are 9 and 36."
print(re.findall('[0-9]+', string))
print(re.findall('[AEIOU]+', string))

x = 'From: Using the : character'
# Greedy special character
print(re.findall('^F.+:', x))
# Non-greedy special character
print(re.findall('^F.+?:', x))

# Specify what piece capture
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
print(re.findall('^From .*@([^ ]*)', lin))
print(re.findall('@(\S+)', lin))

# Include special characters in regular expressions
x = 'We just received $10.00 for cookies'
print(re.findall('\$[0-9.]+',x))