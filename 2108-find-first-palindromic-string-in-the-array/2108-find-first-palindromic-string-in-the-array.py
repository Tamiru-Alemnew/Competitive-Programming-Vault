class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            l_word = list(word)
            r_word = l_word[::-1]
    
            if l_word == r_word:
                return word
                
        return ""
        