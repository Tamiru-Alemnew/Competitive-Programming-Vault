# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])
        dp = [[float("inf")] * (m + 1) for _ in range(n + 1)]
        dp[n][m - 1] = dp[n - 1][m] = 1

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                cur_min = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(cur_min  - dungeon[i][j], 1)

        return dp[0][0]
