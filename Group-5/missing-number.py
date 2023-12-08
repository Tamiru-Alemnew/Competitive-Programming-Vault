class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = sum(nums)
        summ = sum(i for i in range(len(nums)+1))
        return summ - n
        