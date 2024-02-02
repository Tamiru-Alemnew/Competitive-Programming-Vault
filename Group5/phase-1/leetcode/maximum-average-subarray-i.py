class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:  
        s = sum(nums[:k])
        mxs = s
        for i in range(len(nums)-k):
            s = s + nums[i + k] - nums[i]
            mxs = max(s , mxs)
        return mxs / k