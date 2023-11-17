# key search subtract first number

nums=list(map(int,input().split()))
target=int(input())

def twoSum(nums:list[int],target:int)->list[int]:

    nums_map={}

    for i, num in enumerate(nums):
        nums_map[num]=i

    for i,v in enumerate(nums):
        if target-v in nums_map and i != nums_map[target-v]:
            return [i,nums_map[target-nums[i]]]

