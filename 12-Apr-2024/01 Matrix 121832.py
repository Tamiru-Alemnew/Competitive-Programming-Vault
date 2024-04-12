# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def inbound(row , col):
            return (0<= row < len(mat)) and (0<= col < len(mat[0]))

        directions = [(1 , 0 ) , (0 , 1) , (-1 , 0) , (0 , -1)]
        queue = deque()
        ans = [[-1]*len(mat[0]) for _ in range(len(mat))]
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    queue.append((i , j))

        while queue:
            for _ in range(len(queue)):
                row , col = queue.popleft()
                for rc , cc in directions:
                    new_row = row + rc
                    new_col = col + cc 

                    if inbound(new_row, new_col) and ans[new_row][new_col] == -1:
                        ans[new_row][new_col] = ans[row][col] + 1
                        queue.append((new_row, new_col))


        return ans 


