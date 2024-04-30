# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor_arr = 0 
        xor_ind = 0 

        for i , n in enumerate(nums):
            xor_arr ^= n
            xor_ind ^= i + 1

        return xor_arr ^ xor_ind
        