class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        ans = 0 
        def helper(v, H):
            res = 0 
            for i in range(3):
                for j in range(3):
                    if i == 1 and j == 0 or i == 1 and j == 2:
                        pass
                    else:
                        res += grid[v+i][H+j]
            return res
        
        for i in range(len(grid[0])-2):
            for j in range(len(grid)-2):
                ans = max(helper(j, i) , ans)
        return ans
        
            




        