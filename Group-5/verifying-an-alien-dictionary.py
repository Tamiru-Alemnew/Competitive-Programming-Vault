class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        sorted_w = sorted(words ,key = lambda x: [order.index(c) for c in x] )
        return sorted_w == words