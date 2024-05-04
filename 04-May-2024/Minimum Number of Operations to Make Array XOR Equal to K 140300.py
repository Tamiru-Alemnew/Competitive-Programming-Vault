# Problem: Minimum Number of Operations to Make Array XOR Equal to K - https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        for num in nums:
            ans ^= num

        ans ^= k
        return ans.bit_count()
            
                




 



