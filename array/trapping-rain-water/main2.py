#stack

water = list(map(int,input().split()))

def trap(height : list[int]) -> int :
    stack=[]
    volume = 0

    for i in range(len(height)):
        while stack and height[i]>height[stack[-1]]:
            top=stack.pop()

            if not len(stack): # 앞쪽의 벽이 없어서 물이 쏟아질 때
                break

            distance=i-stack[-1]-1
            waters=min(height[i],height[stack[-1]])-height[top] # 벽중에 제일 낮은 벽과 제일 낮은 바닥과의 거리, 물이 찬 공간

            volume+=distance+waters # 물의 양

        stack.append(i)

    return volume

print(trap(water))

