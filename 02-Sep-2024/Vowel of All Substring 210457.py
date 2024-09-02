# Problem: Vowel of All Substring - https://leetcode.com/problems/vowels-of-all-substrings/

class Solution:
    def countVowels(self, word: str) -> int:
        """
        aba

        "a", "ab", "aba", "b", "ba", and "a"

        [1 , 2 , 3 , 2 , 1 , 2 , 1 , 1 , 9 ]

        """
        ans = 0 
        n = len(word)
        
        for i in range(1 , len(word) + 1):
            if word[i-1] in ["a" , "e" , "i" , "o" , "u"] :
                ans += i*( len(word) + 1 -i)

        return ans 
