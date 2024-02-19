class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        col_max =[max(row) for row in grid]
        row_max =[max(column) for column in zip(*grid)]

        increase = 0 
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                increase += min(row_max[r] , col_max[c]) - grid[r][c]

        return increase


