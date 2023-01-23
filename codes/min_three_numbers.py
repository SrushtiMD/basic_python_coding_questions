print("Enter Two numbers")
a = int(input("Enter 1st Number"))
b = int(input("Enter 2nd Number"))
c = int(input("Enter 3rd Number"))

def min():
    if a < b & b < c:
        print(a, "is a smaller number")
    elif a > b & b < c:
        print(b, "is a smaller number")
    elif a == b == c:
        print("The given numbers are equal")
    else:
        print(c, "is smaller number")

min()
