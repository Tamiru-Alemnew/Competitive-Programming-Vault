class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        n, m = len(grid), len(grid[0])
        res = 0

        def dfs(row, col):
            if not ((0 <= row < n) and (0 <= col < m)) or grid[row][col] != "1":
                return

            grid[row][col] = "#"
            for r, c in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                new_row = row + r
                new_col = col + c
                dfs(new_row, new_col)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j)

        return res
