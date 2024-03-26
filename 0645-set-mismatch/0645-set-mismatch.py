class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums = [0] + nums

        for i in range(len(nums)):

            while nums[i] != nums[nums[i]]:
                cur = nums[i]

                nums[nums[i]] , nums[i] = nums[i] , nums[nums[i]]

        result = []
        for i in range(len(nums)):
            if nums[i] != i:
                result.append(nums[i])
                result.append(i)
        return result
        