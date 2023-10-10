class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        start = total = 0 
        for num in nums:
            total += num
            start = min(start,total)
        return abs(start) + 1