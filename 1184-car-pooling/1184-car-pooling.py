class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ps=[0]* 10001
        for c , f , t in trips:
            ps[f+1] +=c
            ps[t+1] -=c
        for i in range(1,1001):
            ps[i] +=ps[i-1]
            if ps[i]> capacity:
                return False
        return True

        