class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l , r = max(weights), sum(weights)
        res= r

        def possible(cap):
            day , cCap = 1, cap
            for w in weights:
                if cCap - w <0:
                    day +=1
                    cCap = cap
                cCap -=w
            return day <= days

        while l <= r:
            cap = l + (r -l)//2
            if possible(cap):
                r = cap -1
                res = min(res,cap)
            else:
                l = cap +1
        return res
            
