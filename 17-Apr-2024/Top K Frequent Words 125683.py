# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency = Counter(words)
        heap = [(-val,key) for key , val in frequency.items()]
        heapify(heap)
        
        result =[]
        for i in range(k):
            freq, word = heapq.heappop(heap)
            result.append(word)

        return result
