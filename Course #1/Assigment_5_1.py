# Name: Miller Quintero
# Date: Oct 25, 2024
# Brief: Program that repeatedly prompts a user for integer numbers until the user enters 
# 'done'. Once 'done' is entered, print out the count of elements, sum and average. If 
# the user enters anything other than a valid number catch it with a try/except and put 
# out an appropriate message and ignore the number

count = 0
sum = 0
while True:
    num = input("Enter a number: ")
    
    if num == "done":
        break
        
    try:
        num = int(num)
    except:
        print("Invalid input")
        # Go to the next iteration
        continue

    sum += num
    count += 1

print("Sum is:",sum,
      "\nAmount of elements is:",count,
      "\nAverage is:",sum/count)