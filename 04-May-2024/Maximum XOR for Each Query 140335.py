# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num

        ans = []
        mask = 2**maximumBit - 1

        while nums:
            cur = xor ^ mask
            ans.append(cur)
            xor ^= nums[-1]
            nums.pop()    

        return ans
            

