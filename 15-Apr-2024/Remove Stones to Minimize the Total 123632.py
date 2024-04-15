# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-p for p in piles]
        heapq.heapify(piles)

        for i in range(k):
            val = -heapq.heappop(piles)
            cur = math.ceil(val / 2)
            heapq.heappush(piles,-cur)
          
        
        return sum(abs(p) for p in piles)