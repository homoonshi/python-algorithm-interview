# Slicing

import re

string=input()

def isPalindrome(string:str) -> bool:
    string.lower()
    string=re.sub('[^a-z0-9]','',string) # 정규 표현식으로 불필요한 문자 필터링

    return string==string[::-1] # 슬라이싱
# Palindrome operation

print(isPalindrome(string))

