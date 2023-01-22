def isPalindrome(s):
    return s == s[::-1]
s = "srushti"
a = isPalindrome(s)
if a:
    print("The given string is palindrome")
else:
    print("The given string is not palindrome")
