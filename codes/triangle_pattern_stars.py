n = 5
def pyramid(n):
    a = n - 1
    for i in range(0, n):
        for j in range(0, a):
            print(end=" ")
        a = a - 1
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")
pyramid(n)
