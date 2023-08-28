class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        result = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    result += 4
                    if r > 0 and grid[r-1][c] == 1:
                        result -= 2
                    if c > 0 and grid[r][c-1] == 1:
                        result -=2
        return result 

                    

