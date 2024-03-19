class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l , r = max(weights) , sum(weights)

        def check(cap):
            day , cCap = 1, cap
            for w in weights:
                if cCap - w <0:
                    day +=1
                    cCap = cap
                cCap -=w
            return day <= days

        while l < r :
            md = (l + r )// 2

            if check(md):
                r = md 
            else:
                l = md +1

        return r
        