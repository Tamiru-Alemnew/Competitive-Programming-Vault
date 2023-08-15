class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        res =[]
        
        for letter in queries:
            q = letter.count(min(letter))
            c = 0 
            for w in words:
                if w.count(min(w)) > q:
                    c += 1
            res.append(c)
        return res

        