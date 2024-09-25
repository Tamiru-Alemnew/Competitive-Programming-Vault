class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = {}

        def insert(word):
            node = trie 

            for char in word:
                if char not in node:
                    node[char] = {}
                    node[char]["cnt"] = 0

                node[char]["cnt"] += 1

                node = node[char]


        def prefix(word):
            node = trie 
            ans = 0 
            for char in word:
                if char not in node:
                    return 0

                ans += node[char]["cnt"]
                node = node[char]
                
            return ans
        
        for word in words:
            insert(word)
      

        ans = [0 for i in range(len(words))]

        for ind ,  word in enumerate(words):
            
            ans[ind] += prefix(word)
            

        return ans 
                    
        