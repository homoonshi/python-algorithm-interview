# improve search structure

nums=list(map(int,input().split()))
target=int(input())

def twoSum(nums:list[int],target:int)->list[int]:

    nums_map={}

    for i, num in enumerate(nums):
        if target-num in nums_map:
            return [nums_map[target-num],i]
        nums_map[num]=i

