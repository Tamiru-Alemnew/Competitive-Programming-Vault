class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        if n < k:
            return -1
        s = [weights[i] + weights[i+1] for i in range(n-1)]
        
        large = small = weights[0] + weights[-1]

        large += sum(heapq.nlargest(k-1, s))
        small += sum(heapq.nsmallest(k-1, s))
        return large - small