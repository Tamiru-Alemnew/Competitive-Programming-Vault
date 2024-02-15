class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = defaultdict(int)

        for c in s:
            freq[c] += 1

        ans = 0
        for c in set(s):
            ans += (freq[c] // 2) * 2

        return ans + 1 if len(s) > ans and ans % 2 ==  0 else ans 

        