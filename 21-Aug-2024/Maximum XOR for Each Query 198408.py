# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        cur = 0 
        for n in nums :
            cur ^= n

        ans = []
        mask =  2**maximumBit - 1

        for i in range(len(nums) - 1 , -1 , -1):
            ans.append(cur ^ mask)
            cur ^= nums[i]

        return ans


        