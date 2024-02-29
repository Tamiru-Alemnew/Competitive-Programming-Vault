class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mp = {
                "2": ["a", "b", "c"],
                "3": ["d", "e", "f"],
                "4": ["g", "h", "i"],
                "5": ["j", "k", "l"],
                "6": ["m", "n", "o"],
                "7": ["p", "q", "r", "s"],
                "8": ["t", "u", "v"],
                "9": ["w", "x", "y", "z"]
            }

        path = []
        ans = []
        def backtrack(i , path):
            nonlocal ans 
            if len(path)==len(digits):
                temp = "".join(path)
                ans.append(temp)
                return 
            
            for num in mp[digits[i]]:
                path.append(num)
                backtrack(i + 1 , path)
                path.pop()

        if len(digits) >0 :
            backtrack(0 ,[])

        return ans