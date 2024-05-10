# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        # top down 
        # memo = {}
        # def climb(n):
        #     if n in memo:
        #         return memo[n]
        #     if n == 1 or n == 0:
        #         return 1 
        #     elif n < 0 :
        #         return 0 
        #     memo[n] = climb(n-1) + climb(n-2)

        #     return memo[n]

        # return climb(n)

        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2 , n +1):
            dp[i] = dp[i-1] + dp[i - 2]
        
        return dp[n]