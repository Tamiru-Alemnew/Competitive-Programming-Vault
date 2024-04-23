# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_points = {}
        for i, interval in enumerate(intervals):
            start_points[interval[0]] = i
        
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        result = [-1] * len(intervals)
       
        for i, interval in enumerate(intervals):
           
            index = bisect_left(sorted_intervals, [interval[1], -float('inf')])
            
            if index != len(intervals):
                result[i] = start_points[sorted_intervals[index][0]]
        
        return result