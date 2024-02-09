class Solution:
    def maxScore(self, s: str) -> int:
        left = 0 
        right = s.count("1")
        ans = 0

        for i in range(len(s)-1):
            left += s[i] == "0"
            right -= s[i] =="1"
            ans =  max(ans , left+right)

        return ans

        