class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        op = 0 
        cur = target
        d = maxDoubles
        while cur > 1 and d >  0:
            op += cur % 2  + 1
            cur = cur // 2
            d -= 1

        return cur + op - 1
        

        