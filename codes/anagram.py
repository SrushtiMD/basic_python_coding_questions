a = "srushti"
b = "abhishek"

a = sorted(a.lower())
b = sorted(b.lower())

def isAnagram():
    if a == b:
        print("The given strings are Anagram")
    else:
        print("The given strings are not Anagram")
print(isAnagram())
