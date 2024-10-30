# Name: Miller Quintero
# Date: Oct 26, 2024
# Brief: Code using find() and string slicing to extract the number at the end of the
# line below. Convert the extracted value to floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(':')
number = float(text[pos+1::])
print(number)