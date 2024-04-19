class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False]*len(grid[0]) for _ in range(len(grid))]    
        directions = [(1 , 0) , (-1 , 0 ) , (0 ,1 ) , ( 0 , -1)]

        def inbound(row , col):
            return (0<= row < len(grid)) and (0<= col < len(grid[0]))

        def dfs(row , col):
            visited[row][col] = True

            for row_change , col_change in directions:
                new_row = row + row_change
                new_col = col + col_change

                if inbound(new_row , new_col) and not visited[new_row][new_col] and grid[new_row]
[new_col] =="1":
                    dfs(new_row , new_col)


        ans = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not visited[i][j]:
                    ans += 1 
[
