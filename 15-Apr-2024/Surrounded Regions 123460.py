# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        zeros = set()
        temp = []
        for i in range(len(grid)):
            if i == 0 or i == len(grid)-1:
                for j in range(len(grid[0])):
                    if grid[i][j] == 'O':
                        zeros.add((i,j))
                        temp.append((i , j))
               
            else:
                if grid[i][0] == "O":
                    zeros.add((i , 0))
                    temp.append((i , 0))

                if grid[i][len(grid[0])-1] == "O":
                    temp.append((i , len(grid[0])-1))
                    zeros.add((i , len(grid[0])-1))

        def inbound(row , col):
            return (0<= row < len(grid)) and (0<= col < len(grid[0]))

        directions = [(1 ,0 ) , (-1 ,0), (0 , 1) , (0 , -1)]
        visited = set()
        def dfs(row , col):
            zeros.add((row , col))
            for row_change , col_change in directions:
                new_row = row + row_change 
                new_col = col + col_change

                if  inbound(new_row , new_col) and (new_row , new_col) not in visited and grid[new_row][new_col] == "O":
                    visited.add((new_row , new_col))
                    dfs(new_row , new_col)
                    print(new_row , new_col)

        for row , col in temp:
            dfs(row , col )

       
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "O" :
                    if (i , j) not in zeros:
                        grid[i][j] = "X"



    
