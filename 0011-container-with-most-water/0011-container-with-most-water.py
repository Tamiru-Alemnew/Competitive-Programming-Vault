class Solution:
    def maxArea(self, height: List[int]) -> int:
        area, maxArea= 0,0
        l , r = 0 ,  len(height)-1
        
        while l < r:
            width = r - l
            area = min(height[l], height[r]) * width
            maxArea= max(maxArea,area)

            if min(height[l],height[r]) == height[l]:
                l += 1
            else:
                r -= 1

        return maxArea

        