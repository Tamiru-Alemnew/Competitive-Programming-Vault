class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        c = 0
        r = 0

        for greed_factor in g:
            while r < len(s) and s[r] < greed_factor:
                r += 1
            if r < len(s):
                c += 1
                r += 1

        return c
