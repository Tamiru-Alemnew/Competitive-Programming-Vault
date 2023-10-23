class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def helper(s):
            ans =[]
            for i in s:
                if i == "#":
                    if ans:
                        ans.pop()
                else:
                    ans.append(i)

            return "".join(ans)
        return helper(s) == helper(t)

