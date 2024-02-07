class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros, l = 0, 0
        for r, n in enumerate(nums):
            zeros += n == 0
            if zeros > k:
                zeros -= nums[l] == 0
                l += 1
        return r - l + 1