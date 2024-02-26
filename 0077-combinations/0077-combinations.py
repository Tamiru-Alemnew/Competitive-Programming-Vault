class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def backtrack(i , path):
            if len(path) == k:
                ans.append(path[:])
                return 
            
            for c in range(i , n+1):
                path.append(c)
                backtrack(c+1 , path)
                path.pop()

        ans = []
        backtrack(1 , [])

        return ans 

        