elements = int(input("Enter a number of elements"))
n1, n2 = 0, 1
print("Fibonacci Sequence:")
for i in range(2, elements):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3)

