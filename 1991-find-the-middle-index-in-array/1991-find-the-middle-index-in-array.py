class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum = 0
        for i , num in enumerate(nums):
            rightSum = total - leftSum  - num 
            if rightSum == leftSum:
                return i 
            leftSum += num
        return -1

        