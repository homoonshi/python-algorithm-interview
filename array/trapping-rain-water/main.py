#two pointer

water = list(map(int,input().split()))

def trap(height:list[int])->int :

    volume=0
    left,right=0,len(height)-1
    left_max,right_max=height[left],height[right]

    while(left!=right):

        left_max=max(height[left],left_max)
        right_max=max(height[right],right_max)

        if(left_max<=right_max): # 둘중 더 낮은 쪽이 높은 쪽으로 이동
            volume+=left_max-height[left]
            left+=1
        else:
            volume+=right_max-height[right]
            right-=1

    return volume

print(trap(water))

