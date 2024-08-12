# Problem: Kth Largest Element in a Stream - https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap = nums[:]
        self.length = k
        heapify(self.minheap)

        while len(self.minheap) > k:
            heappop(self.minheap)
        
    def add(self, val: int) -> int:
        if not self.minheap or len(self.minheap) < self.length:
           heappush(self.minheap , val) 

        elif val > self.minheap[0]:
            heappush(self.minheap , val)
            heappop(self.minheap)

        return self.minheap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)