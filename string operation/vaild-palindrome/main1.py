# convert to list

s=input()

def valid_Palindrome(s : str)->bool:

    strs = []

    for char in s:
        if char.isalnum():  # isalnum() : 영문자, 숫자 여부를 판별하는 함수
            strs.append(char.lower())  # lower() : 소문자로 변환

    while len(strs) > 1 :
        if strs.pop(0)!=strs.pop():
            return False

    return True

print(valid_Palindrome(s))