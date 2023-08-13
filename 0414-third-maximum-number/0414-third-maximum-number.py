class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        count = Counter(nums)
        heap =[(-i,count[i]) for i in count]
        heapq.heapify(heap)
        if len(heap) <3:
            number , freq = heapq.heappop(heap)
            return -number
        else:
            for i in range(3):
                number , freq = heapq.heappop(heap)
            return -number

