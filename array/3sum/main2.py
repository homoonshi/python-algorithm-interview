
num=list(map(int,input().split()))
num.sort()

def threesum(nums : list[int])->list[int]:

    left,right=0
    output=[]

    for i in range(len(nums)-2):

        if i>0 and nums[i]==nums[i-1]:
            continue

        left,right=i+1,len(nums)-1

        while left<right:

            if left>i+1 and nums[left]==nums[left-1]:
                continue

            sum=nums[i]+nums[left]+nums[right]

            if sum<0:
                left+=1
            elif sum>0 :
                right-=1
            else :
                output.append([nums[i], nums[left], num[right]])
                left+=1
                continue

    return output

print(threesum(num))