
num=list(map(int,input().split()))

def threesum(nums : list[int])->list[int]:

    output=[]
    nums.sort()

    for i in range(len(nums)-2):

        if i>0 and nums[i]==nums[i-1]: # 중복된 값 건너뛰기
            continue

        left,right=i+1,len(nums)-1

        while left<right:

            sum=nums[i]+nums[left]+nums[right]

            if sum<0:
                left+=1
            elif sum>0 :
                right-=1
            else :
                output.append([nums[i], nums[left], num[right]])

                while left<right and nums[left]==nums[left+1]: # 중복된 값 처리 1
                    left+=1
                while left<right and nums[right]==nums[right-1]: # 중복된 값 처리 2
                    right-=1
                left+=1
                right-=1
                continue

    return output

print(threesum(num))

