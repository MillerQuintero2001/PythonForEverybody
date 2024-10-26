# Name: Miller Quintero
# Date: Oct 24, 2024
# Brief: Receives hours and rate per hour to print the pay using a function and catching errors

def computepay(h, r):
    pay = 0
    if h > 40:
        pay = (h - 40)*r*1.5 + 40*r
        return pay
    else:
        pay = h*r
        return pay

while True:
    hrs = input("Enter Hours:")
    rate = input("Enter Rate Per Hour:")

    try:
        workedHours = float(hrs)
        payRate = float(rate)
        break;
    except:
        print("Error casting values, try again")

p = computepay(workedHours, payRate)
print("Pay", p)