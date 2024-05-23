# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0]*n for i in range(n)]

        for i in range(n):
            for j in range(i+1):
                dp[i][j] = 1

        l = r = 0
        for i in range(n-2 , -1 , -1):
            for j in range(i + 1 , n):
                dp[i][j] = s[i] == s[j] and (dp[i+1][j-1])
                if dp[i][j]:
                    if j - i > r - l :
                        r , l = j , i

        return s[l:r+1]

