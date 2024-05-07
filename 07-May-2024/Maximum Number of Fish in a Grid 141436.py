# Problem: Maximum Number of Fish in a Grid - https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        """
        [[10,5],
         [8,0]]
        """
        visited = [[False]*len(grid[0]) for i in range(len(grid))]
        directions = [(1 , 0) , (0 , 1) , (-1 , 0) , (0 , -1)]

        
        def inbound(row , col):
            return (0<= row < len(grid)) and (0<= col < len(grid[0]))

        ans = 0 
        current = 0 
        def dfs(row , col):
            nonlocal ans , current
            if visited[row][col]:
                return 

            current +=grid[row][col]
            ans = max(ans , current)
            print(row , col , current)
            visited[row][col] = True

            for cr , cc in directions:
                new_row = row + cr
                new_col = col + cc

                if inbound(new_row , new_col) and grid[new_row][new_col] != 0:
                    dfs(new_row , new_col)
                    

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    current = 0 
                    dfs(i , j)
                    

        return ans 


