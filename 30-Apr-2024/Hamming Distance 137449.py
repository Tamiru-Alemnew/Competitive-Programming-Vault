# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        hamming = 0 
        
        while x > 0 or y > 0:
            if x & 1 != y&1:
                hamming += 1

            x >>= 1
            y >>= 1

        return hamming 

        