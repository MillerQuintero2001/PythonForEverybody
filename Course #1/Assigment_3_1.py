# Name: Miller Quintero
# Date: Oct 24, 2024
# Brief: Receives the amount of worked hours and the pay rate per hour and prints the total pay, there is a mofication if the hours worked are more than 40

hrs = input("Enter Hours: ")
rpHour = input("Enter rate per hour: ")
try:
    h = float(hrs)
    p = float(rpHour)
except:
    print("Error casting values to float")
    quit()
if h > 40:
    pay = (h-40.0)*p*1.5 + (40.0*p)
else:
    pay = h*p
print(pay)