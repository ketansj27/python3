"""
3.1 Write a program to prompt the user for hours and rate per hour using
    input to compute gross pay. Pay the hourly rate for the hours up to 40
    and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours
    and a rate of 10.50 per hour to test the program (the pay should be 498.75).
    You should use raw_input to read a string and float() to convert the string
    to a number.
"""
  #python :

hrs = input("Enter Hours:")
rate = input("enter rate:")
try :
    hrs =int(hrs)
    rate =float(rate)
except :
    print("error, please inter numeric input")
    exit()

if hrs <= 40 :
    Rs = float(hrs)*float(rate)
    print("To pay:",Rs)

# above 40 hours rate increase by 1.5 times
else:
    Rs = float(40)*float(rate)+(float(hrs)-40)*(float(rate)*1.5)
    print("To pay:",Rs)
