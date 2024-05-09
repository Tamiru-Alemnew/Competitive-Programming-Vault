# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*(len(nums)+2)

        for i in range(len(nums)):
            dp[i+2] = dp[i] + nums[i]
            if i > 0 :
                dp[i + 2] = max(dp[i+1] -nums[i-1] + nums[i] , dp[i+2])


        return max(dp[-1] , dp[-2])


        