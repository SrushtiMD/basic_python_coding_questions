## Hey Guys I'm Srushti Deshpande ##
## Here we have some basic python program  ##
**Date - 22/01/2022**

### 1) Write a program to print the given number is odd or even 

```
Num = int(input("Enter a number"))
if (Num % 2) == 0:
    print("The given number is even")
else:
    print("The given number is odd")
```     
### 2)  Write a program to find the given number is positive or negative.  ###

```
num = int(input("Enter a number"))
if num >= 0:
    print("The given number is positive")
else:
    print("The given number is negative")
```

### 3) Write a program to find the sum of two numbers ###

```
num1 = int(input("Enter 1st Number"))
num2= int(input("Enter 2nd Number"))
sum = num1 + num2
print("Sum of two given numbers is : ", sum)

```
### 4) Write a program to find if the given number is prime or not. ###

```
num = int(input("Enter a number"))
if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print("The given number is not a prime number")
    else:
        print("The given number is a prime number")
else:
    print("The given number is not a prime number")

```
### 5) Write a program to check if the given number is palindrome or not ###

```
def isPalindrome(s):
    return s == s[::-1]
s = "srushti"
a = isPalindrome(s)
if a:
    print("The given string is palindrome")
else:
    print("The given string is not palindrome")

```
### 6) Write a program to check if the given number is Armstrong or not. ###

```
num = int(input("Enter a number"))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print("The given number is an Armstrong number")
else:
   print("The given number is not an Armstrong number")

```
### 7) Write a program to check if the given strings are anagram or not.  ###

```
a = input("Enter 1st string")
b = input("Enter 2nd string")

a = sorted(a.lower())
b = sorted(b.lower())

def isAnagram():
    if a == b:
        print("The given strings are Anagram")
    else:
        print("The given strings are not Anagram")
print(isAnagram())

```
### 8) Write a program to find a maximum of two numbers ###

```
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

```
### 9) Write a program to find a minimum of two numbers. ###

```
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

```
### 10) Write a program to find a maximum of three numbers.

```
print("Enter Two numbers")
a = int(input("Enter 1st Number"))
b = int(input("Enter 2nd Number"))
c = int(input("Enter 3rd Number"))

def max():
    if a > b & b > c:
        print(a, "is a greater number")
    elif a < b & b > c:
        print(b, "is a greater number")
    elif a == b == c:
        print("The given numbers are equal")
    else:
        print(c, "is smaller number")

max()
```
### 11) Write a program to find a minimum of three numbers
```
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
```
### 12) Write a program to find a factorial of a number
```
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
```
### 13) Write a program to find a fibonacci of a number.
```
elements = int(input("Enter a number of elements"))
n1, n2 = 0, 1
print("Fibonacci Sequence:")
for i in range(2, elements):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3)
```
### 14) Write a program to find GCD of two numbers
```
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
```
### 15) Write a program to print the following pattern.
![Screenshot](https://www.notion.so/hackkeen/Assignments-c450223b69da48599ee48f3dac7101dc#07c8fe7ae72b4cbc925b7c364be97b4e)
```
n = 5
def pyramid(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("* ",end="")
        print("\r")
pyramid(n)
```

