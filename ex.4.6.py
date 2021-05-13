"""
4.6 Write a program to prompt the user for hours and rate per hour using
for all hours worked above 40 hours. Put the logic to do the computation of
the computation. The function should return a value. Use 45 hours and a rate
use raw_input to read a string and float() to convert the string to a number.
"""
#python :

def computepay(h,r):
    if h > 40:
        return (40*r)+(h-40)*(r*1.5)
    else:
        return h*r

hrs = raw_input("Enter Hours:")
rate = raw_input("Enter Rate:")

hrs = float(hrs)
rate = float(rate)

p = computepay(hrs, rate)
print p
