# Name: Miller Quintero
# Date: Oct 31, 2024
# Brief: Write a program to read through the mbox-short.txt and figure out the distribution by hour of 
# the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time
# and then splitting the string a second time using a colon: From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

# While loop until do a succesful file read
while True:
    name = input("Enter file: ")
    try:
        fh = open(name)
        break
    except:
        print("Error, file name specified doesn't exist in the directory")
    
 # Dictionary declaration   
countDict = dict()

# Iteration through the lines of the file
for line in fh:
    line = line.strip()
    if line.startswith("From "):
        words = line.split()
        hour = words[5].split(':')
        countDict[hour[0]] = countDict.get(hour[0],0) + 1
        
# Now it's time to create a dictionary sorted by key
orderedDict = {key: countDict[key] for key in sorted(countDict)}
# Finally, print it
for k, v in orderedDict.items():
    print(k,v)