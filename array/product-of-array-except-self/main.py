
num = list(map(int,input().split()))
def productExceptSelf(nums:list[int])->list[int]:

    left=1
    right=1

    output=[]

    for i in range(0,len(nums)):
        output.append(left) # 본인을 제외 해야 하기 때문에 리스트에 먼저 추가한다
        left*=nums[i]


    for j in range(len(nums)-1,0-1,-1):
        output[j]=output[j]*right
        right*=nums[j]

    return output


print(productExceptSelf(num))


