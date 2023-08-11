class MedianFinder:

    def __init__(self):
        self.left = []
        self.right =[]

    def addNum(self, num: int) -> None:
        if not self.left or -self.left[0]>= num:
            heapq.heappush(self.left,-num)
        else:
            heapq.heappush(self.right,num)
        
        if len(self.left) > len(self.right) +1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        elif len(self.right) > len(self.left):
            heapq.heappush(self.left,-heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.right) == len(self.left):
            return (self.right[0] - self.left[0])/2.0
        else:
            return -self.left[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()