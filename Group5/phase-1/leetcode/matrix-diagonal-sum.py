class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0 
        c = len(mat) - 1
        for r in range(len(mat)):
            ans += mat[r][r]
            ans += mat[r][c]
            c-=1
            
        return ans - mat[len(mat)//2][len(mat)//2] if len(mat) %2 != 0 else ans