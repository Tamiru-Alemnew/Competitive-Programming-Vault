class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x = 0 
        ans = ""
        for i in range(len(word1)) :
            ans+= word1[i] 
            if i < len(word2):
                ans += word2[i]
        return ans+word2[len(word1):] if len(word1) < len(word2) else ans 
