# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cur = 0 

        for n in nums:
            cur ^= n

        return cur 
        