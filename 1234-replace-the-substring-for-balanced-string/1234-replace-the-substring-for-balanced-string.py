class Solution:
    def balancedString(self, s: str) -> int:
        char_count = Counter(s)
        n = len(s)
      
        if all(count <= n // 4 for count in char_count.values()):
            return 0

        min_len = n
        start_index = 0
      
        for i, char in enumerate(s):
            char_count[char] -= 1

            while start_index <= i and all(count <= n // 4 for count in char_count.values()):
                min_len = min(min_len, i - start_index + 1)
                char_count[s[start_index]] += 1
                start_index += 1

        return min_len