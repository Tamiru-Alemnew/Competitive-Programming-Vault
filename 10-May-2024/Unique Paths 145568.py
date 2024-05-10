# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {}

        def inbound(row , col):
            return (0<= row < m) and (0<= col < n)

        directions = [(0 , 1) , ( 1 , 0 )]

        def backtrack(row , col):
            if row == m-1 and col == n - 1:
                return 1
                
            if (row , col) in memo :
                return memo[(row , col)]

            possible = 0 

            for cr , cc in directions:
                new_row = row + cr
                new_col = col + cc

                if inbound(new_row , new_col):
                    possible += backtrack(new_row ,new_col)

            memo[(row , col)] = possible

            return possible

        ans = backtrack(0 , 0)

        return ans