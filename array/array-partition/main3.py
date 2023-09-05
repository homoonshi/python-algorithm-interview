# like python

num = list(map(int,input().split()))

def arrayPairSum(nums : list[int])->int:
    return sum(sorted(nums)[::2])

print(arrayPairSum(num))

