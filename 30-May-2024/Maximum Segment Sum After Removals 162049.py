# Problem: Maximum Segment Sum After Removals - https://leetcode.com/problems/maximum-segment-sum-after-removals/description/

    
class Solution:
    def maximumSegmentSum(self, nums: List[int], rq: List[int]) -> List[int]:
        n = len(nums)
        
        loc = list(range(n))
        tot = [float('inf')] * n
        
        def find(x):
            if loc[x] != x:
                loc[x] = find(loc[x])
            return loc[x]
        
        
        def union(x, y):
            a, b = find(x), find(y)
            if a != b:
                loc[b] = a
                tot[a] += tot[b]
        
        ans = [0] * n
        for i in reversed(range(n)):
            
            idx = rq[i]
            tot[idx] = nums[idx]
            if idx > 0 and tot[idx - 1] != float('inf'):
                union(idx, idx-1)
            if idx < n - 1 and tot[idx + 1] != float('inf'):
                union(idx, idx+1)
            
            if i > 0:
                ans[i - 1] = max(ans[i], tot[find(idx)])
        
        return ans