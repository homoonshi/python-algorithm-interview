# Two-Pointer swap

n=input()
reverse_str=list(n)

def reverse_string (s : list[str]) -> str :
    left, right = 0, len(s) - 1
    while left < right :
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s

print(reverse_string(reverse_str))

