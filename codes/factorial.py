num = int(input("Enter a number: "))
factorial = 1
if num > 0:
    for i in range(1,num + 1):
        factorial = factorial*i
    print("The factorial of given number is : ", factorial)
elif num == 0:
    print("The factorial of 0 is 1")
else:
   print("factorial does not exists for negative values")
