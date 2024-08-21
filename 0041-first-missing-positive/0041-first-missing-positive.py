class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        number = [0]*(len(nums) + 1)

        for n in nums :
            if 0 < n <= len(nums):
                number[n] += 1

        ans = len(nums) + 1

        for i , v  in enumerate(number[1:]):
            if v == 0 :
                return i + 1 


        return ans 


        