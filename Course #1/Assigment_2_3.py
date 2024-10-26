# Name: Miller Quintero
# Date: Oct 23, 2024
# Brief: Receives the amount of worked hours and the pay rate per hour and prints the total pay, have traceback error control

hrs = input("Enter Hours: ")
rate = input("Enter pay per hour: ")
try:
    hrs = float(hrs)
    rate = float(rate)
except:
    print("Error casting values.")
    quit()
pay = rate*hrs
print('Pay:',pay)