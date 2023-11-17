#brute-force

num=list(map(int,input().split()))

def threesum(nums:list[int])->list[list[int]]:

    nums.sort()
    output=[]

    for i in range(0,len(nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        for j in range(i+1,len(nums)-1):
            if j>i+1 and nums[j]==nums[j-1]:
                continue
            for k in range(j+1,len(nums)):
                if k>j+1 and nums[k]==nums[k-1]:
                    continue
                if(nums[i]+nums[j]+nums[k]==0):
                    output.append([nums[i],nums[j],nums[k]])

    return output


print(threesum(num))

