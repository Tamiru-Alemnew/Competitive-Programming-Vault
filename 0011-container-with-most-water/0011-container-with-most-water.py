from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        area, left ,maxArea= 0,0,0
        right= len(height)-1
        while left < right:
            width = right - left
            area = min(height[left],height[right])*width
            maxArea= max(maxArea,area)

            if min(height[left],height[right]) == height[left]:
                left+=1
            else:
                right -=1
        return maxArea

        
