class Solution:
    def minimumSteps(self, s: str) -> int: 
        count = 0 
        ans = 0
        for i in range(len(s)-1,-1 ,-1):
            if s[i] == "1":
                ans += (len(s)-1-i - count)
                count += 1
        return ans 
            

        