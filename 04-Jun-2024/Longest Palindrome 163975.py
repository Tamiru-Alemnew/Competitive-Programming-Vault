# Problem: Longest Palindrome - https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        ans = 0 
        flag =  True
        for c in count.values():
            if c & 1 == 0 :
                ans += c
            
            elif flag:
                ans += c
                flag = False
            else:
                ans += c -1


        return ans 


        