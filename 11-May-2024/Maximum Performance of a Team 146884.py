# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = [(efficiency[i], speed[i]) for i in range(n)]
        engineers.sort(reverse=True)
        
        max_performance = 0
        min_speed_heap = []
        total_speed = 0
        
        for engineer in engineers:
            engineer_speed = engineer[1]
            engineer_efficiency = engineer[0]
            
            heapq.heappush(min_speed_heap, engineer_speed)
            total_speed += engineer_speed
            
            if len(min_speed_heap) > k:
                total_speed -= heapq.heappop(min_speed_heap)
            
            current_performance = total_speed * engineer_efficiency
            max_performance = max(max_performance, current_performance)
            
        MOD = 10**9 + 7
        return max_performance % MOD
