# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        
        for i in range(count[0]):
            nums[i] = 0
        
        for i in range(count[0], count[0] + count[1]):
            nums[i] = 1
        
        for i in range(count[0] + count[1], len(nums)):
            nums[i] = 2
