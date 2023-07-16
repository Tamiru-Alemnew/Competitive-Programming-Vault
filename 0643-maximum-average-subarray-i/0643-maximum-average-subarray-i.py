class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[:k])
        average= s / k

        for i in range(k, len(nums)):
            s += nums[i] - nums[i - k]
            average = max(average, s / k)

        return average