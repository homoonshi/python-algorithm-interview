#

num = list(map(int,input().split()))

def arrayPairSum(nums : list[int])->int :
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0 :
            sum+=n

    return sum

print(arrayPairSum(num))