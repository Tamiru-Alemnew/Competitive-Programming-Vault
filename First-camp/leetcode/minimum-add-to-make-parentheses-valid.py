class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open = []
        cl = 0 

        for c in s:
            if c =="(":
                open.append(c)
            else:
                if len(open) > 0:
                    open.pop()
                else:
                    cl += 1

        return cl + len(open)

        
