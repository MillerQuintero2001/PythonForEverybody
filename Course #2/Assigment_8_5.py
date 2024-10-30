# Name: Miller Quintero
# Date: Oct 27, 2024
# Brief: Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent 
# the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.

# While loop until the file were readed
while True:
    fname = input("Enter file name: ")
    try:
        fh = open(fname)
        break
    except:
        print("Error, file name specified doesn't exist in the directory")

# Initialization of counter lines that starts with "From "
counterLines = 0

# For loop to parse each line
for line in fh:
    # Strip left and right white spaces to ensure the parsing
    line = line.strip()
    if line.startswith("From "):
        print(line.split()[1])
        counterLines += 1
print("There were", counterLines, "lines in the file with From as the first word")