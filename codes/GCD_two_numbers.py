a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
def gcd(a, b):
    if (a == 0):
        return b
    if (b == 0):
        return a
    if (a == b):
        return a
    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)
print('GCD of', a, 'and', b, 'is', gcd(a, b))
