class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        startValue = 1 
        prefixSum = 0
        for num in nums:
            prefixSum += num
            if prefixSum < 1:
                startValue = max(startValue , 1 - prefixSum)
        return startValue

        