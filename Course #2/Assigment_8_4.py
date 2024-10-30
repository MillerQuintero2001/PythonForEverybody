# Name: Miller Quintero
# Date: Oct 27, 2024
# Brief: Open the file romeo.txt and read it line by line. For each line, split 
# line into a list of words using the split() method. The program should build a 
# list of words. For each word on each line check to see if the word is already in
# the list and if not append it to the list. When the program completes, sort and 
# print the resulting words in python sort() order as shown in the desired output.

# While loop until the file were readed
while True:
    fname = input("Enter file name: ")
    try:
        fh = open(fname)
        break
    except:
        print("Error, file name specified doesn't exist in the directory")

# Declare the empty list to fill it with thw new words
lst = list()
for line in fh:
    wordList = line.strip().split()
    for word in wordList:
        if not word in lst:
            lst.append(word)
# This method changes the original list object, for that reason is necessary use it before print the list
lst.sort()
print(lst)
