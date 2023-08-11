import re

string=input()

def isPalindrome(string:str) -> bool:
    string.lower()
    string=re.sub('[^a-z0-9]','',string)

    return string==string[::-1]
# Palindrome operation

print(isPalindrome(string))

