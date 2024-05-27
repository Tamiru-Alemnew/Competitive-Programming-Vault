# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

from typing import List

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = {}

        def insert(word):
            root = trie
            for char in word:
                if char not in root:
                    root[char] = {}
                root = root[char]
            root["#"] = True  

        def can_build_from_trie(word):
            root = trie
            for char in word:
                if char not in root or "#" not in root[char]:
                    return False
                root = root[char]
            return True

        for word in words:
            insert(word)

        ans = ""
        for word in words:
            if can_build_from_trie(word):
                if len(word) > len(ans) or (len(word) == len(ans) and word < ans):
                    ans = word

        return ans
