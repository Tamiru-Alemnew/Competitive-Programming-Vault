class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        VOWELS = "aeiou"
        window = res = 0
        for r in range(len(s)):
            window += s[r] in VOWELS
            if r >= k:
                window -= s[r - k] in VOWELS
            res = max(res, window)
        return res
        