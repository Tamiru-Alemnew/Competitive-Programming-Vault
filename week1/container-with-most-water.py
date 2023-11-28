class Solution:
    def maxArea(self, height: List[int]) -> int:
        l , r , maxArea = 0 , len(height)-1 ,  0

        while l < r:
            width = r - l
            maxArea= max(maxArea , min(height[l], height[r]) * width)
            
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1

        return maxArea

        