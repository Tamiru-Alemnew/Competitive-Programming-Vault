# Problem: Minimum Score Triangulation of Polygon - https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0 for j in range(n)] for i in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i+2, n):
                m = float('inf')
                for k in range(i+1, j):
                    m = min(m, values[i]*values[j]*values[k] + dp[i][k] + dp[k][j])
                    
                dp[i][j] = m
        return dp[0][n-1]