"""
To find largest and smallest from user input number.
"""
#python :

largest = -1
smallest = None
while True:
    try :

        num = input("Enter a number:")
        if num == "done" :
            break
        num = int(num)

        if smallest is None :
            smallest = num
        elif num < smallest :
            smallest = num
        elif num > largest :
            largest = num
    except :
        print("error,Invalid number")

print("Maximum is",largest)
print("Minimum is",smallest)
