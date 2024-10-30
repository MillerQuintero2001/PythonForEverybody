# Name: Miller Quintero
# Date: Oct 27, 2024
# Brief: Write a program that prompts for a file name, then opens that 
# file and reads through the file, and print the contents of the file 
# in upper case. Use the file words.txt to produce the output below.

# Use words.txt as the file name
while True:
    fname = input("Enter file name with the .txt extension: ")
    try:
        fh = open(fname, "r")
        break
    except:
        print("Error, file name specified doesn't exist in the directory")

for line in fh:
    print(line.upper().strip())
