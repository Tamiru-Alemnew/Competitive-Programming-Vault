# Problem: Minimum Increment to Make Array Unique - https://leetcode.com/problems/minimum-increment-to-make-array-unique/

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        increment = 0 
        
        for i in range(1 , len(nums)):
            if nums[i] <= nums[i-1]:
                dif = nums[i-1]- nums[i] + 1
                nums[i] += dif
                increment += dif

        return increment 