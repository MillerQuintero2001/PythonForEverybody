# Name: Miller Quintero
# Date: Dec 2, 2024
# Brief: Program that receives a file and catch numbers using regular expressions, save them into a list and print the total sum

import re

# Opening file
while(True):
    fileName = input('Please, enter the file name to read it: ')
    try:
        file = open(fileName)
        break
    except:
        print("Error, file name specified doesn't exist in the directory")

totalSum = 0

# Iterating through file
for line in file:
    line = line.rstrip()
    # Regular expression to detect one or more digits
    data = re.findall('[0-9]+', line)
    if len(data) < 1:
        continue
    # Use 'map' function to aply integer casting at iterable object
    totalSum += sum(map(int, data))

print(f"La suma total de números en el archivo es {totalSum}.")

# Here is the list comprehesion version
# file = open('regex_sum_2113593.txt')
# print( sum( [ int(i) for i in re.findall('[0-9]+',file.read()) ] ) )