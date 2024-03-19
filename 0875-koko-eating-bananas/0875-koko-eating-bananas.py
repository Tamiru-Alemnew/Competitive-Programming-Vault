class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1 , max(piles) 
        res = r
        def check (x):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/x)
            return hours <= h
        while l < r :
            k = l +(r-l)//2
            if check(k):
                r = k 
            else: 
                l = k +1
        return r