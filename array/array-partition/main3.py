# like python

num = list(map(int,input().split()))

def arrayPairSum(nums : list[int])->int:
    return sum(sorted(nums)[::2]) # 2칸 씩 건너뛰어 계산 (min 값이므로)

print(arrayPairSum(num))

