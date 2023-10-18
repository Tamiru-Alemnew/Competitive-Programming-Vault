class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur = 0
        maxAlt = 0 
        for g in gain:
            cur += g
            maxAlt = max(maxAlt , cur)
        return maxAlt 


            
