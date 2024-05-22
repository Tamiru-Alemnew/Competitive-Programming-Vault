# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        m = len(triangle[-1])
        dp = [[float("inf")]*m for i in range(n)]
        dp[0][0] = triangle[0][0]

        for i in range(1 , n):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            for j in range(1 , i+1):
                dp[i][j] = min(dp[i-1][j] , dp[i-1][j-1] ) + triangle[i][j]

        return min(dp[n-1])
        