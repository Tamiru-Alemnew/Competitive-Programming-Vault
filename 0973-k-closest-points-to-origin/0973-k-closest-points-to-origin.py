class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if points is None or len(points[0]) == 0:
            return []
        
        if len(points) <= K:
            return points
        
        points.sort(key=lambda x: x[0]*x[0] + x[1]*x[1])
        
        return points[0:K]