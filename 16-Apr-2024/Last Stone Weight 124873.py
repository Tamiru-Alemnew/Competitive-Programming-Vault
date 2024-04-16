# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [ -w for w in stones]
        heapify(stones)
        N = len(stones)
        while len(stones) > 1:
            first_stone = -heapq.heappop(stones)
            second_stone = -heapq.heappop(stones)

            if (first_stone - second_stone) > 0 :
                heapq.heappush(stones , -(first_stone - second_stone ))
        
        return -heapq.heappop(stones) if len(stones) == 1 else 0
        