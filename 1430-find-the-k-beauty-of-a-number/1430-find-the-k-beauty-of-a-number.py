class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        l  , r = 0 , k 
        ans = 0 
        temp  = str(num)
        while r < len(temp) + 1:
            cur = int(temp[l : r])
            if cur != 0 and (num % cur) == 0 :
                ans += 1
            l += 1
            r += 1
        return ans 
