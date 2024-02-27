class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        brackets = ["(" , ")"]
        ans = []
        mp = {"(": 0 , ")":0 }
        md = n 
        def backtrack(n , path):
            nonlocal ans  ,  md
            if n == 0 :
                ans.append("".join(path[:]))
                return 

            if mp[")"] > mp["("] :
                return 

            for i in range(2):
                if mp[brackets[i] ]< md:
                    path.append(brackets[i])
                    mp[brackets[i] ] += 1
                    
                    backtrack(n - 1 , path)
                    
                    mp[brackets[i] ] -= 1
                    path.pop()

        backtrack(2*n , [])
        return ans 

        