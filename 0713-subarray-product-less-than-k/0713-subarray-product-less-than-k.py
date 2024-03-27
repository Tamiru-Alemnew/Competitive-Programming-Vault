class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        cur = 1 
        l = 0 
        ans = 0
        for i in range(len(nums)):
            cur *= nums[i]

            while cur >= k and l <= i:
                cur /= nums[l]
                l += 1

            ans += i - l + 1

        return ans 

            

