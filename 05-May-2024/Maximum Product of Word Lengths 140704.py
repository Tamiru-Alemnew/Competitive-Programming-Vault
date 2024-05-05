# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        N = len(words)
        Binary = [None]*N
        length =[0]*N

        for index ,  word in enumerate(words):
            s = 0 
            for c in word:
                s |= 1<< ord(c) - ord("a")
            
            Binary[index] = s
            length[index] = len(word)

        max_value = 0
        for i in range(N):
            for j in range(1 , N):
                if Binary[i] & Binary[j] == 0 :
                    max_value = max(max_value  ,length[i] * length[j])

        return max_value

