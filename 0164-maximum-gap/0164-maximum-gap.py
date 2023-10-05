class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        if len(nums) >1:
            for i in range(len(nums)):
                ans = max(nums[i] - nums[i-1] , ans)
        return ans

        