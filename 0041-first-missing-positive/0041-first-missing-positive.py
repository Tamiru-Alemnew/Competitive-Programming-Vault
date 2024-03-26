class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [0] + nums

        for i in range(len(nums)):
            while  1<= nums[i] < len(nums) and nums[i] != nums[nums[i]]:
                nums[nums[i]] , nums[i] = nums[i] , nums[nums[i]]

        for i in range(len(nums)):
            if nums[i] != i and 1<= i < len(nums) :
                return i 

        return len(nums)




