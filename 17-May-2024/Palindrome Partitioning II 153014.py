# Problem: Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:

        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]
        
        for i in range(n):
            is_palindrome[i][i] = True  

        for length in range(2, n + 1): 
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        is_palindrome[i][j] = True
                    else:
                        is_palindrome[i][j] = is_palindrome[i + 1][j - 1]

        min_cuts = [float('inf')] * n
        for i in range(n):
            if is_palindrome[0][i]:
                min_cuts[i] = 0
            else:
                for j in range(i):
                    if is_palindrome[j + 1][i]:
                        min_cuts[i] = min(min_cuts[i], min_cuts[j] + 1)
 
        return min_cuts[-1]
