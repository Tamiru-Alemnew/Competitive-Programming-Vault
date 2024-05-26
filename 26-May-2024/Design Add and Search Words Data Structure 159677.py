# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        root = self.trie

        for char in word :
            if char not in root:
                root[char] = {}

            root = root[char]
        root["end"] = True

    def search(self, word: str) -> bool:
        def dfs(index, node) -> bool:
            if index == len(word): 
                return "end" in node
                
            ch = word[index]

            if ch != '.':
                if ch not in node:
                    return False
                else:
                    child = node[ch]

                    if dfs(index + 1, child):
                        return True
            else:
                for child in node.values():
                    if child == True:
                        continue
                        
                    if dfs(index + 1, child):
                        return True

            return False

        return dfs(0, self.trie)




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)