class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ps=[0]* 10001
        for c , s , e in trips:
            ps[s+1] +=c
            ps[e+1] -=c
        for i in range(1,1001):
            ps[i] +=ps[i-1]
            if ps[i]> capacity:
                return False
        return True

        