class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[1])
        end = points[0][1] 
        b = 1
        for s , e in points:
            if s > end:
                b += 1
                end = e 

        return b 

            
        