from bisect import bisect_left

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        triangle_count, n = 0, len(nums)
      
        for i in range(n - 2):  
            for j in range(i + 1, n - 1):  # j is always after i
                k = bisect_left(nums, nums[i] + nums[j], lo=j + 1) - 1
                triangle_count += k - j

        return triangle_count