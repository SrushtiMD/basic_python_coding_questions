num = 7
if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print("The given number is not a prime number")
    else:
        print("The given number is a prime number")
else:
    print("The given number is not a prime number")
