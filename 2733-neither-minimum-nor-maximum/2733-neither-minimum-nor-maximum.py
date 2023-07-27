class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        for i in nums:
            if i != max(nums) and i !=min(nums):
                return i
        return -1