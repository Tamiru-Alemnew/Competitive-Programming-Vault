class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curS = 0
        res =  nums[0]

        for num in nums:
            if curS < 0:
                curS = 0 
            curS += num
            res = max(curS , res)
        return res