class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return None
        ptr=0
        for i in range(len(nums)):
            if nums[i] != nums[ptr]:
                ptr +=1
                nums[ptr] = nums[i] 
        return ptr + 1
        