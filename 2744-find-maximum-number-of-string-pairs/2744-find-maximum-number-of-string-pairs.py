class Solution:
    def is_palindrome(self, word: str) -> bool:
        return word == word[::-1]

    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        word_counts = {}
        count = 0

        for word in words:
            reverse_word = word[::-1]
            if reverse_word in word_counts and word_counts[reverse_word] > 0:
                count += 1
                word_counts[reverse_word] -= 1
            else:
                word_counts[word] = word_counts.get(word, 0) + 1

        return count