class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0  # To track the maximum length of valid substring
        max_count = 0   # To track the maximum count of any single character in the current window
        char_count = [0] * 26  # To store the count of each character in the window
        start = 0

        for end in range(len(s)):
            char_count[ord(s[end]) - ord('A')] += 1
            max_count = max(max_count, char_count[ord(s[end]) - ord('A')])

            # Calculate the number of replacements needed for the current window
            replacements_needed = (end - start + 1) - max_count

            # If the number of replacements needed is greater than k, move the window start
            if replacements_needed > k:
                char_count[ord(s[start]) - ord('A')] -= 1
                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length
