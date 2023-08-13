class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        heap = [(-count[i],i) for i in count]
        heapq.heapify(heap)
        freq , number = heapq.heappop(heap)
        return number