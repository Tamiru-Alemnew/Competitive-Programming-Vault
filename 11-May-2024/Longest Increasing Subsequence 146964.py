# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)

        for i in range(len(nums)):
            for j in range(i + 1 , len(nums)):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j] , dp[i] + 1)

        return max(dp)
