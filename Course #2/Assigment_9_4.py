# Name: Miller Quintero
# Date: Oct 29, 2024
# Brief: Write a program to read through the mbox-short.txt and figure out who has 
# sent the greatest number of mail messages. The program looks for 'From ' lines and 
# takes the second word of those lines as the person who sent the mail. The program 
# creates a Python dictionary that maps the sender's mail address to a count of the 
# number of times they appear in the file. After the dictionary is produced, the program 
# reads through the dictionary using a maximum loop to find the most prolific committer.

# While loop until do a succesful file read
while True:
    name = input("Enter file name: ")
    try:
        file = open(name)
        break
    except:
        print("Error, file name specified doesn't exist in the directory")

# Initialization of the dictionary
countDict = dict()

# Iteration trough the file
for line in file:
    line = line.strip()
    # Check only the correct lines
    if line.startswith("From "):
        words = line.split()
        # Add count into the dictionary
        countDict[words[1]] = countDict.get(words[1],0) + 1

# Initialization of the variables
wordMoreRepeat = list(countDict.keys())[0]
countMoreRepeat = list(countDict.values())[0]
for word,count in countDict.items():
    if count > countMoreRepeat:
        wordMoreRepeat = word
        countMoreRepeat = count

print(wordMoreRepeat, countMoreRepeat)