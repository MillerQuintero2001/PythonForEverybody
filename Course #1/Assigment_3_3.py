# Name: Miller Quintero
# Date: Oct 24, 2024
# Brief: Receives a score and prints the equivalent letter

score = input("Enter Score: ")

try:
    score = float(score)
except:
    score = -1

# Conditional block
if (score >= 0.0)&(score <= 1.0):
    if score >= 0.9:
        print('A')
    elif score >= 0.8:
        print('B')
    elif score >= 0.7:
        print('C')
    elif score >= 0.6:
        print('D')
    else:
        print('F')
else:
    print("Error")