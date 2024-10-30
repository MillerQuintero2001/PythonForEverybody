# Name: Miller Quintero
# Date: Oct 27, 2024
# Brief: Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce 
# an output as shown below. Do not use the sum() function or a variable named sum in your solution.

# Use the file name mbox-short.txt as the file name
while True:
    fname = input("Enter file name: ")
    try:   
        fh = open(fname)
        break
    except:
        print("Error, file name specified doesn't exist in the directory")

count = 0
total = 0.0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        pos = line.find(":")
        total += float(line[pos+1::].strip())
        count += 1
    
print("Average spam confidence:", total/count)
