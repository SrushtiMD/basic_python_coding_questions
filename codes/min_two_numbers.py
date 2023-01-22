print("Enter Two numbers")
a = int(input("Enter 1st Number"))
b = int(input("Enter 2nd Number"))

def min():
    if a < b:
        print(a, "is a smaller number")
    elif a == b:
        print("The given numbers are equal")
    else:
        print(b, "is smaller number")

min()
