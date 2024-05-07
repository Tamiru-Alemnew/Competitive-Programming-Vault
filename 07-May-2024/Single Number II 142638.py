# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        once = twice = 0
        for num in nums:
            once ^= (num & ~twice)
            twice ^= (num & ~once) 

        return once
