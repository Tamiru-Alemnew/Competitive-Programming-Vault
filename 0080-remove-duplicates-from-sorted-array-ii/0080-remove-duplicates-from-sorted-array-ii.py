class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = 2
        
        if len(nums) <= 2:
            return len(nums)

        for i in range(2, len(nums)):
            if nums[i] != nums[cur - 2]:
                nums[cur] = nums[i]
                cur += 1

        return cur 
                

        