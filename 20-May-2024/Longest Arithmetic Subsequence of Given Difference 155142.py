# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        longest =  1 

        for i in range(len(arr)):
            dp[arr[i] ] = dp[arr[i] - difference ] + 1
            longest = max(longest , dp[arr[i]])

        return longest
