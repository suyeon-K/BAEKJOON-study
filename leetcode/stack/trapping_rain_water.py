from typing import List

# 풀이 2. 스택 쌓기
# height를 스택에 쌓아 가다가 변곡점(현재 보다 높아질 때)을 기준으로 격차만큼 물 높이 volume을 채움
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [] 
        volume = 0 # <- 1 + 1 + 3 + 1 = 6

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop() # 1
                
                # 왼쪽에 물을 담을 수 있는 기둥이 존재하는지
                if not len(stack):
                    break
                
                # 물의 횡 길이
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]
                volume += distance * waters

            stack.append(i)

        return volume

# 실패코드
class Solution:
    def trap(self, height) -> int:
        water = 0
        height = [str(x) for x in height]
        height_str = "".join(height).lstrip('0')

        if height_str == "":
            return 0

        height = [int(x) for x in height_str]
        min_num = min(height)
        height = [str(x-min_num) for x in height]
        height_str = "".join(height)
 
        while(height_str.count('0') != 0):
            water += height_str.count('0')
            temp = [int(x) for x in height_str]
            for i in range(len(height_str)):
                if temp[i] != 0:
                    temp[i] = str(temp[i]-1)
                else:
                    temp[i] =str(temp[i])
            height_str = "".join(temp).lstrip('0')

        return water

x = Solution()
print(x.trap([4,2,3]))


# 스택을 이용하지 않은 풀이
class Solution:
    def trap(self, height) -> int:
        total_water = 0

        for i in range(1, len(height)-1):
            l = max(height[:i])
            r = max(height[i+1:])
            water = min(l, r) - height[i]
            if(water>=0):
                total_water += water
        return total_water


# 공간 효율성 업!
class RainWaterTrapper:
    def trap(self, height: List[int]) -> int:
        if height == []:
            return 0
        left = [0 for i in range(len(height))]
        right = [0 for i in range(len(height))]
        total_water = 0
        
        left[0] = height[0]
        for i in range(1, len(height)):
            left[i] = max(left[i-1], height[i])
        
        right[-1] = height[-1]
        for i in range(len(height)-2, -1, -1):
            right[i] = max(right[i+1], height[i])
        
        for i in range(len(height)): 
            total_water += min(left[i], right[i]) - height[i] 
  
        return total_water