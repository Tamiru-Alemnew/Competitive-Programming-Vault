class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        ans = 0 
        flag = True
        for c in count.values():

            if c & 1 and flag:
                ans += c
                flag = False
            elif not c & 1:
                ans += c

        return ans 


        