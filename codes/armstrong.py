num = 250
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
