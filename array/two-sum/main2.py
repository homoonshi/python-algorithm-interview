# in search

nums=list(map(int,input().split()))
target=int(input())

def twoSum(nums:list[int],target:int)->list[int]:

    for i, n in enumerate(nums):
        complement = target-n

        if complement in nums[i+1:]:
            return [nums.index(n),nums[i+1:].index(complement)+(i+1)]


print(twoSum(nums,target))

