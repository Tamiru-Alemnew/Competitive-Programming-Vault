# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        directions = [[0,1], [1,0], [0,-1], [-1,0]]

        queue = deque()
        nonrotten = 0 
        n , m = len(grid) , len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i ,j))
                elif grid[i][j] == 1:
                    nonrotten += 1
        
        time = 0
        while queue and nonrotten > 0:
            for _ in range(len(queue)):
                row , col = queue.popleft()

                for row_change , col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change

                    if (new_row < 0 or new_row == n or new_col < 0 or new_col == m or grid[new_row][new_col] != 1):
                        continue

                    queue.append((new_row , new_col))
                    grid[new_row][new_col] = 2
                    nonrotten -= 1

            time += 1 

        if nonrotten == 0 :
            return time 
        else:
            return -1 