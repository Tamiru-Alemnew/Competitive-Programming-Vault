class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not g or not s :
            return 0 
        g.sort()
        s.sort()
        c = 0 
        l , r  =  0 , 0 
        
        while l < len(g) and r < len(s):
            if s[r] >= g[l]:
                c += 1
                r += 1 
                l += 1
            else: 
                r += 1
        return c 



        