class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        r = 0
        while r < len(nums):
            if r == len(nums) - 1 or nums[r] != nums[r + 1]:
                return nums[r]
            r += 2
