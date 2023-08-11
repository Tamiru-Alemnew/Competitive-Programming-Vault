class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        heap =  [-i[1] for i in count.items()]
        heapq.heapify(heap)
        n = len(arr)
        c, removed= 0, 0 
        while removed < n/2:
            removed += -heapq.heappop(heap)
            c +=1
        return c