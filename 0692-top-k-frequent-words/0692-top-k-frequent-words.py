class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency = Counter(words)
        heap = [(-i[1],i[0]) for i in frequency.items()]
        heapq.heapify(heap)

        result =[]
        for i in range(k):
            freq, word = heapq.heappop(heap)
            result.append(word)
        return result
