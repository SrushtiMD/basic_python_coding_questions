print("Enter Two numbers")
a = int(input("Enter 1st Number"))
b = int(input("Enter 2nd Number"))

def max():
    if a > b:
        print(a, "is a greateer number")
    elif a == b:
        print("The given numbers are equal")
    else:
        print(b, "is greater number")

max()


